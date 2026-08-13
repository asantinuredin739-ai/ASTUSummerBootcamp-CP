from collections import Counter, deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        cnt = Counter(s)

        chars = []
        for c in sorted(cnt.keys(), reverse=True):
            chars.extend([c] * (cnt[c] // k))

        def valid(t):
            p = 0
            need = t * k
            for ch in s:
                if p < len(need) and ch == need[p]:
                    p += 1
            return p == len(need)

        ans = ""
        q = deque([""])

        while q:
            cur = q.popleft()

            for c in chars:
                nxt = cur + c

                if valid(nxt):
                    if len(nxt) > len(ans) or (len(nxt) == len(ans) and nxt > ans):
                        ans = nxt
                    q.append(nxt)

        return ans
