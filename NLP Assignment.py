#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install textblob==0.9.0')
get_ipython().system('pip install nltk')
get_ipython().system('pip install newspaper3k')


# In[3]:


import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article


# In[7]:


nltk.download('punkt') #model that we can use for NLP


# In[8]:


url='https://huggingface.co/datasets/cnn_dailymail/tree/refs%2Fconvert%2Fparquet/1.0.0/'


# In[9]:


article = Article(url)


# In[10]:


article.download() #download url data


# In[11]:


article.parse()#parse the data the parse 


# In[12]:


article.nlp()


# In[13]:


print('Title :',article.title)
print('Author:',article.authors)
print('Publication date:', article.publish_date)
print('Summary:',article.summary)


# In[14]:


analysis = TextBlob(article.text)
if analysis.polarity >0:
    print("positive")
elif analysis.polarity<0:
    print("negative")
else:
    print("Neutral")


# In[15]:


def summarize():
    url = utext.get('1.0',"end").strip
    article = Article(url)
    article.download
    article.parse()
    article.nlp()
    
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    sentiment.config(state='normal')
    
    title.delete('1.0',"end")
    title.insert('1.0',article.title)
    
    author.delete('1.0',"end")
    author.insert('1.0',article.authors)
    publication.delete('1.0','end')
    publication.insert('1.0',article.publish_date)
    
    summary.delete('1.0','end')
    summary.insert('1.0',article.summary)
    
    sentiment.delete('1.0','end')
    analysis = textBlob(article.text)
    
    if analysis.delete >0:
        sentiment.insert('1.0',"Positive")
    elif analysis.delete <0:
        sentiment.insert('1.0',"Negative")
    else :
        sentiment.insert('1.0',"Neutral")
        
    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    sentiment.config(state='disabled')
    
    


# In[16]:


root =tk.Tk()
root.title("Article summerizer")
root.geometry('1200x600')

tlabel= tk.label(root,text="Title")
tlabel.pack()
title=tk.Text(root, height=1,width=140)
title.config(state='disabled',bg='addd')
title.pack()

alabel= tk.label(root,text="Title")
alabel.pack()
author=tk.Text(root, height=1,width=140)
author.config(state='disabled',bg='addd')
author.pack()

plabel= tk.label(root,text="Title")
plabel.pack()
publication=tk.Text(root, height=1,width=140)
publication.config(state='disabled',bg='addd')
publication.pack()

btn=tk.Button(root,text='Summaerize',command = summarize)
btn.pack()

root.mainloop()


# In[ ]:




