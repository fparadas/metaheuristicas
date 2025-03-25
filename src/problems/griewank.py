import numpy as np

def griewank(x):
  """Griewank function

  The Griewank function has many widespread local minima, which are regularly distributed.

  Args:
      x (np.ndarray): The input vector

  Returns:
      float: The value of the Rastrigin function
  """
  return np.sum(x ** 2) / 4000 - np.prod(np.cos(x / np.sqrt(np.arange(1, len(x) + 1)))) + 1

def griewank_boundaries(dims):
    """The boundaries for the Griewank function

    Args:
        dims (int): The number of dimensions
    
    Returns:
        List[Tuple[float, float]]: The boundaries for the Griewank function with 'dims' dimensions
    """
    return [(-600, 600)] * dims