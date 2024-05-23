# import colorgram
# import turtle
# def color_extraction(num_of_colors):
#
#     colors = colorgram.extract('spot_painting.jpg', num_of_colors)
#
#     def extract_colors_list(num_of_colors):
#         ext_color_set = []
#         for i in range(num_of_colors):   # >>> 'colors'가 리스트 데이터이므로, for color in colors: 로 작성해도 됨.
#             single_color = colors[i].rgb
#
#             single_r = single_color[0]
#             single_g = single_color[1]
#             single_b = single_color[2]
#             single_tuple = [(single_r, single_g, single_b)]
#
#             ext_color_set.append(single_tuple)  #>>> 리스트에 데이터를 추가할 때는 += 연산자보다는 .append() 이용을!
#         return ext_color_set
#
#     print(extract_colors_list(num_of_colors))
#
# color_extraction(30)

# # rgb로 변환하는 방법을 문서에서 잘 찾아 읽어보면 아래와 같은 방법이 가능하다 (color object에 .rgb를 추가하면 rgb 색상값으로 변환 가능)
#
# colors = colorgram.extract('spot_painting.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     # rgb_colors.append(color.rgb)
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     rgb_tuple = (r, g, b)
#     rgb_colors.append(rgb_tuple)
# print(rgb_colors)


import turtle as t
import random

color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5),
              (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49),
              (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111),
              (229, 165, 8),
              (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62),
              (5, 38, 33), (68, 219, 155)]

timmy = t.Turtle()
timmy.speed("fastest")
turtle.colormode(255)
timmy.hideturtle()
timmy.penup()
for row in range(10):
    timmy.setposition(x= -200.00, y= -200.00 + (50 * row))
    for i in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)


screen = t.Screen()
screen.exitonclick()



