import csv
table = [{'Name': 'Fox, Susan', 'Phone': '6553',
          'Building': 'Olin-Rice', 'OfficeNum': '230'},

         {'Name': 'Cranford, James', 'Phone': '6698',
          'Building': 'Olin-Rice', 'OfficeNum': '143'},

         {'Name': 'Syed, Una', 'Phone': '5501',
          'Building': 'Campus Center', 'OfficeNum': '399'},

         {'Name': 'Thimus, Reg', 'Phone': '6001',
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
print(field_names)
print(sun_table[0])  # printing just the first row of data
print(sun_table, field_names, 15)






def lookup_office(name, table):
    for row in table:
        if row ['Name'] == name:
            return row ['Building'] , row ['OfficeNum']

    return "No entry" + name

print(lookup_office('Fox, Susan', table))