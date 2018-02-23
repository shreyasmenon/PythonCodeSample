
# coding: utf-8

# # <center>Assignment 2</center>

# ## 1. Define a function to analyze a numpy array
#  - Assume we have an array which contains term frequency of each document. Where each row is a document, each column is a word, and the value denotes the frequency of the word in the document. Define a function named "analyze_tf" which:
#       * takes the array as an input
#       * normalizes the frequency of each word as: word frequency divided by the length of the document. Save the result as an array named **tf** (i.e. term frequency)
#       * calculates the document frequency (**df**) of each word, e.g. how many documents contain a specific word
#       * calculates **tf_idf** array as: **tf / df** (tf divided by df). The reason is, if a word appears in most documents, it does not have the discriminative power and often is called a "stop" word. The inverse of df can downgrade the weight of such words.
#       * for each document, find out the **indexes of words with top 3 largest values in the tf_idf array**. Print out these indexes.
#       * returns the tf_idf array.
#  - Note, for all the steps, ** do not use any loop**. Just use array functions and broadcasting for high performance computation.

# ## 2. Define a function to analyze car dataset using pandas
#  - Define a function named "analyze_cars" to do the follows:
#    * Read "cars.csv" as a dataframe with the first row in the csv file as column names
#    * Sort the data by "cylinders" and "mpg" in decending order and report the first three rows after sorting
#    * Create a new column called "brand" to store the brand name as the first word in "car" column (hint: use "apply" function)
#    * Show the mean, min, and max acceleration values by "cylinders" for each of these brands: "ford", "buick" and "honda"
#    * Create a cross tab to show the average mpg of each brand and each clinder value. Use "brand" as row index and "cylinders" as column index. 
#  - This function does not have any return. Just print out the result of each calculation step.

# ## Submission Guideline##
# - Following the solution template provided below. Use __main__ block to test your functions
# - Save your code into a python file (e.g. assign1.py) that can be run in a python 3 environment. In Jupyter Notebook, you can export notebook as .py file in menu "File->Download as".
# - Make sure you have all import statements. To test your code, open a command window in your current python working folder, type "python assign1.py" to see if it can run successfully.

# In[63]:


# Structure of your solution to Assignment 1 

import numpy as np
import pandas as pd


def analyze_tf(arr):
    
    tf_idf=None
    
    #Normalize the array as save it as tf
    tf = arr/np.sum(arr,axis = 1, keepdims = True )
    
    #document frequency of each word
    df_bool = np.where(arr>0,1,0)
    df = np.sum(df_bool, axis=0, keepdims = True)
    
    #tf/df
    tf_idf = tf/df

    #return indexes of the largest 3 words in tf_idf
    tf_idf_top3indexes =np.argsort(tf_idf)[:,-3:]
    print("********indexes of the top tree values**********")
    print(tf_idf_top3indexes)
    
    #return tf_idf array    
    return tf_idf

def analyze_cars():
    
    #read the cars.csv dataframe
    df = pd.read_csv("cars.csv")
    print("\n**********Panda dataframe for cars.csv**********")
    print(df)
    
    #Sort the data by "cylinders" and "mpg" in decending order and report the first three rows after sorting
    df_sortdesc = df.sort_values(by=['cylinders','mpg'],ascending =False)
    print("\n**********first 3 rows of the sorted data*********")
    print(df_sortdesc.head(3))

    #New column called "brand" to store the brand name as the first word in "car" column
    df["brand"] = df.apply(lambda row : str(row["car"].split(" ")[0]),axis =1)
    print("\n**********New column brand**********")
    print(df["brand"])
    
    #Show the mean, min, and max acceleration values by "cylinders" for each of these brands: "ford", "buick" and "honda"
    df_brands = (df[df.brand.isin(["ford","buick","honda"])])
    grpby_cylinders = df_brands.groupby("cylinders").agg([np.mean,np.min,np.max])
    print("\n**********aggregate of 3 brands grouped by cylinders**********")
    print(grpby_cylinders)
    
    #Create a cross tab to show the average mpg of each brand and each clinder value. Use "brand" as row index
    #and "cylinders" as column index.
    df_crosstab = pd.crosstab(index=df.brand, columns=df.cylinders, values=df.mpg, aggfunc=np.mean)
    print("\n**********crosstab of mean of mpg**********")
    print(df_crosstab)
    
    return None

# best practice to test your class
# if your script is exported as a module,
# the following part is ignored
# this is equivalent to main() in Java

if __name__ == "__main__":
    
    #1 Test Question 1
    arr=np.random.randint(0,3,(4,8))

    tf_idf=analyze_tf(arr)
    
    #Test Question 2
    analyze_cars()

