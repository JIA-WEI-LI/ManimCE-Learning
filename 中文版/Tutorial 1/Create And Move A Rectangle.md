# Create And Move A Rectangle
## Code 程式碼
```python
%%manim -qm -v WARNING CreateAndMoveARectangle
class CreateAndMoveARectangle(Scene):
  def construct(self):
    box = Rectangle(color=GREEN_C, fill_color=RED_D, fill_opacity=0.5, height=1, width=1)

    self.add(box)
    self.play(box.animate.shift(RIGHT*2), run_time=2)
    self.play(box.animate.shift(UP*3), run_time=2)
    self.play(box.animate.shift(DOWN*5+LEFT*5), run_time=2)
    self.play(box.animate.shift(UP*1.5+RIGHT*1), run_time=2)
```
## Video 影片
https://user-images.githubusercontent.com/119060520/204041610-f04e475f-013a-4efc-9579-c0a4ecea87ea.mp4

## 代碼解析
&emsp;&emsp;首先，我們需要先知道我們希望透過動畫做到甚麼事情，在此範例，我們希望：
* 創建一個矩形 ( 可調整其 顏色、長寬 )
* 移動矩形至指定位置

### Create Rectangle 創建矩形
```python
box = Rectangle(color=GREEN_C, fill_color=RED_D, fill_opacity=0.5, height=1, width=1)

self.add(box)
```
&emsp;&emsp;上述指令敘述為：創建一個矩形命名為 `box`，並透過指令 `self.add()` 新增置場景中，其中創建矩形可以透過 `Rectangle()` 指令達成，而矩形的相關設定為：
* `color`：矩形線條顏色
* `fill_color`：矩形填充顏色
* `fill_opacity`：矩形填充顏色之透明度
* `height`：矩形高度
* `width`：矩形寬度
> 其他相關指令：[Rectangle](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Rectangle.html?highlight=Rectangle)

### Move Rectangle 移動矩形
```python
self.play(box.animate.shift(RIGHT*2), run_time=2)
```
&emsp;&emsp;創建動畫時，我們會採用 `self.play()` 來和程式說明此行程式碼要負責運行動畫，而運行的內容則是放在後面的小括弧。
以此範例為例，我們希望可以移動矩形到右邊兩個單位，因此我們可以將程式碼一一拆解觀察：
1. `box`：前面所定義的矩形名稱
2. `.animate`：告知程式我們要對前面的 `box` 進行**動畫**
3. `.shift()`：動畫移動的方法之一，括弧內可以放入方向及移動單位

&emsp;&emsp;在 ManimCE 中，方向主要可以分成四個方位：`LEFT (左)`、`RIGHT (右)`、`UP (上)`、`DOWN (下)`，在方向的後方可以乘上需要移動的單位距離 (若未填入則預設一倍)。
值得一提的是，方向也可以進行組合，透過 `+` 符號可以連結兩個不同的方向達到斜方向移動，如下列舉例為 *向上移動 1.5，向右移動 1*：
```python
self.play(box.animate.shift(UP*1.5+RIGHT*1))
```

## 練習使用
&emsp;&emsp;如果不熟悉關於顏色及大小設定或數學方面的移動，這裡有一個簡單、較為直觀且易上手的 Colab 範例，可以僅靠調整數據達到自定義動畫的目的，
建議可以開多個視窗並試著自行改變數值：
[Colab Example/Manim_Tutorial_1.ipynb](https://github.com/JIA-WEI-LI/ManimCE-Learning/blob/d02088c48a90b9f835a4e489a1efefef38d904db/Colab%20Example/Manim_Tutorial_1.ipynb)

## 官方網站關鍵字
[Rectangle](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.polygram.Rectangle.html?highlight=Rectangle)

## 參考資料
[Manim Tutorial | Updater Animations | Tutorial 1, Manim Explained](https://www.youtube.com/watch?v=MOv6yN7b2aI)
