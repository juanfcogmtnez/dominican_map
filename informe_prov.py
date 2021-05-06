from io import BytesIO
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
import geopandas
import matplotlib.pyplot as plt
import json
import jsonify

	
def hospitales(zona):
	if zona == "SAN PEDRO DE MACORIS":
		zona = "SAN PEDRO DE MACORÍS"
	df = geopandas.read_file('static/json/hospitales.geojson',ignore_geometry=True)
	filtrapor = df['provincia'] == zona
	df = df[filtrapor]	
	df = df.drop(['direccion',"email","nombre_director","nivel","extension","complejidad","srs","region","tipo","unap","telefono","distrito","barrio","seccion","subbario","gerencia","apertura","reforma","zona","sector"], axis=1)
	result = df.to_json(orient="records")
	parsed = json.loads(result)
	return parsed

def centros(zona):
	df = geopandas.read_file('static/json/centros.geojson',ignore_geometry=True)
	filtrapor = df['provincia'] == zona
	df = df[filtrapor]
	df = df.drop(['direccion',"email","srs","region","tipo","unap","telefono","distrito","barrio","seccion","subbarrio","gerencia","apertura","reforma","zona","sector","ID_CENTRO","nivel_atencion"], axis=1)
	result = df.to_json(orient="records")
	parsed = json.loads(result)
	return(parsed)
	
def datos(zona):
	df = geopandas.read_file('static/json/municipios.geojson',ignore_geometry=True)
	zona = zona
	ZONA = zona.upper()
	tabla_hospitales = hospitales(ZONA)
	tabla_centros = centros(ZONA)
	filtrapor = df['provincia'] == zona
	df = df[filtrapor]
	artipo = "La"
	tipo = "provincia"
	artipob = "El"
	este = "esta"
	un = "una"
	tipob ="municipio"
	tipobp ="municipios"
	zona = zona.lower()
	zona = zona.capitalize()
	count = str(df.shape[0])

	superficie = int(df['superficie'].sum())
	poblacion = int(df['poblacion'].sum())
	n_hospitales = int(df['hospital'].sum())
	n_centros = int(df['centro_1_nivel'].sum())
	if poblacion < 0.1:
		poblacion = 0.1	
	if n_hospitales <0.1:
		n_hospitales = 0.001
	if n_centros < 0.1:
		n_centros = 0.001
		
	tasa_hospital = n_hospitales/ (poblacion/100000)
	tasa_centros = n_centros / (poblacion/10000)
	tasa_hospital = n_hospitales / (poblacion/10000)
	tasa_centros = n_centros/ (poblacion/10000)	
	densidad = poblacion/ superficie
	minima_t_h = df[df['tasa_hospital']==df['tasa_hospital'].min()]
	maxima_p = df[df['poblacion']==df['poblacion'].max()]
	hospital_min = minima_t_h.iloc[0]['nombre']
	tasa_h_min = minima_t_h.iloc[0]['tasa_hospital']
	minima_t_c = df[df['tasa_centro_1_nivel']==df['tasa_centro_1_nivel'].min()]
	centro_min = minima_t_c.iloc[0]['nombre']
	tasa_c_min = minima_t_c.iloc[0]['tasa_centro_1_nivel']
	maxima_t_h = df[df['tasa_hospital']==df['tasa_hospital'].max()]
	hospital_max = maxima_t_h.iloc[0]['nombre']
	tasa_h_max = maxima_t_h.iloc[0]['tasa_hospital']
	maxima_t_c = df[df['tasa_centro_1_nivel']==df['tasa_centro_1_nivel'].max()]
	centro_max = maxima_t_c.iloc[0]['nombre']
	tasa_c_max = minima_t_c.iloc[0]['tasa_centro_1_nivel']

	data = {"zona":zona,"ZONA":ZONA,"Artipo":artipo,"tipo":tipo,"count":count,"tipob":tipob,"tipobp":tipobp,"superficie":superficie,"poblacion":poblacion,"densidad":densidad,"n_hospitales":n_hospitales,"n_centros":n_centros,"tasa_centros":tasa_centros,"tasa_hospitales":tasa_hospital,"Artipob":artipob,"un":un,"este":este,"tabla_hospitales":tabla_hospitales,"tabla_centros":tabla_centros,"hospital_min":hospital_min,"tasa_h_min":tasa_h_min,"hospital_max":hospital_max,"tasa_h_max":tasa_h_max,"centro_min":centro_min,"tasa_c_min":tasa_c_min,"centro_max":centro_max,"tasa_c_max":tasa_c_max}
	return (data)
