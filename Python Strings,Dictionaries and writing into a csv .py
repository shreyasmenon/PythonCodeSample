
# coding: utf-8

# # <center>Assignment 1</center>

# ## 1. Define a function to analyze the frequency of words in a string ##
#  - Define a function named "**count_token**" which
#      * has a string as an input 
#      * splits the string into a list of tokens by space. For example, "hello world" will be split into two tokens ['hello','world']
#      * for the tokens, do the following in sequence:
#         * strips all leading and trailing space of each token
#         * removes a token if it contain no more than 1 character (use function *len* on each token, i.e. *len*(token)<=1)
#         * converts all tokens into lower case
#      * create a dictionary containing the count of every remaining token, e.g. {'is': 5, 'hello':1,...}
#      * returns the dictionary as the output
#      
# ## 2. Define a class to analyze a collection of documents ##
#  - Define a new class called "**Text_Analyzer**" which has the following:
#     - two variables: **input_file**, **output_file**. Initialize them using the class constructor.
#     - a function named "**analyze**" that:
#       * reads all lines from input_file and concatenate them into a string
#       * calls the function "count_token" to get a token-count dictionary 
#       * saves the dictionary into output_file with each key-value pair as a line delimited by comma (see "foo.csv" in Exercise 10.3 for examples).
#       
# ## 3. Define a function to analyze a numpy array
#  - Assume we have a array which contains term frequency of each document. Where each row is a document, each column is a word, and the value denotes the frequency of the word in the document. Define a function named "analyze_tf" which:
#       * takes the array as an input
#       * normalizes the frequency of each word as: word frequency divided by the length of the document. Save the result as an array named **tf** (i.e. term frequency)
#       * calculates the document frequency (**df**) of each word, e.g. how many documents contain a specific word
#       * calculates **tf_idf** array as: **tf / df** (tf divided by df). The reason is, if a word appears in most documents, it does not have the discriminative power and often is called a "stop" word. The inverse of df can downgrade the weight of such words.
#       * for each document, find out the **indexes of words with top 3 largest values in the tf_idf array**. Print out these indexes.
#       * return the tf_idf array.
#  - Note, for all the steps, ** do not use any loop**. Just use array functions and broadcasting for high performance computation.
#      
# 
# In[80]:


# Structure of your solution to Assignment 1 

import numpy as np
import csv

#1. Define a function to analyze the frequency of words in a string
def count_token(text):

    token_count={}
    
    for wordToken in text.split(" "):
        #removes a token if it contain no more than 1 character 
        if len(wordToken) >1 :
           #strips all leading and trailing space of each token
           #converts all tokens into lower case
            stippedLowerCaseToken = wordToken.strip().lower() 
        if stippedLowerCaseToken in token_count:
            token_count[stippedLowerCaseToken] +=1
        else:
            token_count[stippedLowerCaseToken]=1
            
    #returns the dictionary as the output        
    return token_count

#2. Define a class to analyze a collection of documents
class Text_Analyzer(object):
        
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
            
    def analyze(self):
        #read the input file under read mode
        txtInputfile = open(str(self.input_file), "r")
        strConcatLines =  ""
        
        #reads all lines from input_file and concatenates them into a string
        for line in txtInputfile:
            strConcatLines += line.replace("\n"," ")  
        
        #calls the function "count_token" to get a token-count dictionary
        dict_wordCount = count_token(strConcatLines)
        
        wordCountRows = []
        for wordCount in dict_wordCount:
            rowTuple = (wordCount ,str(dict_wordCount[wordCount]))
            wordCountRows.append(rowTuple)
        
        #saves the dictionary into output_file with each key-value pair as a line 
        #delimited by comma
        with open(self.output_file,"w") as f:
            writer=csv.writer(f, delimiter=',')
            writer.writerows(wordCountRows)

def analyze_tf(arr):
    
    tf_idf=None
    
    # add your code
    
    return tf_idf

# best practice to test your class
# if your script is exported as a module,
# the following part is ignored
# this is equivalent to main() in Java

if __name__ == "__main__":  
    
    # Test Question 1
    text='''Hello world!
        This is a hello world example !'''   
    print(count_token(text))
    
    # # The output of your text should be: 
    # {'this': 1, 'is': 1, 'example': 1, 'world!': 1, 'world': 1, 'hello': 2}
    
    # Test Question 2
    analyzer=Text_Analyzer("foo.txt", "foo.csv")
    vocabulary=analyzer.analyze()
    
    

