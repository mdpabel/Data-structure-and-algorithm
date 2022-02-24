class Solution:
    def hashed(self, str):
        return "".join(sorted(str))
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            str = self.hashed(s)
            if str not in map:
                map[str] = []
            map[str].append(s)
        return map.values()