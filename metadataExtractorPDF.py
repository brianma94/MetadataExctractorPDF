#_*_ coding: utf-8 _*_
import optparse
import PyPDF2
from PyPDF2 import PdfFileReader

def impr(fileName):
	pdfFile = PdfFileReader(file(fileName,'rb'))
	meta = pdfFile.getDocumentInfo()
	print '- Documento:' + str(fileName)
	for i in meta:
		print '-' + i + ':' + meta[i]

def main():
	parser = optparse.OptionParser('usage %prog " + "-F <PDF file name>')
	parser.add_option('-f', dest='fileName', type='string', help='specify PDF file name')

	(options, args) = parser.parse_args()
	fileName = options.fileName
	if fileName == None:
		print parser.usage
		exit(0)
	else:
		impr(fileName)

if __name__ == '__main__':
	main()