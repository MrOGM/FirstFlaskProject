from flask import Flask, render_template
# iniciales server y especificas el sitio donde obtendra la info en este caso folder pages 
app = Flask(__name__, template_folder="./pages")
# app1 = Flask(_name_, template_folder="./pages")
import requests
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

@app.route("/")
def index():
    # se agrega URL del archivo json que posea la info que queramos
    databaseURL ="https://proyecto-prueb-944a0-default-rtdb.firebaseio.com/HumSensor.json"
    
    # se decodifica y obtiene la informacion del url suministrado
    respuesta = requests.get(databaseURL).content.decode("utf-8")
    
      
    return render_template("index.html", respuesta=respuesta)


@app.route("/index2")
def index2():
    databaseURL = "https://proyecto-prueb-944a0-default-rtdb.firebaseio.com/TempsRandom.json"
    respuesta = requests.get(databaseURL).json()
    # Convert the JSON data into a list of dictionaries
    data = []
    for key, value in respuesta.items():
        data.append({"Key": key, "Value": value})
    
    print(data)

    return render_template("index2.html", data=data)

@app.route("/index3")
def index3():
    databaseURL ="https://proyecto-prueb-944a0-default-rtdb.firebaseio.com/TempsSensor.json"
    databaseURL2 ="https://proyecto-prueb-944a0-default-rtdb.firebaseio.com/TempsRandom.json"

    respuesta = requests.get(databaseURL)
    respuesta = respuesta.json()
    
    respuesta2 = requests.get(databaseURL2)
    respuesta2 = respuesta2.json()

    lectura2 = []
    temp2 = []
    for key, value in respuesta2.items():
        lectura2.append(key)
        temp2.append(value)
    plt.figure()
    plt.plot(lectura2,temp2)
    plt.title("Temps Random")
    
    
    lectura = []
    temp = []
    for key, value in respuesta.items():
        lectura.append(key)
        temp.append(value)

    plt.figure()
    plt.plot(lectura,temp)
    plt.title("Temps Reales")
    plt.show()

if __name__ == '__main__':
    app.run(debug=True)