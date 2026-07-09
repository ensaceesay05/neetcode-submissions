class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # mapping the charCount to the list of anagrams

        for s in strs:
            count = [0] * 26 # a - z

            for c in s:
                count[ord(c) - ord("a")] += 1 # ascii value of each char
            
            result[tuple(count)].append(s)
        
        return list(result.values())