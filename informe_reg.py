from io import BytesIO
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
import geopandas
import matplotlib.pyplot as plt
import json
import jsonify

	
def hospitales(zona):
	df = geopandas.read_file('static/json/hospitales.geojson',ignore_geometry=True)
	filtrapor = df['srs'] == zona
	df = df[filtrapor]	
	df = df.drop(['direccion',"email","nombre_director","nivel","extension","complejidad","srs","region","tipo","unap","telefono","distrito","barrio","seccion","subbario","gerencia","apertura","reforma","zona","sector"], axis=1)
	result = df.to_json(orient="records")
	parsed = json.loads(result)
	return parsed

def centros(zona):
	df = geopandas.read_file('static/json/centros.geojson',ignore_geometry=True)
	filtrapor = df['srs'] == zona
	df = df[filtrapor]
	df = df.drop(['direccion',"email","srs","region","tipo","unap","telefono","distrito","barrio","seccion","subbarrio","gerencia","apertura","reforma","zona","sector","ID_CENTRO","nivel_atencion"], axis=1)
	result = df.to_json(orient="records")
	parsed = json.loads(result)
	return(parsed)
	
def datos(zona):
	df = geopandas.read_file('static/json/provincias.geojson',ignore_geometry=True)
	tabla_hospitales = hospitales(zona)
	tabla_centros = centros(zona)
	filtrapor = df['region'] == zona
	df = df[filtrapor]
	artipo = "La"
	tipo = "región"
	artipob = "La"
	este = "esta"
	un = "una"
	tipob ="provincia"
	tipobp ="provincias"
	zona = zona
	ZONA = zona.upper()
	zona = zona.lower()
	zona = zona.capitalize()
	count = str(df.shape[0])

	superficie = str(int(df['superficie'].sum()))
	densidad = str(int((df['poblacion'].sum())/(df['superficie'].sum())))
	poblacion = str(int(df['poblacion'].sum()))
	n_hospitales = str(int(df['hospital'].sum()))
	tasa_hospital = (int(df['hospital'].sum()) / (int(df['poblacion'].sum())/100000))
	tasa_hospital = str(round(tasa_hospital,2))
	n_centros = str(int(df['centro_1_nivel'].sum()))
	tasa_centros = (int(df['centro_1_nivel'].sum()) / (int(df['poblacion'].sum())/10000))
	tasa_centros = str(round(tasa_centros,2))

	minima_t_h = df[df['tasa_hospital']==df['tasa_hospital'].min()]
	hospital_min = str(minima_t_h['nombre'].item())
	tasa_h_min = str(minima_t_h['tasa_hospital'].item())
	minima_t_c = df[df['tasa_centro_1_nivel']==df['tasa_centro_1_nivel'].min()]
	centro_min = str(minima_t_c['nombre'].item())
	tasa_c_min = str(minima_t_c['tasa_centro_1_nivel'].item())
	maxima_t_h = df[df['tasa_hospital']==df['tasa_hospital'].max()]
	hospital_max = str(maxima_t_h['nombre'].item())
	tasa_h_max = str(maxima_t_h['tasa_hospital'].item())
	maxima_t_c = df[df['tasa_centro_1_nivel']==df['tasa_centro_1_nivel'].max()]
	centro_max = str(maxima_t_c['nombre'].item())
	tasa_c_max = str(maxima_t_c['tasa_centro_1_nivel'].item())

	data = {"zona":zona,"ZONA":ZONA,"Artipo":artipo,"tipo":tipo,"count":count,"tipob":tipob,"tipobp":tipobp,"superficie":superficie,"poblacion":poblacion,"densidad":densidad,"n_hospitales":n_hospitales,"n_centros":n_centros,"tasa_centros":tasa_centros,"tasa_hospitales":tasa_hospital,"Artipob":artipob,"un":un,"este":este,"tabla_hospitales":tabla_hospitales,"tabla_centros":tabla_centros,"hospital_min":hospital_min,"tasa_h_min":tasa_h_min,"hospital_max":hospital_max,"tasa_h_max":tasa_h_max,"centro_min":centro_min,"tasa_c_min":tasa_c_min,"centro_max":centro_max,"tasa_c_max":tasa_c_max}
	return (data)
