 
import numpy as np
import random
from utils import add_class

output_el = Element('output').element

arr = np.array([22,58,87,34,5])
# edited out for now
#pyscript.write('output',F"{arr}")
output_el.innerHTML = f"{arr}"

def shuffle_array(*args):
    #Shuffle
    shuffled = sorted(arr, key=lambda k: random.random())

    #change color
    add_class(output_el, "text-blue-500")    
    #pyscript.write('output', shuffled)
    
    output_el.innerHTML = shuffled
    