read_me = '''
#The Docs for USING 'pygameModule'
#VISIT at : https://github.com/Parvat-web-dev/newPygameModule

Importing the file:

    Download the source code from GIT-HUB and then paste it
    in your folder were you are creating a pygame.py file!
    then follow the command:

        from pygameModule import *

    this command imports all the modules in the pygameModule
    file.
    Note* :
        importing this file will also import:
            pygame, pygame.locals, random, time.
        if you dont have any of these module then it will give some
        errors.
        To fix that run the following command in your terminal:

            pip install pygame

            pip install random

            pip install time
            
    And you are done with importing the file.
    
Help for the modules available in the module:
  
  Available Modules:
    1. size()
    2. frameRate()
    3. rect()
    4. circle()
    5. polygon()
    6. line()
    7. arc()
    8. background()
    9. text()
    10. get_mouse_pos()
    11. mouse()
    12. mouse_pressed()
    13. mouse_to()
    14. mouse_visible()
    15. key()
    
  Docs (or) How To Use The Above Modules:
  
    1. size(width, height):
      This function creates a new pygame window.
      This function replaces the 'pygame.display.set_mode([width, height])'
      
      Parameters:
        1. width:
          This parameter controles the width of the screen.
        2. height:
          This parameter controles the height of the screen.
        
        NOTE*: the height and width are in pixels.
        
    2. frameRate(frames_per_second):
       This function controles the number of frames changing per second.
       
       Parameter:
         1. frames_per_second:
            no of fraames per one second.
            
    3. rect(x, y, width, height, color, radius):
        This function creates a rectangle on the pygame screen.
        
        Parameters:
          1. x:
            The x-position of the top left corner of the rectangle.
          2. y:
            The y-position of the top left corner of the rectangle.
          3. width:
            The width of the rectangle along the x-axis.
          4. height:
            The height of the rectangle along the y-axis.
          5. radius:
               NOTE*: THIS PARAMETER IS OPTIONAL
            The radius of the rectangle.
            It might be used to create rounded corners for the rectangle.
            
    4. circle(x, y, radius, color):
        This function draws a circle on the pygame screen.
        
        Parameters:
          1. x:
            The x-position of the center of the circle.
          2. y:
            The y-position of the center of the circle.
          3. radius:
            The radius of the circle. (in pixels)
          4. color:
            The fill color of the circle.
            
   5. polygon(point_tuple, color, line_width):
      This function creates a polygon with the given points.
      
      Parameters:
        1. point_tuples:
          The coordinates of the points of the polygon.
          example : [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6), ...]
                  You can insert as many point-pairs as you want.
         
        2. color:
          the color of the drawn line.(in rgb())
        
        3. line_width:
          The width of the line.(in pixels)
       
       
   6. line(start_point, end_point, color):
       This function draws a line with the two given points.
       
       Parameters:
            1. start_point:
                The start point of the line.
                (x1, y1)
            2. end_point:
                The end point of the line.
                (x2, y2)
            3. color:
                The color of the line in rgb().
                
    7. arc(start_angle_in_pi, end_angle_in_pi, color, coordinates):
        This function creates an arc with the given properties.
        
        Parameters:
            1. start_angle_in_pi:
                The starting angle in pi radians.
                Mostly the value for this parameter is '0'(zero).
            2. end_angle_in_pi:
                The ending angle in pi radians.
                If you dont understand, you should probably learn some math.
            3. color:
                The color of the arc in rgb().
            4. coordinates:
                the x and y position of the arc.
                (x, y)
           
    8. background(r, g, b):
        This function creates a standard background color for the pygame screen.
        
        Parameters:
            1. r:
                The red configuration of the rgb() color formate.
                range of r:
                    0 ≤ r ≥ 255.
            2. g:
                The green configuration of the rgb() color formate.
                range of g:
                    0 ≤ g ≥ 255.
            3. b:
                The blue configuration of the rgb() color formate.
                range of b:
                    0 ≤ b ≥ 255.
                   
           Some Examples of rgb():
                   rgb(255, 0, 0) = red color
                   rgb(0, 255, 0) = green color
                   rgb(0, 0, 255) = blue color
                   rgb(255, 0, 255) = pink color
                   For more colors visit:
                        https://www.rapidtables.com/web/color/RGB_Color.html
                        
   9. text(TEXT, size, color, coordinates):
        This function displayes the given text on the pygame screen.
        
        Parameters:
        1. TEXT:
            The string of the text you want to display on the screen.
        2. size:
            The size of the text.(in pixels)
        3. color:
            The color of the text.(in rgb())
        4. coordinates:
            The x and y position of top left corner of the text.
            
        Example:
            
            text("You are the best!", 32, (0, 255, 100), (0,0))
            
            #This displays the text in the top left corner of the screen
            # in red color, with the size of 32pixels
            
            -----------------------(or)-------------------------------------
            
            text_to_display = "How are you? Do you like this module"
            text(text_to_display, 24, (0, 0, 255), (0,0))
            
            #This will display the given text in the variable 'text_to_display'
            #in blue color with size of 24 pixels at the top left corner.
            
   10. get_mouse_pos():
        This function returns the mouse's x and y position on a 
        specified condition.
        
        This Function Has No Parameters.
        
   11. mouse(coordinate):
        This function returns the mouse's position for a specified axis.
        
        Parameter:
            1. coordinate:
                X or Y cordinate's mouse position.
                The values for this parameter are:
                    'x' for x-coordinate ,
                    'y' for y-coordinate.
                    
   12. mouse_pressed(button):
        This function checks for the mouse mouse presses and returns a boolean
        value .(either True or False)
        
        Parameter:
            1. button:
                Checks for the given button:
                if the value of button is left:
                    then returns true if the left mouse button is pressed.
                if the value of button is middle or scroll:
                    then returns true if the middle or scrll mouse button is pressed.
                if the value of button is right:
                    then returns true if the right mouse button is pressed.
                    
   13. mouse_to(x, y):
        This function fixes the mouse's position onto a specifies point.
        
        Parameters:
            1. x:
                The x-position of where the mouse should be fixed
            2. y:
                The y-position of where the mouse should be fixed
                
          
  14. mouse_visible(boolean):
        This function controles the visiblity of the mouse.
        
        Parameter:
            1. boolean:
                This parameter takes a boolean value that is either
                'True' or 'False'
                If the value is set to Frue, then the mouse will be visible 
                on the pygame's screen.
                If the value is set to False, then the mouse will not be 
                visible when it is on the pygame's screen.
            
  15. key(Special_key):
        This function checks for the key pressed of the given key.
        
        Parameter:
            1. Special_key:
                The key value:
                    for left_arrow key : 'LEFT'
                    for right_arrow key : 'RIGHT'
                    for up_arrow key : 'UP'
                    for down_arrow key : 'DOWN'
                    for 'a' key : 'a'
                    
                    FOR MORE KEYS VISIT:
                    https://www.pygame.org/docs/ref/key.html
        
        
Created By PARVAT.R.       
            
More Fratures will be added on request.
Please comment for errors.
Thank you, for using this module.
'''


