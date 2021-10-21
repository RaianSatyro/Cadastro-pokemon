from src.dao.pokemon_dao import PokemonDAO
from src.classes.pokemon import Pokemon
from src.db.db_connection import db
from flask.app import Flask
from flask import flash, jsonify, request, render_template


novo_pokemon = Pokemon(1, "Pikachu", 'Eletrico', 'Masculino')
novo_pokemon_dao = PokemonDAO(novo_pokemon)
db.insert_in_BD(novo_pokemon_dao.to_json())



app = Flask(__name__)
@app.route('/pokemon', methods=['GET'])
def pokemon():
    return render_template('pokemon.html')

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port='3001')