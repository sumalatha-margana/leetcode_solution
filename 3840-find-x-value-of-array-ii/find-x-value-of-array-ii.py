class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)
        size = 1
        while size < n:
            size *= 2
        tree = [(1, [0] * k) for _ in range(2 * size)]
        def make_node(x):
            x %= k
            cnt = [0] * k
            cnt[x] = 1
            return (x, cnt)
        def merge(a, b):
            prod1, cnt1 = a
            prod2, cnt2 = b
            cnt = cnt1[:]
            for r in range(k):
                cnt[(prod1 * r) % k] += cnt2[r]
            return ((prod1 * prod2) % k, cnt)
        for i in range(n):
            tree[size + i] = make_node(nums[i])
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])
        def update(pos, value):
            p = size + pos
            tree[p] = make_node(value)
            p //= 2
            while p:
                tree[p] = merge(tree[2 * p], tree[2 * p + 1])
                p //= 2
        def query(left, right):
            left += size
            right += size + 1
            lres = (1, [0] * k)
            rres = (1, [0] * k)
            while left < right:
                if left & 1:
                    lres = merge(lres, tree[left])
                    left += 1
                if right & 1:
                    right -= 1
                    rres = merge(tree[right], rres)
                left //= 2
                right //= 2
            return merge(lres, rres)
        result = []
        for index, value, start, x in queries:
            update(index, value)
            _, cnt = query(start, n - 1)
            result.append(cnt[x])
        return result