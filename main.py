from flask import Flask, render_template, jsonify, url_for, send_file
import read, generate, generate_gen, generate_reg, generate_prov, graph

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
	return render_template('index.html')
		
@app.route('/regiones')
@app.route('/regiones/<region>', methods=['GET','POST'])
def regiones(region=None):
	region = read.region(region)
	return jsonify(region)

@app.route('/provincias')
@app.route('/provincias/<region>', methods=['GET','POST'])
def provincias(region=None):
	region = read.provincia(region)
	return jsonify(region)

@app.route('/municipios')
@app.route('/municipios/<provincia>', methods=['GET','POST'])
def municipios(provincia=None):
	provincia = read.municipio(provincia)
	return jsonify(provincia)
@app.route('/informe')
def gen_docx_gen():
	imagenes = graph.img_pais()
	template = 'plantilla.docx'
	imagen1 = "img1.png"
	imagen2 = "img2.png"
	imagen3 = "img3.png"
	imagen4 = "img4.png"
	document = generate_gen.from_template(template,imagen1,imagen2,imagen3,imagen4)
	document.seek(0)
	return send_file(
        document, mimetype='application/vnd.openxmlformats-'
        'officedocument.wordprocessingml.document', as_attachment=True,
        attachment_filename='informe.docx')
@app.route('/informe/region/<zona>')
def gen_docx_reg(zona):
	imagenes = graph.img_region(zona)
	template = 'plantilla.docx'
	imagen1 = "img1.png"
	imagen2 = "img2.png"
	imagen3 = "img3.png"
	imagen4 = "img4.png"
	document = generate_reg.from_template(template,zona, imagen1,imagen2,imagen3,imagen4)
	document.seek(0)
	return send_file(
        document, mimetype='application/vnd.openxmlformats-'
        'officedocument.wordprocessingml.document', as_attachment=True,
        attachment_filename='informe.docx')

@app.route('/informe/provincia/<zona>')
def gen_docx_prov(zona):
	imagenes = graph.img_provincia(zona)
	template = 'plantilla.docx'
	imagen1 = "img1.png"
	imagen2 = "img2.png"
	imagen3 = "img3.png"
	imagen4 = "img4.png"
	document = generate_prov.from_template(template,zona, imagen1,imagen2,imagen3,imagen4)
	document.seek(0)
	return send_file(
        document, mimetype='application/vnd.openxmlformats-'
        'officedocument.wordprocessingml.document', as_attachment=True,
        attachment_filename='informe.docx')
if __name__ == "__main__":
    app.run(host='0.0.0.0')
