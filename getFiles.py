import os
import pandas as pd
from config import get_config

#os.getcwd()
#num_fold = len(next(os.walk(config['path']))[1])

def load_data():
        
    config = get_config()
    li = []

    if config['all_files'] == '':
        list_fold = (next(os.walk(config['path']))[1][int(config['sla']):])
    else:
        list_fold = next(os.walk(config['path']))[1]

    for i in list_fold:
        for (root, dirs, files) in os.walk(config['path']+'\\'+i,topdown=True):

            for names in files:
                name_cus = names[18:-4]
                df = pd.read_csv(""+root+"\\"+names+"", header=3, encoding = 'utf8')
                df['chat_name'] = pd.Series([name_cus for x in range(len(df.index))])
                df = df[df['วันส่ง'] == i[:4]+"/"+i[4:6]+"/"+i[6:]]
                li.append(df)           
        frame = pd.concat(li, axis=0, ignore_index=True)

    return frame
