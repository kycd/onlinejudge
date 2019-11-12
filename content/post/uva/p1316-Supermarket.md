---
title: "UVa 1316 Supermarket"
author: "Kevin Cheng"
tags: ["UVa", "v13", "greedy", "2-Star", "wip"]
date: 2019-11-12T13:33:08+08:00
---

# 題目
一間超市的商品 $x$ 都存在兩個值 $p\_x, d\_x$，$p\_x$ 代表商品 $x$ 的價值，$d\_x$ 代表商品 $x$ 的保存期限。假設超市每天只能賣掉一項商品，求超市的最大收益。

<!--more-->

# Input
題目包含多組側茲，每組測資一行，第一個數為 $n(1 \le n \le 10000)$，表商品數量，接下來是 $n$ 組的 pair $p\_i$, $d\_i (1 \le p\_i \le 10000，1 \le d\_i \le 10000)$。

# Output
對每組測資輸出一個正整數，表該組測資中超市可獲得的最佳收益，`兩組測資的 output 之間以 space 間格`(特別的規則)。

# 解法
greedy 大概

1. sort by $d\_i$ desc, $p\_i$ desc
2. 從最大保存期限掃回來 對每一天 m 取目前 set 中 $d\_i \ge m$ 的 $max(p\_i)$
3. 將取到商品的移出 set，繼續下一天

掃到 $m = 0$ 時移出 set 的商品就會是最大收益・

# Source Code
還沒寫！

需要 priority queue，難道要回 STL 的懷抱了嗎....

<!-- < readfile file="uva/OOXX" highlight="OOXX" > -->
