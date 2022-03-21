from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

browser = webdriver.Firefox(options=options, executable_path="./drivers/geckodriver")

browser.get('https://whatis.techtarget.com/glossary/Linux')

beeglist = browser.find_element_by_id("definitions-listing")
defs = beeglist.find_elements_by_tag_name("li")

f = open("output.txt", "w")

print(len(defs))

for definition in defs:
    f.write(definition.text)
    f.write("\n")

f.close()
browser.quit()