from decimal import Decimal

import pytest


@pytest.fixture
def candidate_data():
    return {
        "name": "Gabriell",
        "email": "contato@gabrielloliveira.com",
        "age": 18,
        "cpf": "608.249.550-05",
        "salary_claimed": Decimal("500.00"),
    }
