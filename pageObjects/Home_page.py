from selenium.webdriver.common.by import By


class Home_page:
    Enter_Email_xpath = "//input[@id='username']"
    Enter_Password_xpath = "//input[@id='password']"
    Click_SignIn_Button_xpath = "//button[@id='frm-btn']"

    def __init__(self, driver):
        self.driver = driver

    def Enter_Email(self, username):
        self.driver.find_element(By.XPATH, self.Enter_Email_xpath).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(By.XPATH, self.Enter_Password_xpath).send_keys(password)

    def Click_SignIn_Button(self):
        self.driver.find_element(By.XPATH, self.Click_SignIn_Button_xpath).click()
