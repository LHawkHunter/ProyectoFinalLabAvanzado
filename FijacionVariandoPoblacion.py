import numpy as np
import matplotlib.pyplot as plt


def moran(N,i,r):

    populationINI = [0 for _ in range(i)] + [1 for _ in range(N - i)]
    population=populationINI
    counts = [(population.count(0), population.count(1))]
    a=int(population.count(0))-int(population.count(1))
    while len(set(population))==2 and abs(a)<=N*0.60: #el proceso que sigue se repetira,
        G = np.random.rand()#genera un número aleatorio entre 0 y 1
        pBirth=[r*i/(r*i+N-i)]+[(N-i)/(r*i+N-i)] #vector probabilidad, de a y b
        Birth=np.random.randint(N) 
        Death=np.random.randint(N)
        a=int(population.count(0))-int(population.count(1))

        if Birth != Death: #aqui considero que la posicion del que nace y del que muere es distinta
            if G <=pBirth[0]: 
                if population[Birth]==0 and population[Death]==1: #Añado las dos condiciones anteriores,
                #porque se deben cumplir ambas
                    population[Death] = population[Birth]
                    i=i+1
                else:
                    if population[Birth]==0 and population[Death]==0:
                        population[Death] = population[Birth]
                    #print('seg')
                    #print(pBirth)          
            else:                
                if population[Birth]==1 and population[Death]==0:
                    population[Death] = population[Birth]#aqui tambien se deben cumplir ambas
                    i=i-1
                #print('ter')
                #print(pBirth)
                else:
                    if population[Birth]==1 and population[Death]==1:
                        population[Death] = population[Birth]
        else:
            pass
            #print('no change')
            
                
        counts.append((population.count(0), population.count(1)))

#    plt.plot(counts)
#    plt.savefig("Moran1b.png",bbox_inches='tight')
    
    return [population,counts]




def fijacion(n):
    x=0
    for j in range(n):
        population,counts=moran(100,25,1.1)
        #print(population)
        a=np.array(counts)
        plt.plot(a[:,0], color='green')
        plt.plot(a[:,1], color='blue')
        if population[0]==1:
            x=x+1
    plt.savefig("pruebatreshold100.png",bbox_inches='tight')
    
#    print(a,counts,a[:,0])
#    type(counts)
    return x

fijacion(20)

#la siguiente función nos brinda la veces en las cuales la población 1 gana.
#def fijacion(n,ii):
#    x=0
#    for j in range(n):
#        population,counts=moran(50,ii,1.1)
#        #print(population)
##        a=np.array(counts)
##        plt.plot(a[:,0], color='green')
##        plt.plot(a[:,1], color='blue')
#        if population[0]==1:
#            x=x+1
##    plt.savefig("nVeces.png",bbox_inches='tight')
#    
##    print(a,counts,a[:,0])
##    type(counts)
#    return x

#print(fijacion(10))

#def cerosVsfij(n,T):
#    counts2 = []
#    for p in range(T):
#        counts2.append((p,fijacion(n,p)))
#    gra=np.array(counts2)
#    plt.plot(gra[:,0], 1-gra[:,1]/n, 'o',color='green')
#    plt.plot(gra[:,0], gra[:,1]/n, 'o',color='blue')
#    plt.savefig("ceros_iniVsFijacion.png",bbox_inches='tight')
#    print(gra)
#    #plt.figure()
##    plt.plot(gra)
#    return counts2
#        
#cerosVsfij(200,50)      



#plt.show()
##plt.xlabel('Pasos',fontdict = font)
##plt.ylabel('Población',fontdict = font, labelpad = 10)
###plt.legend()
##plt.savefig("Nacimiento.pdf",bbox_inches='tight')
##
