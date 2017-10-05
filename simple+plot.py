
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as mt
get_ipython().magic('matplotlib inline')


# In[12]:


points = np.arange(-5,5,0.01)


# In[18]:


dx,dy = np.meshgrid(points,points)
z = np.sin(dx) + np.sin(dy)
mt.imshow(z)
mt.colorbar()
mt.title("xxxx")


# In[ ]:


np.savez

