from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

# ================= PLAYWRIGHT =================
url = "https://coinmarketcap.com"

with sync_playwright() as p:
    browser = p.chromium.launch(
    executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    headless=False
    )
    context = browser.new_context(
        viewport=None,
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    )
    page = context.new_page()

    page.goto(url, timeout=180000, wait_until="networkidle")

    page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
    page.wait_for_timeout(7000)

    page.screenshot(path="page_loaded.png")

    html = page.content()
    browser.close()

# ================= PARSE =================
soup = BeautifulSoup(html, "html.parser")
title = soup.select(".coin-item-name")
for t in title:
    print(t.text)