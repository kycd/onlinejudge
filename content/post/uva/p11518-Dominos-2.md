---
title: "UVa 11518 Dominos 2"
author: "Kevin Cheng"
tags: ["UVa", "v115", "bfs"]
date: 2024-03-29T18:39:55+08:00
---

# 題目

<!--more-->

# Input

第一行為一數字, 表測資組數

每組測資第一行是三個數字 $n$, $m$, $l$(皆不大於 10000)

n 表示這組骨牌有幾個, 編號為 $1$ ~ $n$

接下來 $m$ 行為骨牌的相依資訊，每行兩個數字 $x$, $y$, 表示推倒 $x$, $y$ 會接著倒下

接下來 $l$ 行為推倒資訊, 每行一個數字 $z$, 表示編號 $z$ 的骨牌會被手動推倒

# Output

每組測資輸出一個數字, 表有多少骨牌被推倒

# 解法

把每個 $z$ 當起點 bfs 著色, 最後掃一次就收工了

# Source Code

{{< readfile file="uva/v115/p11518-Dominos-2.py" highlight="py3" >}}
