---
title: "UVa 11479 Is This the Easiest Problem"
author: "Kevin Cheng"
tags: ["UVa", "v114", "math", "1-Star"]
date: 2020-01-15T15:09:47+08:00
---

# 題目
給三角形的三邊長，求三角形種類，種類有以下四種。

* Invalid: 不是三角形
* Equilateral: 正三角形
* Isosceles: 等腰三角形
* Scalene: 不屬於量兩種的合法三角形

<!--more-->

# Input
第一行為一個正整數 $T$ ($T \le 20)$，表測資筆數。

接下來 $T$行，每行為一組測資，每組測資有三個 32 bit 的整數，以空白分隔。

# Output
對每組測資輸出以下格式，$x$ 為測資編號，由 1 開始，三角形種類如題目描述。

`Case x: triangle type.`

# 解法
排序以後進入國小數學。

唯一要注意的是檢查合法時如果不是用 python 的話要小心 overflow，題目標明 32-bit integer 感覺就會有 overflow 陷阱 + 負數陷阱。

所以不要用 $a + b > c$ 檢查，用 $a > c - b$ 避開 overflow。

負數...不用講吧(攤手)。

# Source Code

{{< readfile file="uva/v114/p11479-Is-this-the-easiest-problem.py" highlight="py3" >}}
