"""
Time : O(sum of square of len of each word)
Space : O(sum of square of len of each word)
Compiled : yes
Problems : no but not perfect solution.
"""
class Solution(object):
    def longestWord(self, words):
        wordset = set(words)
        words.sort(key = lambda c: (-len(c), c))
        for word in words:
            if all(word[:k] in wordset for k in range(1, len(word))):
                return word

        return ""