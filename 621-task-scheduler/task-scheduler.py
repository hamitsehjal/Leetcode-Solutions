class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)

        heap = [(-cnt, task) for task, cnt in counter.items()]
        heapq.heapify(heap)  # O(n) - heapify

        t = 0
        queue = collections.deque()  # ((cnt,ch), t)

        while heap or queue:
            # print(f"time is {t} | heap - {heap} | Queue - {queue}")
            if heap:
                cnt, task = heapq.heappop(heap)
                if cnt + 1 != 0:
                    queue.append(((cnt + 1, task), t + n))

            if queue and t == queue[0][1]:
                pair, _ = queue.popleft()
                heapq.heappush(heap, pair)

            t += 1

        return t
