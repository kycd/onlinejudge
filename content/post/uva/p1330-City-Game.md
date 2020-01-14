---
title: "UVa 1330 City Game"
author: "Kevin Cheng"
tags: ["UVa", "v13", "DP", "3-Star"]
date: 2019-11-05T16:57:17+08:00
---

# 題目
Bob 想在 $M \times N$ 的地圖上，蓋一棟長方形建築物以獲取收益，$收益 = 建築物面積 * 3$

已知字母 `F` 為可用空地，求 Bob 可獲得的最大收益(只蓋一棟)。

<!--more-->

# Input
第一行為數字 $K$，表 case 數量。
每組測資第一行爲數字 $M$($M \leq 1000$), $N$($N \leq 1000$) 表地圖大小。
接下來 $M$ 行，每行會有 $N$ 的字母，字母只會有 `R` 或 `F`，字母之間以空白間隔
每組測資後會有一行空白行。

# Output
輸出字母 `F` 組成的最大長方形面積 $\times$ 3

# 解法
DP，對每個點窮舉以該點為右下點的長方形區域的最大面積，先把每個點的向左延伸最大值記錄下來(相當於長方形的底部長度)，就可以把時間壓在 $O(m^2 * n)$(只要這樣就可以 AC 不用 $O(m * n)$)。

$O(m * n)$ 的解法應該是利用底部長度的 array 做 stack 匹配，但....反正 AC 了XD。

reference: 演算法筆記 Largest Empty Rectangle( http://www.csie.ntnu.edu.tw/~u91029/MaximumSubarray.html#2 )

# Source Code

{{< readfile file="uva/v13/p1330-City-Game.cpp" highlight="c++" >}}
