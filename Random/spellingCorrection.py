# Spelling Correction using TextBlob with Python
from textblob import TextBlob
#misspelled words
blob = TextBlob("thiiis ias TextBlob!")
#correct the spelling
corrected_blob = blob.correct()
#print the original and corrected text
print("Original Text: ", blob)
print("Corrected Text: ", corrected_blob)

