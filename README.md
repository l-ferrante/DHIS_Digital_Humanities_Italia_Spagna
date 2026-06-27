**DHIS - Digital Humanities tra Italia e Spagna**
*Progetto di Data Journalism a.a. 2025/26*
Lorenzo Ferrante e Saverio Solimani

Il progetto è consistito in un'analisi temporale dei progetti di Digital Humanities realizzati in Italia e in Spagna negli ultimi 30 anni, tramite canali di finanziamento pubblici, prendendo come riferimenti principali i dataset non aggregati *Italian Digital Humanities Projects* (https://zenodo.org/records/19003595) e *Mapping digital humanities projects in Spain - 1993-2019* (https://zenodo.org/records/3893546).

Per quanto riguarda l'Italia, è stato ritenuto utile un confronto fra i progetti DH (estratti fra i progetti risultati vincitori nei settori SH) dei bandi ministeriali PRIN 2022 e PRIN 2022 PNRR, per verificare l'impatto del PNRR sul finanziamento alla ricerca DH. Di seguito una breve spiegazione di come sono stati ottenuti questi dati.

**PRIN 2022 - Scraping**

Sul sito del *Ministero dell'Università e della Ricerca* sono disponibili pubblicamente i *Decreti di ammissione al finanziamento* sia per quanto riguarda il bando **PRIN 2022** che per quanto riguarda il bando **PRIN PNRR 2022**.

Se per questi ultimi si è proceduto a uno scraping, per così dire, manuale, i primi sono stati convertiti in markdown (.md), formato che ha mantenuto la struttura del file come tabelle in formato "html-like": è stato quindi possibile fare scraping sfruttando **playgroubd** e un piccolo server web in locale.
Lo scraping ha raccolto più di **1000 progetti** nei settori SH da 1 a 7.


**PRIN 2022 - Filtraggio**

Questi progetti sono poi stati **filtrati** tramite un sistema di **parole chiave** tipiche delle DH.
