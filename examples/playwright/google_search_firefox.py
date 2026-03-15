from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    # Chromium 브라우저 사용
    browser = p.firefox.launch(headless=True)

    context = browser.new_context(
        viewport={"width": 1280, "height": 2000},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.94 Safari/537.36"
    )

    page = context.new_page()

    try:
        # Google 페이지 열기
        page.goto('https://www.google.com', wait_until='domcontentloaded', timeout=60000)
        page.screenshot(path='google_search_playwright_before.png')


        # 검색 입력창이 로드될 때까지 대기
        search_box = page.wait_for_selector('input[name="q"]', timeout=60000)
        
        # 검색 입력창에 "Playwright" 입력하기
        search_box.fill('Playwright')

        # 검색 실행 (Enter 키 누르기)
        search_box.press('Enter')

        # 결과 페이지가 로드될 때까지 기다리기
        page.wait_for_load_state('load')

        # 현재 페이지 제목 출력
        print("현재 페이지 제목:", page.title())

        # 스크린샷 찍기
        page.screenshot(path='google_search_playwright.png')

    except Exception as e:
        print("오류 발생:", e)

    finally:
        context.close()  # 브라우저 컨텍스트 닫기
        browser.close()   # 브라우저 닫기
