# Graphing Movement
## Code 程式碼
```python
%%manim -qm -v WARNING GraphingMovement
class GraphingMovement(Scene):
  def construct(self):
    axes = Axes(
        x_range=[0, 5, 1], y_range=[0, 3, 1], x_length=5, y_length=3,
        axis_config={"include_tip":True, "numbers_to_exclude":[0]}
    ).add_coordinates()
    axes.to_edge(UR)
    axis_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

    graph = axes.plot(lambda x:x**0.5, x_range=[0, 4], color=YELLOW)
    graphing_stuff = VGroup(axes, graph, axis_labels)

    self.play(DrawBorderThenFill(axes), Write(axis_labels))
    self.play(Create(graph))
    self.play(graphing_stuff.animate.shift(DOWN*4))
    self.play(axes.animate.shift(LEFT*3), run_time=3)
```
## Video 影片

## 練習使用
&emsp;&emsp;如果不熟悉關於顏色及大小設定或數學方面的移動，這裡有一個簡單、較為直觀且易上手的 Colab 範例，可以僅靠調整數據達到自定義動畫的目的，
建議可以開多個視窗自我練習上述同時，並試著自行改變數值：
[Colab Example/Manim_Tutorial_1.ipynb](https://github.com/JIA-WEI-LI/ManimCE-Learning/blob/d02088c48a90b9f835a4e489a1efefef38d904db/Colab%20Example/Manim_Tutorial_1.ipynb)

## 參考資料
[Manim Tutorial | Updater Animations | Tutorial 1, Manim Explained](https://www.youtube.com/watch?v=MOv6yN7b2aI)
