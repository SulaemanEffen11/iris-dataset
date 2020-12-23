import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
# Matplot Lib
import matplotlib.pyplot as plt
import seaborn as sns
# Sklearn Libraries
from sklearn.model_selection import train_test_split

ecoli_df = pd.read_csv("/kaggle/input/ecoli-uci-dataset/ecoli.csv")

ecoli_df.head()
