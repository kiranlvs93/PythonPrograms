from my_turtle import MyTurtle

sketch = MyTurtle()
sketch_screen = sketch.my_screen
sketch_screen.listen()
# sketch.move_forward_backward(True)
# sketch.move_forward_backward(True)
# sketch.move_forward_backward(True)
# sketch.move_forward_backward(True)
sketch_screen.onkey(fun=sketch.move_forward, key="w")
sketch_screen.onkey(fun=sketch.move_backward, key="s")
sketch_screen.onkey(fun=sketch.rotate_clockwise, key="d")
sketch_screen.onkey(fun=sketch.rotate_anti_clockwise, key="a")
sketch_screen.onkey(fun=sketch.clear_drawing, key="c")
sketch_screen.onkey(fun=sketch.pen_up, key="q")
sketch_screen.onkey(fun=sketch.pen_down, key="e")

# sketch.move_forward_backward(False)
sketch.close_screen()
