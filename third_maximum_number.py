#leaf value sequence 
px = [1,3, 3, 4, 2]
print('1st time array:  ', px)
px = list(dict.fromkeys(px))
px.sort(reverse=True)
print('px after dict', px)
print('3rd highest:  ', px[2])
