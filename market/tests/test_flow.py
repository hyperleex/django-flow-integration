import pytest
from rest_framework.reverse import reverse

from accounts.models import Job, Account


@pytest.mark.django_db
def test_create_account__job(client, httpx_mock):
    mock_data = {
        "jobId": "3e593e10-54fb-4aa2-872a-5081fa9ae540",
        "type": "account_create",
        "state": "INIT",
        "error": "",
        "errors": None,
        "result": "",
        "transactionId": "",
        "createdAt": "2022-04-12T21:13:13.7315322Z",
        "updatedAt": "2022-04-12T21:13:13.7315322Z",
    }
    httpx_mock.add_response(json=mock_data)

    obj_count = Job.objects.count()

    resp = client.post(reverse("account-list"))

    assert resp.status_code == 201
    assert resp.json() == mock_data

    assert obj_count + 1 == Job.objects.count()
    assert Job.objects.last().job_id == mock_data["jobId"]


@pytest.mark.django_db
def test_create_account__account(client, httpx_mock):
    mock_data = {
        "address": "0xf8d6e0586b0a20c7",
        "keys": [
            {
                "index": 0,
                "type": "local",
                "publicKey": "string",
                "signAlgo": "string",
                "hashAlgo": "string",
                "createdAt": "2021-04-27T05:49:53.211+00:00",
                "updatedAt": "2021-04-27T05:49:53.211+00:00",
            }
        ],
        "type": "custodial",
        "createdAt": "2021-04-27T05:49:53.211+00:00",
        "updatedAt": "2021-04-27T05:49:54.211+00:00",
    }
    httpx_mock.add_response(json=mock_data)

    obj_count = Account.objects.count()

    resp = client.post(reverse("account-list"))

    assert resp.status_code == 201
    assert resp.json() == mock_data

    assert obj_count + 1 == Account.objects.count()
    account = Account.objects.last()

    assert account.address == mock_data["address"]
    assert account.keys.count() == len(mock_data["keys"])

    assert account.keys.last().index == mock_data["keys"][0]["index"]
