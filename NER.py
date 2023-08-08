import spacy 
import json

with open ('Data\got1.txt','r',encoding='utf-8') as f:
    text = f.read()

def load_data(file):
    """loads the json file 
        parameters :filepath 
        returns :object with the json file 
    """
    with open(file,'r',encoding = 'utf-8') as f:
        data = json.load(f)
    return data 

def create_training_data(label,file):
    """
        takes the json file and returns a list in desired format to create an custom entity ruler 
        parameters :label of the NER ,json file 
        returns :List of the dicts with labels and character name 
    """
    data = load_data(file)
    patterns = []
    for items in data:
        pattern = {'label':label,'pattern':items}
        patterns.append(pattern)
    return patterns 

def create_entity_ruler(file,entity_ruler_name):
    """
        Creates an entity ruler and saves it to disk 
        parameters :jsonfile , name of our custom entity ruler 
        returns : None 
    """
    patterns = create_training_data('PERSON',file)
    nlp = spacy.blank('en')
    ruler = nlp.add_pipe('entity_ruler')
    ruler.add_patterns(patterns)
    #add sentencizer to the model 
    nlp.add_pipe("sentencizer")
    nlp.to_disk(entity_ruler_name)
    return "Success"
    


print(create_entity_ruler('characters_for_ner.json','got_ner'))

