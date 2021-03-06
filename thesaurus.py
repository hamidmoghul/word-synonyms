# -*- coding: utf-8 -*-
"""Thesaurus.ipynb

**Find word synonyms(kinda) using Spacy library**
"""

#download spacy library
!python -m spacy download en_core_web_md

# import Spacy and load it
import spacy
nlp = spacy.load("en_core_web_md")

# get the embeddings for the vocabulary words and make a document-term matrix
vocab = list(nlp.vocab.strings)

# eliminate duplicates due to mixing upper and lower case
lower_vocab = [word.lower() for word in vocab]
vocab = list(set(lower_vocab))

# create word vector: 
import numpy as np
word_vectors = [nlp.vocab.get_vector(word) for word in vocab]
word_vectors = np.asarray(word_vectors)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# from sklearn.neighbors import NearestNeighbors
# 
# # Fit a nearest-neighbors model to the dtm
# nn = NearestNeighbors(n_neighbors=5, algorithm='auto', n_jobs=-1)
# 
# # fit to the dtm of all the vocabulary words
# nn.fit(word_vectors)

"""Enter any vocabulary(e.g. 'cool') to querry its synonyms"""

query_word = 'cool'
query_vector = nlp.vocab.get_vector(query_word)[None,:]
query_vector.shape

"""Find the 5 nearest neighboring words using Spacy library"""

neigh_dist, neigh_index = nn.kneighbors(query_vector, n_neighbors=5)
[vocab[int(index)] for index in neigh_index[0]]
