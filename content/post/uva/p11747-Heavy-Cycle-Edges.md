---
title: "UVa 11747 - Heavy Cycle Edges"
author: "Kevin Cheng"
tags: ["UVa", "v117", "MST", "minimum spanning tree", "2.5-Star"]
date: 2019-11-04T18:40:59+08:00
---

# 題目
講了一堆 MST 演算法的實作，當成廢話就好

給 $n$ 個點，$m$ 個邊，求不屬於 MST 的 edge 集合

<!--more-->

# Input
每組測資第一行是兩個數字 $n$, $m$($1 \leq n \leq 1000$, $0 \leq m \leq 25000$)

接下來 $m$ 行為 edge 資訊，每行三個數字 $u$, $v$, $w$($0 \leq u, v \lt n$, $0 \leq w \lt  2^{31}$) 表 edge 的兩個 vertex 編號 + weight


# Output
每組測資輸出一行，將不屬於 MST 的 edge 的 weight 以空白分隔輸出(由小到大)

如果沒有這種 edge 就輸出 `forest`


# 解法
1. 讀取
2. sort
3. kruskal + 掃到不屬於 MST 的 edge 時就記下來。
4. 輸出


# Source Code

{{< readfile file="uva/v117/p11747-Heavy-Cycle-Edges.py" highlight="python" >}}
