from Face import Face
import json

class Carta():
    def __init__(self, frente: Face) -> None:
        self.__frente = frente

    def getFrente(self) -> Face:
        return self.__frente

    def to_json(self) -> dict:
        a =  json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        json_acceptable_string = a.replace("'", "\"")
        json_ = json.loads(json_acceptable_string)
        return json_
    