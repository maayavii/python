print("SJC22MCA-2007 : Amal Manoj")
print("Batch : MCA 2022-24")
from nltk import ngrams
sentence = 'I reside in India'
n = 3
trigrams = ngrams(sentence.split(),n)
for grams in trigrams:
  print(grams)