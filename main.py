#!/usr/bin/env python

from lib.cachelike import *
from dotenv import load_dotenv

# load_dotenv(): loads .env file into the running process
load_dotenv()



if __name__ == "__main__":
    print(check_file("linknyc"))
    pass
