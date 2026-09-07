class Solution:
    
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        start = None
        litter = []

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter.append((i, j))

        k = len(litter)
        litter_id = {pos: i for i, pos in enumerate(litter)}

        queue = [(start[0], start[1], energy, 0, 0)]
        visited = {(start[0], start[1], energy, 0)}

        front = 0

        while front < len(queue):
            r, c, e, mask, moves = queue[front]
            front += 1

            if mask == (1 << k) - 1:
                return moves

            if e == 0:
                continue

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                new_e = e - 1
                new_mask = mask

                if classroom[nr][nc] == 'L':
                    new_mask |= 1 << litter_id[(nr, nc)]

                if classroom[nr][nc] == 'R':
                    new_e = energy

                state = (nr, nc, new_e, new_mask)

                if state not in visited:
                    visited.add(state)
                    queue.append((nr, nc, new_e, new_mask, moves + 1))

        return -1
        