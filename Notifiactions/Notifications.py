#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install plyer


# In[ ]:


from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="Hello Golu",
            message="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
            timeout=5)
        time.sleep(10)


# In[ ]:




