# pyright: reportWildcardImportFromLibrary=false
from manim import *
from manim.utils.color import ManimColor

BG_COLOR = ManimColor("#000000")
ACCENT_BLUE = ManimColor("#58C4DD")
PURE_WHITE = ManimColor("#FFFFFF")
DIM_GREY = ManimColor("#2A2A2A")


class StyledScene(MovingCameraScene):
    pass