import sys

from PyPDF2 import PdfFileReader, PdfFileWriter

args = sys.argv

def process():
    input_file1 = PdfFileReader(args[1])
    input_file2 = PdfFileReader(args[2])
    total_page = input_file1.getNumPages()
    total_page2 = input_file2.getNumPages()
    print("Total pages for doc 1 is {}, and doc 2 {}".format(total_page, total_page2))
    if total_page == total_page2:
        print("Total pages matches both")
    else:
        return

    # start new pdf
    output = PdfFileWriter()
    for i in range(total_page):
        output.addPage(input_file1.getPage(i))
        output.addPage(input_file2.getPage(total_page -1 - i))
    filename = args[3]
    with open("a{}.pdf".format(filename), "wb") as output_stream:
        output.write(output_stream)




if len(args) == 4:
    print('Processing the two files {} {}'.format(args[1], args[2]))
    process()
