import requests
import query_converter
import time

def get_data(query):
    h = { "token": "eS1waYB1pt5B","user": "jcurrey"}
    url = 'https://s3.sportsdatabase.com/NFL/query.json'
    #t1 = time.time()
    converted_query, format_no, grouper = query_converter.get_converted_query(query)
    #t2 = time.time()
    #print("Conv: ", t2 - t1)
    d={"sdql": converted_query}
    r = requests.get(url, data=d, headers=h)
    #t3 = time.time()
    #print("Data: ", t3 - t2)
    #print("Comp: ", t3 - t1)
    return r.json(), format_no, grouper
