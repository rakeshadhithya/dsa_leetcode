#LINK: https://leetcode.com/problems/all-paths-from-source-to-target/

from typing import List
class Solution:
    def dfs(self, graph, n, path, res):
        #if last node(target) deep copy path to res
        if n == len(graph) - 1:
            res.append(path.copy())
        #for each nei of node, add nei to path, do same on nei, remove nei (backtrack)
        for nei in graph[n]:
            path.append(nei)
            self.dfs(graph, nei, path, res)
            path.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        self.dfs(graph, 0, [0], res)
        return res
    
