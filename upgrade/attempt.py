from . import upgradeData
import numpy as np

def try_pm(item, start = 0,  end = 9, k = 1000):

    item = item.lower()

    if item not in upgradeData: 
        print("Item {item} not found")
        return None
    probas = upgradeData[item]
    if(start < 0 or end > len(probas) or end <= start or start > len(probas)):
        print("Invalid start or end")
        return None
    
    # compute the probability distribution of getting item from level start to end after n tries
    # use deep programming to avoid recomputing the same values

    probas = probas[start:end]

    n = len(probas)+1
    dp = np.zeros((n, n))
    dp[0][0] = 1

    dp = np.zeros((n, n))
    for i in range(n - 1):
        dp[i, i] = 1 - probas[i]
        dp[i, i + 1] = probas[i]
    dp[n - 1, n - 1] = 1.0 

    mat = np.linalg.matrix_power(dp, k)
    
    # probability distribution:
    pdf = mat[0] # pdf[i] = probability of getting item at level i
    cdf = np.cumsum(pdf) # cdf[i] = probability of getting item at level <= i

    cdf =  [1 - cdf[i] for i in range(len(cdf))]

    # pad for outside start end
    pdf = np.pad(pdf, (start, len(probas) - end), 'constant')
    cdf = np.pad(cdf, (start, len(probas) - end), 'constant')

    return pdf, cdf