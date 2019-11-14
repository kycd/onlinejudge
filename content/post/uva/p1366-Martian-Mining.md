---
title: "UVa 1366 Martian Mining"
author: "Kevin Cheng"
tags: ["UVa", "v13", "DP", "3-Star"]
date: 2019-11-12T18:36:09+08:00
---

# 題目
NASA 在某個星球上採礦，已知採礦點是個長方形區塊，存在兩種礦石 `Bloggium`、`Yeyenum`，`Bloggium` 的冶煉廠位於正北方，`Yeyenum` 的冶煉廠位於西方，冶煉廠很大，大到足以覆蓋整個北方及西方。

NASA 決定打造輸送帶來輸送礦石至冶煉廠進行精練，但輸送帶有其限制

1. 不能轉彎，只能一直線。
2. 同一個點只能建造一種(往北 or 往西) 的輸送帶。
3. `Yeyenum` 礦石送到 `Bloggium` 冶煉廠會被拋棄，反之亦然。

請算出 NASA 可以運送至冶煉廠的最大礦石數量。

<!--more-->

# Input
輸入含多組測資，每組測資第一行為兩個正整數 $n, m(1 \le n, m \le 500)$
接下來 $n$ 行每行有 $m$ 個正整數，代表由北至南，由西至東的 `Yeyenum` 礦石數量，數量會在 $0 \sim 1000$
接下來 $n$ 行則是 `Bloggium` 礦石的資訊，限制/格式同 `Yeyenum`

當 $n = m = 0$ 時表測資結束。

# Output
對每組測資輸出一個整數 表 NASA 可挖出來的最大礦石數量。

# 解法
DP 題。

對點 $(x, y)$ 來說，假設這個點蓋了往西的輸送帶，代表 $(x, 0~y-1)$ 都得蓋往西的輸送帶，不蓋的話收益不會是最大(因為收不到 $(x, y)$ 的礦石)，蓋往北的輸送帶則會違反限制。

所以 $(x, y)$ 選擇往西時，其最大收益為 $S\_y(x, y) + dp(x - 1, y)$

* $dp(x - 1, y)$ 表示 $(x - 1, y)$ 的最大收益
* $S\_y(x, y)$ 表示 $Yeye(x, 0) + Yeye(x, 1) + ... + Yeye(x, y)$

以此類推，$(x, y)$ 選擇往北時，其最大收益為 $S\_b(x, y) + dp(x, y - 1)$

* $S\_b(x, y)$ 表示 $Blog(0, y) + Blog(1, y) + ... + Blog(x, y)$

最後統整一下公式

* $dp(x, y) = 
\begin{cases}
	max
	\begin{cases}
		dp(x - 1, y) + S\_y(x, y) \cr
		dp(x, y - 1) + S\_b(x, y)
	\end{cases} & \text{for } 1 \le x \le m, 1 \le y \le n \cr
	0 & \text{for } x = 0 \text{ or } y = 0
\end{cases}
$
* $ S\_y(x, y) = \sum\_{i = 1}^x Yeye(i, y) $
* $ S\_b(x, y) = \sum\_{j = 1}^y Blog(x, j) $

# Source Code

{{< readfile file="uva/v13/p1366-Martian-Mining.py" highlight="python3" >}}
