# wordn
Il programma `wordn` può essere utilizzato per filtrare i dati provenienti dallo stdin. In particolare ti permette di ottenere o rimuovere l'n-sima parola di ogni riga dell input.

Esempi (utilizzando come input `ls -al`):
---

```
ls -al | wordn 3 8 9
```
darà come output
```

stefano 14:04 .
stefano 14:01 ..
stefano 10:31 .idea
stefano 14:20 wordn
```
---

È possibile anche invertire l'ordine delle parole, es:
```
ls -al | wordn 9 1
```
darà come output:
```
totale
. drwxrwxr-x
.. drwxrwxr-x
.idea drwxrwxr-x
wordn -rwxrw-r--
```
---
Per eliminare le parole dall'output:
```
ls -al | wordn -d 3 4
```
avremo:
```
totale 20
drwxrwxr-x 3 4096 lug 25 09:31 .
drwxrwxr-x 11 4096 lug 22 14:01 ..
drwxrwxr-x 2 4096 lug 22 10:31 .idea
-rw-rw-r-- 1 515 lug 25 09:31 README.md
-rwxrw-r-- 1 953 lug 24 14:20 wordn
```
---
Per sapere gli indici delle parole dell'output si può richiamare il programma senza parametri, es:
```
ls -al | wordn
```
darà
```
[1]totale [2]20
[1]drwxrwxr-x [2]3 [3]stefano [4]stefano [5]4096 [6]lug [7]25 [8]09:31 [9].
[1]drwxrwxr-x [2]11 [3]stefano [4]stefano [5]4096 [6]lug [7]22 [8]14:01 [9]..
[1]drwxrwxr-x [2]2 [3]stefano [4]stefano [5]4096 [6]lug [7]22 [8]10:31 [9].idea
[1]-rw-rw-r-- [2]1 [3]stefano [4]stefano [5]827 [6]lug [7]25 [8]09:33 [9]README.md
[1]-rwxrw-r-- [2]1 [3]stefano [4]stefano [5]953 [6]lug [7]24 [8]14:20 [9]wordn
```
