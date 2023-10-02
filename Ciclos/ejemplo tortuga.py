import turtle as t

# forward
# backward
# left
# right
# penup pendown

t.penup()
t.backward(300)
t.pendown()

# Cuadrado
for i in range(4):
    t.forward(100)
    t.left(90)
    
t.penup()
t.forward(200)
t.pendown()

# Pentágono
for i in range(5):
    t.forward(100)
    t.left(72)
    
t.penup()
t.forward(300)
t.pendown()

# Octágono
for i in range(8):
    t.forward(100)
    t.left(45)


t.mainloop()