#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install matplotlib


# In[5]:


pip install seaborn


# In[2]:


pip install numpy


# In[1]:


pip install pandas


# In[22]:


pip install pandas openpyxl


# In[1]:


import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib as mt


# In[11]:


df = pd.read_csv(r"E:\Data Storage\Walmart Analysis\walmart.csv")


# In[5]:


df1 = pd.read_excel(r"E:\Data Storage\Walmart Analysis\Backend_sheets.xlsx", sheet_name = "Product_category_nm", engine ="openpyxl")


# In[8]:


df2 = pd.read_excel(r"E:\Data Storage\Walmart Analysis\Backend_sheets.xlsx", sheet_name = "Occupation_name", engine ="openpyxl")


# In[6]:


df1.head()


# In[12]:


df.head()


# In[9]:


df2.head()


# In[7]:


df.columns


# In[9]:


df.shape


# In[14]:


MS = df["Marital_Status"].unique()


# In[15]:


print(MS)


# In[16]:


Ocpt = df["Occupation"].unique()
print(Ocpt)


# In[24]:


Gen = df["Gender"].unique()
print(Gen)


# In[25]:


Cit = df["City_Category"].unique()
print(Cit)


# In[20]:


sorted_ocpt = np.sort(Ocpt)
print(sorted_ocpt)


# In[21]:


prdt = df["Product_Category"].unique()
sorted_prdt = np.sort(prdt)
print(sorted_prdt)


# In[19]:


df_merged = df.merge(df1, left_on = "Product_Category",  right_on = "Product_category", how = "left")
df_merged.drop(columns = ["Product_category"], inplace=True)
df_merged.head()


# In[21]:


df_merged = df_merged.merge(df2, on = "Occupation", how = "left")
df_merged.head()


# In[22]:


df_merged["Gender_name"] = df_merged["Gender"].replace({"M":"Male", "F" : "Female"})
df_merged.head()


# In[30]:


df_merged["Relationship_sts"] = df_merged["Marital_Status"].replace({1:"Married", 0 : "Single"})
df_merged.head()


# In[28]:


df_merged["City_type"] = df_merged["City_Category"].replace({"A":"Tier-I", "B" : "Tier-II", "C":"Tier-III"})
df_merged.head()


# In[33]:


df_merged = df_merged.drop(columns =["Gender", "Occupation","City_Category","Product_Category","Marital_Status"])
df_merged.head(10)


# In[36]:


df_merged = df_merged[["User_ID","Product_ID","Age","Gender_name","City_type","Relationship_sts","Occupation_name","Product_category_name","Stay_In_Current_City_Years","Purchase"]]
df_merged.head()


# In[37]:


df_merged = df_merged.rename(columns = {"Gender_name":"Gender","Relationship_sts":"Marital_Status","Occupation_name":"Job_Description","Product_category_name":"Product_Category","Stay_In_Current_City_Years":"Total_Years","Purchase":"Price"})
df_merged.head(10)

