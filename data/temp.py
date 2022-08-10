import numpy as np
import pandas as pd
data_multi = pd.read_pickle('data-multi-visit.pkl')
data_single = pd.read_pickle('data-single-visit.pkl')
print('fsd')
rx_voc_size = 0
rx_voc = {}
with open('rx-vocab.txt', 'r') as fin:
    for line in fin:
        rx_voc[line.rstrip('\n')] = rx_voc_size
        rx_voc_size += 1

ehr_adj = np.zeros((rx_voc_size, rx_voc_size))

for idx, row in data_multi.iterrows():
    med_set = list(map(lambda x: rx_voc[x], row['ATC4']))
    for i, med_i in enumerate(med_set):
        for j, med_j in enumerate(med_set):
            if j <= i:
                continue
            ehr_adj[med_i, med_j] = 1
            ehr_adj[med_j, med_i] = 1

for idx, row in data_single.iterrows():
    med_set = list(map(lambda x: rx_voc[x], row['ATC4']))
    print(med_set)
    for i, med_i in enumerate(med_set):
        for j, med_j in enumerate(med_set):
           # print(i,med_i)
            if j <= i:
                continue
            ehr_adj[med_i, med_j] = 1
            ehr_adj[med_j, med_i] = 1
print(ehr_adj,"fsda")
print('avg med for one ', np.mean(np.sum(ehr_adj, axis=-1)))
