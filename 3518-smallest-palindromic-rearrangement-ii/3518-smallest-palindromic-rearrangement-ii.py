from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        middle = ""
        half = {}

        total = 0

        for ch in sorted(freq):
            if freq[ch] % 2:
                middle = ch
            half[ch] = freq[ch] // 2
            total += half[ch]

        # factorials
        fact = [1] * (total + 1)
        for i in range(1, total + 1):
            fact[i] = fact[i - 1] * i

        # denominator = product(fact[count])
        denom = 1
        for v in half.values():
            denom *= fact[v]

        # total permutations
        total_perm = fact[total] // denom
        if total_perm < k:
            return ""

        left = []

        remain = total

        letters = sorted(half.keys())

        while remain:

            for ch in letters:

                if half[ch] == 0:
                    continue

                # Number of permutations if we choose ch
                cnt = total_perm * half[ch] // remain

                if cnt >= k:
                    left.append(ch)

                    total_perm = cnt
                    denom //= fact[half[ch]]
                    half[ch] -= 1
                    denom *= fact[half[ch]]

                    remain -= 1
                    break

                else:
                    k -= cnt

        left = "".join(left)

        return left + middle + left[::-1]