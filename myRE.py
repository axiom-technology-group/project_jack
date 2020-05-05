import datetime
import subprocess
import urllib.request as request
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
import PyPDF2

def findAll(file, item):
    """
    This function will find the item in the file
    with the correct given file path and file
    name, and return a count of item in each row.
    """
    with open(file) as f:
        lines = f.readlines()
        count = 0

        for line in lines:
            if item in line:
                count += 1
    f.close()
    return count

def getDate():
    """
    This function will return a string with
    proper date format.
    """
    now = datetime.datetime.now()
    return now[0:18]


def countWords(page, file_type='web', give_graph=False, include_stopwords=False, language='english'):
    """
    This function will count the words in a webpage or pdf
    and return a list containing the word counts for each
    word. (mode 'g' for providing graph)
    """
    if file_type == 'web': 
        reponse = request.urlopen(page)
        soup = BeautifulSoup(reponse.read(), 'html5lib')
        text = soup.get_text(strip=True)
    elif file_type == 'pdf':
        f = open(page, 'rb')
        pdf = PyPDF2.PdfFileReader(f)
        text = ''
    
        for i in range(pdf.numPages):
            text += pdf.getPage(i).extractText()
        f.close()

    tokens = [t for t in text.split()]
    clean = tokens[:]

    if include_stopwords is False:
        for token in tokens:
            if token in stopwords.words(language):
                clean.remove(token)
    freq = nltk.FreqDist(clean)
    
    if give_graph is True:
        freq.plot(20, cumulative=True)
    return freq.items()

print(countWords('Project Part2.docx.pdf', file_type='pdf'))