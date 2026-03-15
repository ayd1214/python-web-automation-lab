from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    # Chromium 브라우저 사용
    browser = p.chromium.launch(headless=True, args=['--ignore-certificate-errors', '--disable-http2'])
    
    context = browser.new_context(
        viewport={"width": 1280, "height": 2000},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.94 Safari/537.36"
    )
    
    page = context.new_page()
    
    try:
        # 페이지 열기 : https://flyasiana.com/C/KR/KO/index
        page.goto('https://google.com', wait_until='load', timeout=60000)
        print("페이지 제목:", page.title())

        # 스크린샷 찍기
        page.screenshot(path='ch_before_click.png', full_page=True)

        # 버튼이 가시적일 때까지 기다림
        page.wait_for_selector('//*[@id="input"]', timeout=60000)  # 더 구체적인 선택자

        # 버튼 클릭하기
        button = page.locator('//*[@id="input"]')  # 앵커 태그로 명확하게 선택
        button.click()

        time.sleep(2)  # 페이지가 로드될 시간을 확보 (옵션)

        # 스크린샷 찍기
        page.screenshot(path='ch_after_click.png', full_page=True)

    except Exception as e:
        print("오류 발생:", e)

    finally:
        context.close()  # 브라우저 컨텍스트 닫기
        browser.close()   # 브라우저 닫기
