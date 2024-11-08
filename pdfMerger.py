import PyPDF2
pdfs=['1.pdf','2.pdf']
merger=PyPDF2.PdfMerger()
for files in pdfs:
    File=open(files,'rb')
    PdfFile=PyPDF2.PdfReader(File)
    merger.append(PdfFile)
File.close()
merger.write("merger.pdf")