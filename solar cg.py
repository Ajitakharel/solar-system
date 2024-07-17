import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 1200, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("solar system ")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Main loop
running = True
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Calculate circle position
    radius =50
    
   
    center_x,center_y = (width // 2, height // 2)
   
    w=300
    h=200
   
    # Draw the circle
    pygame.draw.circle(screen, 'ORANGE', (width // 2, height // 2), 60)


    pygame.draw.ellipse(screen, ('yellow'), (center_x-w//2, center_y-h//2,w,h), 6)
    x = center_x + int(w//2 * math.cos(math.radians(angle*2.3)))
    y = center_y+ int(h//2* math.sin(math.radians(angle*2.3)))
    pygame.draw.circle(screen, ('yellow'), (x, y), 20)

    pygame.draw.ellipse(screen, ('gray'), (center_x-400//2, center_y-300//2,400,300), 6)
    x = center_x + int(400//2 * math.cos(math.radians(angle*2)))
    y = center_y+ int(300//2* math.sin(math.radians(angle*2)))
    pygame.draw.circle(screen, ('gray'), (x, y), 30)


    pygame.draw.ellipse(screen, ('BLUE'), (center_x-500//2, center_y-400//2,500,400), 6)
    x = center_x + int(500//2 * math.cos(math.radians(angle*1.85)))
    y = center_y+ int(400//2* math.sin(math.radians(angle*1.85)))
    pygame.draw.circle(screen, ('BLUE'), (x, y), 40)




    pygame.draw.ellipse(screen, ('red'), (center_x-600//2, center_y-500//2,600,500), 6)
    x = center_x + int(600//2 * math.cos(math.radians(angle*1.7)))
    y = center_y+ int(500//2* math.sin(math.radians(angle*1.7)))
    pygame.draw.circle(screen, ('red'), (x, y), 39)



    pygame.draw.ellipse(screen, ('purple'), (center_x-700//2, center_y-600//2,700,600), 6)
    x = center_x + int(700//2 * math.cos(math.radians(angle*1.6)))
    y = center_y+ int(600//2* math.sin(math.radians(angle*1.6)))
    pygame.draw.circle(screen, ('purple'), (x, y), 40)

    pygame.draw.ellipse(screen, ('cyan'), (center_x-800//2, center_y-700//2,800,700), 6)
    x = center_x + int(800//2 * math.cos(math.radians(angle*1.45)))
    y = center_y+ int(700//2* math.sin(math.radians(angle*1.45)))
    pygame.draw.circle(screen, ('cyan'), (x, y), 43)


    pygame.draw.ellipse(screen, ('green'), (center_x-900//2, center_y-800//2,900,800), 6)
    x = center_x + int(900//2 * math.cos(math.radians(angle*1.29)))
    y = center_y+ int(800//2* math.sin(math.radians(angle*1.29)))
    pygame.draw.circle(screen, ('green'), (x, y), 34)

    


    pygame.draw.ellipse(screen, ('pink'), (center_x-1000//2, center_y-900//2,1000,900), 6)
    x = center_x + int(1000//2 * math.cos(math.radians(angle*1.15)))
    y = center_y+ int(900//2* math.sin(math.radians(angle*1.15)))
    pygame.draw.circle(screen, ('pink'), (x, y), 45)


    
    
    
    pygame.display.flip()

    # Rotate the circle
    angle += 1
    # if angle >= 360:
    #     angle = 1
    
    # Control the frame rate
    pygame.time.Clock().tick(60)
# Quit Pygame
pygame.quit()
sys.exit()
    

