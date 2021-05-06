from openpyxl import load_workbook
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
import itertools
import json
import informe_gen, informe_reg, informe_prov
import jsonify

zona = "SANTIAGO RODRIGUEZ"
doc = DocxTemplate("plantilla.docx")
context = informe_prov.datos(zona)
doc.render(context)
doc.save("test_generate.docx")
