
import os
import csv
import numpy as np
import math




PathOfData=''
#Output path
PathOfResult=''
#the index of numberTestCovered in the CSV files.
IndexOfNTC=11
#the index of label(kill or not) in the CSV files.
IndexOfLabel=-1
#the value of label
Y='yes'
N='no'


testcsvnames=os.listdir(PathOfData)

TestInfo=[]
for csvname in testcsvnames:
    TestInfo.append(csv.reader(open(PathOfData+'/'+csvname)))



ans=[]

for CSV in range(0,len(TestInfo)):
#for CSV in range(2,3):
    prekill=[]
    prelive=[]
    for ROW in TestInfo[CSV]:
                    if ROW[IndexOfLabel]==Y:
                        prekill.append(float(ROW[IndexOfNTC]))
                    if ROW[IndexOfLabel]==N:
                        prelive.append(float(ROW[IndexOfNTC]))
    if (prelive!=[])&(prekill!=[]):
        preall=np.hstack((prekill,prelive))
    if (prelive==[]):
        preall=np.array(prekill)
    if (prekill==[]):
        preall=np.array(prelive)
    c=[1]
    d=[0]
    isKilled=c*len(prekill)+d*len(prelive)
    x=list(set(preall))
    x.sort()
    count=list(preall).count(0)
    p=float(count)/len(preall)
    if p==0:
        count=0
    else:
        X=[]
        for xi in x:
            X.append(float(list(preall).count(xi)))
        for i in range(1,len(x)):
            count=count+X[i]*pow(p,math.log(x[i]+1,2))
    count=math.floor(count)
    pre=[1]*len(preall)
    prob=[]
    for i in range(0,len(preall)):
        prob.append(1-pow(p,math.log(preall[i]+1,2)))
        if pow(p,math.log(preall[i]+1,2))>=0.5:
            pre[i]=0
    out =open(PathOfResult+'/'+testcsvnames[CSV]+'.csv','ab')
    csv_write=csv.writer(out,dialect='excel')
    csv_write.writerow(['Survival probability','Prediction label','Label'])
    for i in range(0,len(preall)):
      #if preall[i]!=0:
        prob=pow(p,math.log(preall[i]+1,2))
        csv_write.writerow([prob,pre[i],isKilled[i]])   
    out.close()

















