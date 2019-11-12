---
title: "UVa 13244 Space Happiness"
author: "Kevin Cheng"
tags: ["UVa", "v132", "math", "等差級數和", "1-Star"]
date: 2019-11-11T10:54:38+08:00
---

# 題目
s 為一奇數，求數列 `0, 1, 3, 5, ..., s - 2, s, s - 2, s - 4, ... , 3, 1, 0` 的總和

<!--more-->

# Input
第一行為測資筆數 $t$

每組測資為一個正整數 $s(1 \le s \le 10^9 + 1)$

# Output
對每組測資輸出一個整數，為題目描述之數列和


# 解法
不看開頭結尾的 0 就是兩個等差數列

1. $[1 + 3 + ... + (s - 2) + s]$
2. $[(s - 2) + (s - 4) + ... + 3 + 1)$

所以就

1. $a\_1 = 1, a\_{n1} = s, n1 = (s + 1) / 2$，$S\_1 = (1 + s) * [(s + 1) / 2] / 2 = $$s^2 + 2s + 1 \over 4$
2. $a\_1 = (s - 2), a\_{n2} = 1, n2 = (s - 2 + 1) / 2$，$S\_2 = [(s - 2) + 1] * [(s - 1) / 2] / 2 = $$s^2 - 2s + 1\over 4$

so，答案就是 $S1 + S2 = $$s^2 + 1 \over 2$

測資很仁慈，int64 就能解

* ps. python 需要額外注意 `/` 和 `//` 的用法....
	
		在 python 用 / 回 return float 型態，在 int64 的範圍精准度會出事
		必須要 // 來 return int 型態
		這東西就是C/C++ 的 /
# Source Code

{{< readfile file="uva/v132/p13244-Space-Happiness.py" highlight="python3" >}}
