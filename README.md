# Python Web Automation Lab

This repository contains small experiments and practice projects for
**web automation and web scraping using Python**.

The goal of this repository is to explore different tools and approaches
for interacting with web pages programmatically, including both static
scraping and browser automation.

------------------------------------------------------------------------

## Tech Stack

-   Python
-   requests
-   BeautifulSoup4
-   Selenium
-   Playwright

------------------------------------------------------------------------

## Repository Structure

examples/ playwright/ \# Browser automation experiments using Playwright
requests_bs4/ \# Static web scraping using requests + BeautifulSoup
selenium/ \# Browser automation using Selenium

assets/ screenshots/ \# Screenshots generated from automation scripts

------------------------------------------------------------------------

## Examples

### Web Scraping with Requests + BeautifulSoup

File: examples/requests_bs4/lolchess_scraper.py

This script demonstrates simple web scraping using `requests` and
`BeautifulSoup`.

What this script does: - Sends an HTTP request to a webpage - Parses the
HTML document - Extracts specific elements using CSS selectors

Skills practiced: - HTTP requests - HTML parsing - Data extraction using
selectors

------------------------------------------------------------------------

### Selenium Automation

File: examples/selenium/asiana_mobile_screenshot.py

This script uses Selenium to open a mobile webpage and capture a
screenshot.

Skills practiced: - Browser automation - WebDriver configuration -
Automated screenshot capture

------------------------------------------------------------------------

### Playwright Automation

Files: - examples/playwright/google_search_firefox.py -
examples/playwright/google_click_experiment.py

These scripts demonstrate basic browser automation using Playwright.

Skills practiced: - Launching browsers with Playwright - Interacting
with page elements - Waiting for page elements to load

------------------------------------------------------------------------

### Proxy Connection Experiment

File: examples/selenium/proxy_connection_test.py

This experiment tests Selenium browser connections using a proxy server.

Skills practiced: - Proxy configuration - Browser networking setup -
Testing automated connections

------------------------------------------------------------------------

## What I Learned

Through these experiments I explored:

-   The difference between static scraping and browser automation
-   How Selenium and Playwright interact with web pages
-   Handling dynamic web content
-   Organizing experimental scripts into a clean repository structure

------------------------------------------------------------------------

## Notes

This repository focuses on learning and experimentation rather than
production-ready projects.

Future improvements may include: - Expanding automation examples -
Adding more structured scraping scripts - Converting experiments into
small standalone projects
