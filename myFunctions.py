import requests
import query_converter

def get_data(query):
    h = { "token": "eS1waYB1pt5B","user": "jcurrey"}
    url = 'https://s3.sportsdatabase.com/NFL/query.json'
    converted_query, format_no = query_converter.get_converted_query(query)
    d={"sdql": converted_query}
    r = requests.get(url, data=d, headers=h)
    return r.json(), format_no
