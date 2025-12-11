from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from config import sheets_id, scopes

service_account_file = 'keys.json'
credentials = Credentials.from_service_account_file(service_account_file, scopes=scopes)

service = build('sheets', 'v4', credentials=credentials)
sheet = service.spreadsheets()

def update_sheet(range_, values):
    body = {"values": values}
    result = sheet.values().update(spreadsheetId=sheets_id, range=range_, valueInputOption="RAW", body=body).execute()
    return result
