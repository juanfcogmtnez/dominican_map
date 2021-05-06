import matplotlib.pyplot as plt
import geopandas as gdp
from descartes import PolygonPatch

def img_pais():
	df = gdp.read_file('static/json/regiones.geojson')
	region = gdp.read_file('static/json/regiones.geojson')
	df.plot()
	plt.axis('off')
	plt.savefig("img1.png", bbox_inches='tight')
	
	df2 = gdp.read_file('static/json/regiones.geojson')
	df2.plot(cmap='terrain')
	plt.axis('off')
	plt.savefig("img2.png", bbox_inches='tight')
	
	df3 = df2
	df3.plot(column='tasa_hospital', cmap='RdYlGn')
	plt.axis('off')
	plt.savefig("img3.png", bbox_inches='tight')
	
	df4 = df2
	df2.plot(column='tasa_centro_1_nivel', cmap='RdYlGn')
	plt.axis('off')
	plt.savefig("img4.png", bbox_inches='tight')
		
def img_region(zona):
	df = gdp.read_file('static/json/regiones.geojson')
	region = gdp.read_file('static/json/regiones.geojson')
	filtrapor = region['nombre'] == zona
	region = region[filtrapor]
	fig, ax = plt.subplots (1, figsize = (8,8))
	df.plot (ax = ax, color = 'grey', edgecolor="black",alpha = 0.2) 
	region.plot (ax = ax, alpha = 1) 
	plt.axis('off')
	plt.savefig("img1.png", bbox_inches='tight')
	
	df2 = gdp.read_file('static/json/provincias.geojson')
	filtrapor = df2['region'] == zona
	df2 = df2[filtrapor]
	df2.plot()
	plt.axis('off')
	plt.savefig("img2.png", bbox_inches='tight')
	
	df3 = df2
	df3.plot(column='tasa_hospital', cmap='RdYlGn')
	plt.axis('off')
	plt.savefig("img3.png", bbox_inches='tight')
	
	df4 = df2
	df2.plot(column='tasa_centro_1_nivel', cmap='RdYlGn')
	plt.axis('off')
	plt.savefig("img4.png", bbox_inches='tight')

def img_provincia(zona):
	df = gdp.read_file('static/json/provincias.geojson')
	region = gdp.read_file('static/json/provincias.geojson')
	filtrapor = region['nombre'] == zona
	region = region[filtrapor]
	fig, ax = plt.subplots (1, figsize = (8,8))
	df.plot (ax = ax, color = 'grey', edgecolor="black",alpha = 0.2) 
	region.plot (ax = ax, alpha = 1) 
	plt.axis('off')
	plt.savefig("img1.png", bbox_inches='tight')
	
	df2 = gdp.read_file('static/json/municipios.geojson')
	filtrapor = df2['provincia'] == zona
	df2 = df2[filtrapor]
	df2.plot()
	plt.axis('off')
	plt.savefig("img2.png", bbox_inches='tight')
	
	df3 = df2
	df3.plot(column='tasa_hospital', cmap='RdYlGn')
	plt.axis('off')
	plt.savefig("img3.png", bbox_inches='tight')
	
	df4 = df2
	df2.plot(column='tasa_centro_1_nivel', cmap='RdYlGn')
	plt.axis('off')
	plt.savefig("img4.png", bbox_inches='tight')

