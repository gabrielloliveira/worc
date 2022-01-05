import json

from rest_framework import status
from rest_framework.reverse import reverse

from worc.apps.core.models import Candidate


def test_create_candidate(api_client, db, candidate_data):
    """
    Test creating a candidate
    """
    response = api_client.post(
        reverse("core:candidate_list_create"), data=candidate_data
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["name"] == candidate_data["name"]
    assert response.data["age"] is not None
    assert Candidate.objects.count() == 1


def test_create_candidate_with_invalid_data(api_client, candidate_data, db):
    """
    Test creating a candidate with invalid data
    """
    data_without_name = candidate_data.copy()
    del data_without_name["name"]

    data_without_email = candidate_data.copy()
    del data_without_email["email"]

    data_without_cpf = candidate_data.copy()
    del data_without_cpf["cpf"]

    response_1 = api_client.post(reverse("core:candidate_list_create"), data={})
    response_2 = api_client.post(
        reverse("core:candidate_list_create"), data=data_without_name
    )
    response_3 = api_client.post(
        reverse("core:candidate_list_create"), data=data_without_email
    )
    response_4 = api_client.post(
        reverse("core:candidate_list_create"), data=data_without_cpf
    )

    assert response_1.status_code == status.HTTP_400_BAD_REQUEST
    assert response_2.status_code == status.HTTP_400_BAD_REQUEST
    assert response_3.status_code == status.HTTP_400_BAD_REQUEST
    assert response_4.status_code == status.HTTP_400_BAD_REQUEST
    assert Candidate.objects.count() == 0


def test_list_candidate(candidate, api_client):
    """
    Test listing candidates
    """
    response = api_client.get(reverse("core:candidate_list_create"))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["name"] == candidate.name


def test_retrieve_candidate(candidate, api_client):
    """
    Test retrieve candidate
    """
    response = api_client.get(
        reverse(
            "core:candidate_retrieve_update_destroy", kwargs={"uuid": candidate.uuid}
        )
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == candidate.name


def test_update_candidate(candidate, candidate_data, api_client):
    """
    Test update candidate
    """
    candidate_data["name"] = "New Name"

    response = api_client.put(
        reverse(
            "core:candidate_retrieve_update_destroy", kwargs={"uuid": candidate.uuid}
        ),
        data=json.dumps(candidate_data),
        content_type="application/json",
    )
    candidate.refresh_from_db()
    assert response.status_code == status.HTTP_200_OK
    assert response.data["name"] == "New Name"
    assert candidate.name == "New Name"
    assert Candidate.objects.count() == 1


def test_destroy_candidate(candidate, api_client):
    """
    Test destroy candidate
    """
    response = api_client.delete(
        reverse(
            "core:candidate_retrieve_update_destroy", kwargs={"uuid": candidate.uuid}
        )
    )
    list_response = api_client.get(reverse("core:candidate_list_create"))
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert list_response.status_code == status.HTTP_200_OK
    assert len(list_response.data["results"]) == 0
    assert Candidate.objects.count() == 0
