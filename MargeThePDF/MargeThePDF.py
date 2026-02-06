from PyPDF2 import PdfMerger

AllPDF = ["1.pdf","2.pdf"]
OurMarger = PdfMerger()
for NewPdf in AllPDF:
    OurMarger.append(NewPdf)
OurMarger.write("Hablu.pdf")
OurMarger.close()
print("Marge the 2 PDF File Done.")
