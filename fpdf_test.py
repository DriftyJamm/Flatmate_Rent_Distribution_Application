from fpdf import FPDF

pdf = FPDF(orientation = 'P', unit = 'pt', format = 'A4')
pdf.add_page()

pdf.set_font(family = 'Times', size = 24, style = 'B')
pdf.cell(w = 300, h = 80, txt = "Flatmates Bill", border = 0, align = "c", ln = 1)
pdf.cell(w = 200, h = 40, txt = "Period", border = 1)
pdf.cell(w = 200, h = 40, txt = "Table", border = 1,ln = 1)

pdf.output("Bill.pdf")