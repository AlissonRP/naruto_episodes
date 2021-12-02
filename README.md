# Naruto Shippuden Episodes Kaggle
 As this year (2021) I started watching One Piece, I decided to web scraping some sites to get information about the episodes, so I created an [application](https://alissonrp.shinyapps.io/op_beta/) to consult the information about the episodes, following the same idea, I also decided to create a database for Naruto Shippuden and made it available this dataset on [Kaggle](https://www.kaggle.com/alisson987/naruto-shippuden-rate) for those who want to do their own analysis.  
  ## Here you will find some files of the dataset:
  * The dataset itself
  * Example of Jupyter Notebook
 
### Reading
 * In python  
  ``` python
  import pandas as pd 
  df=pd.read_csv("https://raw.githubusercontent.com/AlissonRP/naruto_episodes/main/naruto.csv",encoding='cp1252')
  ``` 
 * In R  

  ``` r
 
  df=read.csv("https://raw.githubusercontent.com/AlissonRP/naruto_episodes/main/naruto.csv")
  #or 
  df=readr::read_csv("https://raw.githubusercontent.com/AlissonRP/naruto_episodes/main/naruto.csv")
  ```
