# -*- coding: utf-8 -*-
# 深さ優先探索のサンプル
# V: 頂点集合, d: 接続関係辞書

# Vのグラフ中、vの子どものリストを返す
def getChild(V, v):
    


# グラフVを幅深さ優先探索をする  子、孫を先に探索する
def depthFirstSearch(V, d):
    visited = {v:False for v in V}
    for v in V:
        dfs(v, visited) 

def dfs(v, visited):
    if visited[v] == False:
        visited[v] = True
        print v                 # nodeに対する処理
        for u in getChild(V, v):
            dfs(u, visited)
