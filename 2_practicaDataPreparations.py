import numpy as np
import pandas as pd
dates = pd.date_range('20171001', periods=10)
listA = ['value']
result = pd.DataFrame(np.arange(1,11),index=dates,columns = listA)
print(result)