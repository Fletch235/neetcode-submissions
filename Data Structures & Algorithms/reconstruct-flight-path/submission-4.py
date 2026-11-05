class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True) # return the lexicographically smallest one

        adj = defaultdict(list) # build adjacency list of edges in graph
        for src, dest in tickets:
            adj[src].append(dest)

        out = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            out.append(src)
        
        dfs("JFK")
        out.reverse()
        return out
