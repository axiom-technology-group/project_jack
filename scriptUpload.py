import os
import logging
import datetime

key_path = '/Users/ruby/Development/pem_key/zhanz1.pem'
local_path = '/Users/ruby/Development/pem_key/Item'
log_path = '/Users/ruby/Development/pem_key/Item/log'
max_file = 10
max_size = 5000
server_path = 'ubuntu@ec2-3-21-165-16.us-east-2.compute.amazonaws.com: ~/'

def log(file, mode):
    logging.basicConfig(filename=file, filemode=mode,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.warning('This will get logged to a file Jack')

def get_counter(folder_name):
    list_file = list(filter(lambda file: file.endswith('.txt'), os.listdir(log_path + '/' + folder_name)))
    if len(list_file) == 0:
        return 0
    else:
        last_file = list_file[range(list_file) - 1]
        return int(last_file[7:][0:len(last_file) - 4])

def get_folder_counter():
    list_folder = list(lambda folder: not folder.startswith('.'), os.listdir(log_path))
    if len(list_folder) == 0:
        return 0
    else:
        last_folder = list_folder[len(list_folder) - 1]
        if len(list(os.listdir(log_path + '/' + last_folder))) < max_file:
            return int(last_folder[7:])
        else:
            return int(last_folder[7:]) + 1


def upload(server_path, key_path='.', local_path='.', log_path='.', max_file=10, max_size=5000):
    os.system(
        'scp -i ' + key_path + ' -r ' + local_path + + ' ' + server_path)

    folder_counter = get_folder_counter()
    folder_name = '/logging' + str(get_folder_counter()) + '/'

    try:
        os.makedirs(local_path + '/log/' + folder_name)
    except FileExistsError:
        print('Directory ' + log_path + ' exits')

    counter = get_counter(folder_name)

    file_name = '/logging' + str(counter) + '.log'

    if not os.path.exists(log_path + folder_name + file_name):
        log(log_path + folder_name + file_name, counter, 'w')
        counter += 1

    elif os.path.exists(log_path + folder_name + file_name) and os.path.isfile(log_path + folder_name + file_name):
        if os.path.getsize(log_path + folder_name + file_name) < max_size:
            log(log_path + folder_name + file_name, counter, 'a')
        elif counter == max_file - 1:
            new_folder = log_path + '/log/logging' + \
                str(folder_counter + 1) + '/'
            os.mkdir(new_folder)
            file_name = '/logging0.log'
            log(new_folder + file_name, 'w')
        else:
            file_name = '/logging' + str(counter + 1) + '.log'
            log(log_path + folder_name + file_name, 'w')

    else:
        print('Cannot access file')



