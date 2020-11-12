import json
import time

import requests
import urllib3
from loguru import logger
from requests import Request, Response


class HttpSession(requests.Session):
    pass

