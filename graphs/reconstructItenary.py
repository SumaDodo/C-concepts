class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        a = collections.defaultdict(list)
        for i,j in sorted(tickets)[::-1]:
            a[i] += j,
        actual_route = []
        def route(airport):
            while a[airport]:
                route(a[airport].pop())
            actual_route.append(airport)
        route('JFK')
        return actual_route[::-1]
        #I keep moving forward until I reach the same point        
