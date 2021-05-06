from io import BytesIO
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
import informe

def get_context(texto=None):
	data = informe.informe(texto)
	return(data)
def from_template(template, texto):
    target_file = BytesIO()

    template = DocxTemplate(template)
    context = get_context(texto)  # gets the context used to render the document

    """img_size = Cm(7)  # sets the size of the image
    sign = InlineImage(template, signature, img_size)
    context['signature'] = sign  # adds the InlineImage object to the context"""

    target_file = BytesIO()
    template.render(context)
    template.save(target_file)

    return target_file
