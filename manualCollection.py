from selenium import webdriver
import time
import base64
import os
import requests
import threading

driver = webdriver.Chrome()

keyword = 'realistic drawing of person'
driver.get('https://images.google.com/')
driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input').send_keys(keyword)
driver.find_element_by_xpath('//*[@id="sbtc"]/button').click()

image_urls = []





for i in range(4):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(1)

driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
for i in range(4):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(1)
j = """var images = document.getElementsByTagName('img'); 
var srcList = [];
for(var i = 0; i < images.length; i++) {
    srcList.push(images[i].src);
}
document.write(srcList)"""
driver.execute_script(j)

allLinks = str(driver.find_element_by_xpath('/html/body').text).split(',')
driver.quit()
print(allLinks)
files = os.listdir("imageSets/drawing")
c = 0
for file in files:
    if int(str(file).split('.')[0]) > c:
        c = int(str(file).split('.')[0])


def writing(link, c):
    if "data:image" not in link:
        if "logos" not in link:
            if "http" not in link:
                imgdata = base64.b64decode(link)
                filename = f'imageSets/drawing/{c}.jpeg'
                with open(filename, 'wb') as f:
                    f.write(imgdata)
            else:
                r = requests.get(link)
                filename = f'imageSets/drawing/{c}.jpeg'
                with open(filename, 'wb') as f:
                    f.write(r.content)


c += 1
print(c)
input("hold")

for link in allLinks:
    threading.Thread(target=writing, args=(link, c,)).start()
    c += 1
