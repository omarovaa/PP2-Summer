class Solution(object):
    def subtractProductAndSum(self, n):
        s=str(n)
        sum=0
        pro=1
        for i in range(len(s)):
            if s[i]>='0' and s[i]<='9':
                sum+=int(s[i])
                pro*=int(s[i])
        return pro-sum