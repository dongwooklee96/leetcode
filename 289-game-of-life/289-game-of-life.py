class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

        max_x = len(board) - 1
        max_y = len(board[0]) - 1

        count_list = []
        # first I have to retrieve all the board.
        for x, row in enumerate(board):
            for y, elem in enumerate(row):
                # check all directions and count 1
                cnt = 0
                for direction in directions:
                    xx = x + direction[0]
                    yy = y + direction[1]

                    # check boundary
                    if (0 <= xx <= max_x) and (0 <= yy <= max_y):
                        if board[xx][yy] == 1:
                            cnt += 1
                count_list.append(cnt)

        # change board elem
        idx = 0
        for x, row in enumerate(board):
            for y, elem in enumerate(row):
                nbhd_cnt = count_list[idx]
                if nbhd_cnt < 2:
                    board[x][y] = 0
                elif nbhd_cnt == 2:
                    pass
                elif nbhd_cnt == 3:
                    board[x][y] = 1
                elif nbhd_cnt > 3:
                    board[x][y] = 0
                idx += 1

        print(board)