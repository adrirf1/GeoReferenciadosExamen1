from flask import Flask, render_template, request,redirect
from folium.features import DivIcon
import folium
import requests

app = Flask(__name__)
#21.13188
#-101.68402
@app.route("/")
def form():
    return render_template('index.html')

'''
@app.route("/respuesta")
def respuesta():
    return render_template('respuesta.html', fname=request.args['fname'])
'''
def ubicacion():
    res = requests.get('https://ipinfo.io/')
    datos = res.json()
    loc = datos['loc'].split(',')
    lat = loc[0]
    long = loc[1]
    return float(lat),float(long)

@app.route('/respuesta', methods=['GET', 'POST'])
def respuestaMapa():
    if request.method == "POST":
        x = request.form.get('x')
        y = request.form.get('y')
        nombre = request.form.get('nombre')
        return base(x,y,nombre)
    
    

@app.route('/mapa')
def base(x,y,nombre):
    
    map = folium.Map(
        location=[21.13188,-101.68402],zoom_start=9,#width=500,height=500
    )
    folium.Marker(
        location=ubicacion(),
        popup = "Tu ubicacion actual"
    ).add_to(map)

    folium.Marker(
        location=[x,y],
        popup = "Ubicacion de tu pedido",
        icon=folium.Icon(color='red')
    ).add_to(map)
    #return map._repr_html_()
    map.save('templates/map.html')
    return render_template('respuesta.html',value=nombre)


@app.route('/map')
def map():
    return render_template('map.html')

print(ubicacion())
if __name__ == "__main__":
    app.run(debug=True)