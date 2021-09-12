from Data_format_2 import Data_format_2
import utils_format_2

def get_output_format(json_data):
    groups = json_data['groups'][0]
    thisseason = 2021
    columns = groups['columns']
    data = Data_format_2(columns[0],columns[1],columns[2],columns[3],columns[4],columns[5],columns[6],columns[7],columns[8],columns[9]
                ,columns[10],columns[11],columns[12],columns[13],columns[14],columns[15],columns[16],columns[17],columns[18],columns[19]
                ,columns[20],columns[21],columns[22],columns[23],columns[24],columns[25])
    

    return utils_format_2.tohtml(data,thisseason)