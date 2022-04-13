class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        visit = []
        for _ in range(n):
            temp = []
            for _ in range(n):
                temp.append(0)
            visit.append(temp)
        visit[0][0] = 1

        y, x = 0, 0
        idx = 1

        while True:
            if idx == n * n:
                return visit
                break

            # 오른쪽
            while y + 1 < n and not visit[x][y + 1]:
                y += 1
                idx += 1
                visit[x][y] = idx
            # 아래
            while x + 1 < n and not visit[x + 1][y]:
                x += 1
                idx += 1
                visit[x][y] = idx
            # 왼쪽
            while y - 1 >= 0 and not visit[x][y - 1]:
                y -= 1
                idx += 1
                visit[x][y] = idx
            # 위로
            while x - 1 >= 0 and not visit[x - 1][y]:
                x -= 1
                idx += 1
                visit[x][y] = idx
