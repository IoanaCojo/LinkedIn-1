'''
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

'''

class LengthOfLastWord58:
    def lengthOfLastWord(self, s: str) -> int:
        words=s.split()
        print(words[-1])
        return len(words[-1])


