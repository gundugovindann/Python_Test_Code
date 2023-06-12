s=str(input())
ss=''
i=0
while (s.count("WUB")!=0):
    if s.find('WUB')==0:
        s=s.replace("WUB","",1)
    else:
        s=s.replace("WUB"," ",1)  
print(s)
