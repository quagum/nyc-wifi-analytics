#!/usr/bin/env python

from lib.cachelike import *
from dotenv import load_dotenv

# load_dotenv(): loads .env file into the running process
load_dotenv()

# sync_up(): loads data files if they don't exist
sync_up()


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

df = pd.read_csv("data/linknyc_kiosk_status.csv")

"""print(df.columns)
Index(['generated_on', 'site_id', 'status', 'ppt_id', 'address', 'city',
'state', 'zip', 'boro', 'latitude', 'longitude', 'cross_street_1',
'cross_street_2', 'corner', 'community_board', 'council_district',
'census_tract', 'nta', 'bbl', 'bin', 'install_date', 'active_date',
'wifi_status', 'wifi_status_date', 'tablet_status',
'tablet_status_date', 'phone_status', 'phone_status_date',
'geocoded_column'],dtype='object')
"""
df = df.set_index("site_id")
df = df.drop(columns=["generated_on", "ppt_id", "address", "city", 
                      "state", "cross_street_1", "cross_street_2", 
                      "census_tract", "nta", "bbl", "bin", "geocoded_column"])
"""
Index('status', 'zip', 'boro', 'latitude', 'longitude', 'corner', 
'community_board', 'council_district','install_date', 'active_date',
'wifi_status', 'wifi_status_date', 'tablet_status','tablet_status_date',
'phone_status', 'phone_status_date'],dtype='object')
"""
df['status'] = df['status'].astype('category').cat.codes
df['boro'] = df['boro'].astype('category').cat.codes
df['corner'] = df['corner'].astype('category').cat.codes

df['wifi_status'] = df['wifi_status'].astype('category').cat.codes
df['tablet_status'] = df['tablet_status'].astype('category').cat.codes
df['phone_status'] = df['phone_status'].astype('category').cat.codes

df['install_date'] = df['install_date'].astype('category').cat.codes
df['active_date'] = df['active_date'].astype('category').cat.codes
df['wifi_status_date'] = df['wifi_status_date'].astype('category').cat.codes
df['tablet_status_date'] = df['tablet_status_date'].astype('category').cat.codes
df['phone_status_date'] = df['phone_status_date'].astype('category').cat.codes

"""
plt.matshow(df.corr())
plt.xticks(np.arange(16), df.columns, rotation=90)
plt.yticks(np.arange(16), df.columns, rotation=0)
plt.colorbar()
plt.show()


installation date, active date, wifi status, tablet status, phone status 
have strong inverse relationship with status
"""

from sklearn.linear_model import LinearRegression
model_1 = LinearRegression().fit(df[["install_date"]], df["status"])


plt.scatter(df[["install_date"]], df["status"], color='g')
plt.plot(df[["install_date"]], model_1.predict(df[["install_date"]]),color='r')


plt.show()

if __name__ == "__main__":
    pass
