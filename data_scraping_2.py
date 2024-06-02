from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


# NOTE: The page at the given URL is maintained by "wikipedia", which might be updated in future.

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url)
#read the page - parser will read everything one by one
soup = bs(page.text,'html.parser')

star_table = soup.find_all('table')

temp_list= []

table_rows = star_table[7].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    #each of the i tags in the td tags will be stored as a row - different row for different i tags
    #i tags inside td tags which are inside tr tags
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]


for i in range(1,len(temp_list)):
    
    #all the i tags for each star name, distance, mass and radius
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

#zip - zipped folder and it will unzip the folder for you
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

#creating a new csv file of new information
df2.to_csv('dwarf_stars_1.csv')
