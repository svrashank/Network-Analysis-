from bs4 import BeautifulSoup 
import requests 
import csv
import pandas as pd 
import json 


#Scraping wikipedia page of "The song of fire and ice" for character names 
url = 'https://en.wikipedia.org/wiki/List_of_A_Song_of_Ice_and_Fire_characters'
headers = {"User-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
r = requests.get(url=url,headers = headers).text
soup = BeautifulSoup(r,'html.parser')


#required information is in the class 'mw-headline' ,but there are some unnecessary titles mentioned too  
character_names = soup.find_all('span',{'class':'mw-headline'})
temp_characters =[]
for character in character_names:
    temp_characters.append(character.text)
#Following list contains all the unecessary information 
extras = ['House','Family','Servants and vassals','Vassals','Animals', 'Direwolves','Other characters', 'Dragons', 'References', 'Secondary sources', 'Primary sources', 'Bibliography', 'External links']
#Apply lambda function to the list to replace all the objects in the list above with "" and use the filter function to remove ""
all_characters = list(map(lambda x : '' if (x in extras or x.split()[0] == 'House') else x,temp_characters))
final_characters = list(filter(lambda x: x !='',all_characters))


#We finally have a list of all the major characters mentioned throughout the series of novels 
#Store it in a dataframe and since most of the characters are mentioned by their first name, make a column with just the first names 
characters_dict = {'Name':[]}
for i,j in enumerate(final_characters):
    characters_dict['Name'].append(j) 
characters = pd.DataFrame(characters_dict,index=range(len(final_characters)))
characters['first_name'] = characters['Name'].apply(lambda x: x.split()[0] if len(x.split()) < 3 else x.split()[:2])
#Some characters are mentioned like 'Aegon V' ,using string formatting grab that from the names column 
characters['first_name'] = characters['first_name'].apply(lambda x :'{}'.format(x[0])+' '+'{}'.format(x[1]) if isinstance(x,list) else x)
characters['first_name'] = characters['first_name'].apply(lambda x : 'The Waif' if x =="The" else x)


#Save the dataframe as a csv
characters.to_csv('Characters.csv')

#To create a custom ner we need the characters list as a json file. Dump Name and first Names to this list and save as json 
all_char = []
with open ('characters_for_ner.json','w') as f:
    for char in characters.Name:
        all_char.append(char)
    for char in characters.first_name:
        all_char.append(char)
    json.dump(all_char,f,indent=4)



