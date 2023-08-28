import logging

from selenium.webdriver import Keys

from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')
    LOCATOR_HELLO_LOGIN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_CREATE_POST_BTN = (By.ID, 'create-btn')
    LOCATOR_POST_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_POST_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_POST_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_POST_IMG = (By.XPATH, """//*[@id="create-item"]/div/div/div[6]/div/div/label/input""")
    LOCATOR_POST_ADDED = (By.CSS_SELECTOR, 'h1')
    LOCATOR_CONTACT_LINK = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_INPUT_YOUR_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_INPUT_YOUR_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_INPUT_CONTENT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button/span""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Sending {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Sending {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Clicking login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        logging.info(f"Found text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_login_text(self):
        element_successful_login = self.find_element(TestSearchLocators.LOCATOR_HELLO_LOGIN)
        return element_successful_login.text

    def click_create_post_btn(self):
        logging.info('Clicking create new post button')
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()

    def enter_post_title(self, word):
        logging.info(f'Sending {word} to element {TestSearchLocators.LOCATOR_POST_TITLE[1]}')
        title_field = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE)
        title_field.clear()
        title_field.send_keys(word)

    def enter_post_description(self, word):
        logging.info(f'Sending {word} to element {TestSearchLocators.LOCATOR_POST_DESCRIPTION[1]}')
        description_field = self.find_element(TestSearchLocators.LOCATOR_POST_DESCRIPTION)
        description_field.clear()
        description_field.send_keys(word)

    def enter_post_content(self, word):
        logging.info(f'Sending {word} to element {TestSearchLocators.LOCATOR_POST_CONTENT[1]}')
        content_field = self.find_element(TestSearchLocators.LOCATOR_POST_CONTENT)
        content_field.clear()
        content_field.send_keys(word)

    def enter_img_path(self, path):
        logging.info(f'Sending {path} to element {TestSearchLocators.LOCATOR_POST_IMG[1]}')
        img_field = self.find_element(TestSearchLocators.LOCATOR_POST_IMG)
        img_field.clear()
        img_field.send_keys(path)

    def click_save_btn(self):
        logging.info('Clicking save button')
        self.find_element(TestSearchLocators.LOCATOR_SAVE_BTN).click()

    def get_added_post_title(self):
        post_title = self.find_element(TestSearchLocators.LOCATOR_POST_ADDED)
        text = post_title.text
        logging.info(f"Found text {text} in title {TestSearchLocators.LOCATOR_POST_ADDED[1]}")
        return text

    def click_contact_link(self):
        logging.info('Clicking Contact link')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_LINK).click()

    def enter_contact_name(self, contact_name):
        logging.info(f'Sending {contact_name} to element {TestSearchLocators.LOCATOR_INPUT_YOUR_NAME[1]}')
        name_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_YOUR_NAME)
        name_field.clear()
        name_field.send_keys(contact_name)

    def enter_contact_email(self, contact_email):
        logging.info(f'Sending {contact_email} to element {TestSearchLocators.LOCATOR_INPUT_YOUR_EMAIL[1]}')
        email_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_YOUR_EMAIL)
        email_field.clear()
        email_field.send_keys(contact_email)

    def enter_contact_content(self, content):
        logging.info(f'Sending {content} to element {TestSearchLocators.LOCATOR_INPUT_CONTENT[1]}')
        content_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_CONTENT)
        content_field.clear()
        content_field.send_keys(content)

    def click_contact_us_btn(self):
        logging.info('Clicking Contact us button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        logging.info(f'Got alert {text}')
        return text
