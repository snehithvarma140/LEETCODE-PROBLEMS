class Solution(object):
    def check(self, a, x):
        state = 1
        for i in range(len(x)):
            if x[i] not in a:
                state = 0
        return state
    def countConsistentStrings(self, allowed, words):
        count = 0
        for i in range(len(words)):
            if self.check(allowed, words[i]):
                count += 1
        return count
        