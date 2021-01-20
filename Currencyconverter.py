#!/usr/bin/env python
# coding: utf-8

# In[58]:


def Currency_Converter():
    try:
        import requests as rt
        import bs4
        from bs4 import BeautifulSoup
        import pandas as pd
        import json as js
        import pandas as pd
        df = pd.read_csv('Country and Keys.csv')
        final_df = df.iloc[:,[0,1]]
        x = df.iloc[:,[1]]
        x = x.values.tolist()
        y = df.iloc[:,[0]]
        y = y.values.tolist()
        print('                                                Here are the list of Currencies        ')
        print(' ')
        print('''
        Only a select amount of these currencies are supported by the API we are using. To get full access, it would cost 
        money. If the currency you are looking for isn't supported please use a different converter or use a supported 
        currency. This currency converter converts 1 US Dollar to input currency. The currency list is a bit difficult 
        to read so to find your desired currency, hold CTRL and press F. Then type which currency you want to find. 
        Then look within the parenthesis to find the currency code. To leave the converter, type "QUIT" (Q). ''')
        print('-------------------------------------------------------------------------------------------------------------------------------')
        z = list(zip(x,y))
        #z.insert[0,(['  United Arab Emirates Dirham'],['   AED'])]
        print(z)
        url = "https://v6.exchangerate-api.com/v6/d1772655541269d8ff31bc2e/latest/USD"
        request = rt.get(url)
        data = request.json()
        data
        print('-------------------------------------------------------------------------------------------------------------------------------')

        Currency = True
        while Currency:
            C = input('Which Currency Would you Like to check the value of?:').upper()
            print('-------------------------------------------------------------------------------------------------------------------------------')
            if len(C) != 3:
                print('You cannot use more or less than Three Characters')
            else:
                y = float(input(f'How much of {C} are you converting from USD? Please use numbers and decimals only. :'))
                print(data['conversion_rates'][C]*y)
            if C == 'Q':
                break
    except KeyError:
        print('Input Not supported or Invalid')
Currency_Converter()


# In[ ]:




