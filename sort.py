# -*- coding: utf-8 -*-

# 有向グラフに関してのアルゴリズム

"""
ダイクストラのアルゴリズム
@param V 頂点集合 
@param d 結合強度、変がないときはinfinity
@param s 出発点
"""
def cost_table(V, d, s):
    C = {}
    for i in V:
        print s, i, d[s][i]
        C[i] = d[s][i]          # 最初の辺と繋がったところのリスト
    U = V
    U.remove(s)                 # 考慮していないもの

    while len(U) > 0:
        c = [(x, C[x]) for x in U]
        w = min(c, key=lambda x:x[1])[0]  # 移動コストが最小のところ
        U.remove(w)
        for v in U:
            C[v] = min(C[v], C[w] + d[w][v])  # コストの更新
    return C

inf = float('inf')
V = [0, 1, 2, 3]
d = [[inf, 2, 6, inf],
     [inf, inf, 3, inf],
     [inf, inf, inf, 2],
     [inf, inf, inf, inf]]

print cost_table(V, d, 0)
