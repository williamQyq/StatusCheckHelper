from __future__ import print_function
import os.path
import sys
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'config/keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# If modifying these scopes, delete the file token.json.


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1lKveppzfx1kJIKhFqpywt2xPccCRKhcck7x3wMt4Z7M'
RESULT_RANGE = 'RepairResult!D2'
CLEAR_RANGE = 'RepairResult!D2:I'


def GoogleHelper():
    """
    Prints Repair stauts to spreadsheet.
    """
    aoa=[[1,2,3]]
    service = build('sheets', 'v4', credentials=creds)

    # sheet columns clear result
    sheet = service.spreadsheets()
    # sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,
    #                      range=CLEAR_RANGE,
    #                      body={}).execute()
    # update result to sheet
    sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                          range=RESULT_RANGE,
                          valueInputOption="USER_ENTERED",
                          body={"values": aoa}).execute()
