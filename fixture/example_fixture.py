import pytest
from playwright.sync_api import Page


def before_each_after_each(page: Page):

    print("перед выполнением теста")