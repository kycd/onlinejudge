---
title: "UVa 13291 Frosting on the Cake"
author: "Kevin Cheng"
tags: ["UVa", "v132", "1-star", "Math"]
date: 2020-10-16T17:18:21+08:00
---

# 題目
一塊長方形蛋糕，水平切 $n$ 刀，垂直切 $n$ 刀，然後依題目所描述的規則撒上糖霜，給下刀切塊大小，求各種糖霜的使用量

<!--more-->

# Input
多組測資，每組 3 行

第 1 行為一正整數 $n$($3 \leq n \leq 10^5$)

第 2 行為 n 個正整數，表垂直下刀時的切塊大小 $A_1, ..., A_n$

第 3 行為 n 個正整數，表水平下刀時的切塊大小 $B_1, ..., B_n$

$1 \leq A_1, ..., A_n, B_1, ..., B_n \leq 10^4$

# Output
每組測資印出 1 行 3 個整數，表示三種糖霜的使用量


# 解法
分組，相乘，end！

根據題目的圖平移一下各個顏色的區塊應該很容易就能推出怎麼算的。

# Source Code

{{< readfile file="uva/v132/p13291-Frosting-on-the-Cake.py" highlight="py3" >}}
