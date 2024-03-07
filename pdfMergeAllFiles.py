# THis module merges all the pages of all the pdfs files in a given directory.
import sys
import os
import  PyPDF2

from PyPDF2 import PdfReader, PdfWriter, PdfMerger
print(sys.argv[1])
print(sys.argv[0])
pdfs = []

merger = PdfMerger()
i =  0
for item in os.walk(sys.argv[1]):
  #for i in item:
  #  print(i)
  print(123456)
  


masterItem = []
for i in item[2]:
  masterItem.append(i)

fileSubScript = 0  
while (len(masterItem)>0):
  merger = PdfMerger()
  for filename in masterItem:
    print(sys.argv[1]+filename)
    if (os.stat(sys.argv[1]+filename).st_size != 0):
      merger.append(PdfReader(open(sys.argv[1]+filename, 'rb')))
    masterItem.remove(filename)
  merger.write('result_'+str(fileSubScript)+'.pdf')
  
  print('Completed ......' + str(fileSubScript) + '.....................Attempt')
  fileSubScript = fileSubScript + 1
  print(len(masterItem))  

merger2 = PdfMerger()

for i in range(fileSubScript):
  print('result_'+str(i)+'.pdf')
  merger2.append('result_'+str(i)+'.pdf')

print(i)
# Replace 'final.pdf' with the name you wanted in the below line of code
merger2.write('BSCOPYCENTERPL.pdf')  
'''
#print(len(masterItem))  

#########################################################################
count = 0
for filename in item[2]:
    print(sys.argv[1]+filename) 
    #print(count)
    count = count + 1
   
    merger.append(PdfReader(open(sys.argv[1]+filename, 'rb')))
    # Remove the file from list so that you have list with unprocessed files.
    item[2].remove(filename) 
merger.write('result123.pdf')

 
count = 0
mymerger = PdfMerger()
print(" $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start of First chunk ")
for filename in masterItem:
    print(sys.argv[1]+filename) 
    #print(count)
    count = count + 1
   
    mymerger.append(sys.argv[1]+filename)
    # Remove the file from list so that you have list with unprocessed files.
    masterItem.remove(filename) 
mymerger.write('result456.pdf')
mymerger.close()
print(" $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start of Second chunk ")

mymerger1 = PdfMerger()
for filename in masterItem:
    print(sys.argv[1]+filename) 
    #print(count)
    count = count + 1
   
    mymerger1.append(sys.argv[1]+filename)
    # Remove the file from list so that you have list with unprocessed files.
    masterItem.remove(filename) 
mymerger1.write('result789.pdf')
mymerger1.close()
print(len(masterItem))

print(" $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start of Third chunk ")
mymerger2 = PdfMerger()
for filename in masterItem:
    print(sys.argv[1]+filename) 
    #print(count)
    count = count + 1
    print("B4 Append 73")
    mymerger2.append(sys.argv[1]+filename)
    print("Af Append 75") 
    # Remove the file from list so that you have list with unprocessed files.
    masterItem.remove(filename) 
mymerger2.write('result000.pdf')
print(len(masterItem))
mymerger2.close()
print(" $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start of Fourth chunk ")
mymerger3 = PdfMerger()
for filename in masterItem:
    print(sys.argv[1]+filename) 
    #print(count)
    count = count + 1
    print("B4 Append 86")
    mymerger3.append(sys.argv[1]+filename)
    print("After Append 88")
    # Remove the file from list so that you have list with unprocessed files.
    masterItem.remove(filename) 
mymerger3.write('result111.pdf')
print(len(masterItem))
mymerger3.close()    
print(" $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start of Fourth chunk ")
mymerger4 = PdfMerger()
for filename in masterItem:
    print(sys.argv[1]+filename) 
    #print(count)
    count = count + 1
    print("B4 Append 101")
    mymerger4.append(sys.argv[1]+filename)
    print(" After Append 101")
    # Remove the file from list so that you have list with unprocessed files.
    masterItem.remove(filename) 
mymerger4.write('result222.pdf')
print(len(masterItem))    
mymerger4.close()

'''
