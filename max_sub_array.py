def max_subarray(l,h,li):
    if(l == h):
        return (l,h,li[l])
    m = (l+h)//2
    lst,lend,lmax = max_subarray(l,m,li)
    rst,rend,rmax = max_subarray(m+1,h,li)
    mst,mend,mmax = mid_cross_sub_array(l,m,h,li)
    if(lmax > rmax):
        if(lmax > mmax):
            return (lst,lend,lmax)
        else:
            return (mst,mend,mmax)
    else:
        if(rmax > mmax):
            return (rst,rend,rmax)
        else:
            return (mst,mend,mmax)

def mid_cross_sub_array(l,m,h,li):
    total = li[m]
    lmax = m
    lsum = li[m]
    for i in range(m-1,l-1,-1):
        total += li[i]
        if(total > lsum):
            lsum = total
            lmax = i
    total = li[m+1]
    rmax = m+1
    rsum = li[m+1]
    for i in range(m+2,h+1):
        total += li[i]
        if(total > rsum):
            rsum = total
            rmax = i

    return (lmax,rmax,lsum+rsum)

if __name__ == "__main__":
    n = int(input())
    li = list(map(int,input().split()))
    s_index,e_index,total = max_subarray(0,n-1,li)
    print(s_index,e_index,total)