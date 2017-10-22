import json

class Config:
    def __init__(self, id_, config_file=""):
        self.id = id_
        self._config = json.load(open(config_file, "r"))
    def get_token(self):
        return self._config["connection"]["token"]
    def get_version(self):
        return self._config["bot"]["version"]

