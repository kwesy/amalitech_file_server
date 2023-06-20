from django.core.validators import BaseValidator
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

@deconstructible
class FileSizeValidator(BaseValidator):
    message = _('Ensure the file size is not greater than %(max_size)s bytes.')
    code = 'file_size_limit'

    def __init__(self, max_size, message=None):
        self.max_size = max_size
        self.message = message or self.message

    def compare(self, a, b):
        return a > b

    def clean(self, x):
        return x.size

    def __call__(self, value):
        file_size = self.clean(value)
        if self.compare(file_size, self.max_size):
            params = {'max_size': self.max_size}
            raise ValidationError(self.message, code=self.code, params=params)
