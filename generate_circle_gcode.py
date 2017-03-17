#!/usr/bin/env python

fout = open('test.gcode','w')
#!/usr/bin/env python
import math

thetas = sorted(map(lambda x: 360.0/(x+1),range(10)))

r = 100

xs = [r*math.cos(theta) for theta in thetas] 
ys = [r*math.sin(theta) for theta in thetas] 
coords = zip(xs,ys)

counter = 0
for c in coords:
    x = c[0]
    y = c[1] 
    z = 0
    string = "#{0} G204 X{1} Y{2} Z{3} F100\n".format(counter,x,y,z)
    fout.write(string)   
    counter+=1

fout.close()
