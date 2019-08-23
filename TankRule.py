import pygame
import random

pygame.init()

white = (255,255,255)
black =(0,0,0)
red=(200,0,0)
light_red=(255,0,0)
light_green=(0,244,0)
yellow=(200,200,0)
light_yellow=(255,255,0)
green=(0,115,0)
orange=(255,165,0)

d_width =800
d_length =600

clock=pygame.time.Clock()

tankwidth=40
tankheight=20

turretwidth=5
wheelwidth=5    

ground_height=35

explosion_sound=pygame.mixer.Sound("Explosion.wav")
gun_sound=pygame.mixer.Sound("Gun.wav")

gameDisplay=pygame.display.set_mode((d_width,d_length))
pygame.display.set_caption('TankRule')
icon=pygame.image.load('t.png')
pygame.display.set_icon(icon)

f_time=20

largefont = pygame.font.SysFont("comicsansms",73)
sfont = pygame.font.SysFont("comicsansms",25)
mfont = pygame.font.SysFont("comicsansms",40)

def game_intro():
    intro=True
    while intro:
        gameDisplay.fill(white)
        msg_screen("Welcome to tankRule",green,-120,"large")
        msg_screen("the objective of the game is to shoot and destroy.",black,-50,size="small")
        msg_screen("the enemy tank before they destroy you.",black,0,size="small")
        msg_screen("the more enemies destroy,the harder they get.",black,50,size="small")
        
        button("play", 150,450,100,50, green, light_green,"play")
        button("controls", 350,450,100,50,yellow, light_yellow,"controls")
        button("quit" , 550,450,100,50, red ,light_red,"quit")
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key==pygame.K_c:
                    intro=False
                    gameLoop()

def gameover():
    gameover=True
    while gameover:
        gameDisplay.fill(white)
        msg_screen("Game Over",green,-120,"large")
        msg_screen("you died.",black,-50,size="small")
        
        button("play again", 150,450,150,50, green, light_green,"play")
        button("controls", 350,450,102,50,yellow, light_yellow,"controls")
        button("quit" , 550,450,100,50, red ,light_red,"quit")
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
             
def youwin():
    youwin=True
    while youwin:
        gameDisplay.fill(white)
        msg_screen("You Won",green,-120,"large")
        msg_screen("congratulation!",black,-50,size="small")
        
        button("play again", 150,450,150,50, green, light_green,"play")
        button("controls", 350,450,102,50,yellow, light_yellow,"controls")
        button("quit" , 550,450,100,50, red ,light_red,"quit")
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                
def text_on_button(msg, color,buttonx,buttony,b_width,b_length):
    screen_text = sfont.render(msg, True, color)
    text_rect = screen_text.get_rect(center=(buttonx+b_width/2, buttony+b_length/2 ))       
    gameDisplay.blit(screen_text,text_rect)

def tank(x,y,turpos):
    x=int(x)
    y=int(y)
    
    possibleturret=[(x-27,y-2),
                    (x-26,y-5),
                    (x-25,y-8),
                    (x-23,y-12),
                    (x-20,y-14),
                    (x-18,y-15),
                    (x-15,y-17),
                    (x-13,y-19),
                    (x-11,y-21)]
    
    pygame.draw.circle(gameDisplay, black, (x,y), int(tankheight/2))
    pygame.draw.rect(gameDisplay, black, (x-tankheight, y, tankwidth, tankheight ))
    pygame.draw.line(gameDisplay, black,(x,y), possibleturret[turpos], turretwidth)
    pygame.draw.circle(gameDisplay, black,(x-15,y+20),wheelwidth)
    pygame.draw.circle(gameDisplay, black,(x-9,y+20),wheelwidth)
    pygame.draw.circle(gameDisplay, black,(x-3,y+20),wheelwidth)
    pygame.draw.circle(gameDisplay, black,(x+5,y+20),wheelwidth)
    pygame.draw.circle(gameDisplay, black,(x+10,y+20),wheelwidth)
    pygame.draw.circle(gameDisplay, black,(x+15,y+20),wheelwidth)
    return possibleturret[turpos]

