---
title: "UVa 12895 Armstrong Number"
author: "Kevin Cheng"
tags: ["UVa", "v128", "1-Star", "Math"]
date: 2021-03-04T14:12:51+08:00
---

# 題目
對一個 $p$ 位數整數 $n$，若 $n$ 的每個數字的 $p$ 次方加總後等同 $n$，即可稱 $n$ 為一個阿姆斯壯數

求輸入的數是否為阿姆斯壯數

<!--more-->

# Input
第一行為一正整數 $T$，表測資筆數，接下來 $T$ 行每行含一個正整數 $N$ ( $N \leq 10^9$ )。

# Output
對每個正整數 $N$ 輸出一行，如 $N$ 為阿姆斯壯數，輸出 `Armstrong`，反之輸出 `Not Armstrong`。

# 解法
Python 火力展示題。

# Source Code

{{< readfile file="uva/v128/p12895-Armstrong-Number.py" highlight="py3" >}}
