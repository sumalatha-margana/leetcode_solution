class Solution:
    def frequencySort(self, s: str) -> str:
        char_freq = defaultdict(int)
        for ch in s:
            char_freq[ch] += 1
        
        bucket = [[] for _ in range(len(s) + 1)]
        for char, freq in char_freq.items():
            bucket[freq].append(char)
        
        sorted_string = ""
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                for ch in bucket[i]:
                    sorted_string += ch * i
        return sorted_string
        