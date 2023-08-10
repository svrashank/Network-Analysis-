# Network-Analysis-
### Project Overview 
* The main objective of the project is to examine the extent of relationship between characters and also their significance in each book
* The character names in form of a list was obtained through webscrapping the wikipedia page of the novel
* The list was formated for all instances of a character's name used in the novel
* A custom named entity ruler(NER) was created based on the above character's names list
* This NER was then used on the novel to extract characters from every sentence
* An Edge list dataframe for Graph object was created(all mentioned in detail in the Graph analysis section)
* A characters prominence ,their relationship with other characters all were shown using Pyvis and Networkx module

### Code and Resources 
* The basic idea of this project was inspired by "Network of The Witcher" video by Vu Analytics (https://www.youtube.com/watch?v=fAHkJ_Dhr50)
* Packages and modules - Jupytr Notebook, Pandas ,numpy ,Pyvis, Networkx, NLP -spacy 3.0 , json, pickle, matplotlib, community, BeautifulSoup 
* Code:
  * Many references from the github repo of the referred video(https://github.com/thu-vu92/the_witcher_network)
  * Documentations of Networkx , spacy , pyvis 
  * Custom Entity ruler was created by referring to a series of videos by "Python Tutorials for Digital Humanities"
* Webscraper - Used BeautifulSoup libray to get names of the characters

### Data Cleaning 
* Had to remove filler words and house names from the scraped list of names
* Added different ways they would be addressed 
* Every book had a foreword and honorable mentions to real people in George.R.R.Martin's life. So, I splitted the file on the word Prolouge(every book had one)

### Methodology 
#### Step 1 :Webscrapper for Character Names 
* The Wikipdea page of the novel contained all the character names
* Extracted the names ,did some string formatting and dumped them in a json file (Refer 'character_name_scrapper.py' for detailed explanation)

#### Step2: Create a custom NER 
* 
 

