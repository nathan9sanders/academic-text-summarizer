import numpy as np
import pandas as pd
import nltk
# nltk.download('punkt') # one time execution
# nltk.download('stopwords') # one time execution
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
import math
import re

# function to remove stopwords
def remove_stopwords(sen):
  sen_new = " ".join([i for i in sen if i not in stop_words])
  return sen_new

# returns the top SN sentences in order
def get_summary(scores, sentences, SN):
  scored_sentences = sorted(((score, sentence) for score, sentence in zip(scores, sentences)), reverse=True)
  top_sentences = set([sentence for score, sentence in scored_sentences[:SN]])
  for sentence in sentences:
    if sentence in top_sentences:
      print(sentence)

df = pd.DataFrame(columns=['article_text'])

# just summarizing one at a time
article_list = []
with open('Lecture Transcripts/Week 2/Overview of Text Retrieval Methods.txt', 'r') as f:
  article = f.read().replace('\n', ' ')
  article_list.append(article)
df2 = pd.DataFrame(article_list, columns=['article_text'])
df = df.append(df2)

sentences = []
for s in df['article_text']:
  sentences.append(sent_tokenize(s))

sentences = [y for x in sentences for y in x] # flatten list

SN = math.ceil(len(sentences) * .35)

word_embeddings = {}
with open('model/glove.6B.100d.txt', encoding='utf-8') as f:
  for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    word_embeddings[word] = coefs

# remove punctuations, numbers and special characters
clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ")

# make alphabets lowercase
clean_sentences = [s.lower() for s in clean_sentences]

# get stopwords
stop_words = stopwords.words('english')

# remove stopwords from the sentences
clean_sentences = [remove_stopwords(r.split()) for r in clean_sentences]

sentence_vectors = []
for i in clean_sentences:
  if len(i) != 0:
    v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
  else:
    v = np.zeros((100,))
  sentence_vectors.append(v)

# similarity matrix
sim_mat = np.zeros([len(sentences), len(sentences)])

for i in range(len(sentences)):
  for j in range(len(sentences)):
    if i != j:
      sim_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(1,100), sentence_vectors[j].reshape(1,100))[0,0]

nx_graph = nx.from_numpy_array(sim_mat)
scores = nx.pagerank(nx_graph) 

get_summary(scores, sentences, SN)