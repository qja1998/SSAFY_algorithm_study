# import sys
from collections import defaultdict, deque
# sys.stdin=open('input.txt','r')

# # dfs는 사이클 못 돔
# def dfs(node, graph, visited):
#     if visited[node]:
#         return
#     else:
#         visited[node] = True
#         for n_node in graph[node]:
#             dfs(n_node, graph, visited)
#     return

def bfs(start, end, graph, visited):
    

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    graph_reverse = [[] for _ in range(n+1)] 
    for _ in range(m):
        s, e = map(int,input().split())
        graph[s].append(e)
        graph_reverse[e].append(s)
    
    start, end = map(int, input().split())   # S->T S가 집 T가 회사

    visited_s2e = [False] * (n+1)
    visited_s2e[end] = True
    bfs(start, end, graph, visited_s2e)

    visited_e2s = [False] * (n+1)
    visited_e2s[start] = True
    bfs(end, start, graph, visited_e2s)

    visited_s2e_rev = [False] * (n+1)
    # visited_s2e_rev[end] = True
    bfs(start, end, graph_reverse, visited_s2e_rev)

    visited_e2s_rev = [False] * (n+1)
    # visited_e2s_rev[start] = True
    bfs(end, start, graph_reverse, visited_e2s_rev)
    
    count=0
    for i in range(1,n+1):
        if visited_s2e[i] and visited_e2s[i] and visited_s2e_rev[i] and visited_e2s_rev[i]:
            count+=1

    print(count-2) # 시작 끝 제외

if __name__=="__main__":
    main()