from lib.init import InitChromeDriver
from lib.hp_fun import GetRepairStatus
def Tracker():
    driver = InitChromeDriver()

    GetRepairStatus()