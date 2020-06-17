---
title: "UVa 12933 Easy Graph Problem"
author: "Kevin Cheng"
tags: ["UVa", "v129", "wip", "3-Star", "BFS"]
date: 2020-06-17T15:13:49+08:00
draft: false
---

# 題目
給一個矩形迷宮，求點1 走到點 2 的最小 cost，以及走的過程中必須不停轉彎(左轉右轉迴轉)的最小 cost

<!--more-->

# Input
多組測資，每組第一行為 6 個正整數 $n$, $m$, $r1$, $c1$, $r2$, $c2$($2 \le n, m \le 500$, $1 \le r1, r2 \le n$, $1 \le c1, c2 \le m$)，$n, m$ 表迷宮大小，$(r1, c1)$ 表點1 座標，$(r2, c2)$ 表點2 座標

接下來 n 行，每行 m 個數字($1$ ~ $100$ 或 `*` )，如為數字表示該格的 cost，如為 `*` 表該格無法進入。


# Output
每組測資輸出一行，格式 `Case {case_number}: {minimum_cost} {minimum_cost_must_turn}`

* `{case_number}`: case 編號
* `{minimum_cost}`: 最小 cost
* `{minimum_cost_must_turn}`: 每步都必須轉彎的最小 cost

# 解法
BFS 大概

不停轉彎的就從記錄最小 cost 變成紀錄最小 cost + 來向(記錄量 * 4)

# Source Code

<!--{ {< readfile file="uva/v129/p12933-Easy-Graph-Problem.py" highlight="py3" >} }-->
