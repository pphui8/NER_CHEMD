# transfer csv data to spacy format

import pandas as pd
import spacy
from spacy.tokens import DocBin

# Load your CSV file 
# data = pd.read_csv('temp.csv', encoding='utf-8')
# data = pd.read_csv('training.csv', encoding='utf-8')
data = pd.read_csv('validation.csv', encoding='utf-8')
Tags = ['B-TRIVIAL', 'I-IDENTIFIER', 'B-SYSTEMATIC', 'B-ABBREVIATION', 'B-NO CLASS', 'B-FAMILY', 'I-SYSTEMATIC', 'B-MULTIPLE', 'I-NO CLASS', 'B-IDENTIFIER', 'I-FAMILY', 'I-MULTIPLE', 'I-TRIVIAL', 'I-ABBREVIATION', 'O', 'I-FORMULA', 'B-FORMULA']

nlp = spacy.load("en_core_web_sm") # load other spacy model
db = DocBin()


# Restore the sentences and entities
sentences = []
pre_sentence_index = 0
current_sentences = ''
sentence_start_index = 0

def find_word_indices(sentence, word):
    start_index = sentence.find(word)
    if start_index != -1:  # Word found
        end_index = start_index + len(word) - 1
        return start_index, end_index
    else:
        return None  # Word not found

def find_entities(start, end, sentence, ents):
    for i in range(start, end):
        if data['Tag'][i] != 'O':
            result = find_word_indices(sentence, data['Token'][i])
            if result is not None:
                start_index, end_index = result
            else:
                continue
            if start_index is not None and end_index is not None:
                ents.append((start_index, end_index, data['Tag'][i]))
                # span = doc.char_span(start_index, end_index, label=data['Tag'][i], alignment_mode="contract")
                # ents.append(span)

for i in range(len(data)):
    # doc = nlp.make_doc(data['Token'][i]) # create doc object from text
    if data['Sentence_Index'][i] == pre_sentence_index:
        if data['Token'][i] == '.' or data['Token'][i] == '!' or data['Token'][i] == '?' or data['Token'][i] == ';' or data['Token'][i] == ',' or data['Token'][i] == ')':
            current_sentences = current_sentences[:-1]
        if data['Token'][i] == '(':
            current_sentences += str(data['Token'][i])
            continue
        
        current_sentences += str(data['Token'][i]) + ' '
    else:
        # current_sentences = current_sentences[:-1]
        doc = nlp.make_doc(current_sentences)
        ents = []
        doc_ents = []
        find_entities(start=sentence_start_index, end=i, sentence=current_sentences, ents=ents)

        for start, end, label in ents:
            span = doc.char_span(start, end + 1, label=label, alignment_mode="contract")
            if span is not None:
                doc_ents.append(span)
        
        # print(current_sentences)
        try:
            doc.ents = doc_ents # label the text with the ents
            pass
        except:
            pass
            
        db.add(doc)

        current_sentences = ''
        pre_sentence_index = data['Sentence_Index'][i]
        sentence_start_index = i

# print(doc_ents)
# db.to_disk("./training.spacy") # save the docbin object
db.to_disk("./validation.spacy") # save the docbin object

