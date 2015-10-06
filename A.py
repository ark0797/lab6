file1=open('intinput.txt','w')
a=input()
s=input()
file1.write(a+'\n'+s)
file1=open('intinput.txt','r')
file2=open('output.txt','w')
#file1.read(int(a)*2-1)
i=0
n=0
while i<=len(s)-2:
	if int(s[i])==int(s[i+2]):
		n=s[i]
	i+=2
file2.write(str(n))
file1.close
file2.close