def read_me():
    print('''
#The Docs for USING 'pygameModule'
#VISIT at : https://github.com/Parvat-web-dev/newPygameModule

Importing the file:

    Download the source code from GIT-HUB and then paste it
    in your folder were you are creating a pygame.py file!
    then follow the command:

        from pygameModule import *

    this command imports all the modules in the pygameModule
    file.
    Note* :
        importing this file will also import:
            pygame, pygame.locals, random, time.
        if you dont have any of these module then it will give some
        errors.
        To fix that run the following command in your terminal:

            pip install pygame

            pip install random

            pip install time
            
    And you are done with importing the file.
    
Help for the modules available in the module:
  
  Available Modules:
    1. size()
    2. frameRate()
    3. rect()
    4. circle()
    5. polygon()
    6. line()
    7. arc()
    8. background()
    9. text()
    10. get_mouse_pos()
    11. mouse()
    12. mouse_pressed()
    13. mouse_to()
    14. mouse_visible()
    15. key()
    
  Docs (or) How To Use The Above Modules:
  
    1. size(width, height):
      This function creates a new pygame window.
      This function replaces the 'pygame.display.set_mode([width, height])'
      
      Parameters:
        1. width:
          This parameter controles the width of the screen.
        2. height:
          This parameter controles the height of the screen.
        
        NOTE*: the height and width are in pixels.
        
    2. frameRate(frames_per_second):
       This function controles the number of frames changing per second.
       
       Parameter:
         1. frames_per_second:
            no of fraames per one second.
            
    3. rect(x, y, width, height, color, radius):
        This function creates a rectangle on the pygame screen.
        
        Parameters:
          1. x:
            The x-position of the top left corner of the rectangle.
          2. y:
            The y-position of the top left corner of the rectangle.
          3. width:
            The width of the rectangle along the x-axis.
          4. height:
            The height of the rectangle along the y-axis.
          5. radius:
               NOTE*: THIS PARAMETER IS OPTIONAL
            The radius of the rectangle.
            It might be used to create rounded corners for the rectangle.
            
    4. circle(x, y, radius, color):
        This function draws a circle on the pygame screen.
        
        Parameters:
          1. x:
            The x-position of the center of the circle.
          2. y:
            The y-position of the center of the circle.
          3. radius:
            The radius of the circle. (in pixels)
          4. color:
            The fill color of the circle.
            
   5. polygon(point_tuple, color, line_width):
      This function creates a polygon with the given points.
      
      Parameters:
        1. point_tuples:
          The coordinates of the points of the polygon.
          example : [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6), ...]
                  You can insert as many point-pairs as you want.
         
        2. color:
          the color of the drawn line.(in rgb())
        
        3. line_width:
          The width of the line.(in pixels)
       
       
   6. line(start_point, end_point, color):
       This function draws a line with the two given points.
       
       Parameters:
            1. start_point:
                The start point of the line.
                (x1, y1)
            2. end_point:
                The end point of the line.
                (x2, y2)
            3. color:
                The color of the line in rgb().
                
    7. arc(start_angle_in_pi, end_angle_in_pi, color, coordinates):
        This function creates an arc with the given properties.
        
        Parameters:
            1. start_angle_in_pi:
                The starting angle in pi radians.
                Mostly the value for this parameter is '0'(zero).
            2. end_angle_in_pi:
                The ending angle in pi radians.
                If you dont understand, you should probably learn some math.
            3. color:
                The color of the arc in rgb().
            4. coordinates:
                the x and y position of the arc.
                (x, y)
           
    8. background(r, g, b):
        This function creates a standard background color for the pygame screen.
        
        Parameters:
            1. r:
                The red configuration of the rgb() color formate.
                range of r:
                    0 ≤ r ≥ 255.
            2. g:
                The green configuration of the rgb() color formate.
                range of g:
                    0 ≤ g ≥ 255.
            3. b:
                The blue configuration of the rgb() color formate.
                range of b:
                    0 ≤ b ≥ 255.
                   
           Some Examples of rgb():
                   rgb(255, 0, 0) = red color
                   rgb(0, 255, 0) = green color
                   rgb(0, 0, 255) = blue color
                   rgb(255, 0, 255) = pink color
                   For more colors visit:
                        https://www.rapidtables.com/web/color/RGB_Color.html
                        
   9. text(TEXT, size, color, coordinates):
        This function displayes the given text on the pygame screen.
        
        Parameters:
        1. TEXT:
            The string of the text you want to display on the screen.
        2. size:
            The size of the text.(in pixels)
        3. color:
            The color of the text.(in rgb())
        4. coordinates:
            The x and y position of top left corner of the text.
            
        Example:
            
            text("You are the best!", 32, (0, 255, 100), (0,0))
            
            #This displays the text in the top left corner of the screen
            # in red color, with the size of 32pixels
            
            -----------------------(or)-------------------------------------
            
            text_to_display = "How are you? Do you like this module"
            text(text_to_display, 24, (0, 0, 255), (0,0))
            
            #This will display the given text in the variable 'text_to_display'
            #in blue color with size of 24 pixels at the top left corner.
            
   10. get_mouse_pos():
        This function returns the mouse's x and y position on a 
        specified condition.
        
        This Function Has No Parameters.
        
   11. mouse(coordinate):
        This function returns the mouse's position for a specified axis.
        
        Parameter:
            1. coordinate:
                X or Y cordinate's mouse position.
                The values for this parameter are:
                    'x' for x-coordinate ,
                    'y' for y-coordinate.
                    
   12. mouse_pressed(button):
        This function checks for the mouse mouse presses and returns a boolean
        value .(either True or False)
        
        Parameter:
            1. button:
                Checks for the given button:
                if the value of button is left:
                    then returns true if the left mouse button is pressed.
                if the value of button is middle or scroll:
                    then returns true if the middle or scrll mouse button is pressed.
                if the value of button is right:
                    then returns true if the right mouse button is pressed.
                    
   13. mouse_to(x, y):
        This function fixes the mouse's position onto a specifies point.
        
        Parameters:
            1. x:
                The x-position of where the mouse should be fixed
            2. y:
                The y-position of where the mouse should be fixed
                
          
  14. mouse_visible(boolean):
        This function controles the visiblity of the mouse.
        
        Parameter:
            1. boolean:
                This parameter takes a boolean value that is either
                'True' or 'False'
                If the value is set to Frue, then the mouse will be visible 
                on the pygame's screen.
                If the value is set to False, then the mouse will not be 
                visible when it is on the pygame's screen.
            
  15. key(Special_key):
        This function checks for the key pressed of the given key.
        
        Parameter:
            1. Special_key:
                The key value:
                    for left_arrow key : 'LEFT'
                    for right_arrow key : 'RIGHT'
                    for up_arrow key : 'UP'
                    for down_arrow key : 'DOWN'
                    for 'a' key : 'a'
                    
                    FOR MORE KEYS VISIT:
                    https://www.pygame.org/docs/ref/key.html
        
        
Created By PARVAT.R.       
            
More Fratures will be added on request.
Please comment for errors.
Thank you, for using this module.
''')

