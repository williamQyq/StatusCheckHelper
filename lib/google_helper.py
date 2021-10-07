from lib.module import build, InstalledAppFlow, Request, Credentials, service_account
from config.config import SERVICE_ACCOUNT_FILE, SCOPES, REPAIR_STATUS_SHEET_ID
import pandas as pd
from datetime import datetime

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# If modifying these scopes, delete the file token.json.


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1lKveppzfx1kJIKhFqpywt2xPccCRKhcck7x3wMt4Z7M'

# GoogleHelper return values of not null cells in list


def GoogleGetHelper(INPUT_RANGE):
    """
    Get repair stauts from spreadsheet.
    """
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    result = sheet.values().get(spreadsheetId=REPAIR_STATUS_SHEET_ID,
                                range=INPUT_RANGE,
                                ).execute()
    rows = result.get("values", [])
    headers = rows.pop(0)

    sn_orders = {
        'rows': rows,
        'headers': headers
    }

    return sn_orders


def GoogleUpdateHelper(OUTPUT_RANGE, result_dict):
    """
    Update repair stauts aoa to spreadsheet.
    """
    aoa = list()
    values = list(result_dict.values())
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    values.append(now)                      # add now time to list

    aoa.append(values)                      # append and convert dict.values to list

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    # update status result to sheet
    sheet.values().update(spreadsheetId=REPAIR_STATUS_SHEET_ID,
                          range=OUTPUT_RANGE,
                          valueInputOption="USER_ENTERED",
                          body={"values": aoa}).execute()

    return


def GoogleClearHelper(CLEAR_RANGE):
    """
    Clear range from spreadsheet.
    """
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                         range=CLEAR_RANGE,
                         body={}).execute()

    return
