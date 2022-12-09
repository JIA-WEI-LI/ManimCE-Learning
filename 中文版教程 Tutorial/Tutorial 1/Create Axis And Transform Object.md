# Create Axis And Transform Object
## Code 程式碼
```python
class CreateAxisAndTransformObject(Scene):
  def construct(self):
    axes = Axes( x_range=[-3,3,1], y_range=[-3,3,1], x_length=6, y_length=6)
    axes.to_edge(LEFT, buff=0.5)
    
    circle = Circle(radius=6, color=YELLOW, stroke_opacity=1, fill_color=RED_C, fill_opacity=0.8)
    circle.set(width=2).to_edge(DR, buff=0)
    triangle = Triangle(color=ORANGE, stroke_opacity=1, fill_color=GREY, fill_opacity=1).set(height=2).shift(DOWN*3+RIGHT*3)
    self.play(Write(axes))
    self.play(DrawBorderThenFill(circle))
    self.play(circle.animate.set_width(1))
    self.play(Transform(circle, triangle), run_time=3)
```
## Video 影片

https://user-images.githubusercontent.com/119060520/204139451-1b7189ae-3a3e-4e27-948b-b4a42741d684.mp4


## 代碼解析
&emsp;&emsp;

### Create Axis 創建坐標軸
```python

```

### Transform Object 轉換物件
```python

```

## 練習使用
&emsp;&emsp;如果不熟悉關於顏色及大小設定或數學方面的移動，這裡有一個簡單、較為直觀且易上手的 Colab 範例，可以僅靠調整數據達到自定義動畫的目的，
建議可以開多個視窗自我練習上述同時，並試著自行改變數值：
[Colab Example/Manim_Tutorial_1.ipynb](https://github.com/JIA-WEI-LI/ManimCE-Learning/blob/d02088c48a90b9f835a4e489a1efefef38d904db/Colab%20Example/Manim_Tutorial_1.ipynb)

## 官方網站關鍵字

## 參考資料
[Manim Tutorial | Updater Animations | Tutorial 1, Manim Explained](https://www.youtube.com/watch?v=MOv6yN7b2aI)
