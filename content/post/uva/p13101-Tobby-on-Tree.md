---
title: "UVa 13101 Tobby on Tree"
author: "Kevin Cheng"
tags: ["UVa", "v131", "wip", "BFS", "GCD", "2-Star"]
date: 2020-06-18T15:27:14+08:00
draft: false
---

# 題目
有個遊戲叫減法遊戲，在一數列中，挑選任兩個不相等的數，將大的減掉小的，再把兩個數塞回數列中，最終，整個數列會變成全部一樣的數(就是只能做減法的多數字輾轉相除法啊XD)。

Tobby 對這個遊戲很有興趣，並想多次遊玩，所以他在一個 tree map 中，每天選擇 $node\_u$ 與 $node\_v$，從 $node\_u$ 走到 $node\_v$ 並將過程中的每個 $node$ 的數值蒐集起來(包含 $node\_u$ 及 $node\_v$)，用這些數進行玩減法遊戲。

另外，某些日子會出現 $node$ 的數值異動，這些異動會維持到 Tobby 不玩為止。

求每次 Tobby 玩遊戲時最後剩下的數。

<!--more-->

# Input
題目含多組測資，每組測資第一行唯一正整數 $N$($1 \le N \le 50000$)，表示 tree map 的 $node$ 數量。

第二行有 $N$ 個正整數($1 \le value \le 10000$)，表示 $node\_1$ ~ $node\_N$ 的數值。

再來 $N - 1$ 行，每行有兩個正整數 $u, v$，表示 $node\_u$ 與 $node\_v$ 相連。

接著下一行唯一正整數 $q$，表示 query 數量。

再來 $q$ 行，每行會有三個數字 ($type = 1, u, v$) 或 ($type = 2, u, x$)

$type = 1$ 表示該天 Tobby 從 $node\_u$ 走至 $node\_v$

$type = 2$ 表示從該天起 $node\_u$ 的數值更改為 $x$

# Output
對每組 $type = 1$ 的輸出一行，為該天遊戲最後剩下的數值

# 解法
BFS + gcd?

感覺沒這麼簡單，先用正攻法捅捅看吧

# Source Code
還．沒．寫

<!--{ {< readfile file="uva/v131/p13101-Tobby-on-Tree.py" highlight="py3" >}} -->
