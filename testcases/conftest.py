import pytest
from selenium import webdriver

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("headless")


# Multiple browser Testing
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome(options=chrome_option)
    driver.get("https://www.idrive360.com/enterprise/login")
    driver.maximize_window()
    # driver.implicitly_wait(5)
    yield driver
    driver.quit()
