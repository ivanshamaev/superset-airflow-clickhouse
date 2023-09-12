#!/usr/bin/env python3

import os
import requests
import urllib.parse
from dotenv import load_dotenv
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

load_dotenv(override=True)

username = os.getenv('ADMIN_USERNAME')
password = os.getenv('ADMIN_PASSWORD')

creds = {
'username': username,
'password': password,
'refresh': True,
'provider': 'db'
}
base_url="https://127.0.0.1:8088"

login_url =f"{base_url}/api/v1/security/login"
login_response = requests.post(login_url,json=creds, verify=False)
access_token = login_response.json()

password = urllib.parse.quote_plus(password)
header = {"Authorization":f"Bearer {access_token.get('access_token')}"}
payload = {
  "allow_ctas": True,
  "allow_cvas": True,
  "allow_dml": True,
  "allow_file_upload": True,
  "allow_run_async": True,
  "cache_timeout": 0,
  "configuration_method": "sqlalchemy_form",
  "database_name": "Clickhouse Connect",
  "driver": "",
  "engine": "",
  "expose_in_sqllab": True,
  "external_url": "",
  "sqlalchemy_uri": f"clickhousedb://{username}:{password}@clickhouse",
  "extra": "{}",
  "force_ctas_schema": "",
  "impersonate_user": True,
  "is_managed_externally": True,
  "masked_encrypted_extra": "",
  "parameters": {}
}
database_url = f"{base_url}/api/v1/database/"
database_response = requests.post(database_url, json=payload, headers=header, verify=False)
print(database_response.status_code)
