class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ROWS = len(triangle)

        for r in range(1,ROWS):
            cols = len(triangle[r])

            for c in range(cols):

                if c == 0:
                    # leftmost position, can only come from direct obove
                    triangle[r][c] += triangle[r-1][c]
                elif c == cols-1:
                    # rightmost position, can only come from upper left
                    triangle[r][c] += triangle[r-1][c-1]
                else:
                    triangle[r][c] += min(triangle[r-1][c],triangle[r-1][c-1])


        return min(triangle[-1])
