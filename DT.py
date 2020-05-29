#import readr
import pandas as pd

urlfile="https://raw.githubusercontent.com/profthyagu/Python-Decision-Tree-Using-ID3/master/PlayTennis.csv"

mydata = pd.read_csv(urlfile, error_bad_lines=False)
mydata.to_csv("Tennis.csv",index=False)
print(mydata.head())