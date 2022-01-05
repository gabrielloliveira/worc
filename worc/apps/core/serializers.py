from rest_framework import serializers

from worc.apps.core.models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    uuid = serializers.ReadOnlyField()

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
            "salary_claimed",
            "immediate_availability",
        )

    def validate_cpf(self, value):
        if self.instance and self.instance.cpf != value:
            raise serializers.ValidationError(
                "CPF não pode ser alterado.", code="invalid"
            )
        return value
