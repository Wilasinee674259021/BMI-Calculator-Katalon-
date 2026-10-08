from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://www.calculator.net/bmi-calculator.html")
driver.find_element(By.ID,"cage").click()
driver.find_element(By.XPATH,"//table[@id='calinputtable']/tbody/tr").click()
driver.find_element(By.ID,"cage").clear()
driver.find_element(By.ID,"cage").send_keys("66")
driver.find_element(By.XPATH,"//table[@id='calinputtable']/tbody/tr[2]/td[2]/label[2]/span").click()
driver.find_element(By.ID,"cheightmeter").click()
driver.find_element(By.ID,"cheightmeter").clear()
driver.find_element(By.ID,"cheightmeter").send_keys("166")
driver.find_element(By.ID,"metricweight").click()
driver.find_element(By.ID,"ckg").clear()
driver.find_element(By.ID,"ckg").send_keys("56")
driver.find_element(By.ID,"content").click()
driver.find_element(By.NAME,"x").click()

print(driver.title)

time.sleep(5)
#driver.quit()