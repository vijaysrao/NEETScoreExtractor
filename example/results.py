# importing all the required modules
import PyPDF2
import glob
import csv

def getCentreName (fileName):
    centreName = ''
    idx = file.rfind('\\')
    if idx > 0:
        centreName = file[idx+1:-4]
        print (centreName)

    return centreName

def getData (page, dataList):
    content = page.replace('Srlno. Marks', ' ')
    c = content.split ('\n')
    for i in range (1,len(c)):
        col = c[i]
        if len(col) > 2:
            preData = col.split(' ')
            data = [x for x in preData if x != ""]
            scoreData = data[1::2]
            # print (i, ":", scoreData)
            for score in scoreData:
                dataList.append(score)
    return dataList

csvFileName = 'data.csv'

csvFile = open (csvFileName, 'w',newline='')
write = csv.writer (csvFile)

files = glob.glob('.' + '/**/*.pdf', recursive=True)

countFiles = 1

for file in files:
    centreName = getCentreName (file)

    # creating a pdf reader object
    reader = PyPDF2.PdfReader(file)

    # print the number of pages in pdf file
    numPages = len(reader.pages)

    print (countFiles,':','Processing',file,'with',numPages,'pages')
    listAllScores = [centreName]
    for p in range (numPages):
        listAllScores = getData (reader.pages[p].extract_text(), listAllScores)
        
    print ('Done. Found',len(listAllScores)-1,'scores')
    print ('======')
    write.writerow(listAllScores)

    countFiles = countFiles + 1
        
        