def enemytank(x,y,turpos):
    x=int(x)
    y=int(y)
    
    possibleturret=[(x+27,y-2),
                    (x+26,y-5),
                    (x+25,y-8),
                    (x+23,y-12),
                    (x+20,y-14),
                    (x+18,y-15),
                    (x+15,y-17),
                    (x+13,y-19),
                    (x+11,y-21)]
    
    pygame.draw.circle(gameDisplay, black, (x,y), int(tankheight/2))
    pygame.draw.rect(gameDisplay, black, (x-tankheight, y, tankwidth, tankheight ))
    pygame.draw.line(gameDisplay, black,(x,y), possibleturret[turpos], turretwidth)
    pygame.draw.circle(gameDisplay, black,(x-15,y+20),wheelwidth)
    pygame.draw.circle(gameDisplay, black,(x-9,y+20),wheelwidth)
    pygame.draw.circle(gameDisplay, black,(x-3,y+20),wheelwidth)
    pygame.draw.circle(gameDisplay, black,(x+5,y+20),wheelwidth)
    pygame.draw.circle(gameDisplay, black,(x+10,y+20),wheelwidth)
    pygame.draw.circle(gameDisplay, black,(x+15,y+20),wheelwidth)
    return possibleturret[turpos]

def g_controls():
    controls=True
    while controls:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        msg_screen("Controls",green,-120,"large")
        msg_screen("Move turret: Up and Down arrows .",black,-50,size="small")
        msg_screen("Move tank : Left and Right arrows",black,0,size="small")
        msg_screen("Paused : p.",black,40,size="small")
        msg_screen("Power : 'd' to increment and 'a' to decrement.",black,110,size="small")
        msg_screen("Space to shoot.",black,80,size="small")
    
        button("play", 150,450,100,50, green, light_green,"play")
        button("controls", 350,450,100,50,yellow, light_yellow,"controls")
        button("quit" , 550,450,100,50, red ,light_red,"quit")
        pygame.display.update()
        
                
def msg_screen(msg,color,y_distance,size):
    if size=="large":
        
        screen_text = largefont.render(msg, True, color)
        text_rect = screen_text.get_rect(center=(d_width/2, d_length/2 + y_distance))      
    if size=="med":
        
        screen_text = mfont.render(msg, True, color)
        text_rect = screen_text.get_rect(center=(d_width/2, d_length/2 + y_distance))   
    if size=="small":
        
        screen_text = sfont.render(msg, True, color)
        text_rect = screen_text.get_rect(center=(d_width/2, d_length/2 + y_distance))       
    return gameDisplay.blit(screen_text,text_rect)

def button(msg, x, y, width, length, ac_color, inac_color,action=None):
    cur = pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()
    if x+width > cur[0] > x and y+length > cur[1] > y:
        pygame.draw.rect(gameDisplay ,ac_color, (x, y, width, length))
        if click[0]==1 and action!=None:
            if action =="play":
                gameLoop()
            if action=="controls":
                g_controls()
            if action=="quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, inac_color, (x, y, width, length))
    text_on_button(msg, black, x, y, width, length)

def barrier(xloc,randheight,barrier_width):
    pygame.draw.rect(gameDisplay, black , (xloc,d_length-randheight,barrier_width,randheight))

def pause():
    pause=True
    while pause:
        msg_screen("paused",red,-50,size="large")
        msg_screen("press C for continue or Q for Quit",black,50,size="med")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key==pygame.K_c:
                    pause=False    


def score(score):
    text_score=sfont.render("Score="+str(score), True,black)       
    gameDisplay.blit(text_score,[0,0])

def explosion(x,y):
    pygame.mixer.Sound.play(explosion_sound)
    explode=True
    while explode:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        colorchoices=[red,light_yellow,orange,yellow,light_red]
        
        magnitude=1
        while magnitude<50:
            
            explosionx= x + random.randrange(-1*magnitude,magnitude)
            explosiony= y + random.randrange(-1*magnitude,magnitude)
            pygame.draw.circle(gameDisplay, colorchoices[random.randrange(0,4)],(explosionx,explosiony),random.randrange(1,5))
            magnitude+=1
            pygame.display.update()
            clock.tick(100)
        explode=False

