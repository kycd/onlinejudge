---
title: "UVa 10930 A-sequence"
author: "Kevin Cheng"
tags: ["UVa", "v109", "2-Star", "Set"]
date: 2021-03-16T09:41:41+08:00
draft: false
---

# 題目
若數列滿足條件 $1 \leq a_1 \lt a_2 \lt ... \lt a_n$，且 $a_k$ 不為 $a_1$ ~ $a_{k-1}$ 的任意和，則此數列可稱為 `A-sequence`。

<!--more-->

# Input
每組測資一行，每行第一個數字 $D$($2 \leq D \leq 30$) 代表數列長度，接下來 $D$ 個 $1$ ~ $1000$ 的整數。


# Output
每組測資輸出兩行，第一行輸出數列內容，第二行輸出數列是否為 `A-sequence`。

# 解法
用 Set 紀錄 $a_1$ ~ $a_{k-1}$ 的任意和，$O(logn)$ 就可以判斷 $a_k$ 是否為 $a_1$ ~ $a_{k-1}$ 的任意和，再掃一次 set 把每個 element 加上 $a_k$ insert 進 set 就可以做出 $a_1$ ~ $a_k$ 的任意和。

# Source Code

{{< readfile file="uva/v109/p10930-A-Sequence.py" highlight="py3" >}}
