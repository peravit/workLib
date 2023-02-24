from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import gspread
import gspread_dataframe
from config import get_config
from prep import prep_data


def update_ggs(data):
    config = get_config()
    #df = prep_data()
    df = data
    scope = ['https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(config['path_key'], scope)
    client = gspread.authorize(credentials)
    gc = gspread.service_account(config['path_key'])
    sht3 = gc.open_by_url(config['ggs_url'])
    df_values = df.values.tolist()
    sht3.values_append(config['ggs_name'], {'valueInputOption': 'USER_ENTERED'}, {'values': df_values}) #default = raw



if __name__ == '__main__':
    data = {'Name': ['John', 'Alice', 'Bob', 'Lisa'],
            'Age': [25, 30, 20, 35],
            'Gender': ['Male', 'Female', 'Male', 'Female'],
            'Salary': [50000, 60000, 45000, 70000]}

    # test df
    df = pd.DataFrame(data)
    update_ggs()
