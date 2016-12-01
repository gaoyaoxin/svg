#!/usr/bin/env python
# coding=utf-8





print ("Which element do you want to build?您想创建何种几何元素\n1 for circle 创建圆，请输入1\n2 for line 创建直线，请输入2\n3 for perpendicular bisector 创建中垂线，请输入3")

element = float(input())   #用float()将该字符串转化为浮点数

if element == 1:


    print ("Please input X-axis 横坐标")

    circle_cx = str(float(input()))

    print ("Please input Y-axis 纵坐标")

    circle_cy = str(float(input()))


    print ("Please input R 半径")

    circle_r = str(float(input()))
                            
                            
                            
    print ('<circle cx="'+circle_cx+'\" '+'cy="'+circle_cy+'\" '+'r="'+circle_r+'\" '+'stroke="black" stroke-width="2" fill="transparent"/>')
#<circle cx="200" cy="500" r="200" stroke="black" stroke-width="2" fill="transparent"/>
elif element ==2:

    print ("Please input X1-axis X1横坐标")

    line_x1 = str(float(input()))

    print ("Please input Y1-axis Y1纵坐标")

    line_y1 = str(float(input()))

    print ("Please input X2-axis X2横坐标")

    line_x2 = str(float(input()))

    print ("Please input Y2-axis Y2纵坐标")

    line_y2 = str(float(input()))
    
    print ('<line x1="'+line_x1+'\" '+'y1="'+line_y1+'\" '+'x2="'+line_x2+'\" '+'y2="'+line_y2+'\" ''stroke="black" stroke-width="2"/>')
#<line x1="0" y1="0" x2="200" y2="200" stroke="black" stroke-width="2"/>



elif element ==3:

    print ("Please input X1-axis X1横坐标")

    line_x1 = float(input())

    print ("Please input Y1-axis Y1纵坐标")

    line_y1 = float(input())

    print ("Please input X2-axis X2横坐标")

    line_x2 = float(input())

    print ("Please input Y2-axis Y2纵坐标")

    line_y2 = float(input())

    if line_x1==line_x2:
        newline_x1=str(0.5*(line_x1+line_x2))
        newline_y1=str(0.5*(line_y1+line_y2))
        #this is the mid point
        newline_x2=str(0.5*(line_x1+line_x2)+1)
        #-1会超出画布范围 改为+1
        newline_y2=str(0.5*(line_y1+line_y2))
    
    elif line_y1==line_y2:
        newline_x1=str(0.5*(line_x1+line_x2))
        newline_y1=str(0.5*(line_y1+line_y2))
        #this is the mid point
        newline_x2=str(0.5*(line_x1+line_x2))
        newline_y2=str(0.5*(line_y1+line_y2)+1)
        #-1会超出画布范围 改为+1
    
    else:
        newline_x1=str(0.5*(line_x1+line_x2))
        newline_y1=str(0.5*(line_y1+line_y2))
        #this is the mid point
        newline_x2=666
        newline_y2=777
    print ('<line x1="'+newline_x1+'\" '+'y1="'+newline_y1+'\" '+'x2="'+newline_x2+'\" '+'y2="'+newline_y2+'\" ''stroke="black" stroke-width="2"/>')
    
#<line x1="0" y1="0" x2="200" y2="200" stroke="black" stroke-width="2"/>





else:
    print ("We are still working on other elements.")
#现在画出来都是线段而不是直线
