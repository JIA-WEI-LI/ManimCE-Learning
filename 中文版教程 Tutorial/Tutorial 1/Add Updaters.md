# Add Updaters
## Code 程式碼
```python
%%manim -qm -v WARNING AddUpdaters
class AddUpdaters(Scene):
  def construct(self):
    rectangle = RoundedRectangle(
        stroke_width=8, color=WHITE, fill_color=BLUE_B, width=4.5, height=2
    ).shift(UP*3+LEFT*4)

    mathText = MathTex("\\frac{3}{4} = 0.75").set_color_by_gradient(GREEN, PINK).set(height=1.5)
    mathText.move_to(rectangle.get_center())
    mathText.add_updater(lambda x: x.move_to(rectangle.get_center()))
    
    self.play(FadeIn(rectangle))
    self.play(Write(mathText))
    self.play(rectangle.animate.shift(RIGHT*1.5+DOWN*5), run_time=6)
    self.wait()
    mathText.clear_updaters()
    self.play(rectangle.animate.shift(LEFT*2+UP*1), run_time=6)
```

## Video 影片

https://user-images.githubusercontent.com/119060520/206652740-bf815cb4-2505-446a-b586-0f101667413c.mp4


## 練習使用
&emsp;&emsp;如果不熟悉關於顏色及大小設定或數學方面的移動，這裡有一個簡單、較為直觀且易上手的 Colab 範例，可以僅靠調整數據達到自定義動畫的目的，
建議可以開多個視窗自我練習上述同時，並試著自行改變數值：
[Colab Example/Manim_Tutorial_1.ipynb](https://github.com/JIA-WEI-LI/ManimCE-Learning/blob/d02088c48a90b9f835a4e489a1efefef38d904db/Colab%20Example/Manim_Tutorial_1.ipynb)

## 參考資料
[Manim Tutorial | Updater Animations | Tutorial 1, Manim Explained](https://www.youtube.com/watch?v=MOv6yN7b2aI)
