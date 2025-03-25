import numpy as np

def sphere(x):
  """Sphere function

  The Sphere function has d local minima except for the global one. It is continuous, convex and unimodal.

  Args:
      x (np.ndarray): The input vector

  Returns:
      float: The value of the Rastrigin function
  """

  return np.sum(x ** 2)

def sphere_boundaries(dims):
    """The boundaries for the Sphere function

    Args:
        dims (int): The number of dimensions
    
    Returns:
        List[Tuple[float, float]]: The boundaries for the Sphere function with 'dims' dimensions
    """
    return [(-5.12, 5.12)] * dims