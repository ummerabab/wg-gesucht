import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path =r'C:\Users\hossa\Downloads\New folder\chromedriver\chromedriver.exe')
driver.get('https://www.wg-gesucht.de/wg-zimmer-in-Passau.104.0.1.0.html')
links_dict ={}
results_dict ={}

if(driver.find_element_by_class_name('card_body')):
    print('Class found')
else:
    print('No class found')

results = driver.find_elements_by_class_name('card_body')
links = driver.find_elements_by_class_name('truncate_title')

for num in range(len(links)):

    links_dict[links[num].find_element_by_tag_name('a').get_attribute('href')]=num
print(len(links_dict))
for count in range(len(results)):
    results_dict[results[count].get_attribute('outerText')]=count

print(list(results_dict))
print(list(links_dict))


driver.quit()

    #name = a.find('h3')
   # if name not in results:
        #results.append(name.text)

#df =pd.DataFrame({'name':results})
#df.to_csv('name.csv', index=True, encoding='utf-8')
