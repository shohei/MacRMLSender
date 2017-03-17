#!/usr/bin/env python

fout = open('test.gcode','w')

counter = 0
for i in range(5):
    counter += 1
    x = 0
    y = 0 
    z = 10*i
    string = "#{0} G204 X{1} Y{2} Z{3} F100\n".format(counter,x,y,z)
    fout.write(string)   

for i in range(5):
    counter += 1
    x = 0 
    y = 10*i
    z = 0
    string = "#{0} G204 X{1} Y{2} Z{3} F100\n".format(counter,x,y,z)
    fout.write(string)   

for i in range(5):
    counter += 1
    x = 10*i
    y = 0 
    z = 0
    string = "#{0} G204 X{1} Y{2} Z{3} F100\n".format(counter,x,y,z)
    fout.write(string)   

for i in range(5):
    counter += 1
    x = 0
    y = 0 
    z = -10*i
    string = "#{0} G204 X{1} Y{2} Z{3} F100\n".format(counter,x,y,z)
    fout.write(string)   

for i in range(5):
    counter += 1
    x = 0 
    y = -10*i
    z = 0
    string = "#{0} G204 X{1} Y{2} Z{3} F100\n".format(counter,x,y,z)
    fout.write(string)   

for i in range(5):
    counter += 1
    x = -10*i
    y = 0 
    z = 0
    string = "#{0} G204 X{1} Y{2} Z{3} F100\n".format(counter,x,y,z)
    fout.write(string)   

fout.close()
