
import math

class CatetoError( Exception ):			# definiamo un nuovo tipo di errore che eredita da Exception
    pass					# e che non fa nulla di più

def ipotenusa(x, y) :
    if not isinstance(x, (int, float)):				# se x non è un numero
        raise CatetoError("il cateto x non è un numero")	# lancio l'eccezione CatetoError
    if not isinstance(y, (int, float)):				# se y non è un numero
        raise CatetoError("il cateto y non è un numero")	# lancio l'eccezione CatetoError
    return math.sqrt(x*x + y*y )				# altrimenti tutto bene e faccio il calcolo

if __name__ == '__main__':
    print(ipotenusa(2, 56))