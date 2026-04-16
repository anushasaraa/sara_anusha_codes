class Solution:
    def reverse(self, x: int) -> int:
        sum=0
        temp=abs(x)
        while(temp):
            rem=temp%10
            sum=(sum*10)+rem
            temp=temp//10
        if(x>0 and sum<(2**31)-1 and sum>(-2**31)):
            return sum
        elif(x<0 and sum>(-2**31) and sum<(2**31)-1):
            return -sum       
        else:
            return 0
    
        
