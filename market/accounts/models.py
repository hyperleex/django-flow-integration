from django.db import models


class KeyType(models.TextChoices):
    local = "local", "local"
    aws_kms = "aws_kms", "aws_kms"
    google_kms = "google_kms", "google_kms"


class Key(models.Model):
    index = models.PositiveIntegerField()
    account = models.ForeignKey(
        "Account", on_delete=models.CASCADE, related_name="keys"
    )
    type = models.CharField(max_length=20, choices=KeyType.choices)
    public_key = models.TextField()
    sign_algo = models.CharField(max_length=100)
    hash_algo = models.CharField(max_length=100)

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class AccountType(models.TextChoices):
    custodial = "custodial", "custodial"


class Account(models.Model):
    address = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=AccountType.choices)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.address


class Job(models.Model):
    job_id = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    error = models.CharField(max_length=100, null=True, blank=True)
    errors = models.CharField(max_length=100, null=True, blank=True)
    result = models.CharField(max_length=100, null=True, blank=True)
    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f"{self.job_id}"
