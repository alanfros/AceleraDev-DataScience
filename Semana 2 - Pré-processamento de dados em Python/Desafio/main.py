#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[7]:


import pandas as pd
import numpy as np


# In[8]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[9]:


black_friday.head()


# In[10]:


black_friday.info()


# In[11]:


black_friday.describe()


# In[12]:


# Questão 1 | Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple (n_observacoes, n_colunas).

black_friday.shape


# In[37]:


# Questão 2 | Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

black_friday.query('Gender == "F" & Age == "26-35"').shape[0]


# In[14]:


# Questão 3 | Quantos usuários únicos há no dataset? Responda como um único escalar.

black_friday['User_ID'].nunique()


# In[33]:


# Questão 4 | Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.
print(black_friday.dtypes)
black_friday.dtypes.nunique()


# In[16]:


# Questão 5 | Qual porcentagem dos registros possui ao menos um valor null (None, ǸaN etc)? Responda como um único escalar entre 0 e 1.
(black_friday.shape[0] - black_friday.dropna().shape[0]) / black_friday.shape[0]


# In[17]:


# Questão 6 | Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.
black_friday.isnull().sum().max()


# In[18]:


# Questão 7 | Qual o valor mais frequente (sem contar nulls) em Product_Category_3? Responda como um único escalar.
int(black_friday['Product_Category_3'].mode())


# In[19]:


# Questão 8 | Qual a nova média da variável (coluna) Purchase após sua normalização? Responda como um único escalar.
normaliz = black_friday[['Purchase']]
normaliz_df = (normaliz - normaliz.min()) / (normaliz.max() - normaliz.min())
normalized = normaliz_df.mean()
normalized


# In[41]:


# Questão 9 | Quantas ocorrências entre -1 e 1 inclusive existem da variável Purchase após sua padronização? Responda como um único escalar.
standard = black_friday[['Purchase']]
standard_std = (standard - standard.mean()) / standard.std()
print(standard_std.query('Purchase >= -1 & Purchase <= 1').shape[0])


# In[42]:


# Questão 10 | Podemos afirmar que se uma observação é null em Product_Category_2 ela também o é em Product_Category_3? Responda com um bool (True, False).
black_friday.isna().query('Product_Category_2 == True & Product_Category_3 == False').shape[0] == False


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[30]:


def q1():
    
    return black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[31]:


def q2():
     
     return int(black_friday.query('Gender == "F" & Age == "26-35"').shape[0])


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[ ]:


def q3():
   
    return black_friday['User_ID'].nunique()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[ ]:


def q4():
    
    return int(black_friday.dtypes.nunique())


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[ ]:


def q5():
   
    return float((black_friday.shape[0] - black_friday.dropna().shape[0]) / black_friday.shape[0])


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[ ]:


def q6():
     
    return int(black_friday.isnull().sum().max())


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[ ]:


def q7():
    
    return int(black_friday['Product_Category_3'].mode())


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[38]:


def q8():
    normaliz = black_friday[['Purchase']]
    normaliz_df = (normaliz - normaliz.min()) / (normaliz.max() - normaliz.min())
    normalized = normaliz_df.mean()    
    return float(normalized)


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[ ]:


def q9():
    standard = black_friday[['Purchase']]
    standard_std = (standard - standard.mean()) / standard.std()
    return int(standard_std.query('Purchase >= -1 & Purchase <= 1').shape[0])


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[ ]:


def q10():
   
    return black_friday.isna().query('Product_Category_2 == True & Product_Category_3 == False').shape[0] == False


# In[ ]:




