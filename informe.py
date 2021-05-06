from io import BytesIO
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
import geopandas
import matplotlib.pyplot as plt
import json
def informe(informe=None):
	if informe == None:
		informe = ""
	barra = informe.find("/")
	if barra < 0:
		artipo = "El"
		tipo = "país"
		artipob = "La"
		este = "esta"
		un = "una"
		tipob ="regiones sanitarias"
		zona = "República Dominicana"
		df = geopandas.read_file('static/json/regiones.geojson')
	if barra > 0:
		info = informe.split("/")
		artipob = "La"
		este = "esta"
		un = "una"
		tipob = info[0]
		zona = info[1]
		df = geopandas.read_file('static/json/regiones.geojson')
	if tipob == "regiones":
		tipob == "regiones sanitarias"
		artipob = "La"
	if tipob == "provincias":
		artipo = "La"
		tipo = "región de"
		artipob = "El"
		este = "este"
		un = "un"
		df = geopandas.read_file('static/json/provincias.geojson')
		filtrapor = df['region'] == zona
		df = df[filtrapor]
	if tipob == "municipios":
		artipo = "La"
		tipo = "provincia de"
		df = geopandas.read_file('static/json/municipios.geojson')
		filtrapor = df['provincia'] == zona
		df = df[filtrapor]

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
	tabla_hospitales = hospitales(tipo,ZONA)
	tabla_centros = centros(tipo,ZONA)

	data = {'zona':zona,'ZONA':ZONA,'Artipo':artipo,'tipo':tipo,'count':count,'tipob':tipob,'superficie':superficie,'poblacion':poblacion,'densidad':densidad,'n_hospitales':n_hospitales,'n_centros':n_centros,'tasa_centros':tasa_centros,'tasa_hospitales':tasa_hospital,'Artipob':artipob,'un':un,'este':este,'tabla_hospitales':tabla_hospitales,'tabla_centros':tabla_centros}
	return (data)
	
def hospitales(tipo,ZONA):
	if tipo == "region":
		tipo = "srs"
	df = geopandas.read_file('static/json/hospitales.geojson',ignore_geometry=True)
	if tipo != "país":
		filtrapor = df[tipo] == ZONA
		df = df[filtrapor]
	df = df.drop(['direccion',"email","nombre_director","nivel","extension","complejidad","srs","region","tipo","unap","telefono","distrito","barrio","seccion","subbario","gerencia","apertura","reforma","zona","sector"], axis=1)

	result = df.to_json(orient="records")
	parsed = json.loads(result)
	return(json.dumps(parsed, indent=4))

def centros(tipo,ZONA):
	if tipo == "region":
		tipo = "srs"
	df = geopandas.read_file('static/json/centros.geojson',ignore_geometry=True)

	if tipo != "país":
		centropor = df[tipo] == ZONA
		df = df[centropor]
	df = df.drop(['direccion',"email","srs","region","tipo","unap","telefono","distrito","barrio","seccion","subbarrio","gerencia","apertura","reforma","zona","sector","ID_CENTRO","nivel_atencion"], axis=1)

	result = df.to_json(orient="records")
	parsed = json.loads(result)
	return(json.dumps(parsed, indent=4))
	
	
	
		



