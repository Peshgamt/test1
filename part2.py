from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Открываем страницу
    page.goto("https://example.com")
    
    # Проверяем заголовок
    assert "Example" in page.title(), "Заголовок не содержит 'Example'"
    
    # Находим и кликаем ссылку "More information"
    link = page.locator("css=a:has-text('More information')")
    link.click()
    
    # Проверяем URL после клика
    assert page.url == "https://www.iana.org/help/example-domains", "Неверный URL после клика"
    
    print("Все тесты прошли успешно!")
    browser.close()
