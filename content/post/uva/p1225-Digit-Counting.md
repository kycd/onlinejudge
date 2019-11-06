---
title: "UVa 1225 Digit Counting"
author: "Kevin Cheng"
tags: ["UVa", "v12", "simulation", "1S"]
date: 2019-11-06T14:42:11+08:00
---

# 題目
對一個正整數 $N$，把 $1$~$N$ 黏在一起作成一個新的數後，計算每個 digit($0$~$9$) 的出現次數。

舉例，$N = 13$，黏在一起作成的新整數為 12345678910111213

digit 出現次數: $1$ 出現 6 次，$2$ 出現 2 次，$3$ 出現 3 次，以此類推。

<!--more-->

# Input
測資第一行為一不大於 $20$ 的正整數，表測資筆數
接下來每行為一組測資，每組測資僅一個正整數 $N$($1 \le N \le 10000$)

# Output
每組測資一行，輸出由 $0$~$9$ 的出現次數，以空白分隔。

# 解法
暴力題

單個數字的 digit 的出現次數只要轉字串就能輕鬆拆出來。

再加個迴圈就能算出 $1$~$N$ 的 digit 出現次數

# Source Code

{{< readfile file="uva/v12/p1225-Digit-Counting.py" highlight="python" >}}
