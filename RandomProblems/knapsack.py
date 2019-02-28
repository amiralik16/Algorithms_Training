from collections import defaultdict

def ksnaive(n,wmax):
    if n==-1 or wmax==0:
        return 0
    elif warr[n]>wmax:
        return ksnaive(n-1,wmax)
    else:
        return max(arr[n]+ksnaive(n-1,wmax-warr[n]),ksnaive(n-1,wmax))
    # return result


def ksnaive_helper(arr,warr,wmax):
    return ksnaive(len(arr)-1,wmax)

def ksnaive_m(n,wmax,m):
    if m[n][wmax]:
        return m[n][wmax]
    if n==-1 or wmax==0:
        return 0
    elif warr[n]>wmax:
        m[n][wmax] = ksnaive_m(n-1,wmax, m)
        return m[n][wmax]
    else:
        m[n][wmax] = max(arr[n]+ksnaive_m(n-1,wmax-warr[n],m),ksnaive_m(n-1,wmax,m))
        return m[n][wmax]

def ksnaive_m_helper(arr,warr,wmax):
    m = defaultdict(lambda: defaultdict(int))
    return ksnaive_m(len(arr)-1,wmax,m)

def ks_bottom_up(arr,warr,wmax):
    m = [[[None] for x in range(len(arr)+1)] for i in range(wmax + 1)]
    for i in range(len(arr)+1):
        for j in range(wmax+1):
            if i==0 or j == 0:
                m[j][i] = 0
            elif warr[i-1]>j:
                m[j][i] = m[j][i-1]
            else:
                m[j][i] = max(m[j][i-1],arr[i-1] + m[j-warr[i-1]][i-1])
    return m[j][i]

if __name__ == "__main__":
    arr = [60,100,120]
    warr = [10,20,30]
    wmax = 50
    print(ksnaive_m_helper(arr,warr,wmax))
    print(ks_bottom_up(arr,warr,wmax))