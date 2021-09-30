import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt


#textpath for the textfile used to generate wordcloud
textpath = "sample.txt"

#a set of all punctuation marks using the string module (so you don't have to type everyone in the set)
punctuations = set(string.punctuation)

#basic words like articles and prepositions that we don't want in the word cloud
excluded = ["the","a","to","if","is","from","of","as","at","in"]

#clean_file method strips file of punctuations and numbers
def clean_file(textfile:str):    
    with open(textfile, "r", encoding="utf-8") as f:
        for line in f:
            newline = ''.join(ltr for ltr in line if ltr not in punctuations and ltr.isnumeric() == False)
            return newline    

#strip_articles method strips the clean_file output of all words in excluded list           
def strip_articles(input:str):
    input = input.split()    
    return ' '.join(word for word in input if word.lower() not in excluded)     

#generates a dictionary that gives the frequency of words in a text
def freq(clean_text:str):
    word_freq = {}
    for word in clean_text.split():
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq.update({word: 1})
    return word_freq        

#create_wordcloud method takes the frequency dictionary and generates the wordcloud
#also saves the new wordcloud to a document (extension .png)
def create_wordcloud(dict):
    wc = WordCloud()
    wc.generate_from_frequencies(dict)
    wc.to_file("wordcloud.png")


#driver code
if __name__ == "__main__":
    clean_input = strip_articles(clean_file(textpath))
    dictionary = freq(clean_input)
    create_wordcloud(dictionary)
    #print(freq(clean_input))



    
    
                        
           
        

                
            
                        
                        
                    


   




