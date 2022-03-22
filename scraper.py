from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True


webList = [
    'https://whatis.techtarget.com/glossary/Linux',
    'https://whatis.techtarget.com/glossary/Software-Applications',
    'https://whatis.techtarget.com/glossary/Storage-and-Data-Management',
    'https://whatis.techtarget.com/glossary/Web-services-SOA',
    'https://whatis.techtarget.com/glossary/Operating-Systems',
]

browser = webdriver.Firefox(options=options, executable_path="./drivers/geckodriver")
browser.get('https://whatis.techtarget.com/glossary/Web-services-SOA')

nPages = browser.find_element_by_class_name("browse-alpha-bridge-nav")
nPages = nPages.find_elements_by_tag_name("li")
print(len(nPages))

f = open("output.txt", "w")

pageList = []

for page in nPages:
    anchor = page.find_element_by_tag_name("a")
    link = anchor.get_attribute("href")
    pageList.append(link)

browser.quit()

for pageLink in pageList: 

    nbrowser = webdriver.Firefox(options=options, executable_path="./drivers/geckodriver")
    nbrowser.get(pageLink)

    beeglist = nbrowser.find_element_by_id("definitions-listing")
    defs = beeglist.find_elements_by_tag_name("li")

    print(len(defs))

    for definition in defs:
        f.write(definition.text)
        f.write("\n")
    
    nbrowser.quit()

f.close()