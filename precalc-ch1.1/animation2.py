from manim import *
import random,math
        
class Animation2(Scene):    
    text = [
        MathTex("x").shift(UP * 3),
        Tex("Multiply by 2"),
        Tex("Add 1"),
        MathTex("y")
    ]
    
    def displayFunctionMachine(self):
        text = self.text
        
        self.play(text[0].animate.shift(DOWN * 3.5 + LEFT * 5.5))

        for i in range(1,4):
            text[i]=text[i].next_to(text[i-1],RIGHT,buff=2)

        arrow = [
            Arrow(start=text[i].get_right(), end=text[i+1].get_left(), buff=0.3) for i in range(3)
        ]

        formula = [
            MathTex("x").shift(LEFT * 5.5),
            MathTex("2x").next_to(text[1],UP,buff=1),
            MathTex("2x + 1").next_to(text[2],UP,buff=1),
            MathTex("2x + 1").next_to(text[3],UP,buff=1)
        ]

        for i in range(1,4):
            self.play(Create(arrow[i-1]))
            if(i==0):
                self.play(Write(text[i]),Write(formulas[i]))
            elif(i==1 or i==2):
                self.play(
                    Write(text[i]),
                    Create(SurroundingRectangle(text[i],color=WHITE,buff=0.3)),
                    Transform(formula[i-1],formula[i])
                )
            else:
                self.play(Write(text[i]),Transform(formula[i-1],formula[i]))
           

    def demonstrateFunction(self,num,rt=1):
        text = self.text
        initial = num
        exampleColor=rgb_to_color((128,255,32))
        exampleNumber = [
            Integer(number=initial).set_color(exampleColor).next_to(text[0],UP,buff=2),
            Integer(number=initial * 2).set_color(exampleColor).next_to(text[1],UP,buff=2),
            Integer(number=initial * 2 + 1).set_color(exampleColor).next_to(text[2],UP,buff=2),
            Integer(number=initial * 2 + 1).set_color(exampleColor).next_to(text[3],UP,buff=2)
        ]

        self.play(Write(exampleNumber[0]))

        initialLabel = MathTex("x = " + str(initial)).set_color(exampleColor).next_to(text[0],DOWN,buff=1)
        finalLabel = MathTex("y = " + str(initial * 2 + 1)).set_color(exampleColor).next_to(text[3],DOWN,buff=1)

        self.play(Write(initialLabel))
        
        for i in range(1,4):
            self.play(Transform(exampleNumber[i-1],exampleNumber[i]),run_time=rt)
            self.wait(0.166*math.log(rt)+0.6)
            if(i!=3):
                self.remove(exampleNumber[i-1])

        self.play(Write(finalLabel))
        
        bigArrow=Arrow(start=initialLabel.get_right(),end=finalLabel.get_left(),color=exampleColor, buff=0.3)
        mapToText=Tex("is mapped to").set_color(exampleColor).next_to(bigArrow,DOWN)
        self.play(Create(bigArrow),Create(mapToText))
        
        self.play(exampleNumber[2].animate.shift(RIGHT * 4),run_time=rt)
        self.play(Uncreate(initialLabel),Uncreate(finalLabel),Uncreate(bigArrow),Uncreate(mapToText))



    def demonstrateFunctionCustom(self,ini,twoini,twoiniplusone,rt=1):
        text = self.text
        exampleColor=rgb_to_color((128,255,32))
        exampleNumber = [
            MathTex(ini).set_color(exampleColor).next_to(text[0],UP,buff=2),
            MathTex(twoini).set_color(exampleColor).next_to(text[1],UP,buff=2),
            MathTex(twoiniplusone).set_color(exampleColor).next_to(text[2],UP,buff=2),
            MathTex(twoiniplusone).set_color(exampleColor).next_to(text[3],UP,buff=2)
        ]

        self.play(Write(exampleNumber[0]))

        initialLabel = MathTex("x = " + ini).set_color(exampleColor).next_to(text[0],DOWN,buff=1)
        finalLabel = MathTex("y = " + twoiniplusone).set_color(exampleColor).next_to(text[3],DOWN,buff=1)

        self.play(Write(initialLabel))
        
        for i in range(1,4):
            self.play(Transform(exampleNumber[i-1],exampleNumber[i]),run_time=rt)
            self.wait(0.166*math.log(rt)+0.6)
            if(i!=3):
                self.remove(exampleNumber[i-1])

        self.play(Write(finalLabel))

        bigArrow=Arrow(start=initialLabel.get_right(),end=finalLabel.get_left(),color=exampleColor, buff=0.3)
        mapToText=Tex("is mapped to").set_color(exampleColor).next_to(bigArrow,DOWN)
        self.play(Create(bigArrow),Create(mapToText))
        
        self.play(exampleNumber[2].animate.shift(RIGHT * 4),run_time=rt)
        self.play(Uncreate(initialLabel),Uncreate(finalLabel),Uncreate(bigArrow),Uncreate(mapToText))

                
    def functionExample(self):
        text = self.text
        
        exampleFunction = MathTex("y = 2x + 1")
        self.play(Write(exampleFunction))

        self.wait(3)
        
        self.play(exampleFunction.animate.shift(UP * 3))
        self.displayFunctionMachine()

        self.wait(2)
        self.demonstrateFunction(3,2)
        self.wait(2)
        
        for i in range(2):
            self.demonstrateFunction(random.randint(1,50),0.5)
        self.demonstrateFunctionCustom(r"\frac73",r"\frac{14}{3}",r"\frac{17}{3}",0.6)
        self.demonstrateFunctionCustom("0.47","0.94","1.94",0.6)
        self.demonstrateFunctionCustom(r"\pi",r"2\pi",r"2\pi + 1",0.6)
        self.demonstrateFunctionCustom(r"\sqrt{2}",r"2\sqrt{2}",r"2\sqrt{2} + 1",0.6)
    
    def construct(self):
        self.functionExample()
