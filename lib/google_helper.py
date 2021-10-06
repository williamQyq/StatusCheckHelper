from lib.module import print_function,build,InstalledAppFlow,Request,Credentials,service_account
import pandas as pd

SERVICE_ACCOUNT_FILE = 'config/keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# If modifying these scopes, delete the file token.json.


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1lKveppzfx1kJIKhFqpywt2xPccCRKhcck7x3wMt4Z7M'
RESULT_RANGE = 'RepairResult!A:C'
CLEAR_RANGE = 'RepairResult!D2:I'

# GoogleHelper return values of not null cells in list
def GoogleHelper(INPUT_RANGE, UPDATE_RANGE):
    """
    Get repair stauts from spreadsheet.
    """
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    # sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,
    #                      range=CLEAR_RANGE,
    #                      body={}).execute()
    # update result to sheet
    # sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
    #                       range=RESULT_RANGE,
    #                       valueInputOption="USER_ENTERED",
    #                       body={"values": aoa}).execute()

    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=RESULT_RANGE,
                                ).execute()
    rows = result.get("values", [])
    headers = rows.pop(0)

    # df  = pd.DataFrame(rows,columns=headers)
    # print(df.head())
    return rows
