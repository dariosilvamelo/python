"""
Documentação:
https://pythonhosted.org/PyPDF2/
Mais exemplos de uso:
pip install pdfmerger
"""
from PyPDF2 import PdfMerger

caminho = '.\\321-PDF_PyPDF2_Unindo_dividindo\\pdf\\'
# uniu PDF
merger1 = PdfMerger()
merger1.append(caminho+'arquivo1.pdf')
merger1.append(caminho+'arquivo2.pdf')
merger1.write(caminho+'unidao.pdf')
merger1.close()

# selecionar paginas do pdf
merger2 = PdfMerger()
merger2.append(caminho+'Mesclar_PDF.pdf', pages=(0, 2))  # first 3 pages
merger2.write(caminho+'selecao_paginas_01.pdf')
merger2.close()

merger3 = PdfMerger()
merger3.append(caminho+'Mesclar_PDF.pdf', pages=(0, 6, 2))  # pages 1,3, 5
merger3.write(caminho+'selecao_paginas_02.pdf')
merger3.close()
