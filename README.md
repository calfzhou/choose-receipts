# choose-receipts

发票分组小工具。

给定一批发票，每张发票有一个确定的面额，需要从这些发票中找出一些，凑出一个或多个目标报销金额，希望浪费的发票面额越小越好。

设有 $n>0$ 张发票，面额分别为 $v_1, v_2, ..., v_n$（$\forall 1\leq i\leq n,v_i>0$），给定 $m>0$ 个目标金额，分别为 $g_1, g_2, ..., g_m$（$\forall 1\leq i\leq m,g_i>0$），需要从发票中选出若干张并分成 `m` 个组 $G_i, G_2, ..., G_m$，满足：
$$
\begin{cases}
\forall 1\leq i\leq m,|G_i|=s_i,G_i=\{r_1,r_2,...,r_{s_i}\}\subseteq \{1,2,...,n\} \\
\forall 1\leq i \neq j\leq m,G_i\cap G_j=\varnothing \\
\forall 1\leq i\leq m,amount(G_i)=v_{r_1}+v_{r_2}+...+v_{r_{s_i}}\geq g_i \\
min\{\sum_i amount(G_i)\}
\end{cases}
$$
