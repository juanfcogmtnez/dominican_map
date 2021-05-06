import geopandas

df = geopandas.read_file('static/json/regiones.geojson',ignore_geometry=True)
minima_t_h = df[df['tasa_hospital']==df['tasa_hospital'].min()]
hospital_min = str(minima_t_h['nombre'].values.item())
tasa_h_min = str(minima_t_h['tasa_hospital'].values.item())
minima_t_c = df[df['tasa_centro_1_nivel']==df['tasa_centro_1_nivel'].min()]
centro_min = str(minima_t_c['nombre'].values.item())
tasa_c_min = str(minima_t_c['tasa_centro_1_nivel'].values.item())
maxima_t_h = df[df['tasa_hospital']==df['tasa_hospital'].max()]
hospital_max = str(maxima_t_h['nombre'].values.item())
tasa_h_max = str(maxima_t_h['tasa_hospital'].values.item())
maxima_t_c = df[df['tasa_centro_1_nivel']==df['tasa_centro_1_nivel'].max()]
centro_max = str(maxima_t_c['nombre'].values.item())
tasa_c_max = str(maxima_t_c['tasa_centro_1_nivel'].values.item())


print(df)
print(hospital_min)
print(tasa_h_min)
print(hospital_max)
print(tasa_h_max)
print(centro_min)
print(tasa_c_min)
print(centro_max)
print(tasa_c_max)
