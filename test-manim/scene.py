from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()
        square.next_to(circle, RIGHT, buff=0.5)

        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4))
        self.play(Transform(square,circle))
        self.play(FadeOut(square))


class DiffRot(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        bl_square = Square(color=RED, fill_opacity=0.3).next_to(left_square, DOWN)
        br_square = Square(color=PURPLE, fill_opacity=0.3).next_to(right_square, DOWN)

        self.play(
            left_square.animate.rotate(PI),
            Rotate(right_square, angle=PI),
            bl_square.animate.flip(),
            br_square.animate.shift(2 * LEFT + 2 * UP),
            Transform(left_square,br_square),
            run_time = 2
        )
        self.wait()

class Functions(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-4,4,1],
            y_range=[-5,20,5],
            x_length=8,
            y_length=5,
            tips=True,
            axis_config={"include_numbers": True},
        )

        graph_qfunc = ax.plot(lambda t: t * t - 6, x_range=[-3.9,3.9],color=RED, use_smoothing=True)
        graph_qfunc2 = ax.plot(lambda t: 7 * np.sin(t), x_range=[-3.9,3.0],color=RED, use_smoothing=True)
        
        self.add(ax)
        self.play(Create(graph_qfunc))
        self.play(Transform(graph_qfunc,graph_qfunc2))
        self.wait()


class Texts(Scene):
    def construct(self):
        text=Tex('Here is a piece of text: $y = x^2 - 6$')

        self.play(Write(text))
