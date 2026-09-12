class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)

        arr = []

        for i in range(n):
            l, r, w = intervals[i]
            arr.append((l, r, w, i))

        arr.sort(key=lambda x: x[1])

        ends = [x[1] for x in arr]

        prev = [-1] * n

        for i in range(n):
            l = arr[i][0]

            low = 0
            high = i

            while low < high:
                mid = (low + high) // 2

                if ends[mid] < l:
                    low = mid + 1
                else:
                    high = mid

            prev[i] = low - 1

        dp = [[(0, []) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(1, n + 1):
                best_score, best_list = dp[k][i - 1]
                curr = i - 1
                p = prev[curr]

                old_score, old_list = dp[k - 1][p + 1]

                new_score = old_score + arr[curr][2]
                new_list = old_list + [arr[curr][3]]

                if new_score > best_score:
                    best_score = new_score
                    best_list = new_list

                elif new_score == best_score:
                    if sorted(new_list) < sorted(best_list):
                        best_list = new_list

                dp[k][i] = (best_score, best_list)

        return sorted(dp[4][n][1])

        