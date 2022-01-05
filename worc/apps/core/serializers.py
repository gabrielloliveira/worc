from rest_framework import serializers

from worc.apps.core.models import Candidate
from worc.apps.core.utils import calculate_age_from_birthday


class CandidateSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    uuid = serializers.ReadOnlyField()
    age = serializers.ReadOnlyField()

    class Meta:
        model = Candidate
        fields = (
            "created_at",
            "updated_at",
            "uuid",
            "name",
            "email",
            "cpf",
            "age",
            "birthday",
            "salary_claimed",
            "immediate_availability",
        )

    def validate_cpf(self, value):
        if self.instance and self.instance.cpf != value:
            raise serializers.ValidationError(
                "CPF não pode ser alterado.", code="invalid"
            )
        return value

    def validate_birthday(self, value):
        if calculate_age_from_birthday(value) < 18:
            raise serializers.ValidationError(
                "Candidato deve ser maior de 18 anos.", code="invalid_age"
            )
        return value
