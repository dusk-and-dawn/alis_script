import pandas as pd

with open('/home/owl/names.txt', 'r') as file:
    sortstuff = file.readlines()

useful_lns= sortstuff[18:]
#print(useful_lns[0:100])
clean = []
for index, line in enumerate(useful_lns):
    if line == '\n':
        pass
    else:
        clean.append(line.strip('\n'))
lazy = []
for i in clean:
    if '·' in i:
        pass
    else:
        lazy.append(i)
#print(f'lazy: {lazy}')
names = []
jobs = []
companies = []
#print(clean[0])
for i in range(0, len(lazy), 3):

    try:
        names.append(lazy[i])
        jobs.append(lazy[i+1])
        companies.append(lazy[i+2])
    except:
        print('ups')
#print(names[-1:], jobs[:10], companies[:10])
#print(len(names), len(jobs), len(companies))

data = {
    "name":names,
    "employer":companies,
    "title":jobs
}

df = pd.DataFrame(data)

#df.to_excel('alis_output2.xlsx')
#print(sortstuff)