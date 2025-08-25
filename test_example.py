import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Ожидаем, что заголовок "содержит" подстроку
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Клик на ожидаемую, на странице ссылку
    page.get_by_role("link", name="Get started").click()

    # Ожидаем, что на странице будет заголовок с именем Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


