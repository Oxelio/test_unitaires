class FizzBuzz:
    
    def fizzBuzz(self, param = 15):
        liste = []
        for i in range(1,param+1):
            if not i%15 :
                liste.append("fizzbuzz")
            elif not i%5 :
                liste.append("buzz")
            elif not i%3:
                liste.append("fizz")
            else:
                liste.append(i)
        return liste
    