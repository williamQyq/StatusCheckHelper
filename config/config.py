import os

REPAIR_STATUS_SHEET_ID = '1lKveppzfx1kJIKhFqpywt2xPccCRKhcck7x3wMt4Z7M'
# used to create google credentials 
CWD = "D:\William\William\RepairStatusHelper\\"
SERVICE_ACCOUNT_FILE = CWD+'config/keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

USER_AGENT={'User-Agent':
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
           'Accept-Language': 'en-US, en;q=0.5'}


DRIVER_WAIT_TIME = 15

KEY_LIST_HP = ["service_order","product","service_event","order_status","est_deli_date","track"]