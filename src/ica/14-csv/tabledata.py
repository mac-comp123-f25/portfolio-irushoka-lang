from helpers import * #It imports everythinh

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

# print(select_by_month("February",tabular))


# def average_daylight_time(tabular):


def daylight_hours(rise_hour, rise_min, set_hour, set_min):
    """
    Given four values, the hour and minute of sunrise, and the hour and minute of sunset, this computes the
    number of hours of daylight and returns that value as a floating-point number.
    """
    rise_time = (60 * rise_hour) + rise_min
    set_time = (60 * set_hour) + set_min
    minute_diff = set_time - rise_time
    hour_diff = minute_diff / 60
    return hour_diff


def main():
            # print(lookup_phone('Fox, Susan', directory))
            # print(lookup_phone('Shoop, Libby', directory))

            field_names, sun_table = read_csv("DataFiles/sunRiseSet.csv")
            print(field_names)
            print(sun_table[0])  # printing just the first row of data
            print_table(sun_table, field_names, 15)

            # may15_data = lookup_by_date('May', 15, sun_table)
            # print(may15_data)
            # oct31_data = lookup_by_date('October', '31', sun_table)
            # print(oct31_data)

            # olri = collect_by_building('Olin-Rice', directory)
            # print(olri)
            # cc = collect_by_building('Campus Center', directory)
            # print_table(cc, ['Name', 'Phone', 'Building', 'OfficeNum'])

            # march_data = select_by_month('March', sun_table)
            # july_data = select_by_month('July', sun_table)
            # january_data = select_by_month('January', sun_table)
            # print_table(march_data, field_names, 15)

            # print("Sunsets before 6pm =", count_sunsets_before(18, sun_table))
            # print("Sunsets before 10pm =", count_sunsets_before(22, sun_table))
            # print("Sunsets before 4pm =", count_sunsets_before(16, sun_table))

def daylight_hours(rise_hour, rise_min, set_hour, set_min):
    """
    Given four values, the hour and minute of sunrise, and the hour and minute of sunset, this computes the
    number of hours of daylight and returns that value as a floating-point number.
    """
    rise_time = (60 * rise_hour) + rise_min
    set_time = (60 * set_hour) + set_min
    minute_diff = set_time - rise_time
    hour_diff = minute_diff / 60
    return hour_diff

def average_daylight_time(table):
    sum = 0
    for row in table:
      rise_hour = int(row['SunRiseHour'])
      rise_min= int(row['SunRiseMin'])
      set_hour= int(row['SunSetHour'])
      set_min = int(row['SunSetMin'])
      daylight_hour = daylight_hours(rise_hour,rise_min,set_hour, set_min) #From the function aforementioned
      sum = sum + daylight_hour

    return sum / len(table) #Nbr of rows is known as len


print(average_daylight_time(sun_table))






