from bs4 import BeautifulSoup
import os
import pdfkit
import time

## Remove HTML by ids and classes example
# https://ideone.com/6iQje1 - Each needs an id
## Render using https://pypi.org/project/pdfkit/
# brew install Caskroom/cask/wkhtmltopdf

'''
wkhtmltopdf (pdfkit) uses ES5 (javascript). My code is ES6. Until wkhtmltopdf is
 updated, you must manually convert to ES5. See link below. Also, not saving
 because I don't like how it formats the code.

 Current: resume diegoaguilera$ wkhtmltopdf --enable-javascript --debug-javascript resumeHtml.html testResume.pdf

https://babeljs.io/en/repl#?browsers=&build=&builtIns=false&spec=false&loose=true&code_lz=FDDGHsDsGdwGwKYDo7gOYAoDkAZcBDAEwUKwEoBuEAEiTQQBcApAZQHkA5DAIgCcFoAVwC2yAFaxI3ADQACAGaDIoBgEsoGfkNEAlfAHcAIvgb4ysgN4hZN2eABGYnQJEJZAXllbXeoyfxUwLayAPQhANIIAJ7QAFyy9vjQqqDQIfrgvADWISSCoCbqkCHQWapwcGlw-JBogvj00EG2YfKZshiIDLIA2lnRcgBu-HCCCAC6dvKybI4IKkgIkAy8qgIYDk4uomTmVsFtvB3DR_1RsqqQdo7O2ghk-8GhIRAw8MiomAAG1BZnAL7xX7DUYIf5fSjWJ5hFimXjdfD2cCCBiiWQAMlkr1MKiaTwu8gwZw8nm4iWSqW4Dyh-LCr1giBQ6CJ0R6ZKSKWg3HGSBBY2gGF2NOhIQAwvwTG5NvNuvpVAwABYJDmpZr4zYAIRV0A81y2dyQ5M5gXxNjCAFUAA6ESWyDj4URqp6EcCgVzLOiMACiiFEyw1UQAkoQeIjkaiEPbRFSkJdIAheAAJAAqAFkcLrNdqkJAHQgTaaLdbbUJ7NV7Ag4E7gi63X6GJ6GD6EPWA8HQ0iUaIWIJ7ImEERLmgY3GEyn05nHFqKdAUIjKwXaSErTaGG5iNBQKtLWooNXbLX3Q36E3fUsGG2Q9ww12EIYBFvVDuiiPIPGk2mM54szOkNphPgvBRIuIoAGKZAB3TYvgKiyEQhBaHiponAAgoQCECDqpKyNwsgANR6tOnJMgUu6QEg8GIfhOFyLheH7qajE_sRqCkUUSCgPK5wETROH4QxjHqlO2asYUUBIPwaBFCBwRFqubjQbBlGYQJqjTBgh71o2zatkGIZYIpDBoRh0DQOQsgAISeJAggVHsAk2Jp57aWe_p6TwhnGYhr7vuOX6yKh6GIVQjH_CAAlybahmyJaCpQG4NnCBWvCqepTkeieOnnpeHlQDiDAAApxfGVKWdZtlwPZgmyOlx7eq5F7udwhlFfFPljp-uq4XRhHZrF8UhaaYURcuxZrlieUwd0Lb4OUDkBYBXoAeUXV8QR3AADz4LICr8PI7gADrcMtcAMOAsQ9cxqSLCd1HcEdAB8dHzUJYhEddM0retG0hPgT0yU8akdLVLkttlTWGUts1wKVVmyDZdmWC9NWukeoO6e2zWTSoUPlO1H4Tp4Jy43Ag2hcKsmjfJE3LFNsj6Ag9jJGu80nAA6ozzNuNhPWbdtu0IPtR2XcJv4M0z8puOtj3PdVr3vbO4tc3dP1_dwZOmkDGmo1pmUNTlWO0yoHMS2usPlYjjyMSDetg25mOGSbXP435urs5zksa8EYX4sNS5epAhBwZ2EYYjT-VNPuMJwrKmRZLICAAB6WgmazKAg-5qSy5zuKSGTZFSVsiuKA7jdKsFyoq9NxwJgG8PgURs3Hk76q4SD51kANmiEeDgJasiKrwyJoEqlyEKogyqIQ9RwLIYgOEh-KHMcgFzw4Uxwbw9eN3H1LzWEADijBwSoRQ6jUQfQGd_AD-ANWqNAlrVOclyyK7FaoPorOr1NRQ4A_3RPA9CwBtWyD0sDjC7i0EIxlZBwAATqeQQ9hBz0kLfOBqgE4NXmsvDAJwT5kQ3vPewFFT5QGgNSOWBC_4AKQJaQQ0AFQYFkCA-B4DqK_ygNREBIQ2FYFkJCaqPtBKcMgP_K-dCGFMJ4WA8gUDu4l1tGuYQlpMiAXOGWV08dwDTD8t_I4CpUSzyAcjGwIDx6DCxNUUy7gsZwAALSJ2gPYgAjAAJgmg46Awh7EAGZPH2OEIQexHiIAOLgGgEJ3BwHSFMbYcxE8rFJGgLYjuABNAcvBokbUfjUJJNjuCWn4IMNJ0T-EEWIYsQOxhxoER4bkyAMS4nBBAQ0_JKTrzyDXLwUp7CKkOD_DHGpUsWE_QaQ9H6FimlULMZMie0yZkJMsaAaxHSwmOOce4gJ3j7EAE4AlBNcQABgCRE45XhVAjyMhKMpsSZnxI2hY9pti67gH0JaQCDBskhCmVgO59zRlPJWck2xSdRRQFuc0h5CoAAsfS14kIgComo3FRkhFhQsgFoyFQAFZ4WVNUczIo3Cfq4sxQCkBZKckAQqPigZ_51EkpKDSuAEz0V4r-VC2ZTyp62OIShMhMBIVYpsKI8RDB_lYp4b8yViy5mDHJdVaV8zOXVR5PPS42A5EU2LhKcaFi5DwXaQIQ16EdpGMNYHOCZqzoxUAuee-gx9GOt1CDLcpcEBZWWNgCx2rqoWL_IwFCDAViqHsCiBA2BgWmT-Swoe-hq7ZHvKYcoZlBGCQDaOAm_lDHCFJvNG29U7aNXbFgJORS06gAQE3bI5AKKWhToHUUCpyghgsem32I1DDxTgeAPuQ4B67WHqPQOE8p4zwRYvWwwjKYByDh3BOydU5LCrTq6OnyE7TzYnufEWdiS5xwnkbdUhKGFjFHqvUMp6byiVB3WuW8G5emni3W4bcj1iUgFAsIvd-6D2HRcUdk9p4jFkJuOK8Ap0HHaHg1eeQN510fdPPe1UwiKPGso1R9cgIJFYto3Rn5nW5rgB4kxVClnPLsRs1xoT4D2J2f49ZhyaPhMiW44VcqgWrNSXHDJgFsltOjR0_AXSEy9PKZuwQVTCDDKZeM-VirTTKoVaquW5HBO2PWU46j2yfH7MY8ElxJz1lnMMxcq5KEbkKcYmprj14t5vI-fCb5Mq4k2ZBdwMFEKrOCUpXC8TeQKISiZRilT9zKUcuogFy4V95QomJXU0lHLZVkY2paeFAWr6CEIFEZMUQU5MrS6F1T8mivWZK_NdV4BNVYG1fvc9HrHWmqDoJk11qg5EctUHI1trHMOosc6ixJGUZ1mcu6yUXqGA-onn6jNE83GBqMiG1Y4a1xRtWbGrA8bE1ZGTdDNNXtnRzdjG-DqhNzV5rcQdmsOtnK2wxvpd9ZEWCgHA5UOt-AG1LEIM21tGk5uQgEjOkU3b4y9v7bUQd_6x5juA7PMDfbKj7iB93OdEnj1rpCLCDdpRyiI93YSfdpIccVC5KepcaHL0VxvaBsoFR73bxYLTyoL7tjIGJ5UL9Pc-2_qHYIEeAGLHjpA-zyDthcH4PZ_Bh9URGe44oVYOraG3AYbUdhzRoA8NvwI9VfBRH_GkeK5x9zmnNkeJF-xlLAnbMvex7TjUw4ar-HsSnXgVbliHW4OJ9nKAECDErNwx6sgckfKuOpwpCY3dfLZeMoPJQQ_efxL5-F3vcxogS-ivzyWfOpYmd4kYrKNqqGT0zpAZx86EB1OnovYyWVssK1nsrhXqLe4Zdh9P9fkZKfARVpAGrIBaoByh-rtoDVteNdAJr524CdbHz1-1yxHUDYnvr4baMxtrgm1NwYM3rbL4W8G0NK3I0GXW3IAytGtNbPWTsq_tHDkADZTmRMfyLizA4d-mgsb447vlOqeD11dgeDdhlEWvdtgMQrLiTu9p9k2i2nAG2svoPkNCNKjtDkBhOiLkjlHCEKjpgdgVjvCMHOGGiJiIZKLnutECSDhNULUPUI0IXDqgonqlKHMFTlXEaKqExKLJyCzgaDQXUA0AID0EcpAowc8PSO8EyJgFdBQmIZFONCwCHg_AqCNIWqeMWgbPwXQQgIoTUMoS7H_r1DOMAloYIRApziuCWKov0JAAJGoRNpoTUGgPgHzjodYUsAYWdjIUgPIKCMoDLu4Z-nIVTLaPoKsCGksHYcAXVOoWAdwKYfQGzOEWuCej_qdv5N4b4WMP4UkfKCkQdn7NOk6GEKjpEDEOFP8JCEAA&debug=false&forceAllTransforms=false&shippedProposals=false&circleciRepo=&evaluate=false&fileSize=false&timeTravel=false&sourceType=script&lineWrap=true&presets=es2015-loose&prettier=false&targets=&version=7.8.7&externalPlugins=
'''