def health_bar(playerhealth,enemyhealth):
    
    if playerhealth>75:
        playerhealthcolor=green
    elif playerhealth>50:
        playerhealthcolor=yellow
    elif playerhealth>25:
        playerhealthcolor=red    
    elif playerhealth>0:
        playerhealthcolor=light_red    
    
    
    if enemyhealth>75:
        enemyhealthcolor=green
    elif enemyhealth>50:
        enemyhealthcolor=yellow
    elif enemyhealth>25:
        enemyhealthcolor=red  
    elif enemyhealth>0:
        enemyhealthcolor=light_red    
    pygame.draw.rect(gameDisplay, playerhealthcolor, (680, 25, playerhealth, 25))
    pygame.draw.rect(gameDisplay, enemyhealthcolor, (20, 25, enemyhealth, 25))   
    
    
def fireshell(xy,tankx,tanky,turpos,firepower,xloc,barrier_width,randheight,enemytankX,enemytankY):
    damage=0
    fire=True
    startshell=list(xy)
    
    while fire:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.circle(gameDisplay, red, (startshell[0],startshell[1]),5)   
        startshell[0]-=(10-turpos)*2
        startshell[1]+=int((((startshell[0]-xy[0])*0.015/(firepower/50))**2) - (turpos+turpos/(12-turpos)))
        if startshell[1] > d_length-ground_height:
            hitx=int(startshell[0]*(d_length-ground_height)/startshell[1])
            hity=d_length-ground_height
            explosion(hitx,hity)   
            if enemytankX+10> hitx>enemytankX-10:
                    print("critical hit")
                    damage=25
            elif enemytankX+15> hitx>enemytankX-15:
                    print("hard hit")
                    damage=18
            elif enemytankX+25> hitx>enemytankX-25:
                    print("medium hit")
                    damage=10        
            elif enemytankX+35> hitx>enemytankX-35:
                    print("light hit")
                    damage=5        
            fire=False
        
        checkx1 = startshell[0] <= xloc+barrier_width
        checkx2 = startshell[0] >= xloc
        
        checky1 = startshell[1] <= d_length
        checky2 = startshell[1] >= d_length-randheight
        
        if  checkx1 and checkx2 and checky1 and checky2:
            hitx=int(startshell[0])
            hity=int(startshell[1])
            explosion(hitx,hity)        
            fire=False
        pygame.display.update()
        clock.tick(60)
    return damage

def efireshell(xy,tankx,tanky,turpos,firepower,xloc,barrier_width,randheight,maintankX,maintankY):
    
    damage=0
    currentpower=1
    power_found=False
    while not power_found:
        currentpower+=1
        if currentpower>100:
            power_found=True
        fire=True
        startshell=list(xy)
        
        while fire:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            #pygame.draw.circle(gameDisplay, red, (startshell[0],startshell[1]),5)   
          
            startshell[0]+=(10-turpos)*2
            startshell[1]+=int((((startshell[0]-xy[0])*0.015/(currentpower/50))**2) - (turpos+turpos/(12-turpos)))
            if startshell[1] > d_length-ground_height:
                hitx=int(startshell[0]*(d_length-ground_height)/startshell[1])
                hity=d_length-ground_height
                #explosion(hitx,hity)
                if maintankX+15> hitx>maintankX-15:
                    print("target")
                    power_found=True
                fire=False
            
            checkx1 = startshell[0] <= xloc+barrier_width
            checkx2 = startshell[0] >= xloc
            
            checky1 = startshell[1] <= d_length
            checky2 = startshell[1] >= d_length-randheight
            
            if  checkx1 and checkx2 and checky1 and checky2:
                hitx=int(startshell[0])
                hity=int(startshell[1])
                #explosion(hitx,hity)        
                fire=False
    
    fire=True
    startshell=list(xy)
    while fire:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.circle(gameDisplay, red, (startshell[0],startshell[1]),5)   
        
        startshell[0]+=(10-turpos)*2
        gun_power=random.randrange(int(currentpower*0.90),int(currentpower*1.10))

        startshell[1]+=int((((startshell[0]-xy[0])*0.015/(gun_power/70))**2) - (turpos+turpos/(12-turpos)))
        if startshell[1] > d_length-ground_height:
            hitx=int(startshell[0]*(d_length-ground_height)/startshell[1])
            hity=d_length-ground_height
            explosion(hitx,hity)
            if maintankX+10> hitx>maintankX-10:
                    print("critical hit")
                    damage=25
            elif maintankX+15> hitx>maintankX-15:
                    print("hard hit")
                    damage=18
            elif maintankX+25> hitx>maintankX-25:
                    print("medium hit")
                    damage=10        
            elif maintankX+35> hitx>maintankX-35:
                    print("light hit")
                    damage=5
            fire=False
        
        checkx1 = startshell[0] <= xloc+barrier_width
        checkx2 = startshell[0] >= xloc
        
        checky1 = startshell[1] <= d_length
        checky2 = startshell[1] >= d_length-randheight
        
        if  checkx1 and checkx2 and checky1 and checky2:
            hitx=int(startshell[0])
            hity=int(startshell[1])
            explosion(hitx,hity)        
            fire=False
        pygame.display.update()
        clock.tick(60)
    return damage 
    
