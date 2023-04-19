#!/usr/bin/env python

from lib.cachelike import *
from dotenv import load_dotenv

# load_dotenv(): loads .env file into the running process
load_dotenv()

# sync_up(): loads data files if they don't exist
sync_up()


if __name__ == "__main__":
    pass
