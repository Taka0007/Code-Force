T = int(input())

for i in range(T):
    
    s = input()
    
    if len(s)<=10:
        ans = s
        
    else:
        ans = s[0] + str(len(s)-2) + s[-1]
        
    print(ans)
