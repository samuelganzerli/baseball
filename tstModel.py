from model.model import Model

mymodel = Model()

mymodel._getTeamsOfYear(2012)
mymodel.creaGrafo(2012)
nodi, archi = mymodel.getGraphDetails()
print(f"grafo creato! Il grafo ha {nodi} nodi e {archi}, archi")


