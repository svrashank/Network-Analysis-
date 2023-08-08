import pandas as pd
import numpy as np
import spacy
from spacy import displacy
import networkx as nx
import os 
import matplotlib.pyplot as plt
from pyvis.network import Network
import community as community_louvain 
import math as mt


def read_books(file_path):
    """ 
    stores all the text files of all the books in the series in a single object 
    parameters :
        file_path -> file path to all the text files 
    returns :
        an object containing all the files 
    """
    all_books = [b for b in os.scandir(file_path) if '.txt' in b.name]
    return all_books 

def create_sent_ent_df(book):
    """
    Creates the dataframe with two columns 1)sentences in the book 2) the characters in that sentence
    parameters:
        book_text -> Text file of the book 
    returns :
        Dataframe of sentences and characters in that sentence  
    """
    book_text = open(book,encoding = 'utf-8').read()
    #all text prior to the prologue is unnecessary 
    book_text = book_text.split('PROLOGUE')[2]
    #Load our custom ner for GOT characters  
    nlp = spacy.load('got_ner')
    nlp.max_length = 1768660222
    doc = nlp(book_text)
    sent_ent = []
    for sent in doc.sents:
        ent_list = [ent.text for ent in sent.ents]
        sent_ent.append({'Sentence':sent,'Characters':ent_list})
    sent_ent_df = pd.DataFrame(sent_ent)
    sent_ent_df = sent_ent_df[sent_ent_df['Characters'].map(len)>0]
    sent_ent_df['Characters'] = sent_ent_df['Characters'].map(lambda x:[item.split()[0] for item in x])
    sent_entities = sent_ent_df.reset_index(drop=True)
    return sent_entities

def create_relationships(sent_ent):
    """
    Creates a Pandas dataframe edgelist which contains 3 columns 1)source 2) target 3)Weight
    parameters :
        sent_ent -> sentence entities dataframe 
    returns :
        Edgelist dataframe for networkx
    """


    #if the characters appear within a few sentences of each other or in the same sentence ,then they are connected 
    # create a rolling window of 5 sentences and make a list of all characters in those sentences. Drop Duplicates 
    relationship = []
    for i in range(sent_ent.index[-1]):
        end_i = min(i+5,sent_ent.index[-1])
        char = sum((sent_ent.loc[i:end_i].Characters),[])
        char_unique = [char[i] for i in range(len(char)) if (i == 0) or (char[i] != char[i-1])]
        if len(char_unique) > 1 :
            for idx,a in enumerate(char_unique):
                if idx == len(char_unique) - 1 :
                    continue
                b = char_unique[idx+1]
                rel_char = {'source':a,'target':b}
                relationship.append(rel_char)
    relationship = pd.DataFrame(relationship)

        # if a->b and b->a are the same .Sort them 
    relationship_df = pd.DataFrame(np.sort(relationship.values,axis=1),columns = relationship.columns)
    relationship_df['weight'] = 1 
    relationship_df = relationship_df.groupby(['source','target'],sort = False, as_index = False).sum()
    return relationship_df


def create_adjList(df):
    G = nx.from_pandas_edgelist(df,
                            source = 'source',
                            target = 'target',
                            edge_attr = 'weight',
                            create_using = nx.Graph()
                            )
    return G

def plot_centrality(G):
    cent_dict =[nx.degree_centrality(G),nx.betweenness_centrality(G),nx.closeness_centrality(G)]
    for item in cent_dict:
        centrality_df = pd.DataFrame.from_dict(item,orient='index',columns = ['col_name'])
        return centrality_df.sort_values('col_name',ascending=False)[:9].plot(kind='bar')
    
def build_communities_network(G):
    
    community = community_louvain.best_partition(G)
    nx.set_node_attributes(G,community,'group')
    net = Network(notebook = True, width="1000px", height="800px", bgcolor='#222222', font_color='white',cdn_resources='remote')
    #Increase node size wrt their number of connections 
    d = dict(G.degree)
    scale = 10
    d.update((x,y*scale) for x,y in d.items())
    nx.set_node_attributes(G,d,'size')

    net.show_buttons(filter_= ['physics','edges','nodes'])
    net.from_nx(G)
    net.barnes_hut()
    return net.show("GOT_try_communties.html")

