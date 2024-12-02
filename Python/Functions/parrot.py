class Parrot():
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age

woo=Parrot('Woo',15 )
blu=Parrot('Blu',10)
 
print("Woo is a {}.".format(Parrot.species) )
print("Blu is also a {}.".format(blu.species) )
print("{} is a parrot.".format(woo.name))
print("{} is also a parrot.".format(blu.name))
print("Blu is {} years old.".format(blu.age))
print("Woo is {} years old.".format(woo.age))

    
