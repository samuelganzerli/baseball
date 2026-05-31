from model.model import Model

mymodel = Model()

mymodel.getTeamsOfYear(2012)
mymodel.creaGrafo()
nodi, archi = mymodel.getGraphDetails()
print(f"grafo creato! Il grafo ha {nodi} nodi e {archi}, archi")


