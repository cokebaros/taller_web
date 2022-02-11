from flask import Flask, escape, request, render_template, url_for  # IMportar la libreria

app = Flask(__name__)  # Inicializamos la app con  el nombre

@app.route('/')  # Definimos que en la ruta de inicio será aplicada la función 'hola'

def hola():
    return 'Hi Penguins'  # Retorna 'Hi Penguins'

@app.route('/coach')            # Creamos la ruta "Coach"
def hola_coaches():             # Definimos la función que será devuelta
    nombre = 'Steven'             # Inicializamos un dato
    devolver = request.args.get('nombre', nombre)       # Definimos que será devuelto y renderizado
    return f'Hola, {escape(devolver)}.'      # Retornamos al HTML

@app.route('/inicio')   #Creamos la ruta de inicio
def inicio():
    return render_template('inicio.html')

@app.route('/contacto')    
def contacto():
    return render_template('contacto.html')


app.run(debug=True)   # Para ejecutar




