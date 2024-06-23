import badger2040
badger = badger2040.Badger2040()

badger.set_pen(15)
badger.clear()

badger.set_update_speed(3)

badger.set_pen(0)

badger.set_font("sans")
badger.set_thickness(3)
# Heading line
badger.line(40, 38, 256, 38, 2)

# Line 2
badger.line(40, 68, 256, 68, 2)

badger.line(40, 98, 256, 98, 2)

# Middle line
badger.line(143, 38, 143, 128, 2)

badger.text("AM", 20, 90, -1, 1.3, -90)
badger.text("PM", 276, 37, -1, 1.3, 90)

badger.text("Location Name", 0,15,-1,0.9)
badger.set_thickness(2)
badger.text("sat", 250, 25, -1, 0.7)
badger.update()