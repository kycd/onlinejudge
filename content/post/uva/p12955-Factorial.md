---
title: "UVa 12955 Factorial"
author: "Kevin Cheng"
tags: ["UVa", "v129", "greedy", "1-Star"]
date: 2020-06-10T14:32:12+08:00
draft: false
---

# 題目
將一個正整數 $N$ 拆解為 $N = a\_1! + a\_2! + ... + a\_k!$，$a\_n$ ($1 \le n \le k$) 皆為正整數，求最小 $k$

<!--more-->

# Input
input 含多組測資，每組一行，每行一個 $N$ ($1 \le N \le 10^5$)。


# Output
一個正整數 $k$，使題目等式可成立的最小 $k$

# 解法
階層的特色是，兩個小的不如一個大的 $2 * (n-1)! \le n!$，所以 $a\_n$ 越大越好。

快樂地從後面砍回來就行了，最後的洞都可以用 $1!$ 補起來

# Source Code

{{< readfile file="uva/v129/p12955-Factorial.py" highlight="py3" >}}
