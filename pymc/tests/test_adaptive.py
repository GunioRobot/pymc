"""Test AdaptiveMetropolis."""
import pymc
import numpy as np
from numpy.testing import *
import nose, warnings

def test_square():
    iw = pymc.InverseWishart("A", n = 2, C = np.eye(2))
    mnc = pymc.MvNormalCov("v", mu = np.zeros(2), C = iw, value = np.zeros(2), observed = True)

    M = pymc.MCMC([iw, mnc])
    M.sample(8, progress_bar=0)



if __name__ == '__main__':
    with warnings.catch_warnings():
        warnings.simplefilter('ignore',  FutureWarning)
        nose.runmodule()
