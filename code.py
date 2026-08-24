class Solution:
    def secondHighest(self, s: str) -> int:
        f=[]
        for num in s:
            if num.isdigit():
                if int(num) not in f:
                    f.append(int(num))
        print(f)
        f.sort()
        if len(f)<2:
            return -1
        return f[-2]
        
        
