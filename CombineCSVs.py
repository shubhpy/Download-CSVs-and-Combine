import pandas as pd
from os import listdir
from os.path import isfile, join

Cust_Names = ["MPL","DVC","WBPDCL","NFL","UPRVUNL"]
SUB_CODE = "BCCL"
mypath=  ''

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for Cust in Cust_Names:
    frames = list()
    for fil in onlyfiles:
        if Cust in fil:
            tempDf = pd.read_csv(mypath + fil)
            frames.append(tempDf)
    
    result = pd.concat(frames)
    result.to_csv(mypath+SUB_CODE+"_" +Cust+".csv")
