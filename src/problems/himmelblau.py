import numpy as np

def himmelblau(x, y):
  """Himmelblau function

  The Himmelblau function has four local minima.

  Args:
      x float: The x value
      y float: The y value

  Returns:
      float: The value of the Himmelblau function
  """

  return (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2

def himmelblau_boundaries():
    """The boundaries for the Himmelblau function

    Args:
        dims (int): The number of dimensions
    
    Returns:
        List[Tuple[float, float]]: The boundaries for the Himmelblau function
    """

    return [(-5, 5)]*2
