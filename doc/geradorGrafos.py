#! /usr/bin/env python
import sys
import random

random.seed()

def gera(nomeArq, numVert, numTerm):
	
	
  f=open(nomeArq,'w')
  f.write("Nodes "+str(numVert)+"\n")
  f.write("Edges "+str((numVert*(numVert-1))/2)+"\n")
  #Atribui pesos entre 10 e 1000 com probabilidade uniforme para arestas
  for i in range(numVert):
    for j in range(i+1,numVert):
      f.write("E "+str(i+1)+" "+str(j+1)+" "+str(random.randint(10,1000))+"\n")
  f.write("\n")
  f.write("Terminals\n")
  terminals = random.sample(range(1,numVert+1),numTerm)
  for i in terminals:
    f.write("T "+str(i)+"\n")
  f.close()
  



#Entrada nome-arq, numero de vertices, numero de terminais
if(len(sys.argv) != 4):
  print "Entre com\n geradorGrafos nome-arq numero-de-vertices numero-terminais"
else:
  gera(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
