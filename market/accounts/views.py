from typing import Dict

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Job
from accounts.serializers import JobSerializer, AccountSerializer
from accounts.services.account import AccountService


class SerializationError(Exception):
    ...


def save_entity(data: Dict, serializer_cls) -> Job:
    serializer = serializer_cls(data=data)
    if not serializer.is_valid():
        raise SerializationError("serialization error")
    return serializer.save()


class AccountList(APIView):
    service = AccountService()

    def get(self, request):
        return Response(self.service.list())

    def post(self, request):
        data = self.service.create()
        if "job_id" in data:
            try:
                save_entity(data, JobSerializer)
            except SerializationError:
                return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        if "address" in data:
            try:
                save_entity(data, AccountSerializer)
            except SerializationError:
                return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_account(request, address):
    return Response(AccountService().get(address=address))


@api_view(["POST"])
def update_job(request):
    try:
        job = save_entity(request.data, JobSerializer)
        data = AccountService().get(address=job.result)
        save_entity(data, AccountSerializer)
    except SerializationError:
        return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({"status": "ok"})
