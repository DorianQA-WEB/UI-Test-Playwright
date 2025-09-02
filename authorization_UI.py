from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page


    def enter_username(self, username: str):
        self.page.fill('input[name="username"]', username)

    def enter_password(self, password: str):
        self.page.fill('input[name="password"]', password)

    def click_login_button(self):
        self.page.click('button[type="submit"]')

    def is_error_message_displayed(self):
        return self.page.is_visible(".error-message")
