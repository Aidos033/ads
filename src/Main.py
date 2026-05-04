# from collections import deque
# import heapq

# # ── Graph (Tasks 1–3) ──────────────────────────────────────────
# graph = {
#     'A': ['C', 'B', 'D'], 'B': ['A', 'C', 'E', 'G'],
#     'C': ['A', 'B', 'D'], 'D': ['C', 'A'],
#     'E': ['G', 'F', 'B'], 'F': ['G', 'E'], 'G': ['F', 'B'],
# }

# # ── Task 1: DFS ────────────────────────────────────────────────
# def dfs(graph, start):
#     visited, stack, order = set(), [start], []
#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             visited.add(node)
#             order.append(node)
#             print(f"  Visit {node} | stack={list(reversed(stack))} | visited={order}")
#             for nb in reversed(graph[node]):
#                 if nb not in visited:
#                     stack.append(nb)
#     return order

# # ── Task 2: BFS ────────────────────────────────────────────────
# def bfs(graph, start):
#     visited, queue, order = {start}, deque([start]), []
#     while queue:
#         node = queue.popleft()
#         order.append(node)
#         new = [nb for nb in graph[node] if nb not in visited]
#         print(f"  Visit {node} | new neighbours={new} | queue={list(queue) + new}")
#         for nb in new:
#             visited.add(nb)
#             queue.append(nb)
#     return order

# # ── Task 4: Dijkstra ───────────────────────────────────────────
# roads = {
#     'Edinburgh': [('Stirling', 50), ('Dundee', 100), ('Glasgow', 70)],
#     'Stirling':  [('Edinburgh', 50), ('Perth', 40), ('Glasgow', 50)],
#     'Perth':     [('Stirling', 40), ('Dundee', 60)],
#     'Glasgow':   [('Stirling', 50), ('Edinburgh', 70)],
#     'Dundee':    [('Perth', 60), ('Edinburgh', 100)],
# }

# def dijkstra(graph, src, dst):
#     dist = {n: float('inf') for n in graph}
#     prev, dist[src] = {}, 0
#     pq = [(0, src)]
#     while pq:
#         d, u = heapq.heappop(pq)
#         if d > dist[u]: continue
#         print(f"  Process {u} (dist={d})")
#         for v, w in graph[u]:
#             if dist[u] + w < dist[v]:
#                 dist[v] = dist[u] + w
#                 prev[v] = u
#                 heapq.heappush(pq, (dist[v], v))
#     path, node = [], dst
#     while node:
#         path.append(node)
#         node = prev.get(node)
#     return list(reversed(path)), dist[dst]

# # ── Run all tasks ──────────────────────────────────────────────
# print("=== Task 1: DFS from A ===")
# dfs_order = dfs(graph, 'A')
# print("Order:", ' → '.join(dfs_order))

# print("\n=== Task 2: BFS from A ===")
# bfs_order = bfs(graph, 'A')
# print("Order:", ' → '.join(bfs_order))

# print("\n=== Task 3: Comparison ===")
# print(f"DFS: {' → '.join(dfs_order)}")
# print(f"BFS: {' → '.join(bfs_order)}")

# print("\n=== Task 4: Shortest path Edinburgh → Dundee ===")
# path, dist = dijkstra(roads, 'Edinburgh', 'Dundee')
# print(f"Path: {' → '.join(path)} = {dist} miles")
