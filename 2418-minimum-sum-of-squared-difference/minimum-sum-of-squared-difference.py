class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff_counts = {}
        for a, b in zip(nums1, nums2):
            d = abs(a - b)
            diff_counts[d] = diff_counts.get(d, 0) + 1
            
        total_k = k1 + k2
        
        max_heap = [-diff for diff in diff_counts.keys()]
        import heapq
        heapq.heapify(max_heap)
        
        while total_k > 0 and max_heap:
            curr_diff = -heapq.heappop(max_heap)
            if curr_diff == 0:
                break
                
            count = diff_counts[curr_diff]
            next_diff = -max_heap[0] if max_heap else 0
            diff_step = curr_diff - next_diff
            ops_needed = diff_step * count
            
            if total_k >= ops_needed:
                total_k -= ops_needed
                diff_counts[next_diff] = diff_counts.get(next_diff, 0) + count
                del diff_counts[curr_diff]
            else:
                full_steps = total_k // count
                remainder = total_k % count
                
                if full_steps > 0:
                    reduced_diff = curr_diff - full_steps
                    diff_counts[reduced_diff] = diff_counts.get(reduced_diff, 0) + count
                    diff_counts[curr_diff] -= count
                    curr_diff = reduced_diff
                
                if remainder > 0:
                    diff_counts[curr_diff] -= remainder
                    diff_counts[curr_diff - 1] = diff_counts.get(curr_diff - 1, 0) + remainder
                    
                if diff_counts[curr_diff] == 0:
                    del diff_counts[curr_diff]
                
                total_k = 0
                
        ans = 0
        for diff, count in diff_counts.items():
            ans += (diff ** 2) * count
            
        return ans