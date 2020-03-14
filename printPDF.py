from bs4 import BeautifulSoup
import os

## Remove HTML by ids and classes example
# https://ideone.com/6iQje1 - Each needs an id

#Define file to write
newHtmlFile = 'resumeHtml.html'

#Check to see if file exists
try:
    os.remove(newHtmlFile)
except OSError:
    pass

# Create a list of ids to remove
#idsToRemove = ['aboutmeID', 'technicalID',
idsToRemove = ['banner', 'navMenu', 'bntDownloadID', 'footerMapArea']
classToRemove = ['contact', 'footer', 'contactDetailsID']

#Define local file to open
link = open('index.html')

#Load page
soup = BeautifulSoup(link.read(), "html.parser")

#Iterate through all idsToRemove
for ids in idsToRemove:
    #print(ids)
    elements = soup.find_all("div", id=ids)

    for element in elements:
        #print('New element to delete - ', ids)

        #print(element)
        element.decompose()

#Iterate through all classToRemove
for ids in classToRemove:
    print(ids)
    elements = soup.find_all("section", id=ids)

    for element in elements:
        print('New element to delete - ', ids)

        #print(element)
        element.decompose()

#Convert to list to write
output = soup.prettify()

#Write to file
with open(newHtmlFile, 'a') as results_file:
    results_file.write(output)

print('Done writing')

## Render using https://pypi.org/project/pdfkit/
