#!/usr/bin/env python
# coding=utf-8





print "Which element do you want to build?您想创建何种几何元素\n 1 for circle 创建圆，请输入1; 2 for line 创建直线，请输入2"

element = int(raw_input())   #通过raw_input()输入的数字是字符串
                            #用int()将该字符串转化为整数

if element == 1:


print "Please input X-axis 横坐标"

cx = raw_input()

print "Please input Y-axis 纵坐标"

cy = raw_input()


print "Please input R 半径"

r = raw_input()
                            
                            
                            
    print ("<circle "cx"=\"cx\" "cy"=\"500\" "r"=\"r\" "stroke"=\"black\" "stroke-width"=\"2\" "fill=\"transparent\"/>")

elif element ==2:
    
    print "We are still working on this elements."
else:
    print "We are still working on other elements."


<
    
