from programma import *

def test_primo_cateto_stringa():
    ''' se viene passata una stringa al primo parametro ci si aspetta una eccezione CatetoError '''
    try:
        ipotenusa('cinque', 3)
    except CatetoError:
        pass
    except Exception as e:
        raise Exception("E' stata lanciata una eccezione diversa da CatetoError:" + str(e))
    else:
        raise Exception("Non è stata lanciata l'eccezione CatetoError")

def test_secondo_cateto_stringa():
    ''' se viene passata una stringa al secondo parametro ci si aspetta una eccezione CatetoError '''
    try:
        ipotenusa(3, 'cinque')
    except CatetoError:
        pass
    except Exception as e:
        raise Exception("E' stata lanciata una eccezione diversa da CatetoError:" + str(e))
    else:
        raise Exception("Non è stata lanciata l'eccezione CatetoError")

def test_cateti_interi():
    ''' ci si aspetta il valore 5.0 '''
    assert ipotenusa(3, 4) == 5.0 , "Il risultato è sbagliato"

def test_cateti_float():
    ''' ci si aspetta il valore 5.0 '''
    assert ipotenusa(3.0, 4.0) == 5.0 , "Il risultato è sbagliato"

def test_cateti_misti1():
    ''' ci si aspetta il valore 5.0 '''
    assert ipotenusa(3  , 4.0) == 5.0 , "Il risultato è sbagliato"

def test_cateti_misti2():
    ''' ci si aspetta il valore 5.0 '''
    assert ipotenusa(3.0, 4  ) == 5.0 , "Il risultato è sbagliato"

