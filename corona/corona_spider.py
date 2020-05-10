import scrapy
import myRE as re


def modifyNames(input_list):
    length = len(input_list) // 2
    output = list()

    for i in range(length):
        name1 = input_list[2 * i]
        name2 = input_list[2 * i + 1]
        if name1.endswith(',') or name1.endswith('/'):
            name1 = name1[:len(name1) - 1] + '/'
            output.append(name1 + name2)
        else:    
            output.append(name1 + ' ' + name2)
    
    return output


def modifyData(input_list):
    output = list()
    i = 0
    NAindex = 0
    NAcounter = 0
    while i < len(input_list) - 1:
        if input_list[i] == '\n' or input_list[i] == '\n ':
            if input_list[i + 1] != '\n':
                output.append(input_list[i + 1].replace(',', '', 3).strip())
            else:
                NAindex = i
                while NAindex < len(input_list) - 1 and input_list[NAindex + 1] == '\n':
                    NAindex += 1
                    NAcounter += 1
                for x in range(NAcounter):
                    output.append('N/A')
                    NAcounter = 0
                i = NAindex - 2
            i = i + 2
        else:
            output.append(input_list[i].replace(',', '', 10).strip())
            i += 1
    
    return output
            



class CoronaSpider(scrapy.Spider):
    name = 'corona'
    start_urls = [
        'https://www.worldometers.info/coronavirus/'
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = re.getDate() + '-%s.txt' % page
        with open(filename, 'w') as f:
            categories = modifyNames(response.css(
                '#main_table_countries_today th::text')[:22].getall())
            categories.append('Test/1M Pop')
            categories.append('Continent')
            for i in range(len(categories) - 1):
                f.write(categories[i] + ',')
            f.write(categories[len(categories) - 1] + '\n')

            country = 8
            
            while country < 223:
                curr = modifyData(response.xpath(
                    '//*[@id="main_table_countries_today"]/tbody[1]/tr[' + str(country) + ']').css('tr ::text').getall())
                for a in range(len(curr) - 1):
                    f.write(curr[a] + ',')
                f.write(curr[len(curr) - 1] + '\n')
                country += 1
            f.close()
