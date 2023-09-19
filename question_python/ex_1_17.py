#크기가 1인 벡터(Unit Vector)

x,y,z = 1,2,3

norm = (x**2+y**2+z**2)**0.5
print(norm)

x,y,z = x/norm,y/norm,z/norm
norm = (x**2+y**2+z**2)**0.5
print(norm)