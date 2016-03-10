def reverseMatrix(width, height, byte):
    # res = []
    for i in range(height):
        byte[i*width:(i+1)*width] = list(reversed(byte[i*width:(i+1)*width]))
        # tmp = byte[i*width:(i+1)*width]
        # print tmp
        # tmp.reverse()
        # res.extend(tmp)
    return byte



print reverseMatrix(3, 2, [1,2,3,4,5,6])