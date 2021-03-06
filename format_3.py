import json
from prettytable import PrettyTable

def add_paddings(c):
    max_list = 0
    for lst in c:
        if len(lst) > max_list:
            max_list = len(lst)
    for lst in c:
        if len(lst) < max_list:
            lst += ['-'] * (max_list - len(lst))

def get_output_format(jsondata):

    headers = jsondata['headers']
    headers.append('sdql as terms')
    columns = [d['columns'] for d in jsondata['groups']]
    sdqls = ["".join(d['sdql as terms']) for d in jsondata['groups']]
    
    for col, sdql in zip(columns, sdqls):
        col.append([sdql])
    
    tables = []
    for c in columns:
        i = 0
        pt = PrettyTable()
        add_paddings(c)
        for header, column in zip(headers, c):
            print(i)
            i += 1
            pt.add_column(header, column)
        tables.append(pt)

    tables_json = []
    all_data = []
    for table in tables:
        tables_json.append(json.loads(table.get_json_string()))

    for table in tables_json:
        for t in table:
            if t == headers:
                continue
            all_data.append(t)

    big_table = PrettyTable()
    big_table.field_names = headers
    for row in all_data:
        values = []
        for header in headers:
            values.append(row[header])
        big_table.add_row(values)
        html=big_table.get_html_string(attributes={"id":"myTable3", "class": "table"})
    return(html)