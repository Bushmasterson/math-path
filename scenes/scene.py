# pyright: reportWildcardImportFromLibrary=false
# pyright: reportAttributeAccessIssue=false

# ─── Force vertical 9:16 frame BEFORE anything else ───
from manim import config
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.frame_rate = 60
config.background_color = "#000000"

from manim import *
import math
import numpy as np

from _style import StyledScene, ACCENT_BLUE, PURE_WHITE, DIM_GREY

B = ACCENT_BLUE
W = PURE_WHITE
D = DIM_GREY

# Visible area: x ∈ [-4.5, 4.5], y ∈ [-8, 8]
# Safe zone (TikTok/Reels UI): content inside y ∈ [-6, 6]


class MathPath(StyledScene):
    """
    ~48s vertical (9:16) montage — TikTok / Reels / Shorts / X.
    Palette: black / white / blue. Brand: Math Path.
    """

    def construct(self) -> None:
        # ═══════════════════════════════════════════════════
        # ACT 1 · 0.0 – 2.0s · BRAND INTRO
        # ═══════════════════════════════════════════════════
        b1 = Text("MATH", color=W, font_size=170, weight=BOLD)
        b2 = Text("PATH", color=B, font_size=170, weight=BOLD)
        b2.next_to(b1, DOWN, buff=-0.1)
        logo = VGroup(b1, b2)

        self.camera.frame.save_state()
        self.camera.frame.scale(2.2)
        self.play(
            self.camera.frame.animate.restore(),
            FadeIn(logo, scale=0.4),
            run_time=0.8, rate_func=rush_from,
        )
        self.play(logo.animate.scale(1.08), run_time=0.2)
        self.play(
            logo.animate.scale(1 / 1.08).set_opacity(0),
            self.camera.frame.animate.scale(0.85),
            run_time=0.5, rate_func=rush_into,
        )
        self.camera.frame.restore()
        # 2.0s

        # ═══════════════════════════════════════════════════
        # ACT 2 · 2.0 – 9.5s · UNIT CIRCLE → SINE
        # ═══════════════════════════════════════════════════
        circle_c = np.array([0.0, 3.6, 0.0])
        circle = Circle(radius=1.4, color=B, stroke_width=5).move_to(circle_c)

        axes = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-1.3, 1.3, 1],
            x_length=8.0, y_length=2.4,
            axis_config={
                "stroke_color": W, "stroke_width": 2,
                "include_tip": False, "include_numbers": False,
            },
        ).move_to(np.array([0.0, -2.2, 0.0]))

        self.play(
            LaggedStart(Create(circle), Create(axes), lag_ratio=0.35),
            run_time=0.6, rate_func=rush_from,
        )

        theta = ValueTracker(0.0)

        def circle_pt() -> np.ndarray:
            a = theta.get_value()
            return circle_c + 1.4 * np.array([np.cos(a), np.sin(a), 0.0])

        def wave_pt() -> np.ndarray:
            return axes.c2p(theta.get_value(), np.sin(theta.get_value()))

        radius = always_redraw(lambda: Line(circle_c, circle_pt(), color=W, stroke_width=5))
        dot_c = always_redraw(lambda: Dot(circle_pt(), color=W, radius=0.11))
        dot_w = always_redraw(lambda: Dot(wave_pt(), color=B, radius=0.11))
        connector = always_redraw(lambda: DashedLine(
            circle_pt(), wave_pt(), color=D, stroke_width=1.5, dash_length=0.12
        ))
        sine_curve = always_redraw(lambda: axes.plot(
            np.sin, x_range=[0, max(theta.get_value(), 1e-3)],
            color=B, stroke_width=5,
        ))

        self.add(radius, dot_c, dot_w, connector, sine_curve)
        self.play(theta.animate.set_value(4 * PI), run_time=5.0, rate_func=linear)

        cos_curve = axes.plot(np.cos, x_range=[0, 4 * PI], color=W, stroke_width=3)
        sin_lbl = Text("sin", color=B, font_size=38, weight=BOLD)
        sin_lbl.move_to(np.array([-3.3, -0.9, 0.0]))
        cos_lbl = Text("cos", color=W, font_size=38, weight=BOLD)
        cos_lbl.move_to(np.array([-3.3, -1.5, 0.0]))

        self.play(
            Create(cos_curve),
            FadeIn(sin_lbl, shift=RIGHT * 0.2),
            FadeIn(cos_lbl, shift=RIGHT * 0.2),
            run_time=0.5,
        )
        self.wait(0.25)
        self.play(
            FadeOut(radius, dot_c, dot_w, connector, sine_curve,
                    cos_curve, sin_lbl, cos_lbl, circle, axes),
            run_time=0.35, rate_func=rush_into,
        )
        # 9.5s

        # ═══════════════════════════════════════════════════
        # ACT 3 · 9.5 – 13.5s · PYTHAGORAS
        # ═══════════════════════════════════════════════════
        a, b = 2.0, 3.0
        c = np.sqrt(a * a + b * b)

        triangle = Polygon(
            np.array([0.0, 0.0, 0.0]),
            np.array([a, 0.0, 0.0]),
            np.array([0.0, b, 0.0]),
            color=W, stroke_width=5,
            fill_color=B, fill_opacity=0.15,
        )

        sq_a = Square(side_length=a, color=B, stroke_width=4, fill_opacity=0.15)
        sq_a.next_to(triangle, DOWN, buff=0)
        sq_b = Square(side_length=b, color=B, stroke_width=4, fill_opacity=0.15)
        sq_b.next_to(triangle, LEFT, buff=0)

        sq_c = Square(side_length=c, color=W, stroke_width=4, fill_opacity=0.15)
        sq_c.rotate(np.arctan2(b, a))
        sq_c.move_to(np.array([-a / 2, b / 2, 0.0]))

        grp = VGroup(triangle, sq_a, sq_b, sq_c)
        grp.move_to(np.array([0.5, 1.5, 0.0]))
        grp.scale(0.9)

        formula = MathTex(r"a^2", r"+", r"b^2", r"=", r"c^2", font_size=100)
        formula[0].set_color(B)
        formula[1].set_color(W)
        formula[2].set_color(B)
        formula[3].set_color(W)
        formula[4].set_color(W)
        formula.move_to(np.array([0.0, -5.0, 0.0]))

        self.play(Create(triangle), run_time=0.3, rate_func=rush_from)
        self.play(Create(sq_a), Create(sq_b), run_time=0.35)
        self.play(Create(sq_c), run_time=0.3)
        self.play(Write(formula), run_time=0.45)
        self.play(formula[4].animate.set_color(B).scale(1.25), run_time=0.2)
        self.play(formula[4].animate.scale(1 / 1.25).set_color(W), run_time=0.2)
        self.wait(0.35)
        self.play(FadeOut(grp, formula), run_time=0.3, rate_func=rush_into)
        # 13.5s

        # ═══════════════════════════════════════════════════
        # ACT 4 · 13.5 – 19.5s · COMPLEX PLANE · e^(iθ)
        # ═══════════════════════════════════════════════════
        cp = ComplexPlane(
            x_range=[-2, 2, 1], y_range=[-2, 2, 1],
            x_length=5.4, y_length=5.4,
            background_line_style={"stroke_color": D, "stroke_width": 1},
            axis_config={"stroke_color": W, "stroke_width": 2},
        ).move_to(np.array([0.0, -0.4, 0.0]))

        euler = MathTex(r"e^{i\theta}", font_size=100, color=W)
        euler.move_to(np.array([0.0, 5.0, 0.0]))

        self.play(Create(cp, run_time=0.4, rate_func=rush_from),
                  Write(euler, run_time=0.4))

        tt = ValueTracker(0.0)

        def rot_pt() -> np.ndarray:
            ang = tt.get_value()
            return cp.c2p(np.cos(ang), np.sin(ang))

        vec = always_redraw(lambda: Line(cp.c2p(0, 0), rot_pt(), color=W, stroke_width=5))
        dot = always_redraw(lambda: Dot(rot_pt(), color=B, radius=0.13))
        spiral = always_redraw(lambda: ParametricFunction(
            lambda ang: cp.c2p(np.cos(ang), np.sin(ang)),
            t_range=(0, max(tt.get_value(), 1e-3), 0.02),
            color=B, stroke_width=3,
        ))

        self.add(spiral, vec, dot)
        self.play(tt.animate.set_value(6 * PI), run_time=4.8, rate_func=linear)
        self.wait(0.2)
        self.play(FadeOut(spiral, vec, dot, cp, euler), run_time=0.3, rate_func=rush_into)
        # 19.5s

        # ═══════════════════════════════════════════════════
        # ACT 5 · 19.5 – 25.0s · FOURIER PARTIAL SUMS
        # ═══════════════════════════════════════════════════
        faxes = Axes(
            x_range=[-PI, PI, PI / 2],
            y_range=[-1.4, 1.4, 1],
            x_length=8.0, y_length=3.0,
            axis_config={
                "stroke_color": W, "stroke_width": 2,
                "include_tip": False, "include_numbers": False,
            },
        ).move_to(np.array([0.0, -0.3, 0.0]))

        four_lbl = MathTex(
            r"f(x) = \sum_{n=1}^{N} \frac{\sin((2n-1)x)}{2n-1}",
            font_size=46, color=W,
        ).move_to(np.array([0.0, 5.0, 0.0]))

        self.play(Create(faxes, run_time=0.4, rate_func=rush_from),
                  Write(four_lbl, run_time=0.45))

        def partial(n: int):
            def f(x: float) -> float:
                s = 0.0
                for k in range(1, n + 1):
                    s += (4 / PI) * np.sin((2 * k - 1) * x) / (2 * k - 1)
                return s
            return f

        wave = None
        for n in [1, 3, 7, 15, 31, 63]:
            new = faxes.plot(partial(n), x_range=[-PI, PI, 0.004],
                             color=B, stroke_width=3)
            if wave is None:
                wave = new
                self.play(Create(wave), run_time=0.35, rate_func=rush_from)
            else:
                self.play(Transform(wave, new), run_time=0.4)
        self.wait(0.3)
        self.play(FadeOut(faxes, wave, four_lbl), run_time=0.3, rate_func=rush_into)
        # 25.0s

        # ═══════════════════════════════════════════════════
        # ACT 6 · 25.0 – 30.5s · TAYLOR → sin(x)
        # ═══════════════════════════════════════════════════
        taxes = Axes(
            x_range=[-PI, PI, PI / 2],
            y_range=[-1.4, 1.4, 1],
            x_length=8.0, y_length=3.0,
            axis_config={
                "stroke_color": W, "stroke_width": 2,
                "include_tip": False, "include_numbers": False,
            },
        ).move_to(np.array([0.0, -0.3, 0.0]))

        sin_ref = taxes.plot(np.sin, x_range=[-PI, PI, 0.005],
                             color=D, stroke_width=3)

        tay_lbl = MathTex(
            r"\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots",
            font_size=44, color=W,
        ).move_to(np.array([0.0, 5.0, 0.0]))

        self.play(Create(taxes, run_time=0.35, rate_func=rush_from),
                  Create(sin_ref, run_time=0.35),
                  Write(tay_lbl, run_time=0.45))

        def taylor_sin(n_terms: int):
            def f(x: float) -> float:
                s = 0.0
                for k in range(n_terms):
                    s += ((-1) ** k) * (x ** (2 * k + 1)) / math.factorial(2 * k + 1)
                return s
            return f

        tcurve = None
        for n in [1, 2, 3, 4, 5, 6, 8]:
            new = taxes.plot(taylor_sin(n), x_range=[-PI, PI, 0.004],
                             color=B, stroke_width=3)
            if tcurve is None:
                tcurve = new
                self.play(Create(tcurve), run_time=0.3, rate_func=rush_from)
            else:
                self.play(Transform(tcurve, new), run_time=0.35)
        self.wait(0.2)
        self.play(FadeOut(taxes, sin_ref, tcurve, tay_lbl),
                  run_time=0.3, rate_func=rush_into)
        # 30.5s

        # ═══════════════════════════════════════════════════
        # ACT 7 · 30.5 – 36.0s · DERIVATIVE · TANGENT
        # ═══════════════════════════════════════════════════
        daxes = Axes(
            x_range=[-1, 4, 1], y_range=[-0.5, 4, 1],
            x_length=7.0, y_length=5.2,
            axis_config={
                "stroke_color": W, "stroke_width": 2,
                "include_tip": False, "include_numbers": False,
            },
        ).move_to(np.array([0.0, -0.5, 0.0]))

        fcurve = daxes.plot(lambda x: 0.4 * x * x, color=B, stroke_width=5)
        f_lbl = MathTex(r"f(x) = \tfrac{1}{2}x^2", font_size=60, color=W)
        f_lbl.move_to(np.array([0.0, 5.4, 0.0]))

        self.play(Create(daxes, run_time=0.35, rate_func=rush_from),
                  Create(fcurve, run_time=0.45),
                  Write(f_lbl, run_time=0.35))

        x0 = ValueTracker(0.7)

        def tangent_line():
            xv = x0.get_value()
            slope = 0.8 * xv
            yv = 0.4 * xv * xv
            p1 = daxes.c2p(xv - 0.7, yv - slope * 0.7)
            p2 = daxes.c2p(xv + 0.7, yv + slope * 0.7)
            return Line(p1, p2, color=W, stroke_width=5)

        tangent = always_redraw(tangent_line)
        tdot = always_redraw(lambda: Dot(
            daxes.c2p(x0.get_value(), 0.4 * x0.get_value() ** 2),
            color=B, radius=0.12,
        ))

        deriv_lbl = MathTex(r"f'(x) = x", font_size=60, color=B)
        deriv_lbl.move_to(np.array([0.0, -5.0, 0.0]))

        self.add(tangent, tdot)
        self.play(FadeIn(deriv_lbl, shift=UP * 0.2), run_time=0.35)
        self.play(x0.animate.set_value(3.2), run_time=1.2, rate_func=smooth)
        self.play(x0.animate.set_value(0.7), run_time=0.9, rate_func=smooth)
        self.play(x0.animate.set_value(2.8), run_time=0.8, rate_func=smooth)
        self.wait(0.2)
        self.play(FadeOut(daxes, fcurve, tangent, tdot, f_lbl, deriv_lbl),
                  run_time=0.3, rate_func=rush_into)
        # 36.0s

        # ═══════════════════════════════════════════════════
        # ACT 8 · 36.0 – 41.5s · INTEGRAL · RIEMANN
        # ═══════════════════════════════════════════════════
        iaxes = Axes(
            x_range=[-0.3, 4, 1], y_range=[-0.3, 3, 1],
            x_length=7.0, y_length=4.5,
            axis_config={
                "stroke_color": W, "stroke_width": 2,
                "include_tip": False, "include_numbers": False,
            },
        ).move_to(np.array([0.0, -0.5, 0.0]))

        gcurve = iaxes.plot(
            lambda x: 0.6 * np.sin(x) + 1.4,
            x_range=[0, 3.5], color=B, stroke_width=5,
        )
        i_lbl = MathTex(r"\int_0^b f(x)\,dx", font_size=70, color=W)
        i_lbl.move_to(np.array([0.0, 5.4, 0.0]))

        self.play(Create(iaxes, run_time=0.35, rate_func=rush_from),
                  Create(gcurve, run_time=0.45),
                  Write(i_lbl, run_time=0.35))

        xr = ValueTracker(0.01)

        def riemann():
            xv = xr.get_value()
            n = max(int(xv * 8), 1)
            dx = xv / n
            rects = VGroup()
            for i in range(n):
                xl = i * dx
                h = 0.6 * np.sin(xl) + 1.4
                r = Rectangle(
                    width=iaxes.c2p(dx, 0)[0] - iaxes.c2p(0, 0)[0],
                    height=iaxes.c2p(0, h)[1] - iaxes.c2p(0, 0)[1],
                    color=W, fill_opacity=0.4, stroke_width=1,
                )
                r.move_to(iaxes.c2p(xl + dx / 2, h / 2))
                rects.add(r)
            return rects

        ri = always_redraw(riemann)
        self.add(ri)
        self.play(xr.animate.set_value(3.5), run_time=2.8, rate_func=linear)

        area = MathTex(r"\text{Area} = \int_0^{3.5} f(x)\,dx",
                       font_size=48, color=B)
        area.move_to(np.array([0.0, -5.0, 0.0]))
        self.play(FadeIn(area), run_time=0.35)
        self.wait(0.2)
        self.play(FadeOut(iaxes, gcurve, ri, i_lbl, area),
                  run_time=0.3, rate_func=rush_into)
        # 41.5s

        # ═══════════════════════════════════════════════════
        # ACT 9 · 41.5 – 45.5s · FORMULA FLASHES
        # ═══════════════════════════════════════════════════
        flashes = [
            MathTex(r"\int_a^b f(x)\,dx", font_size=140, color=W),
            MathTex(r"\frac{d}{dx}\,e^{x} = e^{x}", font_size=120, color=B),
            MathTex(r"e^{i\pi} + 1 = 0", font_size=150, color=W),
            MathTex(r"\zeta(2) = \frac{\pi^{2}}{6}", font_size=140, color=B),
        ]

        for f in flashes:
            f.move_to(ORIGIN)
            self.play(FadeIn(f, scale=1.5, shift=UP * 0.15),
                      run_time=0.22, rate_func=rush_from)
            self.play(FadeOut(f, scale=0.7, shift=DOWN * 0.15),
                      run_time=0.18, rate_func=rush_into)
        # 4 × 0.4 = 1.6s + overhead ≈ 4.0s → 45.5s

        # ═══════════════════════════════════════════════════
        # ACT 10 · 45.5 – 48.0s · FINALE
        # ═══════════════════════════════════════════════════
        fa = Text("MATH", color=W, font_size=190, weight=BOLD)
        fb = Text("PATH", color=B, font_size=190, weight=BOLD)
        fb.next_to(fa, DOWN, buff=-0.1)
        fg = VGroup(fa, fb)

        tagline = Text("FOLLOW THE PATTERN", color=D, font_size=34, weight=BOLD)
        tagline.next_to(fg, DOWN, buff=0.6)

        self.camera.frame.save_state()
        self.camera.frame.scale(1.5)

        self.play(
            FadeIn(fg, scale=0.5),
            self.camera.frame.animate.restore(),
            run_time=0.7, rate_func=rush_from,
        )
        self.play(FadeIn(tagline, shift=UP * 0.15), run_time=0.35)
        self.play(fg.animate.scale(1.06), tagline.animate.scale(1.06),
                  run_time=0.3)
        self.play(fg.animate.scale(1 / 1.06).set_opacity(0),
                  tagline.animate.scale(1 / 1.06).set_opacity(0),
                  self.camera.frame.animate.scale(0.75),
                  run_time=0.55, rate_func=rush_into)
        self.camera.frame.restore()
        self.wait(0.3)
        # 48.0s