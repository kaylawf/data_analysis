import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/kaylawright-freeman/Documents/data/data_analysis/MH/Student Mental health.csv')

df = pd.DataFrame({
                    'time':df['Timestamp'],
                    'gender':df['Choose your gender'],
                    'age':df['Age'],
                    'course':df['What is your course?'],
                    'year':df['Your current Year of Study'],
                    'GPA':df['What is your CGPA?'],
                    'mar_stat':df['Marital status'],
                    'depression':df['Do you have Depression?'],
                    'anxiety':df['Do you have Anxiety?'],
                    'panic':df['Do you have Panic attack?'],
                    'treat':df['Did you seek any specialist for a treatment?']
               })

## do another wherer you create the DF by looping through the keys

for a in df.keys()[1:]:
     t = [x for x in df[a] if str(x) == 'nan']
     u = [x for x in df[a].unique() if str(x) != 'nan']
     j = list(range(len(u)))
     k = list(range(len(u)))
     labels = list(range(len(u)))
     for b in range(len(u)):
          l = df[a][df[a]==u[b]]
          j[b] = l
          k[b] = 100*len(j[b])/(len(df[f'{a}'])-len(t))
          labels[b] = u[b]
     fig,ax = plt.subplots()
     ax.pie(k, labels=labels, autopct='%1.1f%%')
     if not os.path.exists('all'):
          os.mkdir('all')
     fig.savefig(f'all/{a}')

for z in df.keys()[1:]:
     m = [x for x in df[z] if str(x) == 'nan']
     n = [x for x in df[z].unique() if str(x) != 'nan']
     for c in n:
          f = np.where(df[z] != c)[0]
          df_sub = df.drop(f)
          for a in df_sub.keys()[1:]:
               t = [x for x in df_sub[a] if str(x) == 'nan']
               u = [x for x in df_sub[a].unique() if str(x) != 'nan']
               # if len(u) > 1:
               j = list(range(len(u)))
               k = list(range(len(u)))
               labels = list(range(len(u)))
               for b in range(len(u)):
                    l = df_sub[a][df_sub[a]==u[b]]
                    j[b] = l
                    k[b] = 100*len(j[b])/(len(df_sub[f'{a}'])-len(t))
                    labels[b] = u[b]
               fig,ax = plt.subplots()
               ax.pie(k, labels=labels, autopct='%1.1f%%')
               ax.title.set_text(f'{z}_{c}_{a}')
               if not os.path.exists(f'{z}'):
                    os.mkdir(f'{z}')
               if not os.path.exists(f'{z}/{c}'):
                    os.mkdir(f'{z}/{c}')
               fig.savefig(f'{z}/{c}/{a}')