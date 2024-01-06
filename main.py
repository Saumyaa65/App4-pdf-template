from fpdf import FPDF
import pandas as pd

pdf= FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df=pd.read_csv("topics (1).csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Arial", style="B", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=24, txt=row["Topic"], align="L", ln=1)
    pdf.line(8,26,180,26)

    pdf.ln(250)
    pdf.set_font(family="Arial", size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

    for i in range(row["Pages"]-1):
        pdf.add_page()
        pdf.ln(273)
        pdf.set_font(family="Arial", size=12)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

pdf.output("Output.pdf")