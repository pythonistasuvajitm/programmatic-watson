from django.conf import settings
from django.core.validators import FileExtensionValidator
from rest_framework import serializers
from watson_app.validators import validate_file


class FileSerializer(serializers.Serializer):
    file = serializers.FileField(validators=[FileExtensionValidator(allowed_extensions=settings.ALLOWED_EXTENSIONS),
                                             validate_file])
