class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        '''
        state = (node + removals)
        '''
        def isValid(r,c):
            return 0 <= r < m and 0 <= c < n

        queue=deque([(0,0,0,k)]) # row,col,steps,removals
        visit={(0,0,k)} # row,col,removals

        directions=[(0,-1),(0,1),(-1,0),(1,0)]
        m=len(grid)
        n=len(grid[0])

        while queue:
            row,col,steps,removals = queue.popleft()

            if row == m-1 and col == n-1:
                return steps
            
            for dr,dc in directions:
                nxt_row,nxt_col = row+dr,col+dc
                if isValid(nxt_row,nxt_col):
                    if grid[nxt_row][nxt_col] == 1:
                        # obstacle
                        if removals and (nxt_row,nxt_col,removals-1) not in visit:
                            visit.add((nxt_row,nxt_col,removals-1))
                            queue.append((nxt_row,nxt_col,steps+1,removals-1))
                    else:
                        # no obstacle
                        if (nxt_row,nxt_col,removals) not in visit:
                            visit.add((nxt_row,nxt_col,removals))
                            queue.append((nxt_row,nxt_col,steps+1,removals))     
        return -1
            