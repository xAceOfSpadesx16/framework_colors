from django.conf import settings
from colors.color_definitions import BootstrapColorChoices


CONFIG_DEFAULTS = {
    "default": {
        "choices": BootstrapColorChoices,
        "color_type": "BACKGROUND",
        "only_use_custom_colors": False,
    }
}


def get_config():
    USER_CONFIG = getattr(settings, "COLORS_APP_CONFIG", {})
    CONFIG = CONFIG_DEFAULTS.copy()
    CONFIG.update(USER_CONFIG)
    return CONFIG
