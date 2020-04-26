from fpdf import FPDF
import re

log_path = '/Users/ruby/Development/pem_key/Item/log'

def grep_error(log_path):
    file_count = 0
    error_message = 0
    for folder in list(filter(lambda folder: folder.startswith('logging'), os.listdir(log_path))):
        for file in list(filter(lambda file: file.endswith('.log'), os.listdir(log_path + '/' + folder))):
            error_message += grep('error', log_path + '/' + folder + '/' + file)
            file_count += 1

    return tuple((file_count, error_message))

def grep(searched_item, searched_file):
    f = open(searched_file, 'r')
    lines = f.readline()
    count = 0

    for line in lines:
        if searched_item in line:
            count += 1
    return count



file, error = grep_error(log_path)
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Error: ' + str(error) + '  File: ' + str(file))
pdf.output('report.pdf', 'F')
