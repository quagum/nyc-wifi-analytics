#!/usr/bin/env python

from typing import Callable
import os
import os.path
import requests

cache_map = {
    "linknyc_locations": "s4kf-3yrf",
    "linknyc_kiosk_status": "n6c5-95xh",
    "nyc_wifi_hotspot_location": "yjub-udmw"
}

    
api_url_retrieval: Callable[[str,str],str] = lambda document,end="csv" : f"https://data.cityofnewyork.us/resource/{document}.{end}"
api_url_retrieval.__doc__ = """
api_url_retrieval: get's the url base from a particular dataset

Potential File Endings:
- csv
- json
- geojson
"""

def sync_up(file_type='csv'):
    """Brings new files if they don't exist locally
    
    Keyword arguments:
    file_type -- the ending file type, file_type available: 'csv','json','geojson'
    """
    for k in cache_map:
        ret_f = f"{k}.{file_type}"
        retrieval_url = f"{api_url_retrieval(cache_map[k],file_type)}"
        if(not os.path.isfile(ret_f)):
            req = requests.get(retrieval_url)
            with open(f"{ret_f}", "w") as f:
                f.write(req.text)
            print(f"\tCreated new file: {ret_f}")


if __name__ == "__main__":
    sync_up()
    pass
