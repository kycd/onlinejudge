---
title: "UVa 12854 Automated Checking Machine"
author: "Kevin Cheng"
tags: ["UVa", "v128", "1-Star", "xor"]
date: 2021-03-04T17:26:34+08:00
---

# 題目
給兩個長度為 5 的板子，1 代表凸，0 代表凹，判斷兩塊板子能不能完美重疊(無縫)。

<!--more-->

# Input
多組測資，每組測資兩行，每行五個數字，數字只有 0 或 1，空白間隔

# Output
可完美重疊輸出 `Y`，反之輸出 `N`

# 解法
就 XOR，end。

# Source Code

{{< readfile file="uva/v128/p12854-Automated-Checking-Machine.py" highlight="py3" >}}
