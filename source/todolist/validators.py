from django.core.validators import BaseValidator

from django.utils.deconstruct import deconstructible
from django.utils.translation import ngettext_lazy


@deconstructible
class MinLengthValidator(BaseValidator):
    message = 'Длина поля "%(value)s" состаляет %(show_value)d! Значение должно состоять минимум из %(limit_value)d символов!'
    code = 'too_short'

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)


class MaxLengthValidator(BaseValidator):
    message = ngettext_lazy(
        'Длина этого поля может составлять максимум %(limit_value)d значений (Вы ввели %(show_value)d значений).',
        'Длина этого поля может составлять максимум %(limit_value)d значений (Вы ввели %(show_value)d значений).',
        'limit_value')
    code = 'max_length'

    def compare(self, a, b):
        return a > b

    def clean(self, x):
        return len(x)