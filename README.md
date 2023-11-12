# turtle-module-python
Exploring turtle module functionalities in python

### The Turtle module in Python provides a set of in-built functions for drawing and creating graphics. Some of the key functions include:

    turtle.forward(distance): Moves the turtle forward by the specified distance. 
---
     turtle.backward(distance): Moves the turtle backward by the specified distance.
---
    turtle.right(angle): Turns the turtle to the right by the specified angle.
---
    turtle.left(angle): Turns the turtle to the left by the 
    specified angle.
---
    turtle.penup(): Lifts the turtle's pen, so it doesn't draw while moving.
---
    turtle.pendown(): Lowers the turtle's pen, so it starts drawing again.
---
    turtle.color(color): Sets the pen color.
---
    turtle.pensize(width): Sets the width of the pen.
---
    turtle.circle(radius): Draws a circle with the specified radius.
---
    turtle.dot(size, color): Draws a dot at the current 
---
    turtle position with the specified size and color.
----
    turtle.begin_fill() and turtle.end_fill(): Used to fill the area between them with the current pen color.

### <u>The turtle module also provides a number of functions to control the appearance of the turtle. Some of the key f unctions include: </u>

    turtle.shape(shape): Sets the shape of the turtle. The default shape is an arrow, but you can also change it to a circle, square, or triangle.
---

    turtle.shapesize(stretch_wid=None, stretch_len=None, outline=None): Stretches the width and height of the turtle shape based on the stretch_wid and stretch_len values. The outline argument specifies the width of the outline around the turtle shape.

---
    
        turtle.speed(speed): Sets the speed of the turtle. The speed can be set between 0 and 10. The default speed is 3.
---
    turtle.bgcolor(color): Sets the background color of the turtle window.
---
    turtle.title(title): Sets the title of the turtle window.
---
    turtle.clear(): Removes all drawings from the turtle window.
---
    turtle.reset(): Resets the turtle to its initial position.
---

    turtle.hideturtle(): Makes the turtle invisible. The turtle is visible by default.
---
    turtle.showturtle(): Makes the turtle visible.
---
    turtle.write(text): Writes the specified text at the turtle position.
---
    turtle.goto(x, y): Moves the turtle to the specified coordinates.
---
    turtle.stamp(): Leaves an impression of a turtle shape at the current location.
---
    turtle.seth(angle): Sets the direction of the turtle to angle. Here, angle is in degrees.
---
    turtle.home(): Moves the turtle to the origin, i.e., coordinates (0,0).
---
    turtle.circle(radius, extent=None): Draws a circle with the specified radius. The extent argument determines which part of the circle is drawn. If the extent is not specified, it draws a complete circle.
---
    turtle.bye(): Closes the turtle window.
---
    turtle.done(): Makes the turtle window stay open until you close it.
---
    turtle.isvisible(): Returns True if the turtle is visible.
---
    turtle.heading(): Returns the current heading of the turtle.
---
    turtle.distance(x, y): Returns the distance between the turtle and the specified coordinates.
---
    turtle.towards(x, y): Returns the angle between the turtle and the specified coordinates.
---
    turtle.xcor(): Returns the turtle's x-coordinate.
---
    turtle.ycor(): Returns the turtle's y-coordinate.
