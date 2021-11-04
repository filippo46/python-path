
def noalpha(s):
    '''Ritorna un insieme contenente tutti i caratteri non alfabetici contenuti in s, 
       senza ripetizioni, versione efficiente'''
    caratteri = set(s)				# insieme dei caratteri di s
    return { c for c in caratteri if not c.isalpha() }

def words(s):
    '''Ritorna la lista delle parole contenute nella stringa s'''
    noa = noalpha(s)
    for c in noa:
        s = s.replace(c, ' ')
    return s.split()

def fwords(filename, encoding='utf-8'):
    '''Ritorna la lista di parole contenute nel file filename, 
       aperto con encoding indicato (default 'utf-8')'''
    with open(filename, encoding=encoding) as f:
        text = f.read()
    return words(text)


if __name__ == '__main__':
    def test_noalpha(s):
        print(s)
        ss = ''.join(noalpha(s))
        print('Non alfabetici:', '"'+ss+'"' )
    test_noalpha("""Frase (con parentesi [],{}, simboli vari %&#@), accapo,
    numeri 0987 e puntegg.!""")
    test_noalpha("FraseSenzaCaratteriNonAlfabetici")

    def test_words(s):
        print(s)
        print('words:', words(s))

    s = """def words(s):
    '''Ritorna la lista delle parole contenute nella stringa s'''
    noa = noalpha(s)
    for c in noa:
    s = s.replace(c, ' ')
    return s.split()"""
    test_words(s)
