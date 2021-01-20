#!/usr/bin/env python
# coding: utf-8

# In[16]:


print('Print your answer twice.')
inquiry = input('Would you like to take a screenshot?: ').lower()
while inquiry == 'yes':
    inquiry = input('Would you like to take a screenshot?: ').lower()
    print('----------------------------------------------------')
    if inquiry == 'yes':
        def Photo():
            import pyautogui, time
            time_needed = int(input("How many seconds do you need to prepare?: "))
            print(f'Go to the screen you want a screenshot of. After {time_needed} seconds, check your downloads file')
            time.sleep(time_needed)
            screenshot = pyautogui.screenshot()
            screenshot.save(r'C:\Users\kjd27\Downloads\screenshot.jpg')
        Photo()
        print('Check your Downloads')
    if inquiry == 'no':
        print('Goodbye')
        break


# In[ ]:




