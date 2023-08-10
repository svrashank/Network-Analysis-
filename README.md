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
#### 1: Webscrapper for Character Names 
* The Wikipdea page of the novel contained all the character names
* Extracted the names ,did some string formatting and dumped them in a json file (Refer 'character_name_scrapper.py' for detailed explanation)

#### 2: Create a custom NER 
* Load the json file with character names ,using for loop create a dictionary consisting of label and the entity
* Pass this Dictionary as an NER into an empty spacy object
* Add a sentencizer to our custom ner

#### 3: Network Analysis of Book 1 
* Using our custom NER (GOT_NER) , a create a dataframe consisting of two columns 1)The sentence 2) Names of characterx in that sentence
* A set of characters are supposed to be closely related if they are mentioned in the same or subsequent few sentences
* Created a rolling window of 5 sentences. If two characters appeared within those 5 sentences then they were grouped together
* Using groupby and sum function we can calculate the number of time a set of characters interacted in a novel
* With the above information an edge list dataframe can be created and hence a graph object (G) was created 
* Graph visualizations :
  * Betweeness 
  * Centrality
  * Closeness 
* Communities module of python can show sets of character that frequently interact with each other
* ![alt text](https://github.com/svrashank/Network-Analysis-/blob/master/GOT_book1.JPG "Book 1 network and communities")

 #### 4: Character Relavancy and path between characters 
 * In the second notebook I create a graph object for all the books and store them using pickle module for future use
 * Using the graph object for all the books we cam track a characters importance throughout the series using measure centrality of all the books
 * ![alt text](https://github.com/svrashank/Network-Analysis-/blob/master/Char_evolve1.JPG 'Character Evolution')
 * ![alt text](https://github.com/svrashank/Network-Analysis-/blob/master/char_evolve2.JPG 'Character Evolution 2')
 * I further wanted to add a function that returns the most relevant path betweeen two characters
 * Example - Ramsay and jon may have a direct weight of 10 but there may be an alternative path with a greater weight
 * Some research into finding an algorithm showed that longest path problem to be np-hard
 * Instead ,setttled for the least relevant path between two characters using Djikstra's algorithm
 * ![alt text](https://github.com/svrashank/Network-Analysis-/blob/master/shortest%20path.JPG 'Shortest path') 

