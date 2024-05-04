import copy


class Model:
    def __init__(self):
        #variabile di istanza che contiene risultato finale (in sto caso raccolta di parziali finali distinti)
        self._listaParzialiFinali = []

    def applicaMetodoRicorsivo(self,dimensioneLato):

        #pulisco variabile di istanza da eventuali precedente utilizzo del metodo ricorsivo che vi avevano salvato sue soluzioni
        self._listaParzialiFinali.clear()

        #creo tabella nxn che sarà inidicazione dei posti disponibili inizialialmente (tutti ovviamente all'inizio) e
        #andrà come parametro al metodo ricorsivo
        scacchiera = []
        riga = []
        for i in range(dimensioneLato):
            riga.append("libera")
        for i in range(dimensioneLato):
            scacchiera.append(riga)


        #applico metodo ricorsivo con un parziale iniziale pari a 0
        self.metodoRicorsivo(0,scacchiera)

        #ora la variabile d'istanza stata aggiornata quindi:
        if max(self._listaParzialiFinali) < dimensioneLato:
            print(f"non è possibile inserire {dimensioneLato} regine in una scacchiera {dimensioneLato}x{dimensioneLato} senza che si possano mangiare a vicenda")
            return False
        else:
            print(f"è possibile inserire {dimensioneLato} regine in una scacchiera {dimensioneLato}x{dimensioneLato} senza che si possano mangiare a vicenda")
            return True

    def metodoRicorsivo(self, parziale,scacchiera):
        #dove parziale è numero regine messe su scacchiera ad una certa leaf (su un certo livello su una certa linea temporale)
        #(ogni volta che si entra nell'esle quel valore andrà aumentato di uno e fornito aggiornato al metodo di ricorsione sucessivo

        if len(self.getInsiemePostiDisponili(scacchiera))==0:
            #entrati nell'if quindi parziale non si aggiornerà piu, è un parziale finale della linea temporale sua e quindi
            #lo aggiungo a soluzione totale che in sto caso è una lista di parziali finali
            self._listaParzialiFinali.append(parziale)
            return
        else:
            postiDisponibili=self.getInsiemePostiDisponili(scacchiera)
            for tupla in postiDisponibili:
                #conservo copia di lista di liste scacchiera del livello di ricorsione corrente per il backtrack alla fine
                scacchieraPerBackTrack=copy.deepcopy(scacchiera)

                #vado quindi a aggiornare lista di liste scacchiera che è parametro per il metodo (livello) ricorsivo
                # seguente su stessa linea temporale e anche parametro di riferimento per
                #l'if di fine di quel metodo appunto  (andra ovviamente inserita aggionrata come parametro del seguente
                #metodo ricorsivo ma ne va tenuta copia per il backtrak dopo l'applicazione dell'altro metodo
                #per riportare valore della variabile input del metodo del livello corrente a quello del livello corrente appunto)
                scacchiera[tupla[0]][tupla[1]]='nonDisponibile'
                postiDisponibili.discard(tupla)
                k=0
                j=0
                while k <= len(scacchiera) and k>=0 and j<= len(scacchiera) and j>=0:
                    k=tupla[0]+1
                    j=tupla[1]+1
                    scacchiera[k][j] = 'nonDisponibile'
                    postiDisponibili.discard((k,j))
                while k <= len(scacchiera) and k>=0 and j<= len(scacchiera) and j>=0:
                    k=tupla[0]+1
                    j=tupla[1]-1
                    scacchiera[k][j] = 'nonDisponibile'
                    postiDisponibili.discard((k,j))
                while k <= len(scacchiera) and k >= 0 and j <= len(scacchiera) and j >= 0:
                    k = tupla[0] - 1
                    j = tupla[1] - 1
                    scacchiera[k][j] = 'nonDisponibile'
                    postiDisponibili.discard((k, j))
                while k <= len(scacchiera) and k>=0 and j<= len(scacchiera) and j>=0:
                    k=tupla[0]-1
                    j=tupla[1]+1
                    scacchiera[k][j] = 'nonDisponibile'
                    postiDisponibili.discard((k,j))
                while k <= len(scacchiera) and k>=0 and j<= len(scacchiera) and j>=0:
                    k=tupla[0]+1
                    j=tupla[1]
                    scacchiera[k][j] = 'nonDisponibile'
                    postiDisponibili.discard((k,j))
                while k <= len(scacchiera) and k >= 0 and j <= len(scacchiera) and j >= 0:
                    k = tupla[0] + 1
                    j = tupla[1]
                    scacchiera[k][j] = 'nonDisponibile'
                    postiDisponibili.discard((k, j))
                while k <= len(scacchiera) and k>=0 and j<= len(scacchiera) and j>=0:
                    k=tupla[0]-1
                    j=tupla[1]
                    scacchiera[k][j] = 'nonDisponibile'
                    postiDisponibili.discard((k,j))
                while k <= len(scacchiera) and k>=0 and j<= len(scacchiera) and j>=0:
                    k=tupla[0]
                    j=tupla[1]+1
                    scacchiera[k][j] = 'nonDisponibile'
                    postiDisponibili.discard((k,j))
                while k <= len(scacchiera) and k>=0 and j<= len(scacchiera) and j>=0:
                    k=tupla[0]
                    j=tupla[1]-1
                    scacchiera[k][j] = 'nonDisponibile'
                    postiDisponibili.discard((k,j))

                #aggiorno il parziale aggiungendo uno (dato che siamo entrati nell'else significa che ho potuto
                #aggiungere e aggiunto nuova regina sulla scacchiera); andrà dato come parametro al seguente metodo ricorsivo come aggiornato
                #essendo un parziale della ricorsione su una certa linea temporale
                parziale=parziale+1

                #lancio metodo ricorsione sucessivo
                self.metodoRicorsivo(parziale,scacchiera)

                #backtrack
                scacchiera= scacchieraPerBackTrack




        return


    def getInsiemePostiDisponili(self,tabella):
        insiemePostiDisponibili=set()
        for i in range(len(tabella)):
            for j in range(len(tabella)):
                if tabella[i][j]=='libera':
                    insiemePostiDisponibili.add( (i,j) )
        return insiemePostiDisponibili


if __name__ == '__main__':
    model=Model()
    print(model.applicaMetodoRicorsivo(6))