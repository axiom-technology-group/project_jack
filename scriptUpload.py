import os
import logging
import datetime

key_path = '/Users/ruby/Development/pem_key/zhanz1.pem'
local_path = '/Users/ruby/Development/pem_key/Item'
log_path = '/Users/ruby/Development/pem_key/Item/log'
max_file = 10
max_size = 5000

os.system(
    'scp -i ' + key_path + ' -r ' + local_path +  ' ubuntu@ec2-3-21-165-16.us-east-2.compute.amazonaws.com:~/')

def log(file, counter, mode):
    logging.basicConfig(filename=file, filemode=mode,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.warning('This will get logged to a file Jack')

def get_counter():
    list_file = list(filter(lambda file: file.endswith('.txt'), os.listdir(log_path + '/' + folder_name)))
    if len(list_file) == 0:
        return 0
    else:
        return int(list_file[range(list_file) - 1][7])

def get_folder_counter():
    list_folder = list(os.listdir(log_path))
    if len(list_folder) == 0:
        return 0
    else:
        last_folder = list_folder[len(list_folder) - 1]
        if len(list(os.listdir(log_path + '/' + last_folder))) < max_file:
            return int(last_folder[7])
        else:
            return int(last_folder[7]) + 1

folder_name = '/logging' + str(get_folder_counter()) + '/'

try:
    os.makedirs(local_path + '/log/' + folder_name)
except FileExistsError:
    print('Directory ' + log_path + ' exits')

counter = get_counter()

file_name = '/logging' + str(counter) + '.log'

if not os.path.exists(log_path + folder_name + file_name):
    log(log_path + folder_name + file_name, counter, 'w')
    counter += 1

elif os.path.exists(log_path + folder_name + file_name) and os.path.isfile(log_path + folder_name + file_name):
    if os.path.getsize(log_path + folder_name + file_name) < max_size:
        log(log_path + folder_name + file_name, counter, 'a')
    else:
        file_name = '/logging' + str(counter + 1) + '.log'
        log(log_path + folder_name + file_name, counter, 'w')

else:
    print('Cannot access file')



