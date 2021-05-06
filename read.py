import geopandas
import pandas as pd
import geojson
import fiona
from fiona import drivers

def region(filtro=None):
		if filtro == None:
			data = geopandas.read_file('static/json/regiones.geojson')
			return geojson.dumps(data)				
		
		data = geopandas.read_file('static/json/regiones.geojson')
		filtrapor = data['nombre'] == filtro
		data = data[filtrapor]
		return geojson.dumps(data)

def provincia(filtro=None):
		if filtro == None:
			data = geopandas.read_file('static/json/provincias.geojson')
			return geojson.dumps(data)				
		
		data = geopandas.read_file('static/json/provincias.geojson')
		filtrapor = data['region'] == filtro
		data = data[filtrapor]
		return geojson.dumps(data)

def municipio(filtro=None):
		if filtro == None:
			data = geopandas.read_file('static/json/municipios.geojson')
			return geojson.dumps(data)				
		
		data = geopandas.read_file('static/json/municipios.geojson')
		filtrapor = data['provincia'] == filtro
		data = data[filtrapor]
		return geojson.dumps(data)

def reset():			
		data = geopandas.read_file('static/json/reset.geojson')
		return ""


