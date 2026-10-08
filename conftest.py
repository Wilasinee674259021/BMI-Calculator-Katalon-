import os
import pytest


REPORTS_DIR = os.path.join(os.path.dirname(__file__), "reports")
SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, "screenshots")


def pytest_configure(config):
    # สร้างโฟลเดอร์เก็บรายงานและภาพหน้าจอ (ถ้ายังไม่มี)
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)


def pytest_html_report_title(report):
    report.title = "Selenium Test Report - BMI Calculator / Google Search"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # hook นี้ทำงานหลังจบแต่ละ test case เพื่อแนบภาพหน้าจอ
    # เข้าไปในรายงาน HTML โดยอัตโนมัติ เฉพาะตอนที่ test ล้มเหลว (fail)
    outcome = yield
    report = outcome.get_result()

    pytest_html = item.config.pluginmanager.getplugin("html")
    extra = getattr(report, "extra", [])

    if report.when == "call" and pytest_html is not None:
        driver = item.funcargs.get("driver", None)

        if report.failed and driver is not None:
            screenshot_name = f"{item.name}.png"
            screenshot_path = os.path.join(SCREENSHOTS_DIR, screenshot_name)
            try:
                driver.save_screenshot(screenshot_path)
                relative_path = os.path.join("screenshots", screenshot_name)
                extra.append(pytest_html.extras.image(relative_path))
                extra.append(pytest_html.extras.url(driver.current_url))
            except Exception as e:
                print(f"ไม่สามารถบันทึกภาพหน้าจอได้: {e}")

    report.extra = extra
