from playwright import sync_playwright


with sync_playwright() as p:
    browser = p.webkit.launch(headless=False)
    context = browser.newContext()
    page = context.newPage()
    page.goto('https://google.com')
    page.screenshot(path='screenshots/single-{browser}.png')
    browser.close()