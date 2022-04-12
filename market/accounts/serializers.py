from rest_framework import serializers

from accounts.models import Job, Account, Key


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        exclude = ["account"]


class AccountSerializer(serializers.ModelSerializer):
    keys = KeySerializer(many=True)

    class Meta:
        model = Account
        fields = "__all__"

    def create(self, validated_data):
        keys_data = validated_data.pop("keys")
        account = Account.objects.create(**validated_data)
        Key.objects.bulk_create(
            [Key(account=account, **key_data) for key_data in keys_data]
        )
        return account