from pygame import *
from pygame.locals import *
import pygame, time, random

print()
print("Hello from pygameModule.")
print("For more help input : read_me()")

pygame.init()

def size(width, height):
    screen = pygame.display.set_mode([width, height])
    return screen

def frameRate(frames_per_second):
    fps = pygame.time.Clock().tick(frames_per_second)
    return fps

def rect(x, y, width, height, color, radius=None):
    rectangle = pygame.draw.rect(pygame.display.get_surface(), color, [x, y, width, height], radius)
    return rectangle

def circle(x, y, radius, color):
    cir = pygame.draw.circle(pygame.display.get_surface(), color, coordinates, radius)
    return cir

def polygon(points_tuple, color, width_of_line):
    poly = pygame.draw.polygon(pygame.display.get_surface(), color, points_tuple, width)
    return poly

def line(start_point, end_point, color):
    lne = pygame.draw.line(pygame.display.get_surface(), color, start_point, end_point)
    return lne

def arc(start_angle_in_pi, end_angle_in_pi, color, coordinates):
    a = pygame.draw.arc(pygame.display.get_surface(), color, coordinates, start_angle_in_pi, end_angle_in_pi)
    return a

def background(r, g, b):
    bg = pygame.display.get_surface().fill((r, g, b))
    return bg

