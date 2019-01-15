from rest_framework import serializers

from .models import ApplicationSubmission


class SubmissionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationSubmission
        fields = ('id', 'title', 'status')


class SubmissionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationSubmission
        fields = ('id', 'title',)
