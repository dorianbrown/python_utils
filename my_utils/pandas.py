import numpy as np
from multiprocessing import cpu_count, Pool
import pandas as pd


def parallelize(data, func, n_jobs=cpu_count()):
    data_split = np.array_split(data, n_jobs)
    pool = Pool(n_jobs)
    data = pd.concat(pool.map(func, data_split))
    pool.close()
    pool.join()
    return data

