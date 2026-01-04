from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
# global driver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


chrome_service = Service(executable_path='C:\KSR_Clt\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_service)
# PATH= "C:\KSR_Clt\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


#
# driver=webdriver.Chrome(PATH)
driver.get("https://access.ex.indianoil.in/oam/server/obrareq.cgi?encquery%3DKlay46rTppZ4k%2BzWxgx0zJRWlHGE3hr34MlJB%2B8uvnMG%2Bj8y1exrfJtSEtKDHRvgVIibyOp7dD8%2Fe4exfZSVOxPjYDzliiofrqBH6FpyKlL9M4zQxBZbeYoDAYeOEpea1kO00Hk9MnglE5GZBlH2IEiBHDQOPj5GBuVnfyNXdwwsWimFCF4DwK45VEd9fxFDlns6TkYneuQOffg3rG8O6b%2F2layC56lITPcIAD25s769zI8Sbwot0HLG7M82Xn4yiOExjMd758TnJ2%2FYj1h7e8Ys8hPvHFMsH%2Bl8eJyb42FYxlexw%2B%2FYO99o8ah0wJ5z7hSrlOTAvopxPz6BYIhE%2BiT9rrpXI%2FE14LGxmxmHhv4yMXXmpomzNu6h5sGY7iw5DWeegpQUNeRcFyv3o38%2BjPXLcl%2B0I143GkT3mxzTxJIGo6lu2pOue9%2BoCurjn0kd%20agentid%3DOHS_Siebel%20ver%3D1%20crmethod%3D2&ECID-Context=1.0067ASqsNbbBt1o5oVx0iY000RFI000OSo%3BkXjE")
search=driver.find_element(By.ID,"username")
search.send_keys("0000187729_01")
search.send_keys(Keys.TAB)
search=driver.find_element(By.ID,"password")
search.send_keys("epic@080223")
search.send_keys(Keys.TAB)
search=driver.find_element(By.ID,"submitid")
search.send_keys(Keys.RETURN)



time.sleep(5)
# driver.quit()
