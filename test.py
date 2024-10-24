# driver = webdriver.Chrome(executable_path = '../driver/chromedriver')

# dirver.get(url)

# magnifier_button = dirver.find_element_by_id('ma')

import requests
from bs4 import BeautifulSoup

url = 'https://lolchess.gg/?hl=ko-KR&utm_source=dak.gg&utm_medium=inhouse&utm_campaign=family'
header_info =  {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'}

page = requests.get(url, headers = header_info)
page = page.text

soup = BeautifulSoup(page, 'html.parser')

top10_dacks = soup.find_all(class_ = 'css-35tzvc emls75t4')

top10_dacks_list = list()   

for each_data in top10_dacks :
    dack_name = each_data.text
    dack_name = dack_name.strip()
    top10_dacks_list.append(dack_name)


print(top10_dacks_list)
print(len(top10_dacks_list))