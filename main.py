import requests
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def show_pokedex():

    pokemon_list = []

    for index in range(1, 152):

        URL = f"https://pokeapi.co/api/v2/pokemon/{index}"
        respuesta = requests.get(URL).json()
        pokemon_list.append(respuesta)
  
    return render_template("index.html", pokemon_list=pokemon_list)

if __name__ == "__main__":
    app.run(debug=True)
