from alisscript2 import df
import pandas as pd

#print(df['name'])

signatures = []
alis_conns = []
alis_matches = []

for i in df['name']:
    signatures.append(i.lower())

#print(signatures)

with open('Connections.csv', 'r') as file:
    lines = file.readlines()

#print(lines[4:15])


for j in lines[4:]:
    x = j.split(',')
    y = str(x[0]) + ' ' + str(x[1])
    alis_conns.append(y.lower())

print(alis_conns[0:10])

for x in alis_conns:
    if x in signatures:
        alis_matches.append(x)

print(alis_matches)
