# ManimCE Practice

> This article will not be regularly updated and practice ManimCE

&emsp;&emsp;This page is only written for the practice of ManimCE related content, and some English are translated by Google, please forgive me if there is any inconsistency.

* Tutorial 1
  * [Create And Move A Rectangle](https://github.com/JIA-WEI-LI/ManimCE-Learning/blob/b95633fa6a5db2539b653cb205e5120b5053ffbe/%E4%B8%AD%E6%96%87%E7%89%88%E6%95%99%E7%A8%8B%20Tutorial/Tutorial%201/Create%20And%20Move%20A%20Rectangle.md)
  * [Create Axis And Transform Object](https://github.com/JIA-WEI-LI/ManimCE-Learning/blob/b95633fa6a5db2539b653cb205e5120b5053ffbe/%E4%B8%AD%E6%96%87%E7%89%88%E6%95%99%E7%A8%8B%20Tutorial/Tutorial%201/Create%20Axis%20And%20Transform%20Object.md)  
  * [Add Updaters](https://github.com/JIA-WEI-LI/ManimCE-Learning/blob/b95633fa6a5db2539b653cb205e5120b5053ffbe/%E4%B8%AD%E6%96%87%E7%89%88%E6%95%99%E7%A8%8B%20Tutorial/Tutorial%201/Add%20Updaters.md)
  * [Add Updater_2](https://github.com/JIA-WEI-LI/ManimCE-Learning/blob/b95633fa6a5db2539b653cb205e5120b5053ffbe/%E4%B8%AD%E6%96%87%E7%89%88%E6%95%99%E7%A8%8B%20Tutorial/Tutorial%201/Add%20Updaters_2.md)
* Tutorial 2
  * [Graphing Movement](https://github.com/JIA-WEI-LI/ManimCE-Learning/blob/b95633fa6a5db2539b653cb205e5120b5053ffbe/%E4%B8%AD%E6%96%87%E7%89%88%E6%95%99%E7%A8%8B%20Tutorial/Tutorial%202/Graphing%20Movement.md)
---

# Install Manim and LaTeX package in Colab
After creating a new notebook, paste the following code block in a cell, then execute it.
```python
!sudo apt update
!sudo apt install libcairo2-dev ffmpeg \
    texlive texlive-latex-extra texlive-fonts-extra \
    texlive-latex-recommended texlive-science \
    tipa libpango1.0-dev
!pip install manim
!pip install IPython --upgrade
```
For my personal habits, in order to ensure that LaTeX Traditional Chinese is displayed correctly, the following instructions are usually added
```python
!sudo apt install texlive-full
```
>Warning: using directives will increase load time

You should start to see Colab installing all the dependencies specified in these commands. After the execution has completed, you will be prompted to restart the runtime. Click the “restart runtime” button at the bottom of the cell output.

---

## Reference Website & Suggested Website
**Official document：**[Manim Community v0.17.1.post()](https://docs.manim.community/en/stable/index.html)
### Youtube Channel / Playlist
[ManimCE Tutorials 2021](https://www.youtube.com/playlist?list=PLWOlLjdyZm2NQD1YZmEPB0dwbd0yKINAT) *by Brian Amedee*
