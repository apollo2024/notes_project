from Data import Data
from Interface import Interface

file = "data.json"
base = Data(file)
user = Interface(base)
while user.userHere:
    user.start()
base.saveDatabase(file)