import pandas as pd
import random
import time
import numpy as np

#Enter the path to the file with words. Must be .csv
words1=pd.read_csv(r"C:\Users\Amit\OneDrive\Desktop\Workbooks\words_pos.csv")
words=words1["word"]

testlist=random.choices(words,k=10)

times=[]
lenghts=[]

for i in testlist:
    lenghts.append(len(i))
    print(i)
    prior=time.time()
    while True:
        ask=input()
        if ask == i:
            post=time.time()
            print(u'\u2713')
            times.append(post-prior)
            break
        else:
            print(u'\u2716')
            continue

print(f'Mean time per letter{np.sum(times)/np.sum(lenghts)}')

