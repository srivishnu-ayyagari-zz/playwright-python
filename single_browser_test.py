from playwright import sync_playwright


with sync_playwright() as p:
    # Initialize the browser Chromium/FireFox/Webkit
    browser = p.webkit.launch(headless=False)

    # Creating the context
    context = browser.newContext()

    # Executing the test cases
    page = context.newPage()
    page.goto('https://google.com')

    # Capturing the screenshots
    page.screenshot(path='screenshots/single-{browser}.png')

    # Closing the browser
    browser.close()