---
title: "UVa 13245 Prime Darts"
author: "Kevin Cheng"
tags: ["UVa", "v132", "3-Star", "DP"]
date: 2020-10-28T17:47:07+08:00
---

# 題目
有個飛鏢靶均分為 $n$ 等分，將 $1$ & 前 $n - 1$ 個質數分別填入任意區塊，表示飛鏢射中該區域可獲得的分數

給一個目標分數 $q$，求剛好拿到分數 $q$ 所需要的最少鏢數為何。

<!--more-->

# Input
第一行唯一正整數 $t$，表接下來的測資數量

接下來 $t$ 行每行有兩個數字 $n$ ($1 \leq n \leq 100$), $q$ ($1 \leq q \leq 5000$)

# Output
對每組測資印出單行，一個數字，表題目所求之鏢數。

# 解法
看起來像質數的的找零錢 DP 題

每組測資就是 $n$ 種硬幣(幣值為 $1$ & 前 $n - 1$ 個質數)，求組出 $q$ 的最小硬幣數。

but，總測資組數沒給，實測每組測資算一次會 TLE

所以必須直接把 $q \times n$ 的表建起來

令 $f(x, y)$ 為 $q = x, n = y$ 之答案

$f(x, y) = min(f(x, y - 1), f(x - primes[y], y) + 1)$

老樣子，算 $f(x, y)$ 就是考慮 $primes[y]$ 這個最大幣值用與不用

* 用了: $f(x - primes[y], y)$
* 不用: $f(x, y-1)$

# Source Code

{{< readfile file="uva/v132/p13245-Prime-Darts.py" highlight="py3" >}}
