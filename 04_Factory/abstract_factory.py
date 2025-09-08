from abc import ABCMeta, abstractmethod

####
# AbstractFactory
class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def criar_pizza_veg(self):
        pass

    @abstractmethod
    def criar_pizza(self):
        pass

# ConcreteFactoryA
class PizzaBrasileira(PizzaFactory):
    
    def criar_pizza_veg(self):
        return PizzaMandioca()

    def criar_pizza(self):
        return PizzaCamarao()

# ConcreteFactoryB
class PizzaItaliana(PizzaFactory):
    
    def criar_pizza_veg(self):
        return PizzaBrocoli()

    def criar_pizza(self):
        return PizzaPepperoni()

#####
# AbstractProductA
class PizzaVeg(metaclass=ABCMeta):

    @abstractmethod
    def preparar(self):
        pass

# AbstractProductB
class Pizza(metaclass=ABCMeta):

    @abstractmethod
    def servir(self, PizzaVeg):
        pass

# ConcreteProduct
class PizzaMandioca(PizzaVeg):

    def preparar(self):
        print(f'Preparando {type(self).__name__}')

class PizzaCamarao(Pizza):

    def servir(self, PizzaVeg):
        print(f'{type(self).__name__} é servida com camarão na {type(PizzaVeg).__name__}')

class PizzaBrocoli(PizzaVeg):

    def preparar(self):
        print(f'Preparando {type(self).__name__}')

class PizzaPepperoni(Pizza):

    def servir(self, PizzaVeg):
        print(f'{type(self).__name__} é servida com pepperoni na {type(PizzaVeg).__name__}')

#####

# client
class Pizzaria:

    def fazer_pizzas(self):
        for factory in [PizzaBrasileira(), PizzaItaliana()]:
            self.factory = factory
            self.pizza = self.factory.criar_pizza()
            self.pizza_veg = self.factory.criar_pizza_veg()
            self.pizza_veg.preparar()
            self.pizza.servir(self.pizza_veg)

pizzaria = Pizzaria()
pizzaria.fazer_pizzas()

