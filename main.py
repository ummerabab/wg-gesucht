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
#print('links', links)
for num in range(len(links)):

    links_dict[links[num].find_element_by_tag_name('a').get_attribute('href')]=num
print(len(links_dict))
for count in range(len(results)):
    results_dict[results[count].get_attribute('outerText')]=count
list1 =[]
titles_list = list(results_dict)
links_list = list(links_dict)

for num in range(len(titles_list)):
    list1.append([titles_list[num], links_list[num]])

print(list1)
my_pages = pd.DataFrame(list1, columns=['Description', 'Links'])
my_pages.to_csv('dataset.csv')
#content_dict =[]
#for link in links_dict:
    #driver.get(link)

    #content= driver.find_elements_by_id('freitext_2_content')
    #print(content.find_element_by_tag_name('p').get_attribute('innerHTML'))
   # content_dict.append(content)
#print(content_dict)
#print(results_dict)
#print(links_dict)
#results_dict.update(links_dict)
#print('updated dictionary 1:')
#print(results_dict)


driver.quit()
