---
title: "UVa 12802 Gift From the Gods"
author: "Kevin Cheng"
tags: ["UVa", "v128", "2-Star", "Prime"]
date: 2021-03-05T15:36:54+08:00
---

# 題目
輸出 input 數字的 double。直到輸入為迴文質數時終止。

<!--more-->

# Input
多行，每行一個 $1$ ~ $10^6$ 的自然數

# Output
就 double。

# 解法
因為 size 只有 $10^6$，所以可以把整個質數表存下來，$O(1)$ 確認是否為質數。

迴文...對每一種語言應該都沒難度吧。

# Source Code

{{< readfile file="uva/v128/p12802-Gift-From-the-Gods.py" highlight="py3" >}}
