import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests


def zillow_api_request(city):

    pd.options.display.max_columns = None

    df = pd.read_csv('./api_keys.csv')
    zwsid = df.loc[df['API'] == 'zillow']['KEY'].iloc[0]
    rapid_api_key = df.loc[df['API'] == 'rapid']['KEY'].iloc[0]

    url = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"
    querystring = {"location": city, "status_type":"ForRent", "price":""}
    headers = {
        "X-RapidAPI-Key": rapid_api_key,
        "X-RapidAPI-Host": "zillow-com1.p.rapidapi.com"
    }

    z_rent = requests.request("GET", url, headers=headers, params=querystring)
    z_rent
    z_rent.text
    z_rent_json = z_rent.json()
    z_rent_json.keys()
    total_pages = z_rent_json['totalPages']
    total_pages_list = list(range(1,total_pages + 1))
    columns=['units', 'listingStatus', 'zpid', 'longitude', 'buildingName','address', 'isBuilding', 'hasImage', 'lotId', 'imgSrc', 'latitude']


    z_rent_json = pd.json_normalize(data= z_rent_json['props'])
    data_df=pd.DataFrame(columns=columns)

    for page in total_pages_list[:20]:
        querystring = {"location": city, "page":page , "status_type":"ForRent", "price":""}
        z_rent_json = requests.request("GET", url, headers=headers, params=querystring)
        z_rent_json = z_rent.json()
        z_rent_json = pd.json_normalize(z_rent_json['props']).iloc[:,:11]
        data_df = data_df.append(z_rent_json,ignore_index=True)

    time.sleep(1.0)
    data_df_expanded = data_df.explode('units').reset_index()
    unit_info_df = data_df_expanded.reset_index()
    unit_info_df = unit_info_df.drop(['index'], axis=1)
    unit_info_df = unit_info_df.drop(['level_0'], axis=1)


    unit_info_df.to_csv(f"./Resources/{city}.csv", index=False)