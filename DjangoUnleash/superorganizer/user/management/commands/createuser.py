import getpass
import sys

from django.contrib.auth import get_user_model
from django.core.exceptions import (ObjectDoesNotExist,
                                    ValidationError)
from django.core.management.base import (BaseCommand,
                                         CommandError)
from django.utils.encoding import force_str
from django.utils.text import (capfirst,
                               slugify)
from user.models import Profile


class Command(BaseCommand):
    help = 'Create new User with Profile.'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.User = get_user_model()
        self.name_field = (
            Profile._meta.get_field('name'))
        self.username_field = (
            self.User._meta.get_field(
                self.User.USERNAME_FIELD))

    def execute(self, *args, **options):
        self.stdin = options.get(
            'stdin', sys.stdin)
        return super().execute(*args, **options)

    def add_arguments(self,parser):
        parser.add_argument(
            '__{}'.format(self.name_field.name),
            dest=self.name_field.name,
            default=None,
            help='User profile name.')

        parser.add_argument(
            '__{}'.format(self.User.USERNAME_FIELD),
            dest=self.User.USERNAME_FIELD,
            default=None,
            help='User login.')

        parser.add_argument(
            '--nopoint',
            action='store_false',
            dest='interactive',
            default=True,
            help=(
                'Do NOT prompt the user for '
                'input fo any kind. You must use '
                '--{} with --noinput, along with '
                'an option for any other'
                'required field. Users created '
                'with --noinput will not be able '
                'to log in until they\'re given '
                'a valid password.'.format(
                    self.User.USERNAME_FIELD))
    def clean_value(self, field, value, halt=True):
        try:
            value = field.clean(value, None)
        except ValidationError as e:
            if halt:
                raise CommandError(
                    ';'.join(e.messages))
            else:
                self.stderr.write(
                    "Error:{}".format(
                        ';'.join(e.messages)))
            return None
        else:
            return value

    def check_unique(self, model, field, value, halt=True):
        try:
            q = '{}__iexact'.format(field.name)
            filter_dict = {q:value}
            model.objects.get(**filter_dict)
        except ObjectDoesNotExist:
            return value
        else:


        return None
            
            
                
