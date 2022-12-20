from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ModerationConfig(AppConfig):
    name = 'content_moderation.moderation'

    def ready(self):
        try:
            import content_moderation.moderation.signals  # noqa F401
        except ImportError:
            pass
