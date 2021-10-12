from selenium.webdriver.support import expected_conditions
from lib.module import WebDriverWait, EC, By
from config.config import DRIVER_WAIT_TIME,KEY_LIST_HP

def GetRepairStatus(driver, sn, order_num):
    # get Service Order Number Element
    try:
        order_num_input = WebDriverWait(driver, DRIVER_WAIT_TIME).until(
            EC.presence_of_element_located(
                (By.ID, "ctl00_Content_ctl00_txtCSO")
            )
        )
        # enter order num
        order_num_input.send_keys(order_num)

        sn_input = WebDriverWait(driver, DRIVER_WAIT_TIME).until(
            EC.presence_of_element_located(
                (By.ID, "ctl00_Content_ctl00_txtSN")
            )
        )
        # enter serial number
        sn_input.send_keys(sn)

        get_status = WebDriverWait(driver, DRIVER_WAIT_TIME).until(
            EC.presence_of_element_located(
                (By.ID, "ctl00_Content_ctl00_csoGetStatus")
            )
        )
        # click get status
        get_status.click()
    except:
        print(f'*Failure Timeout*:Cannot send keys to input: {sn}')

    # wait until status elements located
    try:
        WebDriverWait(driver, 10).until(
            (lambda x: StatusRetrived(driver))
        )
    except:
        print(f'*Failure Timeout*:Cannot retrive repair status: {sn}')

    table_result = GetStatusTable(driver)
    return table_result


def StatusRetrived(driver):
    try:
        table_ele = WebDriverWait(driver, DRIVER_WAIT_TIME).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "ein_tablebig")
            )
        )
        return table_ele
    except:
        print("*Failure*:Cannot wait repair status table located.")

# retrieve hp status table
def GetStatusTable(driver):

    res = dict.fromkeys(KEY_LIST_HP)
    try:
        res['service_order'] = WebDriverWait(driver, DRIVER_WAIT_TIME).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(@id,'ctl00_Content_ctl00_rptOrderList_ctl00_') and contains(@id,'CSO')]")
            )
        ).text
    except:
        res['service_order'] = "NA"
    
    try:
        res['product'] = WebDriverWait(driver, DRIVER_WAIT_TIME).until(
            EC.presence_of_element_located(
                (By.ID, "ctl00_Content_ctl00_rptOrderList_ctl00_lblModel")
            )
        ).text
    except:
        res['product'] = "NA"
    
    try:
        res['service_event'] = WebDriverWait(driver, DRIVER_WAIT_TIME).until(
            EC.presence_of_element_located(
                (By.ID, "ctl00_Content_ctl00_rptOrderList_ctl00_lblService")
            )
        ).text
    except:
        res['service_event'] = "NA"

    try:
        res['order_status'] = WebDriverWait(driver, DRIVER_WAIT_TIME).until(
            EC.presence_of_element_located(
                (By.ID, "ctl00_Content_ctl00_rptOrderList_ctl00_lblStatus")
            )
        ).text
    except:
        res['order_status'] = "NA"

    try:
        res['est_deli_date'] = WebDriverWait(driver, DRIVER_WAIT_TIME).until(
            EC.presence_of_element_located(
                (By.ID, "ctl00_Content_ctl00_rptOrderList_ctl00_lblDelivery")
            )
        ).text
    except:
        res['est_deli_date'] = "NA"
    
    try:
        res['track'] = WebDriverWait(driver, DRIVER_WAIT_TIME).until(
            EC.presence_of_element_located(
                (By.ID, "ctl00_Content_ctl00_rptOrderList_ctl00_lblTracking")
            )
        ).text
    except:
        res['track'] = "NA"

    return res