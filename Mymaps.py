#!/usr/bin/env python
# coding: utf-8

# In[3]:


def Mymaps():
    import googlemaps
    from datetime import datetime
    try:
        Key = input('API Key:')
        gmaps = googlemaps.Client(key=Key)
        Adress = input('Put Google indexed (your/an adress) adress:')
        City = input("Enter your/a city")
        State = input('Enter your/a state')

        # Geocoding an address
        geocode_result = gmaps.geocode(f'{Adress}, {City}, {State}')
        print(geocode_result)

        # Look up an address with reverse geocoding
        reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

        # Request directions via public transit
        now = datetime.now()
        print('''
        Your modes of transit
    ------------------------------
    walking
    transit
    car/driving
    bicycle
    ''')
        mode_of_transit = input('Mode of transit')
        directions_result = gmaps.directions(Adress,
                                             City,State,
                                             mode=mode_of_transit,
                                             departure_time=now)
    except ValueError:
        print("Does not work due to lack of API key")
Mymaps()


# In[ ]:




