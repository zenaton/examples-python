import os

from Zenaton.core.client import Client

# LOADING CONFIG FROM .env file
env = {}
with open('.env') as f:
    for line in f:
        if line.startswith('#') or line.strip() == '':
            continue
        key, value = line.strip().split('=')
        env[key] = value

app_id = env.get('ZENATON_APP_ID')
api_token = env.get('ZENATON_API_TOKEN')
app_env = env.get('ZENATON_APP_ENV')

if not app_id:
    raise Exception('Please include your ZENATON_APP_ID in the .env file')

if not api_token:
    raise Exception('Please include your ZENATON_API_TOKEN in the .env file')

if not app_env:
    raise Exception('Please include your ZENATON_APP_ENV in the .env file')

Client(app_id, api_token, app_env)