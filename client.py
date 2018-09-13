import os

from Zenaton.core.client import Client

app_id = 'KJXPYBCOMZ'
# app_id = os.environ.get('ZENATON_APP_ID')
api_token = 'RPKZ0JYdSpZ4UDq5McoUmXng0TBjnW4N3BYHvuD88VWrIo0IVvpCcsTmRug2'
app_env = 'dev'

Client(app_id, api_token, app_env)