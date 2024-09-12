import sys
from collections import defaultdict
from heapq import heappop, heappush

INF = 1100100100100100100

class Asset:
    def __init__(self, required, gain):
        self.required = required
        self.gain = gain
        self.uid = global_uid[0]
        global_uid[0] += 1

    def __lt__(self, other):
        if self.required != other.required:
            return self.required < other.required
        return self.uid < other.uid

global_uid = [0]

class Node:
    def __init__(self, id):
        self.id = id
        self.value = 0
        self.adj = []

    def join(self, main, other):
        for asset in other:
            heappush(main, Asset(asset.required, asset.gain))

    def dfs(self, parent):
        sets = []
        for node in self.adj:
            if node != parent:
                sets.append(node.dfs(self))

        main = []
        for s in sets:
            if len(main) < len(s):
                main = s

        for s in sets:
            if s != main:
                self.join(main, s)

        if self.value > 0:
            heappush(main, Asset(0, self.value))
        else:
            required = -self.value
            gain = self.value

            while main and (gain <= 0 or required >= main[0].required):
                asset = heappop(main)
                required = max(required, -gain + asset.required)
                gain += asset.gain

            if gain > 0:
                heappush(main, Asset(required, gain))

        return main

def solve():
    input = sys.stdin.read
    data = input().split()
    index = 0

    z = int(data[index])
    index += 1

    results = []
    for _ in range(z):
        n = int(data[index])
        index += 1

        nodes = [Node(i) for i in range(n + 1)]

        destination = int(data[index])
        index += 1

        for i in range(1, n + 1):
            nodes[i].value = int(data[index])
            index += 1
        nodes[0].value = INF

        nodes[0].adj.append(nodes[destination])
        nodes[destination].adj.append(nodes[0])

        for _ in range(n - 1):
            a = int(data[index])
            b = int(data[index + 1])
            index += 2
            nodes[a].adj.append(nodes[b])
            nodes[b].adj.append(nodes[a])

        final_assets = nodes[1].dfs(None)
        have = 0
        while final_assets and final_assets[0].required <= have:
            asset = heappop(final_assets)
            have += asset.gain

        if have >= INF:
            results.append("escaped")
        else:
            results.append("trapped")

    print("\n".join(results))

if __name__ == "__main__":
    solve()
