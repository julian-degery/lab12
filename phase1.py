#!/usr/bin/env python
# coding: utf-8

# # ME 30 Lab 12

# __Jake Fulton__ LabSection_02.

# 2019-05-08

# #### Description and Summary: 
# 
# > What was done:
# 
# > How it was done:
# 
# > What was learned:

# ## Imports

# In[1]:


import pandas as pd


# ***
# ## Phase 1

# In[2]:


def file_open(filename1, filename2, filename3, filename4):
    AWI=pd.read_csv(filename1)
    CC=pd.read_csv(filename2)
    CFV=pd.read_csv(filename3)
    CSH=pd.read_csv(filename4)
    return(AWI,CC,CFV,CSH)


# In[3]:


file_open('Average_Wage_Index_1973-2017.csv','College_1971-2018.csv','Fresh_vegetables_1947-2015.csv','Slaughter_steers_and_heifers_1947-2015.csv')


# In[4]:


def AWI_dictCreate(AWI):
    AWI_dict={}
    for index, row in AWI.iterrows():
        AWI_dict[row['Year']]=float(row[' Amount '].strip(' ').replace(',',''))
    return(AWI_dict)


# In[5]:


AWI_dictCreate(pd.read_csv('Average_Wage_Index_1973-2017.csv'))


# In[6]:


### Old Code for setup
#def CFV_year_dictCreate(CFV):
    #CFV_dict={}
    #for i in CFV.itertuples():
        #CFV_dict[i[1]]={}
    #return(CFV_dict)


# In[7]:


#CFV_year_dictCreate(pd.read_csv('Fresh_vegetables_1947-2015.csv'))


# In[8]:


### Old code for setup
#def CFV_month_dictCreate(CFV):
    #for i in CFV.itertuples():
        #month=1
        #for j in range(12):
            #CFV_dict[i[1]][month]=i[j+2]
            #month+=1
    #return(CFV_dict)


# In[9]:


#CFV_month_dictCreate(pd.read_csv('Fresh_vegetables_1947-2015.csv'))


# In[10]:


def CFV_dictCreate(CFV):

### Originally CFV_year_dictCreate()
    CFV_dict={}
    for i in CFV.itertuples():
        CFV_dict[i[1]]={}
        
### Originally CFV_month_dictCreate()
    for i in CFV.itertuples():
        month=1
        for j in range(12):
            CFV_dict[i[1]][month]=i[j+2]
            month+=1
    return(CFV_dict)


# In[11]:


CFV_dictCreate(pd.read_csv('Fresh_vegetables_1947-2015.csv'))


# In[12]:


### Old code for setup
#def CSH_year_dictCreate(CSH):
    #CSH_dict={}
    #for i in CSH.itertuples():
        #CSH_dict[i[1]]={}
    #return(CSH_dict)


# In[13]:


#CSH_year_dictCreate(pd.read_csv('Slaughter_steers_and_heifers_1947-2015.csv'))


# In[14]:


### Old code for setup
#def CSH_month_dictCreate(CSH):
    #for i in CSH.itertuples():
        #month=1
        #for j in range(12):
            #CSH_dict[i[1]][month]=i[j+2]
            #month+=1
    #return(CSH_dict)


# In[15]:


#CSH_month_dictCreate(pd.read_csv('Slaughter_steers_and_heifers_1947-2015.csv'))


# In[16]:


def CSH_dictCreate(CSH):
    
## Origingally CSH_year_dictCreate()
    CSH_dict={}
    for i in CSH.itertuples():
        CSH_dict[i[1]]={}
        
### Originally CSH_month_dictCreate()
    for i in CSH.itertuples():
        month=1
        for j in range(12):
            CSH_dict[i[1]][month]=i[j+2]
            month+=1
    return(CSH_dict)


# In[17]:


CSH_dictCreate(pd.read_csv('Slaughter_steers_and_heifers_1947-2015.csv'))


# In[18]:


def CC_dictCreate(CC):
    year=1971
    CC_dict={}
    for index, row in CC.iterrows():
        if (str(row['Unnamed: 20'])).startswith('$'):
            CC_dict[year]=float(row['Unnamed: 20'].strip('$').replace(',',''))
            year+=1
        else:
            continue
    print(CC_dict)


# In[19]:


CC_dictCreate(pd.read_csv('College_1971-2018.csv'))


# In[20]:


def phase1(filename1, filename2, filename3, filename4):
    AWI, CC, CFV, CSH = file_open(filename1, filename2, filename3, filename4)
    AWI_dict = AWI_dictCreate(AWI)
    CFV_dict = CFV_dictCreate(CFV)
    CSH_dict = CSH_dictCreate(CSH)
    CC_dict = CC_dictCreate(CC)
    return AWI_dict, CFV_dict, CSH_dict, CC_dict


# In[21]:


phase1('Average_Wage_Index_1973-2017.csv','College_1971-2018.csv','Fresh_vegetables_1947-2015.csv','Slaughter_steers_and_heifers_1947-2015.csv')

