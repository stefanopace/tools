# _Curl-o-Matic_

creare una directory chiamata `test-data`, al suo interno creare le directory `requests` e `responses`.  
All'interno di `requests` creare un file con estensione `.curl` contenente un comando curl del quale si vuole verificare che il contenuto della risposta non cambi. (Se ne può inserire anche più di uno)

Una volta inseriti tutti i file `.curl` lanciare il comando `python3 curl-o-matic.py fix` per salvare le risposte delle curl nella directory `responses`.

Lanciando il comando `python3 curl-o-matic.py` verranno rieseguite tutte le curl e controllato che il risultato sia lo stesso di quello contenuto nelle risposte salvate in precedenza.