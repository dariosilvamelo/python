import os

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def milimetro(mm):
    return mm/0.352777


pdf = canvas.Canvas(".\\999-Relatorio-Pdf\\Relatorio.pdf", pagesize=A4)
pdf.setFont("Courier", 20)
pdf.setFillColor("red")
# são coordenadas x=(297),y=(210) milimetros para folha (A4)
#

pdf.drawImage('C:\\0 - Aplicativos\\Fiscal\\Comercial\\LOGOTIPO.JPG',
              milimetro(10), milimetro(230))
pdf.drawString(milimetro(10), milimetro(220), "Lista de nomes")
pdf.drawString(milimetro(10), milimetro(217), "==============")
pdf.drawString(milimetro(10), milimetro(211), " ")
pdf.setFillColor("black")
pdf.setFont("Times-Bold", 10)
pdf.drawString(milimetro(10), milimetro(210), "Dário da Silva Melo")
pdf.drawString(milimetro(10), milimetro(205), "Patrícia da Silva Melo")
pdf.drawString(milimetro(10), milimetro(200), "Carulina da Silva Melo")
pdf.drawString(milimetro(10), milimetro(195), "Lusmar Rocha da Silva")
pdf.drawString(milimetro(10), milimetro(190), "Clariano Francisco Filho")
pdf.circle(milimetro(30), milimetro(160), milimetro(20))

# A primeita lista é para definir o numro de colula
# cada elemento colocado na lista é uma coluna
# é precido colocar a posição onde começa

# A segunda lista é para definir o numro de linhas
# cada elemento colocado na lista é uma linha
# é precido colocar a posição onde começa


pdf.grid([milimetro(7), milimetro(55), milimetro(85), milimetro(115), milimetro(145), milimetro(175)],
         [milimetro(214), milimetro(209), milimetro(204), milimetro(199), milimetro(194), milimetro(189), milimetro(184)])

pdf.grid([10, 20, 30, 40], [50, 60, 70, 80, 90])

pdf.save()
print('Relatorio Salvo Com Sucesso')
