# Remove comment from next line if you're not using a deticated editor to modify the code
# from microbit import *

game_state = 0
choice = 0
# 1 rock 2 paper 3 scissors

basic.show_leds("""
. # # # .
. . . # .
. . # # .
. . . . .
. . # . .
""")
  

    
def on_button_pressed_ab():
  global game_state
  if game_state == 0:
    game_state = 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_pin0_rock():
  global game_state
  if game_state == 2:
    global choice
    choice = 1
    game_state = 3
input.on_pin_pressed(TouchPin.P0, on_pin0_rock)

def on_pin1_paper():
  global game_state
  if game_state == 2:
    global choice
    choice = 2
    game_state = 3
input.on_pin_pressed(TouchPin.P1, on_pin1_paper)

def on_pin2_scissors():
  global game_state
  if game_state == 2:
    global choice
    choice = 3
    game_state = 3
input.on_pin_pressed(TouchPin.P2, on_pin2_scissors)

def gamestate2_timer():
  if game_state == 2:
    basic.pause(1000)
    game_state = 3
    
def game_update():
  global game_state
  
  if game_state == 0:
    basic.show_leds("""
    . # # # .
    . . . # .
    . . # # .
    . . . . .
    . . # . .
    """)
  elif game_state == 1:
    basic.show_number(1)
    basic.pause(250)
    basic.show_number(2)
    basic.pause(250)
    basic.show_number(3)
    basic.pause(250)
    basic.show_leds("""
    . . # . .
    . . # . .
    . . # . .
    . . . . .
    . . # . .
    """)
    
    game_state = 2
  elif game_state == 2:
	pass
  elif game_state == 3:
    global choice
    winloss = 0
    comp_choice = randint(1,3)
    
    if comp_choice == 1: basic.show_string('R')
    elif comp_choice == 2: basic.show_string('P')
    elif comp_choice == 3: basic.show_string('S')
    
    basic.pause(500)
      
    if choice == 1:
      if comp_choice == 2:
        pass
      elif comp_choice == 3:
        winloss = 1
      elif comp_choice == 1:
        winloss = 2
        
    elif choice == 2:
      if comp_choice == 3:
        pass
      elif comp_choice == 1:
        winloss = 1
      elif comp_choice == 2:
        winloss = 2
        
    elif choice == 3:
      if comp_choice == 1:
        pass
      elif comp_choice == 2:
        winloss = 1
      elif comp_choice == 3:
        winloss = 2
        
    if winloss == 0: basic.show_icon(IconNames.SAD)
    elif winloss == 1: basic.show_icon(IconNames.HAPPY)
    elif winloss == 2: 
      basic.show_leds("""
      . . . . .
      . # . # .
      . . . . .
      . # # # .
      . . . . .
      """)
    basic.pause(1000)
    
    game_state = 0
    
basic.forever(game_update)
