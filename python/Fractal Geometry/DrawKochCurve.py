import math
from manim import *

class DrawKochCurve(Scene):
  def construct(self):
    # ManimCELogo(self)

    def KochCurve(n, length=12, stroke_width=8, color=("#0A68EF", "#4AF1F2", "#0A68EF")):
      l = length / (3 ** n)
      LineGroup = Line().set_length(l)

      def NextLevel(LineGroup):
        return VGroup(*[LineGroup.copy().rotate(i) for i in [0, PI/3, -PI/3, 0]]).arrange(RIGHT, buff=0, aligned_edge=DOWN)
      
      for i in range(n):
        LineGroup = NextLevel(LineGroup)
      koch_curve = (VMobject(stroke_width=stroke_width).set_points(LineGroup.get_all_points()).set_color(color))
      return koch_curve

    level = Variable(0, Tex("level"), var_type=Integer).set_color("#4AF1F2")
    txt = (VGroup(Tex("Koch Curve", font_size=60), level).arrange(DOWN, aligned_edge=LEFT).to_corner(UL))
    koch = KochCurve(0, stroke_width=12).to_edge(DOWN, buff=2.5)

    self.add(txt, koch)
    self.wait()

    for i in range(1, 6):
      self.play(
          level.tracker.animate.set_value(i),
          koch.animate.become(KochCurve(i, stroke_width=12-(2*i)).to_edge(DOWN, buff=2.5))
          )
      self.wait()

    for i in range(4, -1, -1):
      self.play(
          level.tracker.animate.set_value(i),
          koch.animate.become(KochCurve(i, stroke_width=12 - (2 * i)).to_edge(DOWN, buff=2.5))
          )
      self.wait()