#Define file to write
newHtmlFile = 'resumeHtml.html'
newPDFFile = 'diegoAguileraResume.pdf'
fullPath = 'file:///Users/diegoaguilera/Projects/resume/resumeHtml.html'

WKHTMLTOPDF_PATH = '/usr/local/bin/wkhtmltopdf'

#Check to see if file exists
try:
    os.remove(newHtmlFile)
except OSError:
    pass

# Create a list of ids to remove
#idsToRemove = ['aboutmeID', 'technicalID',
idsToRemove = ['banner', 'navMenu', 'bntDownloadID', 'footerMapArea', 'jobSkills']
classToRemove = ['contact', 'footer', 'contactDetailsID', 'technical', 'reffernces']

#Define local file to open
link = open('index.html')

#Load page
soup = BeautifulSoup(link.read(), "html.parser")

#Iterate through all idsToRemove
for ids in idsToRemove:
    elements = soup.find_all("div", id=ids)

    for element in elements:
        #print('New element to delete - ', ids)
        element.decompose()

#Iterate through all classToRemove
for ids in classToRemove:
    elements = soup.find_all("section", id=ids)

    for element in elements:
        #print('New element to delete - ', ids)
        element.decompose()

#Convert to list to write
output = soup.prettify()

#Write to file
with open(newHtmlFile, 'a') as results_file:
    results_file.write(output)

print('Done writing new HTML file')

time.sleep(1)

options = {
    'enable-javascript' : None,
    'javascript-delay' : 1000,
    'enable-local-file-access' : None,
    'debug-javascript' : None,
    'no-collate' : None,
    'enable-external-links' : None
}
config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)

#Create PDF
pdfkit.from_file(newHtmlFile, newPDFFile, options=options, configuration=config)

print('Done creating PDF')
