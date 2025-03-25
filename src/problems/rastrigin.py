import numpy as np

def rastrigin(x):
  """Rastrigin function

  The Rastrigin function has several local minima. It is highly multimodal, but locations of the minima are regularly distributed.

  Args:
      x (np.ndarray): The input vector

  Returns:
      float: The value of the Rastrigin function
  """

  d = len(x)

  return np.sum(x ** 2 - 10 * np.cos(2 * np.pi * x)) + 10*d

def rastrigin_boundaries(dims):
    """The boundaries for the Rastrigin function

    Args:
        dims (int): The number of dimensions
    
    Returns:
        List[Tuple[float, float]]: The boundaries for the Rastrigin function with 'dims' dimensions
    """
    return [(-5.12, 5.12)] * dims