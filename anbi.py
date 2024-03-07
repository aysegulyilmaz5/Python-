
#First Approach
import animal
import bird

obj1 = animal.Animal()
obj1.display()

obj2=bird.Bird()
obj2.display()

#Second Approach
from animal import Animal
from bird import Bird

obj1= Animal()
obj1.display()

obj2=Bird()
obj2.display()
