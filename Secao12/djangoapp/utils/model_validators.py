from django.core.exceptions import ValidationError  # type: ignore


def validate_png(image):
    if not image.name.lower().endswith('.png'):
        raise ValidationError(
            'Apenas arquivos PNG são permitidos.',
            code='invalid_file_type',
        )
