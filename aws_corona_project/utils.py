import os
import datetime
from myClasses import MyLogging
from config import LOG_PATH

def goLog(
        script, log_path=LOG_PATH, level='info', mode='w', max_size=10000000):
    """
    This function will help other program to log what they did
    or error messages. 
    """
    if not os.path.exists(log_path):
        raise FileNotFoundError('Path does not exist.')

    try:
        os.makedirs(log_path + 'log/')
    except FileExistsError:
        mode = 'a'
    log_path = log_path + 'log/'

    list_file = list(filter(lambda file: file.endswith(
        '.log'), os.listdir(log_path)))
    if len(list_file) == 0:
        file_name = 'AWS.ZHANZ1.DATA_log_01.log'
    else:
        last_file = list_file[len(list_file) - 1]
        if os.path.getsize(log_path + last_file) < max_size:
            file_name = last_file
        else:
            current_num1 = int(last_file[20])
            current_num2 = int(last_file[21])
            if (current_num2 + 1) == 10:
                current_num1 += 1
                current_num2 = 0
            else:
                current_num2 += 1
            num = str(current_num1) + str(current_num2)
            file_name = 'AWS.ZHANZ1.DATA_log_' + num + '.log'

    MyLog = MyLogging()
    MyLog.basicConfig(filename=log_path+file_name, filemode=mode, level=20)
    MyLog.log(level, script)


def getDate():
    """
    This function will return a string with
    proper date format.
    """
    now = datetime.date.today()
    return str(now)


def csvToJson(file_name):
    """
    This function will be able to turn csv file
    into Json file
    """
    try:
        input_csv = open(file_name, 'r')
    except FileNotFoundError:
        raise FileNotFoundError('File does not exist')
    except IOError:
        raise IOError('Failed to read the file')
    file_name = file_name.replace('.csv', '.json')
    output_json = open(file_name, 'w')

    output_json.write('{\n')
    output_json.write('\t"date": ' + '"' + getDate() + '"' + ',\n')
    lines = input_csv.readlines()
    types = lines[0].split(',')

    for i in range(1, len(lines)):
        data = lines[i].split(',')
        for x in range(len(types)):
            if x == 0:
                output_json.write('\t "' + data[0] + '": {\n')
            elif x == (len(types) - 1):
                output_json.write(
                    '\t\t"' + types[x].strip() + '": ' + '"' + data[x].strip() + '"\n')
            else:
                output_json.write(
                    '\t\t"' + types[x].strip() + '": ' + '"' + data[x].strip() + '"' + ',\n')
        output_json.write('\t},\n')
    output_json.write('}')
    input_csv.close()
    output_json.close()


def prepareData(input_list):
    if len(input_list) == 0:
        return ''
    else:
        output = ''
        for i in range(len(input_list) - 1):
            output += "'" + str(input_list[i]).replace(' ', '_') + "', "
        return output + "'" + input_list[len(input_list) - 1] + "'"


def getHTML(file_path):
    try:
        f = open(file_path)
    except:
        raise FileNotFoundError('File does not exist.')
    html = f.read()
    f.close()
    return html


def getList(input_list):
    if len(input_list) == 0:
        return ''
    else:
        output = ''
        for element in input_list:
            output += element + ', '
        return output[:-2]
