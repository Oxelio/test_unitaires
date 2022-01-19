class Calcul:
    
    def add(self, nbr1, nbr2):
            try:
                return nbr1 + nbr2
            except TypeError as error:
                return error
