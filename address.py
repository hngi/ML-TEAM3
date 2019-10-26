import nlp
import pandas as pd
import googlemaps

gmaps = googlemaps.Client(key='INSERT KEY HERE')
dataframe = pd.read_csv('isthisarealjob_table_posts.csv')
dataframe = dataframe.drop(['3', '4', '2018-02-28 00:14:37', '2018-02-28 00:14:37.1', 'hello-world-071235157V21576', 'world,good', 'Unnamed: 9', 'NULL', 'NULL.1'], axis= 1)
dataframe = dataframe[['danny', '#world is greater than #good things', 'Hello World']]
dataframe_address = dataframe['#world is greater than #good things']


#input an address
address= input("Enter address: ")


# Geocoding an address
geocode_result = gmaps.geocode(address)

if geocode_result == []:
    print ("This address is invalid")
else:
    geocode_result= geocode_result[0]
    
    if 'plus_code' in geocode_result:
        print("The Company address is valid")
    else:
        print("This address is vague, This job invite is likely a scam")

