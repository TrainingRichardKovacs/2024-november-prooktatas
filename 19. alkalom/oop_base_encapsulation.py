"""
Encapsulation - Egységbezárás

Minden, az objektumhoz tartozó metódus, változó és egyéb attributum legyen private addig
amíg nem akarom publikusság tenni az adott attributumot.

private - csak az osztályon belül lehet elérni, módosítani
public - az osztályon belül és kívül is lehet elérni és módosítani

protected - 


class classname() {

    construktor (){
    
        private int valtozo = 10;
        public int valtozo2 = 20;
    }
}


"""

class Test:

    def __init__(self):
        # ez public instance változó
        self.test_val = "almafa"

        # ez a private instance változó
        self.__price = 10_000

    ##### not good, but works #####
    def get_price(self):
        return self.__price
    
    def set_price(self, value):
        self.__price = value
        return self.__price    
    ##### not good, but works #####

    #### better, but still not the best ####
    def __get_price(self):
        return self.__price

    def __set_price(self, value):
        self.__price = value
        return self.__price
    
    price = property(__get_price, __set_price)

    #### better, but still not the best ####

    #### the best of all setter / getter solution ####
    @property
    def price_2(self):
        ...

    @price_2.getter
    def price_2(self):
        return self.__price
    
    @price_2.setter
    def price_2(self, value):
        self.__price = value
        return self.__price

    #### the best of all setter / getter solution ####


test = Test()

test._Test__price = 21_000

print(test._Test__price)

print(test.get_price())