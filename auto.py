def edit(s,t):
    l1=len(s)
    l2=len(t)
    a=[]
    for i in range(l1+1):
        b=[0]*(l2+1)
        a.append(b)
    for i in range(l1+1):
        for j in range(l2+1):
            if i==0:
                a[i][j]=j
            elif j==0:
                a[i][j]=i
            else:
                if s[i-1]==t[j-1]:
                    a[i][j]=a[i-1][j-1]
                else:
                    a[i][j]=min(a[i-1][j-1],a[i][j-1],a[i-1][j])+1
                    
    return a[l1][l2]




f = open("dict.txt", "r")
lines=f.readlines()
f.close()
print("Enter the word")
s=input()
print("Possible auto corrected values are:- ")
for i in lines:
    w=edit(s,i.strip())
    if w<=1:
        print(i.strip())
    
