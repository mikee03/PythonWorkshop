DNA=open("DNA.txt").read()
D=len(DNA)
numc=0
numg=0
for i in range(1,D):
    if DNA[i]=='C':
        num=len(DNA[i])
        numc=numc+num
    if DNA[i]=='G':
        num1=len(DNA[i])
        numg=numg+num1
sum1=numc+numg
division=sum1/18.0
Percent=division*100
print("The percent of C+G is",Percent, "%")

