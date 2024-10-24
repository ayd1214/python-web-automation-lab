from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import TimeoutException



proxy_ip_port = '10.27.0.0:80'

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.ssl_proxy = proxy_ip_port

capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

# replace 'your_absolute_path' with your chrome binary absolute path
driver = webdriver.Chrome()
driver.set_page_load_timeout(5)
try:
    driver.get('https://www.tiktok.com/signup/phone-or-email/email')
except TimeoutException:
    print("Proxy: ", proxy_ip_port, "invalid")
