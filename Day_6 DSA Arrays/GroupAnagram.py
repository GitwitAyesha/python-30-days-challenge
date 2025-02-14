from collections import defaultdict
class Solution:
    def GroupAnagram(slef,strs:list[str])-> list[list[str]]:
        res = defaultdict(list)
        for i in strs:
            result = ''.join(sorted(i))
            res[result].append(i)
        return list(res.values())
sol = Solution()
string = ['ana','book','jahil']
print(sol.GroupAnagram(string))