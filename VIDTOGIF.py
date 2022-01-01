#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install moviepy


# In[2]:


from moviepy.editor import VideoFileClip


# In[3]:


from tkinter.filedialog import *


# In[4]:


video = askopenfilename()
clip = VideoFileClip(video)
clip.write_gif("mygif.gif",fps = 10)


# In[ ]:




