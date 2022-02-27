def dekorator_fuggveny(dekoralando_fuggveny):
    def tenyleges_funkcionalitas():
        print("Fuggvenyhivas elott vagyunk")

        # meghivjuk
        return_val = dekoralando_fuggveny

        print("Fuggvenyhivas utan vagyunk")
        return return_val
    return tenyleges_funkcionalitas()


@dekorator_fuggveny
def dekoralni_kivant_fuggveny(bemenet: int):

    return bemenet + 1


print(dekoralni_kivant_fuggveny(1))
