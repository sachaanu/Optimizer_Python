
%pylab inline
import seaborn as sns
from pandas import *
import numpy

StartString = "x x x x x x x"
TargetString = "U T K A R S h"
STRTList=StartString.split()
TGTList=TargetString.split()

new_list =[]
Final = []
count=0

if len(STRTList)| len(TGTList) == 0:
    print ( "Error : length of Either String is lower than 1 Character")

if len(STRTList) != len(TGTList):
    print("Length of Strings is not equal to compare")
    
new_list = list(STRTList)
index=0
while (TGTList) != STRTList:
    for k in range(index,len(STRTList)):
        X = numpy.random.randint(1,256)
        Y =chr(X)
        
        if TGTList[k] == STRTList[k]:
            count=count+1
            continue
        else:
            
            STRTList[k] = Y
            
            if STRTList[k]==TGTList[k]:
                count=count+1
                index=k

                continue
                
            else:
                index=k
                count=count+1

                break
print(count,new_list,TGTList)
        