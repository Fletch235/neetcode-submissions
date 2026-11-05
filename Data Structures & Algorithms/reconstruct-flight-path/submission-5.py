class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)

        adj = defaultdict(list)

        for src, dest in tickets:
            adj[src].append(dest)

        out = []
        def dfs(src):
            while adj[src]:
                dest = adj[src].pop()
                dfs(dest)
            out.append(src)

        dfs("JFK")
        out.reverse()
        return out