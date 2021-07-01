class Solution(object):
    def largestAltitude(self, gain):
        pain=[]
        j=1
        for i in range(len(gain)):
            if len(pain) == 0:
                pain.append(0)
                pain.append(0+gain[i])
            else:
                pain.append(pain[j]+gain[i])
                j+=1
        return(max(pain))