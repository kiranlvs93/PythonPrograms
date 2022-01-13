from my_turtle import MyTurtle

sketch = MyTurtle()
sketch_screen = sketch.my_screen
sketch_screen.listen()
sketch_screen.onkeypress(fun=sketch.move_forward, key="w")
sketch_screen.onkeypress(fun=sketch.move_backward, key="s")
sketch_screen.onkeypress(fun=sketch.rotate_clockwise, key="d")
sketch_screen.onkeypress(fun=sketch.rotate_anti_clockwise, key="a")
sketch_screen.onkeypress(fun=sketch.clear_drawing, key="c")
sketch_screen.onkeypress(fun=sketch.pen_up, key="q")
sketch_screen.onkeypress(fun=sketch.pen_down, key="e")

sketch.close_screen()
