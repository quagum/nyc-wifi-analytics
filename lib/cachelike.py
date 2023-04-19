#!/usr/bin/env python

from typing import Callable
from enum import Enum
import os
import os.path
import requests

cache_map = {
    "linknyc_locations": "s4kf-3yrf",
    "linknyc_kiosk_status": "n6c5-95xh",
    "nyc_wifi_hotspot_location": "yjub-udmw"
    }

data_dir = ""

# End = Enum('End',['CSV','JSON','GEOJSON'])
    
api_url_retrieval: Callable[[str,str],str] = lambda document,end="csv" : f"https://data.cityofnewyork.us/resource/{document}.{end}"
api_url_retrieval.__doc__ = """
api_url_retrieval: get's the url base from a particular thing

Potential File Endings:
- csv
- json
- geojson
"""

check_file: Callable[[str], bool] = lambda path: os.path.isfile(path)

def sync_up(file_type='csv'):
    """
    
    """
    print(file_type)
    for k in cache_map:
        retrieval_url = f"{api_url_retrieval(k,file_type)}"
        # file does not exist locally
        if(not check_file(retrieval_url)):
            
            print(f"make new {retrieval_url}")

            


if __name__ == "__main__":
    for i,k in enumerate(cache_map):
        v = cache_map[k]
        print(f"{k}\t{v}\t{check_file(k)}")
        print(f"{api_url_retrieval(k)}")
        print(f"{api_url_retrieval(k,'json')}")        


    sync_up()
    sync_up('json')
    # print(list(End))
    pass
