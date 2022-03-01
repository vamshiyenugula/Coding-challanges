# Importing required libraries

import csv

def read_csv(path):
    """ 
    This function will take path for csv file as input and
    returns list of dictionaries
    """
    try:
        if type(path) == str:
            final_data_list = []
            # opening file
            with open(path,'r') as csv_file:
                reader = csv.reader(csv_file)
                # creating empty list for storing data
                rows = []
                # creating count variable to find first row (column names)
                count = 0
                # seperating columns name and rest of the data
                for item in reader:
                    if count == 0:
                        column_names = item[0].split(';')
                        count = count+1
                    else:
                        rows.append(item)
            # finding column names leangth
            column_leangth = len(column_names)
            # creating dictinory and appending in list 
            for item_num in range(len(rows)):
                # finding each row leangth
                row_leangth = len(rows[item_num])
                # creating empty dictionary
                temp_dir = {}
                while row_leangth < column_leangth:
                    rows[item_num].append('none')
                    row_leangth = len(rows[item_num])
                for inner_item in range(column_leangth):
                    temp_dir[column_names[inner_item]] = rows[item_num][inner_item]
                final_data_list.append(temp_dir)
            return final_data_list
        else:
            return TypeError
    
    # returing error if any 
    except Exception as error:
        return error

