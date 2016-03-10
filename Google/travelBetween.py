def travelBetween(ca, nc):
    in_ca, in_nc, out_ca, out_nc = ca[0], nc[0], 0, 0
    for i in range(1,len(ca)):
        in_ca, in_nc, out_ca, out_nc = max(in_ca+ca[i], out_nc+ca[i]), max(in_nc+nc[i], out_ca+nc[i]), in_ca, in_nc
    return max(in_ca, in_nc)


ca = [1,2,3,6,7,3,2,7]
nc = [3,5,2,1,7,4,2,3]

print sum(ca), sum(nc)
print travelBetween(ca, nc)