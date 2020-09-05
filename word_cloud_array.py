
get_ipython().system('pip install wordcloud')
get_ipython().system('pip install fileupload')
get_ipython().system('pip install ipywidgets')
get_ipython().system('jupyter nbextension install --py --user fileupload')
get_ipython().system('jupyter nbextension enable --py fileupload')


import wordcloud 
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

# This is the uploader widget

import fileupload
import io

def _upload( ):

    _upload_widget = fileupload.FileUploadWidget( )
    
    

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my","we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them","their", "what", "which", "who", "whom", "this", "that","am", "are", "was", "were", "be", "been", "being", "have", "has", "had", "do","does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too","very", "can", "will", "just"]

    # LEARNER CODE START HERE
                           
    words = file_contents.split(" ")
    words_list = []
    #All the uninteresting words are ignored to form a new list of words below:
    for word in words:
        for uninteresting_word in uninteresting_words:
            if word is not uninteresting_words:
                words_list.append(word)
    #Punctuations marks are removed below:
    for word in words_list:
        if not word.isalpha():
            word = ''.join([letter for letter in word if word.isalpha()])
            
    words_dict={}
    #The frequency of words are assigned as the values of the keys in the words dictionary named as "words_dict":                       
    for word in words_list:
        if word not in words_dict.keys():
            words_dict[word] = words_list.count(word)
    #wordcloud                       
    cloud= wordcloud.WordCloud()
    cloud.generate_from_frequencies(words_dict)
    return cloud.to_array()
    
# Display your wordcloud image

from matplotlib import pyplot as plt

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
