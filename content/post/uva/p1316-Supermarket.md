---
title: "UVa 1316 Supermarket"
author: "Kevin Cheng"
tags: ["UVa", "v13", "heap", "greedy", "2.5-Star"]
date: 2019-11-12T13:33:08+08:00
---

# 題目
一間超市的商品 $x$ 都存在兩個值 $p\_x, d\_x$，$p\_x$ 代表商品 $x$ 的價值，$d\_x$ 代表商品 $x$ 的保存期限。假設超市每天只能賣掉一項商品，求超市的最大收益。

<!--more-->

# Input
題目包含多組測試，每組測資第一個數為 $n(1 \le n \le 10000)$，表商品數量，接下來是 $n$ 組的 pair $p\_i$, $d\_i (1 \le p\_i \le 10000，1 \le d\_i \le 10000)$。

測資中會包含額外的空白，但可以保證測資的內容(pair 資訊/數量之類的)會是正確的。

`這鳥測資是來整 python 的對吧....`

# Output
對每組測資輸出一個正整數，表該組測資中超市可獲得的最佳收益

`每組測資一行(題目 pdf 把所有答案印在一行)`

沒仔細看題目只看 Sample output 的我吃了兩次 WA.....

# 解法
greedy，從後面排回來，對每一天 $m$，取 $d\_i \ge m$ 的商品中，$p\_i$ 最大者作為該日販賣商品

不太記得該怎麼解釋這種排法，依稀記得是因為從後面才會是不變動的最佳解

步驟:

1. sort 商品 by $d\_i$ desc，順便紀錄最大保存期限 $d$。
2. 從 $d$ 掃回來，對每一天 m ，將 $d\_i = m$ 的商品放入 candicate set 中。
3. 取 candicate set 中 $max(p\_i)$ 的商品
4. 將該商品移出 candicate set，繼續下一天

掃到 $m = 0$ 時所有被移出 candicate set 的商品就會是最大收益・

實作上我使用兩個 heap

第一個 heap `warehouse` 用來處理 step 1，以及 step 2 拿來取商品時很方便

第二個 heap `rack` 則是 candicate set，可以讓 step 3, 4 在取 $max(p\_i)$ 只要一個 pop() 而且是 $O(log\_n)$。

這題因為 python3 沒有內建 heap 所以我逃回 C++ stl 了。

# Source Code
{{< readfile file="uva/v13/p1316-Supermarket.cpp" highlight="c++" >}}
