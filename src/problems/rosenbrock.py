import numpy as np

def rosenbrock(x):
    """Rosenbrock function

    The Rosenbrock function, also referred to as the Valley or Banana function, is a popular test problem for gradient-based optimization algorithms.

    The function is unimodal, and the global minimum lies in a narrow, parabolic valley. However, even though this valley is easy to find, convergence to the minimum is difficult (Picheny et al., 2012).


    Args:
        x (np.ndarray): The input vector

    Returns:
        float: The value of the Rosenbrock function
    """
    return np.sum(100.0 * (x[1:] - x[:-1] ** 2.0) ** 2.0 + (1 - x[:-1]) ** 2.0)


def rosen_boundaries(dims):
    """The boundaries for the Rosenbrock function

    Args:
        dims (int): The number of dimensions
    
    Returns:
        List[Tuple[float, float]]: The boundaries for the Rosenbrock function with 'dims' dimensions
    """
    return [(-2.048, 2.048)] * dims