class Solution:
    def minimumPushes(self, word):
        n = len(word)
        pushes = 0
        for i in range(n):
            pushes += (i // 8) + 1
        return pushes
