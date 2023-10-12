from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "redwind01_com_cookie_cutter_starter.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import redwind01_com_cookie_cutter_starter.users.signals  # noqa: F401
        except ImportError:
            pass
