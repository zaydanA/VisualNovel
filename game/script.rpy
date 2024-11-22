# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Rachel", color="#FFC0CB",what_cps=2)
define l = Character("Lidya", color="#00008B",what_cps=2) 

image zeilsmile2:
    "zeil smile2.png"
    zoom 1.25
image zeilsmile:
    "zeil smile.png"
    zoom 1.25
image extra:
    "extra normal.png"
    zoom 1.25
    
transform midleft:
    xpos 0.2  # Horizontal center (50% of the screen width)
    ypos 1.0  # Vertical center (50% of the screen height)
transform midright:
    xpos 0.8  # Horizontal center (50% of the screen width)
    ypos 1.0  # Vertical center (50% of the screen height)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg classroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    play sound "audio 1.mp3"

    show extra at left

    # These display lines of dialogue.
    r "Hmm, new school, fresh start!"

    show zeilsmile at right with easeinright

    play sound "audio 2.mp3"
    l "Hi, nice to meet you [r]!"


    show extra at midleft with easeinleft

    play sound "audio 3.mp3"
    r "Hi, lets be friends [l]!"

    hide zeilsmile
    show zeilsmile2 at right 
    play sound "audio 4.mp3"
    l "Ok bff!"
    show zeilsmile2 at midright with move
    play sound "audio 5.mp3"
    # This ends the game.
    r "Ok bff!"

    return
