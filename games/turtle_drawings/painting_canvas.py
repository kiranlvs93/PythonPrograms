from my_turtle import MyTurtle


# kiddo = MyTurtle()
# kiddo.draw_square()

# draw dashed line
# for _ in range(15):
#     kiddo.draw_dashed_line(10)

# Draw shapes from triangle to decagon
# for no_of_sides in range(3, 11):
#     kiddo.draw_shape(no_of_sides)

# Random walk a specific number of times
# kiddo.random_walk('fastest', 150)

# Random walk a specific number of times with random rgb colors
# kiddo = MyTurtle(pen_size=5, screen_color_mode=255)
# kiddo.random_walk_rgb('fastest', 150)


# Draw a Spirograph
# kiddo = MyTurtle(pen_size=3, screen_color_mode=255, speed='fastest')
# kiddo.draw_spirograph(radius=100, gap_size=20)

# Draw a Hirst painting
kiddo = MyTurtle(pen_size=5, screen_color_mode=255, speed='fastest')
kiddo.hirst_painting(20)
kiddo.close_screen()
