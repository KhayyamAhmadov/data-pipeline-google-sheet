import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from config import sheets_id, scopes

service_account_file = 'keys.json'

credentials = Credentials.from_service_account_file(service_account_file, scopes=scopes)

service = build('sheets', 'v4', credentials=credentials)
sheet = service.spreadsheets()

range = "A1:Z500"
result = sheet.values().get(spreadsheetId=sheets_id, range=range).execute()

data = result.get("values", [])

print(data)