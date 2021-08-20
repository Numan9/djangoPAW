import json
from prettytable import PrettyTable

def get_output_format(jsondata):
    # headers = data['headers']
    # headers.append('sdql as terms')
    # columns = [d['columns'] for d in data['groups']]
    # sdqls = ["".join(d['sdql as terms']) for d in data['groups']]

    # for col, sdql in zip(columns, sdqls):
    #     col.append([sdql])

    # tables = []
    # for c in columns:
    #     pt = PrettyTable()
    #     for header, column in zip(headers, c):
    #         if len(column) != len(pt._rows):
    #             column += ['-'] * (len(pt._rows) - len(column))
    #         pt.add_column(header, column)
    #     tables.append(pt)

    # tables_json = []
    # all_data = []
    # for table in tables:
    #     tables_json.append(json.loads(table.get_json_string()))

    # for table in tables_json:
    #     for t in table:
    #         if t == headers:
    #             continue
    #         all_data.append(t)

    # big_table = PrettyTable()
    # big_table.field_names = headers

    # for row in all_data:
    #     values = []
    #     for header in headers:
    #         values.append(row[header])
    #     big_table.add_row(values)
    
    # return big_table.get_html_string()

    headers = jsondata['headers']
    headers.append('sdql as terms')

    columns = [d['columns'] for d in jsondata['groups']]
    sdqls = ["".join(d['sdql as terms']) for d in jsondata['groups']]
    
    for col, sdql in zip(columns, sdqls):
        col.append([sdql])
    
    tables = []
    for c in columns:
        pt = PrettyTable()
        for header, column in zip(headers, c):
            if len(column) != len(pt._rows):
                column += ['-'] * (len(pt._rows) - len(column))
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
    #print(headers)
    big_table.field_names = headers
    for row in all_data:
        values = []
        for header in headers:
            values.append(row[header])
        big_table.add_row(values)
    return big_table.get_html_string(attributes={"id":"myTable3"})

# ['date', 'team', 'o:team']
# ['S(margin)']
# ['date', 'game number', 'week', 'wins', 'ats margin', 'ats streak', 'attendance', 'passes', 'passing first downs', 'passing touchdowns', 'passing yards']
# ['date', 'lead changes', 'line', 'losses', 'margin', 'margin after the first', 'margin after the third', 'margin at the half', 'matchup losses', 'matchup wins', 'money line', 'month', 'open line', 'open total']
