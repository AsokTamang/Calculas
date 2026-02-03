import jax.numpy as jnp
from jax import vmap,grad

x_array_jnp = jnp.array([1.,2.,3.])
b = jnp.array([1,2,3,4])
type(b)
b = b.astype('float32')  #inorder for the operations and calculations we are converting the type of b into float
print(b)
b[1] = 5  #this will cause an error cause we cannot change the value at the particular index directly
#so we use .at
b.at[1].set(5)  #changing the value at index 1
