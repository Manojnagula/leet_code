class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        a = len(str1)
        b=len(str2)
        if a<b:
            strx = str1
            str_ = str2
        else:
            strx =str2
            str_=str1
        max_str = ''
        for i in range(1,len(strx)+1):
            sub_str = strx[:i]
            if sub_str*(len(strx)//i) == strx and sub_str*(len(str_)//i) == str_:
                max_str =  sub_str
        return max_str

            
        