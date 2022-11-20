In diesem Projekt geht es um ein Wörterbuc, welches sehr zuverlässig
und ausführlich werden soll. Fällt euch also auf dass ein Wort fehlt
oder falsch eingetragen wurde, könnt ihr euch gerne bei mir melden
In der words.json sind folgende Wörter / Namen aufgelistet:

- Firmennamem
- Vornamen
- Nachnamen
- Städte
- Nomen
- Verben
- Adjective
- Adverben

Diese Liste ist nicht KOMPLETT! Falls Wörter fehlen oder falsch eingedragen sind, dann meldet es gerne.
Des weiteren findet ihr ein Python Modul mit dem die Liste nach Wörtern durchsucht werden kann.

from WordClassificator.py import WordClassification

wc = WordClassification()       # Lädt die words.json File mit dem argument path="/path/to/words.json" kann man den Speicherort angeben

wc.classificate('Bauman')       # Gibt die Kategorie zurück in der das Wort gefunden wurde. Falls das Wort in der liste nicht existiert kommt ein False zurück

wc.classificate_sentence('Ein beliebiger Satz')         # Gibt eine Litse mit Tupels zurück in denen sich das Wort und die jeweilige Kategorie befindet. Beispiel: [('Bauman', 'nachname'), ...]

wc.get('Ein beliebiger Satz', type='Kategorie', types=['Kategorien', ...], max_results=1)         # Filtert einen Satz nach einer Bestimmten Kategorie.
                                                                                                  # Mit type oder types können eine oder mehrere Wörter mit den entsprechenden Kategorien zurückgegeben werden.
                                                                                                  # Mit max_results kann eine Anzahl von Wörtern pro Kategorie angegeben werden. Andere Wörter in der Selben Kategorie werden Ignoriert.
