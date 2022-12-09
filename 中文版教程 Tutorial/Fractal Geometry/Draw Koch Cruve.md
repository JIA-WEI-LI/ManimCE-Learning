# Draw Koch Cruve 繪製科赫曲線
> refer to https://gitlab.com/cw-manim/koch-curve
```python
%%manim -qm -v WARNING DrawKochCurve
class DrawKochCurve(Scene):
  def construct(self):
    # ManimCELogo(self)

    def KochCurve(n, length=12, stroke_width=8, color=("#5544FF", "#88FF88", "#FF3322")):
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
```

## 成品
https://user-images.githubusercontent.com/119060520/205667737-7c1490df-325d-41be-89ce-8759cf5ab43e.mp4

> Colab 連結：https://colab.research.google.com/drive/1RmXT0d_uOWYia0Q-Q6tZzJ9_2Y02Uhto#scrollTo=xURUy-y7UOcl
