import numpy as np
import importlib
from hypothesis import given
import hypothesis.strategies as some

import MyFunctions


@given(some.lists(some.integers(min_value=0)))
def test_list_return_is_sqrt( a_list):
    for i in range (len(a_list)-1):
        arg = float(a_list[i])
        #print (arg )
        root = MyFunctions.mySqrt( arg)
        assert( root>=0 )
        np.testing.assert_approx_equal( root*root , arg, significant=15 )
 

@given(some.lists(some.decimals(min_value=-1e5,max_value=1e5 ,allow_nan=False, allow_infinity=False) ))
def test_list_sin_cos( a_list):
    for i in range (len(a_list)-1):
        arg = float(a_list[i])
        #print (arg )
        cosValue = MyFunctions.myCos( arg)
        sinValue = MyFunctions.mySin( arg)
        assert( cosValue<=1 )
        assert( sinValue<=1 )
        assert( cosValue>=-1 )
        assert( sinValue>=-1 )
        np.testing.assert_approx_equal( cosValue**2 + sinValue**2 , 1.0, significant=15 )
