import nltk
from nltk import ngrams
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')  # Added download for stopwords

from nltk.tokenize import sent_tokenize, word_tokenize

text1 = "The data given satisfies the requirement for model generation. Thisis used in Data Science Lab."

# Sentence tokenization
print("Sentence tokenization: ")
print(sent_tokenize(text1))

# Word tokenization
print("\nWord tokenization: ")
print(word_tokenize(text1))

# Tokenizing words
text = word_tokenize(text1)

# Removing stop words
text2 = [word for word in text if word.lower() not in stopwords.words('english')]  # Convert to lowercase to match stopwords
print("\nRemoving stop words: ")
print(text2)

# Generating trigrams (not unigrams)
print("\nn-grams (Trigrams): ")
trigrams = ngrams(text2, 3)
for grams in trigrams:
    print(grams)
