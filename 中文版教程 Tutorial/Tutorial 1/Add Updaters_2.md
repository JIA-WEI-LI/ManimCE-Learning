# Add Updater_2
## Code 程式碼
```python
%%manim -qm -v WARNING AddUpdaters_2
class AddUpdaters_2(Scene):
  def construct(self):
    r = ValueTracker(0.5)
    circle = always_redraw(
        lambda: Circle(radius=r.get_value(), stroke_color=YELLOW, stroke_width=5)
    )
    line_radius = always_redraw(
        lambda: Line(start=circle.get_center(), end=circle.get_bottom(), stroke_color=RED_B, stroke_width=10)
    )
    line_circumference = always_redraw(
        lambda: Line(stroke_color=YELLOW, stroke_width=5).set(length=2*r.get_value()*PI).next_to(circle, DOWN, buff=0.2)
    )
    triangle = always_redraw(
        lambda: Polygon(circle.get_top(), circle.get_left(), circle.get_right(), fill_color=GREEN_C)
    )

    self.play(
        LaggedStart(Create(circle), DrawBorderThenFill(line_radius), DrawBorderThenFill(triangle)),
        run_time=4, lag_ratio=0.75
    )
    self.play(ReplacementTransform(circle.copy(), line_circumference), run_time=2)
    self.play(r.animate.set_value(2), run_time=5)
```
## Video 影片



## 練習使用
&emsp;&emsp;如果不熟悉關於顏色及大小設定或數學方面的移動，這裡有一個簡單、較為直觀且易上手的 Colab 範例，可以僅靠調整數據達到自定義動畫的目的，建議可以開多個視窗自我練習上述同時，並試著自行改變數值：
[Colab Example/Manim_Tutorial_1.ipynb](https://github.com/JIA-WEI-LI/ManimCE-Learning/blob/d02088c48a90b9f835a4e489a1efefef38d904db/Colab%20Example/Manim_Tutorial_1.ipynb)

## 參考資料
[Manim Tutorial | Updater Animations | Tutorial 1, Manim Explained](https://www.youtube.com/watch?v=MOv6yN7b2aI)
