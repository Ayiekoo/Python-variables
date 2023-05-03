#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The boolean function; bool()
# Use the bool() function to get whether a value is true or false
boo(56 == 48)


# In[2]:


bool(56 == 48)


# In[3]:


bool(60)


# In[4]:


# In Python, any non-zero numerical value (including negative numbers) is considered "truthy" and will evaluate to True when converted to a boolean value.

# Therefore, bool(60) would evaluate to True because the integer value 60 is non-zero.
bool(60)


# In[5]:


# In Python, an empty string ('') is considered "falsy" and will evaluate to False when converted to a boolean value.

# Therefore, bool('') would evaluate to False because an empty string is considered falsy.

bool('')


# In[6]:


# In Python, any non-empty string (i.e., a string with one or more characters) is considered "truthy" and will evaluate to True when converted to a boolean value.

# Therefore, bool('Python') would evaluate to True because the string 'Python' is non-empty.
bool('Python')


# In[7]:


# In Python, the reserved keyword None represents a null object, and it is considered "falsy" and will evaluate to False when converted to a boolean value.

# Therefore, bool(None) would evaluate to False because None is considered falsy.
bool(None)


# In[ ]:




