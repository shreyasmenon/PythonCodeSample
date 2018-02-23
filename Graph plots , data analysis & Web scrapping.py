
# coding: utf-8

# In[110]:


import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def mpg_plot():
    
    #read csv into a dataframe
    df = pd.read_csv("auto-mpg.csv")
    
    #Plot avg mpg by origin over years by creating a crosstab
    pd.crosstab(index=df.model_year, columns=df.origin , values=df.mpg, aggfunc=np.mean)    .plot(title="avg mpg by origin over years" ,kind='line', figsize=(8,4)).legend( loc='center left', bbox_to_anchor=(1, 0.5));
    plt.show()

def getReviews(movie_id):
    
    reviews=[] # variable to hold all reviews

    page_url="https://www.rottentomatoes.com/m/"+movie_id+"/reviews/?type=top_critics"
    page = requests.get(page_url)

    if page.status_code==200:
        
        soup = BeautifulSoup(page.content,'html.parser')
        
        #get the review row collection
        div_topCritics = soup.select("div#reviews div.content div.review_table div.review_table_row")
         
        #iterate through all the reviews 
        for idx, review_div in enumerate(div_topCritics):
            reviewer_name=""
            review_date=""
            review_desc=""
            review_score=""
            
            #reviewer name
            anchor_name = review_div.select("div.critic_name a.bold")
            if anchor_name != []:
                reviewer_name = anchor_name[0].get_text()
            
            #review description
            div_reviewdesc =review_div.select("div.the_review")
            if div_reviewdesc != []:
                review_desc =div_reviewdesc[0].get_text()
                
            #review date
            div_reviewdate =review_div.select("div.review_date")
            if div_reviewdate != []:
                review_date =div_reviewdate[0].get_text()
                
            #review score
            div_score =review_div.select("div.review_desc div.small")
            if div_score != []:
                review_score = div_score[0].get_text().split(' ')[-1]
            
            #Append the complte tuple
            review_tup = (reviewer_name,review_date,review_desc,review_score)
            reviews.append(review_tup)
            
        
    return reviews

# best practice to test your class
# if your script is exported as a module,
# the following part is ignored
# this is equivalent to main() in Java
if __name__ == "__main__":

    mpg_plot()

    movie_id='finding_dory'
    reviews=getReviews(movie_id)
    print(reviews)

