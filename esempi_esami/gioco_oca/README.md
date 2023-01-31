### Gioco dell'oca
Il **gioco dell’oca** è un gioco in cui i partecipanti, lanciando due dadi e muovendosi di un numero di caselle pari alla somma del
lancio, devono raggiungere l’ultima casella del circuito.

Le **regole** sono le seguenti. I giocatori, a turno lanciano **due dadi**, poi spostano la propria pedina di un numero di caselle pari alla
somma del lancio. Vince chi arriva per primo all’ultima casella con un lancio esatto, terminando il suo movimento sulla casella
63; se un giocatore ottiene un numero più alto di quello necessario per raggiungere l’ultima casella, dopo aver raggiunto la
casella 63 dovrà tornare indietro (e.g, se il giocatore si trova nella casella 59 e i dadi sommano 6, la casella di "arrivo" sarebbe 65
ma la casella finale effettiva diventa 61).

Sul tabellone esistono alcune caselle speciali, elencate di seguito.
* **PRIGIONE**: si rimane fermi per tre turni;
* **SALI**: il giocatore che arriva in questa casella avanza di tre caselle;
* **SCENDI**: il giocatore che arriva in questa casella retrocede di tre caselle; 
* **SCHELETRO**: si torna alla casella 1.

La definizione del tabellone del gioco dell'oca è contenuta in un file tabellone.txt, che contiene le informazioni sulle caselle
speciali, una per riga e nel formato seguente:
    
    COMANDO CASELLA

Dove ***COMANDO*** è una stringa che coincide con uno dei nomi delle caselle speciali elencate in precedenza e ***CASELLA*** è il
numero della casella in cui è posizionata, e le caselle valide vanno da 1 a 62 (la casella 63 è la casella di fine e non può essere
una casella speciale). Si suppone che il formato del file in ingresso sia sempre corretto. I comandi e le caselle possono essere
inseriti in un ordine qualsiasi. Inoltre, è garantito che le caselle di movimento non facciano capitare il giocatore su una nuova
casella speciale.

Si scriva un programma Python per gestire una partita al gioco dell'oca tra il computer e il giocatore umano. Entrambi i giocatori
partono dalla casella 0 (la prima esterna al tabellone), e il giocatore iniziale deve essere scelto in maniera casuale. Il programma,
deve stampare la sequenza di mosse della partita fino alla vittoria di uno dei giocatori, con il seguente formato:
    
    Turno [x]: [giocatore] lancio dadi: [d1] e [d2], casella [casella di arrivo]
    eventuali effetti della casella speciale di arrivo

dove d1 e d2 sono il risultato del lancio di dadi se il giocatore non è bloccato, o l'indicazione che il giocatore è bloccato (e il
numero di turni rimanenti alla fine del blocco):

    Turno [x]: [giocatore] bloccato per [turni rimanenti, incluso quello attuale] turni

Alla fine partita, occorre stampare il nome del giocatore che ha vinto la partita
    
    Ha vinto [giocatore]

## Esempio

### Contenuto del file tabellone.txt
    
    SALI 5
    SALI 58
    PRIGIONE 13
    SALI 12
    SCHELETRO 55
    SCENDI 19
    PRIGIONE 35
    SCENDI 43
    SALI 49
    PRIGIONE 23
    SCENDI 50
    SCENDI 27
    PRIGIONE 47
    PRIGIONE 62

### Esempio di partita
Nel seguito, viene visualizzato **UN possibile esito** della partita (dal momento che il lancio dei dadi avviene in modo casuale, ogni
partita sarà diversa da un'altra). **Per brevità**, alcune righe sono state omesse dalla stampa in output e sostituite (<u>solo per la
visualizzazione nel testo del compito</u>) con i caratteri "[...]".

La vostra soluzione **DEVE** ovviamente riportare l'output completo.

    Turno 1:Giocatore lancio dadi: 1 e 1, casella 2
    Turno 1:Computer lancio dadi: 4 e 5, casella 9
    [...]
    Turno 4:Giocatore lancio dadi: 1 e 2, casella 18
    Turno 4:Computer lancio dadi: 3 e 6, casella 30
    Turno 5:Giocatore lancio dadi: 4 e 1, casella 23
    Sei finito in prigione, rimani bloccato per 3 turni
    Turno 5:Computer lancio dadi: 5 e 3, casella 38
    Turno 6:Giocatore bloccato per 3 turni
    Turno 6:Computer lancio dadi: 2 e 3, casella 43
    Retrocedi fino alla casella 40
    Turno 7:Giocatore bloccato per 2 turni
    Turno 7:Computer lancio dadi: 1 e 2, casella 43
    Retrocedi fino alla casella 40
    [...]
    Turno 10:Giocatore lancio dadi: 2 e 4, casella 46
    Turno 10:Computer lancio dadi: 6 e 2, casella 55
    Hai incontrato lo scheletro, ritorni alla casella di partenza!!!
    [...]
    Turno 16:Computer lancio dadi: 1 e 4, casella 31
    Turno 17:Giocatore lancio dadi: 6 e 2, casella 58
    Avanzi fino alla casella 61
    [...]
    Turno 47:Giocatore lancio dadi: 2 e 1, casella 24
    Turno 47:Computer lancio dadi: 1 e 6, casella 59
    Turno 48:Giocatore lancio dadi: 3 e 2, casella 29
    Turno 48:Computer lancio dadi: 1 e 3, casella 63
    Ha vinto Computer