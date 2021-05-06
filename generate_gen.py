from io import BytesIO
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
import informe_gen

def get_context():
	data = informe_gen.informe()
	return(data)

def from_template(template,imagen1,imagen2,imagen3,imagen4):
	target_file = BytesIO()
	template = DocxTemplate(template)
	context = informe_gen.data
	img_size = Cm(12)  # sets the size of the image
	i1 = InlineImage(template, imagen1, img_size)
	i2 = InlineImage(template, imagen2, img_size)
	i3 = InlineImage(template, imagen3, img_size)
	i4 = InlineImage(template, imagen4, img_size)
	context['imagen1'] = i1
	context['imagen2'] = i2
	context['imagen3'] = i3
	context['imagen4'] = i4
	target_file = BytesIO()
	template.render(context)
	template.save(target_file)

	return target_file
