from lib.init import InitChromeDriver
from lib.hp.hp_fun import GetRepairStatus
def Tracker(sn, order_num):
    # init chrome driver
    driver = InitChromeDriver()
    driver.get("https://h20212.www2.hp.com/Cso_Status/CsoStatus.aspx?lc=EN&cc=US")

    # get repair stats table result from hp repair stauts
    result = GetRepairStatus(driver, sn, order_num)
    # quit chrome driver
    driver.quit()

    return result
