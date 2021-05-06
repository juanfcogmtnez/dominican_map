import geopandas
import json

tipo = "region"
ZONA = "METROPOLITANA"

if tipo == "region":
	tipo = "srs"
df = geopandas.read_file('static/json/hospitales.geojson',ignore_geometry=True)
if tipo != "país":
	filtrapor = df[tipo] == ZONA
df = df[filtrapor]
df = df.drop(['direccion',"email","nombre_director","nivel","extension","complejidad","srs","region","tipo","unap","telefono","distrito","barrio","seccion","subbario","gerencia","apertura","reforma","zona","sector"], axis=1)

result = df.to_json(orient="records")
parsed = json.loads(result)
print(json.dumps(parsed, indent=4))
