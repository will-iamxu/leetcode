class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        maxHeap = []
        for char, cnt in count.items():
            maxHeap.append([-cnt, char])
        heapq.heapify(maxHeap)
        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1 

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt != 0:
                prev = [cnt, char]
        
        return res 
