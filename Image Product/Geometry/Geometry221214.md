# Quadrilateral Diagonal
## Code 程式碼
```python
%%manim -qm -v WARNING Geometry221214
class Geometry221214(Scene):
  def construct(self):
    # Draw Graph
    line_1 = Line(np.array([-2, 0, 0]), np.array([2, 0, 0]))
    dot_rot = Dot(line_1.point_from_proportion(0.35)).set_color(RED)
    line_2 = line_1.copy().rotate(90*DEGREES, about_point=dot_rot.get_center()).scale(1.2)
    dots = list(range(4))
    dots[0] = Dot(line_1.get_start()).scale(0)
    dots[1] = Dot(line_2.get_start()).scale(0)
    dots[2] = Dot(line_1.get_end()).scale(0)
    dots[3] = Dot(line_2.get_end()).scale(0)

    dots = VGroup(*[i for i in dots])
    lines = list()
    for i in range(len(dots)):
      for j in range(len(dots)):
        if i < j:
          lines.append(Line(dots[i].get_center(), dots[j].get_center()))
    lines = VGroup(*[i for i in lines])

    # Rightangle
    rightangle = Square(color=WHITE, fill_opacity=0).scale(0.1).align_to(dot_rot, RIGHT+DOWN).shift(np.array([-0.08, 0.08, 0]))
    graph = VGroup(lines, rightangle, dots).rotate(10*DEGREES)

    dot_labels = ['A', 'B', 'C', 'D']
    dot_label_pos = [LEFT, DOWN, RIGHT, UP]
    num_labels = list(range(3))
    for i, j in enumerate(dot_labels):
      dot_labels[i] = MathTex(j).next_to(dots[i], dot_label_pos[i])
    for i in list(range(3)):
      num_labels[i] = MathTex(i+3).move_to(Dot(Line(dot_labels[i].get_center(), dot_labels[i+1].get_center()).get_center()))

    mark_ques = MathTex('?').move_to(Dot(Line(dot_labels[3].get_center(), dot_labels[0].get_center()).get_center()))
    all_graph = VGroup(graph, *[i for i in dot_labels], *[i for i in num_labels], mark_ques, dot_rot.scale(0))
  
    self.add(all_graph.shift(DOWN*0.5))
```

## Image 圖像
![Geometry221214](https://user-images.githubusercontent.com/119060520/207645400-6d172953-ab46-4345-9f1a-f5357febbc56.png)

