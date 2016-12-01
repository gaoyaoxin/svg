#!/usr/bin/env python
# coding=utf-8





print ("Which element do you want to build?您想创建何种几何元素\n 1 for circle 创建圆，请输入1; 2 for line 创建直线，请输入2\n ; 2 for ???line 创建中垂线，请输入3")

element = int(input())   #用int()将该字符串转化为整数

if element == 1:


    print ("Please input X-axis 横坐标")

    circle_cx = input()

    print ("Please input Y-axis 纵坐标")

    circle_cy = input()


    print ("Please input R 半径")

    circle_r = input()
                            
                            
                            
    print ('<circle cx="'+circle_cx+'\" '+'cy="'+circle_cy+'\" '+'r="'+circle_r+'\" '+'stroke="black" stroke-width="2" fill="transparent"/>')
#<circle cx="200" cy="500" r="200" stroke="black" stroke-width="2" fill="transparent"/>
elif element ==2:

    print ("Please input X1-axis X1横坐标")

    line_x1 = input()

    print ("Please input Y1-axis Y1纵坐标")

    line_y1 = input()

    print ("Please input X2-axis X2横坐标")

    line_x2 = input()

    print ("Please input Y2-axis Y2纵坐标")

    line_y2 = input()
    
    print ('<line x1="'+line_x1+'\" '+'y1="'+line_y1+'\" '+'x2="'+line_x2+'\" '+'y2="'+line_y2+'\" ''stroke="black" stroke-width="2"/>')
#<line x1="0" y1="0" x2="200" y2="200" stroke="black" stroke-width="2"/>


elif element ==2:

    print ("Please input X1-axis X1横坐标")

    line_x1 = input()

    print ("Please input Y1-axis Y1纵坐标")

    line_y1 = input()

    print ("Please input X2-axis X2横坐标")

    line_x2 = input()

    print ("Please input Y2-axis Y2纵坐标")

    line_y2 = input()
    
    print ('<line x1="'+line_x1+'\" '+'y1="'+line_y1+'\" '+'x2="'+line_x2+'\" '+'y2="'+line_y2+'\" ''stroke="black" stroke-width="2"/>')
#<line x1="0" y1="0" x2="200" y2="200" stroke="black" stroke-width="2"/>
#




else:
    print ("We are still working on other elements.")
