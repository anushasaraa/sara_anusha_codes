class Solution:
    def alternateDigitSum(self, n: int) -> int:
        x=str(n)
        s=int(x[:1])
        for i in range(1,len(x)):
            if(i%2==0):
                s+=int(x[i])
            else:
                s-=int(x[i])
        return s
