"""Color definitions for various CSS frameworks."""

from collections import namedtuple
from enum import Enum

Color = namedtuple("Color", ["name", "bg_css_class", "text_css_class"])


class Bootstrap5(Enum):
    BLUE = Color("Blue", "bg-primary-200", "text-primary")
    GREEN = Color("Green", "bg-success-200", "text-success")
    YELLOW = Color("Yellow", "bg-warning-200", "text-warning")
    RED = Color("Red", "bg-danger-200", "text-danger")
    PURPLE = Color("Purple", "bg-purple-200", "text-purple")
    INDIGO = Color("Indigo", "bg-indigo-200", "text-indigo")
    PINK = Color("Pink", "bg-pink-200", "text-pink")
    ORANGE = Color("Orange", "bg-orange-200", "text-orange")
    TEAL = Color("Teal", "bg-teal-200", "text-teal")
    CYAN = Color("Cyan", "bg-cyan-200", "text-cyan")
    GRAY = Color("Gray", "bg-gray-200", "text-gray")
