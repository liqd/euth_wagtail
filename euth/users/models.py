from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from euth.contrib import validators as euth_validators

USERNAME_INVALID_MESSAGE = _('Enter a valid username. This value may contain '
                             'only letters, digits, spaces and @/./+/-/_ '
                             'characters. It must start with a digit or a '
                             'letter.')
USERNAME_NOT_UNIQUE = _('A user with that username already exists.')
USERNAME_HELP = _('Required. 60 characters or fewer. Letters, digits, spaces '
                  'and @/./+/-/_ only.')
USERNAME_VALIDATOR = validators.RegexValidator(r'^[\w]+[ \w.@+-]*$',
                                               USERNAME_INVALID_MESSAGE,
                                               'invalid')

EMAIL_NOT_UNIQUE = _('A user with that email address already exists.')

IS_STAFF_HELP = _('Designates whether the user can log into this admin site.')
IS_ACTIVE_HELP = _('Designates whether this user should be treated as active. '
                   'Unselect this instead of deleting accounts.')


class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    username = models.CharField(_('username'),
                                max_length=60, unique=True,
                                help_text=USERNAME_HELP,
                                validators=[USERNAME_VALIDATOR],
                                error_messages={
                                    'unique': _(USERNAME_NOT_UNIQUE),
    })

    email = models.EmailField(_('email address'), unique=True,
                              error_messages={
                                  'unique': EMAIL_NOT_UNIQUE,
    })
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=IS_STAFF_HELP)
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=IS_ACTIVE_HELP)
    date_joined = models.DateTimeField(editable=False, default=timezone.now)
    avatar = models.ImageField(upload_to='users/images', blank=True,
                               validators=[euth_validators.validate_logo])

    objects = auth_models.UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s <%s>' % (self.username, self.email)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.username

    def signup(self, username, email, commit=True):
        """Update the fields required for sign-up."""
        self.username = username
        self.email = email
        if commit:
            self.save()
