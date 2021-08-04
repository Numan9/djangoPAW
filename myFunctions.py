import requests

def get_data(query):
    h = { "token": "eS1waYB1pt5B","user": "jcurrey"}
    url = 'https://s3.sportsdatabase.com/NFL/query.json'
    d={"sdql": query}
    r = requests.get(url, data=d, headers=h)
    return r.json()
