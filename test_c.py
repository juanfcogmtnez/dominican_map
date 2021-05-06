import geopandas
import json

tipo = "region"
ZONA = "METROPOLITANA"

if tipo == "region":
	tipo = "srs"
df = geopandas.read_file('static/json/centros.geojson',ignore_geometry=True)

if tipo != "país":
	filtrapor = df[tipo] == ZONA
df = df[filtrapor]
df = df.drop(['direccion',"email","srs","region","tipo","unap","telefono","distrito","barrio","seccion","subbarrio","gerencia","apertura","reforma","zona","sector","ID_CENTRO","nivel_atencion"], axis=1)

result = df.to_json(orient="records")
parsed = json.loads(result)
print(json.dumps(parsed, indent=4))
