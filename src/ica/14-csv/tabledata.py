import csv
table = [{'Name': 'Fox, Susan', 'Phone': '6553',
          'Building': 'Olin-Rice', 'OfficeNum': '230'},

         {'Name': 'Cranford, James', 'Phone': '6698',
          'Building': 'Olin-Rice', 'OfficeNum': '143'},

         {'Name': 'Syed, Una', 'Phone': '5501',
          'Building': 'Campus Center', 'OfficeNum': '399'},

         {'Name': 'Thimus, Reg', 'Phone': '6001',
          'Building': 'Leonard', 'OfficeNum': '22'},
         {'Name': 'Friedman, Maryam', 'Phone': '6001',
          'Building': 'Leonard', 'OfficeNum': '22'}]

def read_csv(csv_filename):
    """
    Build a list of dictionaries from a CSV file without converting numeric
    values into integers.

    :param csv_filename: the name of the CSV file to read
    :return: list of field names (column headers in the CSV file) and
    list of dictionaries holding the data (one dictionary for each row)
    """
    data_in = open(csv_filename, 'r')
    csv_reader = csv.DictReader(data_in)
    fields = csv_reader.fieldnames

    table = []
    for rowDict in csv_reader:
        table.append(rowDict)
    data_in.close()
    return fields, table

field_names, sun_table = read_csv("DataFiles/sunRiseSet.csv")
# print(field_names)
# print(sun_table[0])  # printing just the first row of data
# print(sun_table, field_names, 15)





def lookup_office(name, table):
    for row in table:
        if row ['Name'] == name:
            return row ['Building'] , row ['OfficeNum']

    return "No entry" + name

# print(lookup_office('Fox, Susan', table))




def read_csv(csv_filename):
    """
    Build a list of dictionaries from a CSV file without converting numeric
    values into integers.

    :param csv_filename: the name of the CSV file to read
    :return: list of field names (column headers in the CSV file) and
    list of dictionaries holding the data (one dictionary for each row)
    """
    data_in = open(csv_filename, 'r')
    csv_reader = csv.DictReader(data_in)
    fields = csv_reader.fieldnames

    tabular = []
    for rowDict in csv_reader:
        tabular.append(rowDict)
    data_in.close()
    return fields, tabular

fieldNames, tabular = read_csv("DataFiles/sunRiseSet.csv")
# print(tabular, fieldNames, 10)


def lookup_by_date(monthname, monthday, tabular):
    for row in tabular:
        if row['Month'] == monthname and row['Day'] == monthday:
            return  row


# print(lookup_by_date('January', '10', tabular))


def collect_by_building(capital_letter, table):
    """
    Given the name of a building, and a sunTable, make a list of all
    the entries in the sunTable belonging to that building and return
    that list
    """
    match_list = []

    for row in table:
        str = row['Name']
        if str.startswith(capital_letter):
            match_list.append(str)

    return match_list

# print(collect_by_building('F', table))



def select_by_month(monthname,tabular):
    empty_list = []
    for row in tabular:
        if row['Month'] == monthname:
            empty_list.append(row)
    return empty_list

print(select_by_month("February",tabular))


# def average_daylight_time(tabular):



