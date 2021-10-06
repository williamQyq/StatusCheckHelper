from lib.module import webdriver,Options,user_agent
import os

# init set up chrome driver
def InitChromeDriver():
    
    chrome_driver_path = GetChromeDriverPath()
    chrome_options = Options()

    chrome_options.add_experimental_option("detach",True)                                   #Run Chrome driver without closing when finished
    chrome_options.add_argument(f'user-agent={user_agent}')                                 #Set user agent headers for Chrome driver
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('headless')                                               #Run Chrome driver without opening browser 
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

    return driver

def GetChromeDriverPath():
    cwd = os.getcwd()
    driver_path = '\driver\chromedriver.exe'
    chrome_driver_path = cwd+driver_path

    return chrome_driver_path
    