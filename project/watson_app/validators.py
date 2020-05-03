from django.conf import settings
from django.core.exceptions import ValidationError
import magic


def validate_file(file_obj):
    file_name = file_obj.name
    mime_type = magic.from_buffer(file_obj.read(), mime=True)
    if mime_type.lower() not in settings.ALLOWED_MIMETYPES:
        raise ValidationError(
            f"{file_name} is not a valid {mime_type}"
        )
