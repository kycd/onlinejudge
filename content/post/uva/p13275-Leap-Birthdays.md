---
title: "UVa 13275 Leap Birthdays"
author: "Kevin Cheng"
tags: ["UVa", "v132", "Math", "1-Star"]
date: 2020-10-07T11:40:14+08:00
---

# 題目
給出生年月日 + 欲查詢年份，求過了幾次生日。

快樂的閏年計算題。

(ps. 出生那年不算度過生日，因為那天忙著出生)

<!--more-->

# Input
第一行為一整數 $T$ ($T \leq 100$)，表 case 數量。

接下來 $T$ 行，每行一組測資，每組測資含四個整數 $D$, $M$ ($1 \leq M \leq 12$), $Y$ ($1850 \leq Y \leq 2016$), $QY$ ($Y \leq QY \leq 3000$)。

其中 $D$, $M$, $Y$ 表出生年月日，可以假設這個日期會是合法日期(不會出現2/30 這種鬼日子)

$QY$ 為想查詢的年份

# Output

對每組測資輸出一行 `Case C: X`，其中 $C$ 為測資編號，$X$ 為題目所求的次數。
# 解法
就...標準閏年題

# Source Code

{{< readfile file="uva/v132/p13275-Leap-Birthdays.py" highlight="py3" >}}
