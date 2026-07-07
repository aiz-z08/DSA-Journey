class Solution:
    def sumAndMultiply(self, n: int) -> int:
        temp=n
        num=0
        sum=0
        while temp>0:
            dig=temp%10
            sum+=dig
            if dig>0:
                num=10*num+dig
            temp//=10
        x=int(str(num)[::-1])
        return x*sum