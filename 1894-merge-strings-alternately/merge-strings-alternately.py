class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = len(word1)
        b=len(word2)
        temp=''
        j=0
        i=0
        while i < min(a,b):
            temp+=word1[i]+word2[i]
            i+=1
            j=i

        if a<b:
            temp+=word2[j:]
            return temp
        else:
            temp+=word1[j:]
            return temp
        