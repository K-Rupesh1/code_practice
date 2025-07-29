import colorgram

colors = colorgram.extract('colorgram_module\image.jpg', 35)

for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    print(new_color)

'''colors_list=[Rgb(r=226, g=231, b=236)
Rgb(r=58, g=106, b=148)
Rgb(r=224, g=200, b=109)
Rgb(r=134, g=84, b=58)
Rgb(r=223, g=138, b=62)
Rgb(r=196, g=145, b=171)
Rgb(r=234, g=226, b=204)
Rgb(r=224, g=234, b=230)
Rgb(r=141, g=178, b=204)
Rgb(r=139, g=82, b=105)
Rgb(r=209, g=90, b=69)
Rgb(r=188, g=80, b=120)
Rgb(r=68, g=105, b=90)
Rgb(r=237, g=225, b=233)
Rgb(r=134, g=182, b=136)
Rgb(r=133, g=133, b=74)
Rgb(r=63, g=156, b=92)
Rgb(r=48, g=156, b=194)
Rgb(r=183, g=192, b=201)
Rgb(r=214, g=177, b=191)
Rgb(r=19, g=57, b=93)
Rgb(r=21, g=68, b=113)
Rgb(r=112, g=123, b=149)
Rgb(r=229, g=174, b=165)
Rgb(r=172, g=203, b=182)
Rgb(r=158, g=205, b=215)
Rgb(r=69, g=58, b=47)
Rgb(r=108, g=47, b=60)
Rgb(r=53, g=70, b=65)
Rgb(r=72, g=64, b=53)
Rgb(r=134, g=42, b=38)
Rgb(r=47, g=66, b=61)
Rgb(r=0, g=122, b=125)]'''

