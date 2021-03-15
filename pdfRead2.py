# coding=UTF-8
import PyPDF2
import sys

def pdf(filename):
    pdffile = PyPDF2.PdfFileReader(open(filename,'rb'))
    docinfo = pdffile.getDocumentInfo()
    for a in docinfo:
        print(a,":",docinfo)

def main():
    cmd = sys.argv[1:]
    for filename in cmd:
        a = filename
    pdf(a)

if __name__ == '__main__':
    main()
