import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from pageObjects.Home_page import Home_page
from utilities.Logger import LoggenClass


class Test_singin:
    log = LoggenClass.log_generator()

    @pytest.mark.smoke
    @allure.title("Verify that login is working in IDrive360 website")
    @allure.description("TC#1 - simple login check on IDrive360 website.")
    def test_signin(self, setup):
        self.driver = setup
        self.hp = Home_page(self.driver)
        self.log.info("Verify URL")
        assert self.driver.title == "IDrive® 360 - Sign in to your account"
        # print(self.driver.title)
        self.log.info("Enter the Email")
        self.hp.Enter_Email("augtest_040823@idrive.com")
        self.log.info("Enter the Password")
        self.hp.Enter_Password("123456")
        self.log.info("Click SignIN Button")
        self.hp.Click_SignIn_Button()
        self.log.info("Wait till 40 sec complete locator get visible")
        time.sleep(40)
        # print(self.driver.title)
        self.log.info("Verify ErrorMessage and CurrentPage URL")
        header_message = self.driver.find_element(By.XPATH, "//h5[@class='id-card-title']").text
        assert header_message == "Your free trial has expired", "Error - Invalid message"
        assert self.driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true", "Error - Invalid URL"
        allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
