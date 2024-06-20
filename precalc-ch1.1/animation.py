from manim import *

class Animation(Scene):
    def reviewFunction(self):
        textFunction = [
            MathTex("y = 2x + 1").shift(UP * 2),
            MathTex("y = 3x^2 - 6x + 4").shift(UP),
            MathTex("y = x^4 + 4x^3 - 7x^2 + 5x + 3"),
            MathTex(r"y = \frac{x^2 + 3x + 2}{x + 1}").shift(DOWN),
            MathTex(r"y = 2 \sin(4x + 6) - 4").shift(DOWN * 2)
        ]
        for i in range(5):
            self.play(Write(textFunction[i]))
            self.wait(1)

        unwriteAnimation = [Unwrite(x) for x in textFunction]
        self.play(*unwriteAnimation)
        
    def whatIsAFunction(self):
        question = Tex("But what exactly is a function?", color=ORANGE).shift(UP * 2)
        answer = Tex(r"A \underline{function} is a mathematical relation \\ that maps a set of input values to a set of output values \\ such that each input value \\ is mapped to exactly one outout value.")
        self.play(Write(question))
        self.wait(1)
        self.play(Write(answer))
        self.wait(1)
        self.play(Unwrite(question),Unwrite(answer))
        
    def construct(self):
        self.reviewFunction()
        self.wait(1)
        self.whatIsAFunction()
