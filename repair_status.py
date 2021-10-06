from lib.google_helper import RESULT_RANGE, GoogleHelper

def main():
    SN_ORDER_NUM_RANGE = 'RepairResult!A:C'
    RESULT_RANGE = 'RepairResult!D2:I'

    # get SN and Order num sheet values
    sn_order_nums = GoogleHelper(SN_ORDER_NUM_RANGE,RESULT_RANGE)

    # switch brand 
    
    # await and crawl results


    #out put result
    

if __name__ == '__main__':
    main()