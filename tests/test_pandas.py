from my_utils.pandas import parallelize
import pandas as pd


def func(x):
    return 2 * x + 1


def test_parallelize():
    test_df = pd.DataFrame({"a": range(1000), "b": range(1000)})
    parallelize(test_df["a"], func)
    parallelize(test_df["a"], func, n_jobs=1)
    parallelize(test_df.iloc[0], func)
