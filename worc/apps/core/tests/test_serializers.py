from decimal import Decimal

import pytest
from django.db import IntegrityError
from model_bakery import baker
from rest_framework.exceptions import ErrorDetail

from worc.apps.core.serializers import CandidateSerializer


def test_create_candidate_with_age_less_than_18(db, candidate_data):
    """
    Test that a candidate cannot be created with age less than 18.
    """
    for i in range(17):
        data = candidate_data.copy()
        data["age"] = i
        serializer = CandidateSerializer(data=data)
        assert not serializer.is_valid()
        assert serializer.errors["age"] == [
            ErrorDetail(
                string="Ensure this value is greater than or equal to 18.",
                code="min_value",
            )
        ]


def test_create_candidate_with_invalid_cpf(db, candidate_data):
    """
    Test that a candidate cannot be created with an invalid CPF.
    """
    invalid_cpfs = [
        {"cpf": "12345678901", "error": "Número de CPF inválido."},
        {"cpf": "11111111111", "error": "Número de CPF inválido."},
        {"cpf": "66666666666", "error": "Número de CPF inválido."},
        {"cpf": "77777777777", "error": "Número de CPF inválido."},
        {"cpf": "88888888888", "error": "Número de CPF inválido."},
        {"cpf": "99999999999", "error": "Número de CPF inválido."},
        {"cpf": "123.123.123-31", "error": "Número de CPF inválido."},
        {"cpf": "123.123.123-32", "error": "Número de CPF inválido."},
        {"cpf": "123.123.123", "error": "CPF deve conter 11 números."},
        {"cpf": "abcabcabcabcab", "error": "CPF deve conter 11 números."},
        {"cpf": "123.123.123-", "error": "CPF deve conter 11 números."},
    ]
    list_cpfs = [x["cpf"] for x in invalid_cpfs]
    for cpf in list_cpfs:
        data = candidate_data.copy()
        data["cpf"] = cpf
        serializer = CandidateSerializer(data=data)
        assert not serializer.is_valid()
        assert serializer.errors["cpf"] == [
            ErrorDetail(
                string=invalid_cpfs[list_cpfs.index(cpf)]["error"],
                code="invalid_cpf",
            )
        ]


def test_create_candidate_with_email_duplicate(db, candidate_data):
    """
    Test that a candidate cannot be created with an email that already exists.
    """
    base_data = candidate_data.copy()
    del base_data["cpf"]
    valid_cpfs = ["608.249.550-05", "960.762.690-73"]

    first_candidate = baker.make("core.Candidate", cpf=valid_cpfs[0], **base_data)

    assert first_candidate.pk is not None
    with pytest.raises(IntegrityError):
        baker.make("core.Candidate", cpf=valid_cpfs[1], **base_data)


def test_create_candidate_with_cpf_duplicate(db, candidate_data):
    """
    Test that a candidate cannot be created with an email that already exists.
    """
    first_candidate = baker.make("core.Candidate", **candidate_data)

    assert first_candidate.pk is not None
    with pytest.raises(IntegrityError):
        baker.make("core.Candidate", **candidate_data)


def test_update_cpf_candidate(db, candidate_data):
    """
    Test that a candidate CPF cannot be updated.
    """
    candidate = baker.make("core.Candidate", **candidate_data)
    candidate_data["cpf"] = "960.762.690-73"
    serializer = CandidateSerializer(instance=candidate, data=candidate_data)
    assert not serializer.is_valid()
    assert serializer.errors["cpf"] == [
        ErrorDetail(string="CPF não pode ser alterado.", code="invalid")
    ]