def power(level):
        text=sfont.render("power: "+str(level)+"%",True,black)
        gameDisplay.blit(text,[d_width/2,0])
        
def gameLoop(): 
    
    exit=False
    
    playerhealth=100
    enemyhealth=100
    
    maintankX= d_width * 0.9
    maintankY= d_length * 0.9
    tankmove=0
    turpos=0
    turmove=0
    
    enemytankX= d_width * 0.1
    enemytankY= d_length * 0.9
    
    barrier_width=50
    xloc=(d_width/2) + random.randint(-0.1*d_width , 0.1*d_width)
    randheight=random.randrange(d_length*0.1, d_length*0.6)
    
    firepower=50
    changepower=0
    
    while not exit:
        gun=tank(maintankX,maintankY,turpos)
        enemygun=enemytank(enemytankX,enemytankY,turpos)
       

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    tankmove=-5
                elif event.key==pygame.K_RIGHT:
                    tankmove=5
                elif event.key==pygame.K_UP:
                    turmove=1
                elif event.key==pygame.K_DOWN:
                    turmove=-1
                elif event.key==pygame.K_p:
                    pause()    
                elif event.key==pygame.K_SPACE:
                    pygame.mixer.Sound.play(gun_sound)
                    damage=fireshell(gun,maintankX,maintankY,turpos,firepower,xloc,barrier_width,randheight,enemytankX,enemytankY)
                    enemyhealth-=damage
                   
                    possmove=['l','r']
                    possindex=random.randrange(0,2)
                    
                    for x in range(random.randrange(0,10)):
                        
                        if d_width*0.3 > enemytankX >= d_width*0.03 :
                             if possmove[possindex] =='l':
                                 enemytankX-=5
                             elif possmove[possindex] =='r':
                                 enemytankX+=5
                             gameDisplay.fill(white)
                             health_bar(playerhealth,enemyhealth)    
                             gun=tank(maintankX,maintankY,turpos)
                             enemygun=enemytank(enemytankX,enemytankY,7)
                             firepower+=changepower
                             power(firepower)
                             barrier(xloc,randheight,barrier_width)
                             gameDisplay.fill(green,rect=[0,d_length-ground_height,d_width,ground_height])
                             pygame.display.update()
                             clock.tick(f_time)    

                    
                    pygame.mixer.Sound.play(gun_sound)
                    damage=efireshell(enemygun,enemytankX,enemytankY,turpos,50,xloc,barrier_width,randheight,maintankX,maintankY)
                    playerhealth-=damage
                    
                elif event.key==pygame.K_a:
                    changepower=-1
                elif event.key==pygame.K_d:
                    changepower=1
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    tankmove=0
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    turmove=0
                if event.key==pygame.K_a or event.key==pygame.K_d:
                    changepower=0
        gameDisplay.fill(white)
        
        maintankX+=tankmove
        
        turpos+=turmove
        if turpos > 8:
            turpos=8
        elif turpos < 0:
            turpos=0
        if  maintankX-(tankwidth/2) < xloc+barrier_width:
            maintankX+=5
        if playerhealth < 1:
            gameover()
        elif enemyhealth < 1:
            youwin()
        health_bar(playerhealth,enemyhealth)    
        tank(maintankX,maintankY,turpos)
        enemytank(enemytankX,enemytankY,7)
        firepower+=changepower
        if firepower>100:
            firepower=100
        elif firepower<1:
            firepower=1
        power(firepower)
        
        barrier(xloc,randheight,barrier_width)
        gameDisplay.fill(green,rect=[0,d_length-ground_height,d_width,ground_height])
        pygame.display.update()
        clock.tick(f_time)    

    pygame.quit()
    quit()
    
game_intro()
gameLoop()