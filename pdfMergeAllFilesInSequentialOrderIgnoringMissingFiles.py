# This module will pick files from two different directories and pick the all the pages from both corresponding PDF files 
# For example : file names Org0001_*pg1 and Org0001_*pg3 are treated as corresponding file. All the pages of each of these files is merged in to 
# the output file. Same processes is repeated for all the files. In case if a corresponding file is missing in either first or second directory
# it is simply ignored and all the files are merged.


import sys
import os
import PyPDF2

def retFirstPageOfPdf_1(inputFileName) -> PyPDF2.PdfReader.pages:
    #Open PDF file and read the first page and write it as different PDF
    print('Start of Process')
    pdfFH = open(inputFileName, "rb")
    pdfReader = PyPDF2.PdfReader(pdfFH)
    pageObj = pdfReader.pages[0]
    pdfWriter = PyPDF2.PdfWriter()
    pdfWriter.add_page(pageObj)
    with open("output.pdf", 'wb') as pdfWFh:
      pdfWriter.write(pdfWFh)

    print(inputFileName)
    pass

def retFirstPageOfPdf(inputFileName, pageNumber = 0) -> PyPDF2.PdfReader.pages:
    #Open PDF file and read the first page and write it as different PDF
    print('Start of Process: ' + inputFileName  + ' ......' + str(pageNumber))
    print(inputFileName)
    print(type(inputFileName))
    pdfFH = open(str(inputFileName), "rb")
    pdfReader = PyPDF2.PdfReader(pdfFH)
    pageObj = pdfReader.pages[pageNumber]
    #Add Error handling and try catch block around this code to catch issues
    return pageObj
    
def retListOfFilesInADir(inputPath):
    listOfPdfFiles = []
    for dirpath, dirs, files in sorted(os.walk(inputPath)):
        for filename in files:
            if filename.lower().endswith(".pdf"):
                listOfPdfFiles.append(os.path.join(dirpath, filename))
    return listOfPdfFiles            

if __name__ == "__main__":
# Driver code
    print(sys.argv[1], sys.argv[2])
    # Get list of files from input dir1
    inputList1 = retListOfFilesInADir(sys.argv[1])
    #print(inputList1)
    # Get list of files form input dir2
    inputList2 = retListOfFilesInADir(sys.argv[2])
    #print(inputList2)

    # Merge both input lists
    listOfPdfFiles_1 = zip(inputList1, inputList2)
    
    print(' # '*20)
    print(type(listOfPdfFiles_1))
    pdfWriter = PyPDF2.PdfWriter()
    merger = PyPDF2.PdfMerger()
    for files in listOfPdfFiles_1:
      for file in files:     
        print(type(file))
        print(file)       
        merger.append(PyPDF2.PdfReader(file,'rb'))
    merger.write("result.pdf")
