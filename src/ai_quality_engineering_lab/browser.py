from playwright.sync_api import sync_playwright
from ai_quality_engineering_lab.observation import build_observation
from ai_quality_engineering_lab.executor import (
    UnknownElementReferenceError,
    execute_click,
)
from ai_quality_engineering_lab.tools import ClickAction

def open_browser(url: str):
    with sync_playwright() as playwright:
        browser =  playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)

        context = build_observation(page)

        action = ClickAction(
            action="click",
            arguments={
                "element_ref": "e999",
            },
        )

        try:
            execute_click(action, context)
        except UnknownElementReferenceError as error:
            print(f"Action execution failed: {error}")

open_browser("https://automationexercise.com")