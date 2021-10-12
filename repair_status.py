import pprint
from lib.google_helper import GoogleGetHelper, GoogleUpdateHelper
from lib.hp.hp_repair_tracker import Tracker
import pandas as pd

def main():
    SN_ORDER_NUM_RANGE = 'RepairResult!A:C'

    # get SN and Order num sheet values
    sn_order = GoogleGetHelper(SN_ORDER_NUM_RANGE)
    df = pd.DataFrame(sn_order['rows'], columns=sn_order['headers'])

    # switch brand
    # ...

    # await and crawl results
    for index, row in df.iterrows():
        if(row['Brand'] == 'HP'):
            result = Tracker(row['SN'], row['Order Num'])
            GoogleUpdateHelper(f'RepairResult!D{index+2}:J', result)
            print(f'Update Progress: {(index+1)/len(df.index)*100}%')

    # out put result
    print("Finished.")
    return

if __name__ == '__main__':
    main()
