from decimal import Decimal

import pytest
from model_bakery import baker
from rest_framework.test import APIClient


@pytest.fixture
def candidate_data():
    return {
        "name": "Gabriell",
        "email": "contato@gabrielloliveira.com",
        "age": 18,
        "cpf": "608.249.550-05",
        "salary_claimed": Decimal("500.00"),
    }


@pytest.fixture
def candidate_json_data():
    return {
        "name": "Gabriell",
        "email": "contato@gabrielloliveira.com",
        "age": 18,
        "cpf": "608.249.550-05",
        "salary_claimed": "500.00",
    }


@pytest.fixture
def candidate(db, candidate_data):
    return baker.make("core.Candidate", **candidate_data)


@pytest.fixture
def user(db):
    return baker.make("users.User", is_staff=True, is_superuser=True)


@pytest.fixture
def api_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client
