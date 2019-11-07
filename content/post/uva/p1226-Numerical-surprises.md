---
title: "UVa 1226 Numerical Surprises"
author: "Kevin Cheng"
tags: ["UVa", "v12", "Big Integer", "1-Star"]
date: 2019-11-07T14:28:33+08:00
---

# 題目
廢文一堆，然後最後講說要算 $P$ % $N$，除了 $P$ 是大數以外沒有特別的地方

<!--more-->

# Input
第一行為測資筆數。

接下來每組測資為兩行，第一行為 $N$($1 \lt N \lt 10^{9}$)

第二行為 $P$($1 \lt P \lt 10^{2000}$)

# Output
每組測資輸出一個數 $P$ % $N$

# 解法
遇到大數，開出 java 的 BigInteger 或 python 就對了

特別推薦 python，integer 直接是大數。

# Source Code

{{< readfile file="uva/v12/p1226-Numerical-surprises.py" highlight="python" >}}
