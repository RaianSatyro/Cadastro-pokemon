class PokemonDAO():
    def __init__(self, instancia_poke):
        self._pokemon_json = {}
        self.preenche_valores_json(instancia_poke)

    def preenche_valores_json(self, instancia):
        self._pokemon_json['id'] = instancia.id
        self._pokemon_json['name'] = instancia.name
        self._pokemon_json['Type'] = instancia.type
        self._pokemon_json['sex'] = instancia.sex

    def to_json(self):
        return self._pokemon_json

    def __str__(self):
        return str(self._pokemon_json)
#Pokemon