def text(TEXT, size, color, coordinates):
    pygame.font.init()
    myfont = pygame.font.Font('freesansbold.ttf', size)
    textsurface = myfont.render(TEXT, False, color)
    pygame.display.get_surface().blit(textsurface, coordinates)
    return textsurface, myfont

def get_mouse_pos():
    pos = pygame.mouse.get_pos()
    return pos

def mouse(coordinate):
    mouseX, mouseY = pygame.mouse.get_pos()
    if str(coordinate).lower() == 'x' or str(coordinate).lower() == '1':
        return mouseX
    if str(coordinate).lower() == 'y' or str(coordinate).lower() == '2':
        return mouseY

def mouse_pressed(button):
    which = button
    if str(which).lower() == 'left'or str(which).lower() == '0':
        left_click = pygame.mouse.get_pressed()[0]
        return left_click
    elif str(which).lower() == 'middle' or str(which).lower() == 'scroll' or str(which).lower() == '1':
        left_click = pygame.mouse.get_pressed()[1]
        return left_click
    elif str(which).lower() == 'right' or str(which).lower() == '2':
        left_click = pygame.mouse.get_pressed()[2]
        return left_click

def mouse_to(x, y):
    to = pygame.mouse.set_pos([x, y])
    return to

def mouse_visible(boolean):
    visible = pygame.mouse.set_visible(boolean)
    return visible

def key(Special_key):
    K = ['K', '_']
    inputed = []
    if 'K_' in Special_key:
        for a in Special_key:
            inputed.append(a)
        inputed.remove(K[0])
        inputed.remove(K[1])
    Special_key = ""
    for a in inputed:
        Special_key += str(a) 
    x = "pygame.K_"+Special_key
    keys = pygame.key.get_pressed()[eval(x)]
    return keys


