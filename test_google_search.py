import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver():
    # ทำงานก่อนเริ่มทุกๆ Test Case: เปิด Browser และไปที่ Google
    # Selenium Manager (built-in ตั้งแต่ Selenium 4.6+) จะจัดการ chromedriver ให้อัตโนมัติ
    # ถ้าต้องการระบุ path ของ chromedriver.exe เอง ให้ใช้ Service แทน (ดูคอมเมนต์ด้านล่าง)
    #
    # from selenium.webdriver.chrome.service import Service
    # service = Service(executable_path="./src/chromedriver.exe")
    # drv = webdriver.Chrome(service=service)

    drv = webdriver.Chrome()
    drv.get("https://www.google.com")

    yield drv

    # ทำงานหลังจบทุกๆ Test Case: ปิด Browser และคืนทรัพยากรระบบทั้งหมด
    drv.quit()


def test_tc_101_search_by_keyword(driver):
    search_box = driver.find_element(By.ID, "APjFqb")
    search_box.send_keys("NPRU")
    search_box.send_keys(Keys.ENTER)


@pytest.mark.skip(reason="Temporarily disabling this test case")
def test_tc_102_search_software(driver):
    search_box = driver.find_element(By.ID, "APjFqb")
    search_box.send_keys("Software")
    search_box.send_keys(Keys.ENTER)
