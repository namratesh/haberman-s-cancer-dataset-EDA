#!/usr/bin/env python
# coding: utf-8

# This is Haberman's data set to calculateperson will survive after
# surgery of breast cancer

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'notebook')
import seaborn as sns


# In[2]:


cancer = pd.read_csv("haberman_csv.csv")
cancer.head()


# In[4]:


cancer.shape


# It has 4 columns and 306 rows.

# In[3]:


cancer.info()


#  It has 4 columns, 306 entries in each column.
#  All values are in int64, so need to change it.
#  
#  
#  
# 

# In[5]:


#let's see how many patient will survive more than 5  years or die
cancer['Survival_status'].value_counts()


# 1: patient will survive more than 5 years,          
# 2: pateint will die before 5 years

# In[6]:


cancer.plot(kind = "scatter", x ="Age_of_patient_at_time_of_operation", y = "Survival_status" )


# In[7]:


cancer.plot(kind = "scatter", x ="Patients_year_of_operation", y = "Survival_status" )


# In[8]:


cancer.plot(kind = "scatter", x ="Number_of_positive_axillary_nodes_detected", y = "Survival_status" )


# by plotting scatter plot we are not able to differniate what features are important to us

# In[9]:


sns.set_style("whitegrid")
sns.FacetGrid(cancer, hue = "Survival_status", size =4).map(plt.scatter,"Age_of_patient_at_time_of_operation","Patients_year_of_operation").add_legend()


# In[10]:


sns.set_style("whitegrid")
sns.pairplot(cancer, hue = "Survival_status", size = 4)


# plotting all plots  don't give much senese of data

# In[11]:


sns.set_style("darkgrid")
sns.FacetGrid(cancer, hue = 'Survival_status', size = 6).map(sns.distplot,"Age_of_patient_at_time_of_operation").add_legend()


# In[12]:


sns.set_style("darkgrid")
sns.FacetGrid(cancer, hue = 'Survival_status', size = 6).map(sns.distplot,"Patients_year_of_operation").add_legend()


# In[13]:


sns.set_style("darkgrid")
sns.FacetGrid(cancer, hue = 'Survival_status', size = 6).map(sns.distplot,"Number_of_positive_axillary_nodes_detected").add_legend()


# Potting this types plot also didn't give any relation about survival status, data are overlapping

# In[14]:


#plotting pdf and cdf
counts, bin_edges = np.histogram(cancer['Survival_status'], bins = 10, density = True)
pdf = counts/sum(counts)
print(pdf)
print(cdf)
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:],cdf)
plt.plot(bin_edges[1:],pdf)


# Even we are not getting anything from this plot

# In[ ]:


cancer_survive = cancer.loc[cancer['Survival_status'] == 1]
cancer_not_survive = cancer.loc[cancer['Survival_status'] == 2]


# In[ ]:


counts, bin_edges = np.histogram(cancer_not_survive, bins = 10, density = True)
pdf = counts/sum(counts)
print(pdf)
print(cdf)
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:],cdf)
plt.plot(bin_edges[1:],pdf)


# In[ ]:


counts, bin_edges = np.histogram(cancer_not_survive, bins = 10, density = True)
pdf = counts/sum(counts)
print(pdf)
print(cdf)
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:],cdf)
plt.plot(bin_edges[1:],pdf)

counts, bin_edges = np.histogram(cancer_survive, bins = 5, density = True)
pdf = counts/sum(counts)
print(pdf)
print(cdf)
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:],cdf)
plt.plot(bin_edges[1:],pdf)
plt.legend('cancer_survive')


# here, also didn't get anything about it

# In[ ]:


sns.jointplot(x ="Age_of_patient_at_time_of_operation", y = "Patients_year_of_operation", data = cancer_survive, kind = "kde", size = 8 )


# In[ ]:


sns.violinplot(x = "Survival_status", y = "Patients_year_of_operation", data = cancer, size =10)


# In[ ]:


sns.violinplot(x = "Survival_status", y = "Patients_year_of_operation", data = cancer, size =10)


# In[ ]:




