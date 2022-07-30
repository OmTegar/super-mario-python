#Imports from the pygame library.
import pygame
import time



#BossHealths
KongHealth = 3
BowserHealth = 5

#Imports the keys
from pygame.locals import(
  KEYUP,
  KEYDOWN,
  K_RIGHT,
  K_LEFT,
  K_UP
)

#Clock
Clock = pygame.time.Clock()


#Just for better looks in the console
print("")
#Checks the character. We will for now assume it is Mario.

#Gravity
Gravity = 0.05
Gravity2 = 0.01

#Checks the level
level = 0
#Score
NumScore = 0

#Checks the Character
Character = "None"

#Initializes the pygame
pygame.init()
#Initializes the font
pygame.font.init()

Move = False
if level == 0 or level == 0.5:
  Move = False
if level >= 1 and level <= 10:
  Move = True
if level == 11:
  Move = False

#The title font
TitleFont = pygame.font.SysFont("Comic Sans MS",40)
Title = TitleFont.render("Mario Platformer",False,(255,0,0))
Title2 = TitleFont.render("Mario Platformer",False,(0,0,255))



#The Score font
ScoreFont = pygame.font.SysFont("Comic Sans MS",30)
ScoreText = ScoreFont.render("Score: "+ str(NumScore),False,(0,0,0))


#Choose YOUR FIGHTER!
CYFFont = pygame.font.SysFont("Comic Sans MS",40)
CYF = CYFFont.render("Choose your character!",False,(50,50,50))
CYF2 = CYFFont.render("Choose your character!",False,(200,200,200))

#Builds the screen
screen = pygame.display.set_mode((500,250))

#The main class for the objects
class GameObject:

  def __init__(self,x,y,width,height,image):
    self.x = x
    self.y = y
    self.vx = 0
    self.vy = 0
    self.width = width
    self.height = height
    self.image = image
    self.img = pygame.image.load(image)
    self.img = pygame.transform.scale(self.img,(width,height))
    self.img_flip = pygame.transform.flip(self.img, True, False)
    self.hitbox = pygame.Rect(x,y,width,height)
    self.collision = [False] * 9    
    self.InAir = False
    self.Show = False
    self.Defeat = False
    self.FacingRight = True

  
   
  # set center
  def set_center(self, screen):
    self.rect.center = screen.get_rect().center

  # recreates this GameObject's hitbox so that it aligns with the GameObject's position
  def UpdateHitbox(self):
    self.hitbox = pygame.Rect(self.x,self.y,self.width,self.height)


  # handle collisions
  def check_collision(self, rect):
    self.collision[0] = rect.collidepoint(self.hitbox.topleft)
    self.collision[1] = rect.collidepoint(self.hitbox.topright)
    self.collision[2] = rect.collidepoint(self.hitbox.bottomleft)
    self.collision[3] = rect.collidepoint(self.hitbox.bottomright)
    self.collision[4] = rect.collidepoint(self.hitbox.midleft)
    self.collision[5] = rect.collidepoint(self.hitbox.midright)
    self.collision[6] = rect.collidepoint(self.hitbox.midtop)
    self.collision[7] = rect.collidepoint(self.hitbox.midbottom)
    self.collision[8] = rect.collidepoint(self.hitbox.center)

def clicked(self):
  mouse = pygame.mouse.get_pos()
  if mouse[0] > self.x and mouse[0] < self.x + self.width and mouse[1] > self.y and mouse[1] < self.y + self.height:
    return True

def CollisionGround(Player,Ground):
  Player.check_collision(Ground.hitbox)
  if Player.collision[7]:
    Player.vy = 0
    Player.InAir = False
    Player.y = Ground.y - Player.height
  elif Player.collision[6]:
    Player.y += 2

  if Player.collision[4]:
    Player.x += 1.5
  if Player.collision[5]:
    Player.x -=1.5
    

def GroundHitbox(Ground):
  Ground.hitbox = pygame.Rect(Ground.x,Ground.y,Ground.width,Ground.height)

def EnemyCollision(Enemy):

  global NumScore 
  Player.check_collision(Enemy.hitbox)
  if Player.collision[4] or Player.collision[5]:
    time.sleep(1)
    Player.x = 20
    Player.y = 20
  elif Player.collision[7] and Player.vy > 0:
    Enemy.Defeat = True
    NumScore = NumScore + 1
    Player.vy = -2

#When you collide with an enemy you can't defeat
def EnemyCollision2(Enemy):
  Player.check_collision(Enemy.hitbox)
  if True in Player.collision:
    time.sleep(1)
    Player.x = 20
    Player.y = 20

    
  

#The objects for the title screen
TitleBackground = GameObject(0,0,500,250,"Assets/TitleScreen/TitleAsset.png")
PlayButton = GameObject(210,100,50,30,"Assets/TitleScreen/PlayButton.png")


#The Character slects
SelMario = GameObject(30,90,100,130,"Assets/CharacterSelect/MarioSel.png")

SelLuigi = GameObject(132,90,100,130,"Assets/CharacterSelect/LuigiSel.png")

SelYoshi = GameObject(234,90,100,130,"Assets/CharacterSelect/YoshiSel.png")

SelWario = GameObject(336,90,100,130,"Assets/CharacterSelect/WarioSel.png")

#Level1 setup
Ground1 = GameObject(0,180,200,70,"Assets/Level1/Ground.png")

Ground2 = GameObject(300,160,200,90,"Assets/Level1/Ground.png")

#Level2 setup
Ground3 =GameObject(0,180,500,70,"Assets/Level2/Ground2.png")
Ground4 =GameObject(300,110,200,70,"Assets/Level2/Ground2.png")


#Level3 setup
Ground5 =GameObject(0,180,150,70,"Assets/Level3/Ground3.png")
Ground6 =GameObject(350,180,150,70,"Assets/Level3/Ground3.png")
Ground7 =GameObject(150,225,200,70,"Assets/Level3/Ground3.png")
Water = GameObject(150,180,200,50,"Assets/Level3/Water.png")

#Level4 setup
Ground8 =GameObject(0,160,200,90,"Assets/Level4/Ground4.png")
Ground9 =GameObject(350,140,150,110,"Assets/Level4/Ground4.png")

Pipe = GameObject(150,110,50,50,"Assets/Level4/Pipe.png")

#Level5 setup
Ground10 =GameObject(0,160,500,90,"Assets/Level4/Ground4.png")

#Level6 setup
Ground11 =GameObject(0,160,300,90,"Assets/Level6/Ground6.png")
Ground12 =GameObject(300,210,200,80,"Assets/Level6/Ground6.png")
Ceiling =GameObject(0,0,300,50,"Assets/Level6/Ground6Down.png")

#Level7 setup
Ground13 =GameObject(0,210,200,80,"Assets/Level5/Ground5.png")
Ground14 =GameObject(300,170,200,80,"Assets/Level5/Ground5.png")

#Level8 setup
Ground15 =GameObject(-30,200,200,80,"Assets/Level8/Cloud.png")
Ground16 =GameObject(350,150,250,80,"Assets/Level8/Cloud.png")

#Level9 setup
Ground17 =GameObject(0,200,100,50,"Assets/Level9/Level9Ground.png")
Ground18 =GameObject(400,100,100,150,"Assets/Level9/Level9Ground.png")
Ground19 =GameObject(200,100,100,50,"Assets/Level9/Level9Ground.png")
Ground20 =GameObject(50,200,400,50,"Assets/Level10/Ground10.png")
Ground21 =GameObject(0,140,50,110,"Assets/Level10/Ground10.png")

#Characters
Player = GameObject(20,20,42,90,"Assets/Characters/Mario.png")

#Backgrounds
Level1Background = GameObject(0,0,500,250,"Assets/Backgrounds/Level1Background.png")
Level2Background = GameObject(0,0,500,250,"Assets/Backgrounds/Level2Background.png")
Level3Background = GameObject(0,0,500,250,"Assets/Backgrounds/Level3Background.png")
Level4Background = GameObject(0,0,500,250,"Assets/Backgrounds/Level4Background.png")
Level5Background = GameObject(0,0,500,250,"Assets/Backgrounds/Level5Background.png")
Level7Background = GameObject(0,0,500,250,"Assets/Backgrounds/Level7Background.png")


#Enemies
Goomba = GameObject(300,115,45,45,"Assets/Enemies/Goomba.png")
Koopa = GameObject(200,90,42,90,"Assets/Enemies/Koopa.png")
Cheep = GameObject(275,175,50,40,"Assets/Enemies/CheepCheep.png")
Piranha = GameObject(155,50,36,64,"Assets/Enemies/Piranha.png")
Spiny = GameObject(400,Ground12.y - 45,57,45,"Assets/Enemies/Spiny.png")

Kong = GameObject(350,Ground10.y - 112,88,112,"Assets/Enemies/DKEVIL.png")
KongGood = GameObject(20,Ground10.y - 112,88,112,"Assets/Enemies/Kong.png")
MontyMole = GameObject(350,Ground14.y - 45,45,45,"Assets/Enemies/MontyMole.png")

Lakitu = GameObject(200,100, 90,93,"Assets/Enemies/Lakitu.png")
DryBones = GameObject(225,Ground19.y-90,42,90,"Assets/Enemies/DryBones.png")

Bowser = GameObject(350,Ground20.y- 180,180,180,"Assets/Enemies/Bowser.png")

#Flag
Flag1 = GameObject(450,70,50,90,"Assets/OtherAssets/Flag.png")

#Replay
Replay = GameObject(200,100,100,100,"Assets/OtherAssets/Replay.png")

#Runs the code
running = True

#Enemy vx
Goomba.vx = 0.1
Koopa.vx = 0.2
Cheep.vx = -0.2
Piranha.vy = 0.6
Kong.vx = -0.3
Spiny.vx = -0.1
MontyMole.vx = -0.2
Lakitu.vy = 0.2
DryBones.vy = 0.2
Ground19.vy = 0.2
Bowser.vx = -0.7

#The main game loop
while running == True:
  Clock.tick(200)

  EndFont = TitleFont.render("You Won! Your score was " + str(NumScore),False,(0,0,255))

  #Moves Bowser
  Bowser.x += Bowser.vx
  if Bowser.x < 50:
    Bowser.vx = 0.7
  elif Bowser.x > 350:
    Bowser.vx = -0.7

  #Moves the Goomba
  Goomba.x += Goomba.vx
  if Goomba.x < 300:
    Goomba.vx = 0.1
  elif Goomba.x > 400:
    Goomba.vx = -0.1

  #Moves Ground19
  Ground19.y += Ground19.vy
  if Ground19.y < 100:
    Ground19.vy = 0.2
  if Ground19.y > 200:
    Ground19.vy = -0.2

  #Moves DryBones
  DryBones.y += DryBones.vy
  if DryBones.y < 100:
    DryBones.vy = 0.2
  if DryBones.y > 200:
    DryBones.vy = -0.2

  #Moves the Mole
  MontyMole.x += MontyMole.vx
  if MontyMole.x < 300:
    MontyMole.vx = 0.2
  elif MontyMole.x > 350:
    MontyMole.vx = -0.2

  #Moves the Lakitu
  Lakitu.y += Lakitu.vy
  if Lakitu.y > 100:
    Lakitu.vy = -0.2
  if Lakitu.y < 0:
    Lakitu.vy = 0.2

  #Moves DK
  Kong.x += Kong.vx
  if Kong.x > 350:
    Kong.vx = -0.3
  elif Kong.x < 200:
    Kong.vx = 0.3

  #Moves the Koopa
  Koopa.x += Koopa.vx
  if Koopa.x < 200:
    Koopa.vx = 0.2
  elif Koopa.x > 300:
    Koopa.vx = -0.2

  #Moves the Cheep
  Cheep.x += Cheep.vx
  if Cheep.x < 170:
    Cheep.vx = 0.2
  elif Cheep.x > 300:
    Cheep.vx = -0.2

  #Moves the Piranha
  Piranha.y += Piranha.vy
  if Piranha.y < 50:
    Piranha.vy = 0.6
  elif Piranha.y > 175:
    Piranha.vy = -0.6

  #Moves the Spiny
  Spiny.x += Spiny.vx
  if Spiny.x < 300:
    Spiny.vx = 0.1
  elif Spiny.x > 400:
    Spiny.vx = -0.1

  #Player vx and hitbox
  Player.x += Player.vx
  Player.UpdateHitbox()

  #When to show something
  if level == 0 or level == 0.5:
    Goomba.Show = False
    Goomba.Defeat = False
  if level == 1 and Goomba.Defeat == False:
    Goomba.Show = True
  if level == 2:
    Goomba.Show = False
  if Goomba.Defeat == True:
    Goomba.Show = False

  if level == 0 or level == 0.5:
    Koopa.Show = False
    Koopa.Defeat = False
  if level == 2 and Koopa.Defeat == False:
    Koopa.Show = True
  if level == 3:
    Koopa.Show = False
  if Koopa.Defeat == True:
    Koopa.Show = False

  if level == 0 or level == 0.5:
    Kong.Show = False
    Kong.Defeat = False
  if level == 5 and Kong.Defeat == False:
    Kong.Show = True
  if level == 6:
    Kong.Show = False
  if Kong.Defeat == True:
    Kong.Show = False

  if level == 0 or level == 0.5:
    MontyMole.Show = False
    MontyMole.Defeat = False
  if level == 7 and MontyMole.Defeat == False:
    MontyMole.Show = True
  if level == 8:
    MontyMole.Show = False
  if MontyMole.Defeat == True:
    MontyMole.Show = False

  if level == 0 or level == 0.5:
    Lakitu.Show = False
    Lakitu.Defeat = False
  if level == 8 and Lakitu.Defeat == False:
    Lakitu.Show = True
  if level == 9:
    Lakitu.Show = False
  if Lakitu.Defeat == True:
    Lakitu.Show = False

  if level == 0 or level == 0.5:
    DryBones.Show == False
    DryBones.Defeat = False
  if level == 9 and DryBones.Defeat == False:
    DryBones.Show = True
  if level == 10:
    DryBones.Show = False
  if DryBones.Defeat == True:
    DryBones.Show = False

  if level == 0 or level == 0.5:
    Bowser.Show == False
    DryBones.Defeat = False
  if level == 10 and Bowser.Defeat == False:
    Bowser.Show = True
  if level == 11:
    Bowser.Show = False
  if Bowser.Defeat == True:
    Bowser.Show = False


  
  #The event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    #Arrow keys
    if event.type == KEYDOWN:
      if event.key == K_RIGHT and level != 0 and level != 0.5 and level != 11:
        Player.vx = 1.5
        Player.FacingRight = True
      if event.key == K_LEFT and level != 0 and level != 0.5 and level != 11:
        Player.vx = -1.5
        Player.FacingRight = False
      if event.key == K_UP and level != 0 and level != 0.5 and level != 11:
        if Player.InAir == False:          
          Player.y -= 1
          Player.UpdateHitbox()

          if Character == "Mario":
            Player.vy = -3
          elif Character == "Luigi":
            Player.vy = -3.5
          elif Character == "Yoshi":
            Player.vy = -3
          elif Character == "Wario":
            Player.vy = -3
          

         
    if event.type == KEYUP:
      if event.key == K_RIGHT:
        Player.vx = 0
      if event.key == K_LEFT:
        Player.vx = 0

    #Handles the buttons
    if event.type == pygame.MOUSEBUTTONDOWN:

      #If you click the playbutton
      if clicked(PlayButton) == True and level == 0:
        level = 0.5

      #If you select Mario
      elif clicked(SelMario) == True and level == 0.5:
        level = 1
        Character = "Mario"
        print("You are now "+ Character)

      #If you select Luigi
      elif clicked(SelLuigi) == True and level == 0.5:
        level = 1
        Character = "Luigi"
        print("You are now "+ Character)

      #If you select Luigi
      elif clicked(SelYoshi) == True and level == 0.5:
        level = 1
        Character = "Yoshi"
        print("You are now "+ Character)

      elif clicked(SelWario) == True and level == 0.5:
        level = 1
        Character = "Wario"
        print("You are now "+ Character)


      elif clicked(Replay) == True and level == 11:
        level = 0

        

  if Character == "Mario":
    Player.img = pygame.image.load("Assets/Characters/Mario.png")
    Player.img = pygame.transform.scale(Player.img,    (42,90))
    Player.img_flip = pygame.transform.flip(Player.img, True, False)
  if Character == "Luigi":
    Player.img = pygame.image.load("Assets/Characters/Luigi.png")
    Player.img = pygame.transform.scale(Player.img,    (42,93))
    Player.img_flip = pygame.transform.flip(Player.img, True, False)
  if Character == "Yoshi":
    Player.img = pygame.image.load("Assets/Characters/Yoshi.png")
    Player.img = pygame.transform.scale(Player.img,    (60,90))
    Player.img_flip = pygame.transform.flip(Player.img, True, False)

  if Character == "Wario":
    Player.img = pygame.image.load("Assets/Characters/Wario.png")
    Player.img = pygame.transform.scale(Player.img,    (48,90))
    Player.img_flip = pygame.transform.flip(Player.img, True, False)
    

  #Draws stuff at the title screen
  if level == 0:
    NumScore = 0
    KongHealth = 3
    BowserHealth = 5
    screen.fill((0,255,255))
    screen.blit(TitleBackground.img,(TitleBackground.x,TitleBackground.y))
    screen.blit(Title2,(127,30))
    screen.blit(Title,(130,30))
    screen.blit(PlayButton.img,(PlayButton.x,PlayButton.y))

    Goomba.Defeat = False
    Koopa.Defeat = False
    MontyMole.Defeat = False
    Bowser.Defeat = False
    Kong.Defeat = False

  #Character select screen
  if level == 0.5:
    screen.fill((0,255,255))
    screen.blit(CYF2,(103,30))
    screen.blit(CYF,(105,30))

    #Create a panel
    Panel = pygame.Rect(0,60,500,180)
    pygame.draw.rect(screen,(50,50,50),Panel)

    #Draw the selects
    screen.blit(SelMario.img,(SelMario.x,SelMario.y))
    screen.blit(SelLuigi.img,(SelLuigi.x,SelLuigi.y))
    screen.blit(SelYoshi.img,(SelYoshi.x,SelYoshi.y))
    screen.blit(SelWario.img,(SelWario.x,SelWario.y))

  #When the level is 1
  if level == 1:

    #Show this
    screen.fill((0,255,255))
    screen.blit(Level1Background.img,(Level1Background.x,Level1Background.y))
    screen.blit(Ground1.img,(Ground1.x,Ground1.y))
    GroundHitbox(Ground1)
    screen.blit(Flag1.img,(Flag1.x,Flag1.y))

    #Everything for the goomba
    screen.blit(Ground2.img,(Ground2.x,Ground2.y))
    if Goomba.Show == True:
      screen.blit(Goomba.img,(Goomba.x,Goomba.y))
      Goomba.UpdateHitbox()
      EnemyCollision(Goomba)
      
    #Gravity Stuff
    collide_platform = False
    CollisionGround(Player,Ground1)
    collide_platform = True in Player.collision

    CollisionGround(Player,Ground2)
    if not collide_platform:
      collide_platform = True in Player.collision

    if collide_platform == False:
      Player.InAir = True
      #Player.vy = -0.2
  
    if Player.InAir == True:
      Player.vy = Player.vy + Gravity
    Player.y += Player.vy
    
  if level == 2:
    screen.fill((0,255,255))
    screen.blit(Level2Background.img,(Level2Background.x,Level2Background.y))
    screen.blit(Ground3.img,(Ground3.x,Ground3.y))
    screen.blit(Ground4.img,(Ground4.x,Ground4.y))
    screen.blit(Flag1.img,(450,Ground4.y - Flag1.height))

    if Koopa.Show == True:
      screen.blit(Koopa.img,(Koopa.x,Koopa.y))
      Koopa.UpdateHitbox()
      EnemyCollision(Koopa)
    #Gravity Stuff
    collide_platform = False
    CollisionGround(Player,Ground3)
    collide_platform = True in Player.collision

    CollisionGround(Player,Ground4)
    if not collide_platform:
      collide_platform = True in Player.collision

    if collide_platform == False:
      Player.InAir = True
      #Player.vy = -0.2

    if Player.InAir == True:
      Player.vy = Player.vy + Gravity
    Player.y += Player.vy

  if level == 3:
    screen.fill((0,255,255))
    screen.blit(Level3Background.img,(Level3Background.x,Level3Background.y))
    screen.blit(Water.img,(Water.x,Water.y))
    screen.blit(Ground5.img,(Ground5.x,Ground5.y))
    screen.blit(Ground6.img,(Ground6.x,Ground6.y))
    screen.blit(Ground7.img,(Ground7.x,Ground7.y))

    screen.blit(Flag1.img,(Flag1.x,Ground6.y-Flag1.height))

    screen.blit(Cheep.img,(Cheep.x,Cheep.y))
    EnemyCollision2(Cheep)
    Cheep.UpdateHitbox()

    #Gravity Stuff
    collide_platform = False
    CollisionGround(Player,Ground5)
    collide_platform = True in Player.collision

    CollisionGround(Player,Ground6)
    if not collide_platform:
      collide_platform = True in Player.collision

    CollisionGround(Player,Ground7)
    if not collide_platform:
      collide_platform = True in Player.collision

    if collide_platform == False:
      Player.InAir = True
      #Player.vy = -0.2
  

    Player.check_collision(Water.hitbox)
    if Player.InAir == True and not(True in Water.collision):
      Player.vy = Player.vy + Gravity
    
    
    if Player.InAir == True and True in Water.collision:
      Player.vy = Player.vy + Gravity2

    Player.y += Player.vy

  if level == 4:
    screen.fill((0,255,255))
    screen.blit(Level4Background.img,(Level4Background.x,Level4Background.y))
    
    screen.blit(Piranha.img,(Piranha.x,Piranha.y))
    EnemyCollision2(Piranha)
    Piranha.UpdateHitbox()

    screen.blit(Flag1.img,(Flag1.x,Ground9.y - Flag1.height))
    
    screen.blit(Ground8.img,(Ground8.x,Ground8.y))
    screen.blit(Ground9.img,(Ground9.x,Ground9.y))
    
    
    
    screen.blit(Pipe.img,(Pipe.x,Pipe.y))

    

    #Gravity Stuff
    collide_platform = False
    CollisionGround(Player,Ground8)
    collide_platform = True in Player.collision

    CollisionGround(Player,Ground9)
    if not collide_platform:
      collide_platform = True in Player.collision

    CollisionGround(Player,Pipe)
    if not collide_platform:
      collide_platform = True in Player.collision

    if collide_platform == False:
      Player.InAir = True
      #Player.vy = -0.2

    if Player.InAir == True:
      Player.vy = Player.vy + Gravity
    Player.y += Player.vy

  if level == 5:
    #print(KongHealth)
    screen.fill((0,255,255))
    screen.blit(Level5Background.img,(Level5Background.x,Level5Background.y))
    screen.blit(Ground10.img,(Ground10.x,Ground10.y))
    

    

    if Kong.Show == True:
      Kong.UpdateHitbox()
      screen.blit(Kong.img,(Kong.x,Kong.y))
      Player.check_collision(Kong.hitbox)
      if Player.collision[4] or Player.collision[5]:
        time.sleep(1)
        Player.x = 20
        Player.y = 20
      elif Player.collision[7] and Player.vy > 0:
        KongHealth = KongHealth - 1
        Player.vy = -2
        #Player.x -= 100
      if KongHealth <= 0:
        Kong.Defeat = True
        NumScore = NumScore + 2
    
    
    if Kong.Defeat == True:
      screen.blit(KongGood.img,(KongGood.x,KongGood.y))
      screen.blit(Flag1.img,(Flag1.x,Ground10.y-Flag1.height))

    collide_platform = False
    CollisionGround(Player,Ground10)
    collide_platform = True in Player.collision

    if collide_platform == False:
      Player.InAir = True
      #Player.vy = -0.2

    if Player.InAir == True:
      Player.vy = Player.vy + Gravity
    Player.y += Player.vy
      
  if level == 6:
    screen.fill((0,0,30))

    screen.blit(Ground11.img,(Ground11.x,Ground11.y))
    screen.blit(Ground12.img,(Ground12.x,Ground12.y))
    screen.blit(Ceiling.img,(Ceiling.x,Ceiling.y))
    

    screen.blit(Flag1.img,(Flag1.x,Ground12.y - Flag1.height))

    screen.blit(Spiny.img,(Spiny.x,Spiny.y))
    Spiny.UpdateHitbox()
    EnemyCollision2(Spiny)

    Ceiling.hitbox = pygame.Rect(Ceiling.x,Ceiling.y,Ceiling.width+25,Ceiling.height)

    Player.check_collision(Ceiling.hitbox)
    if Player.collision[6]:
      Player.vy += 2
    if Player.collision[4]:
      Player.x += 5

    collide_platform = False
    CollisionGround(Player,Ground11)
    collide_platform = True in Player.collision

    CollisionGround(Player,Ground12)
    if not collide_platform:
      collide_platform = True in Player.collision

    if collide_platform == False:
      Player.InAir = True
      #Player.vy = -0.2

    if Player.InAir == True:
      Player.vy = Player.vy + Gravity
    Player.y += Player.vy

  if level == 7:
    screen.fill((0,255,255))
    screen.blit(Level7Background.img,(Level7Background.x,Level7Background.y))
    screen.blit(Ground13.img,(Ground13.x,Ground13.y))
    screen.blit(Ground14.img,(Ground14.x,Ground14.y))
    screen.blit(Flag1.img,(Flag1.x,Ground14.y - Flag1.height))

    if MontyMole.Show == True:
      screen.blit(MontyMole.img,(MontyMole.x,MontyMole.y))
      MontyMole.UpdateHitbox()
      EnemyCollision(MontyMole)

    collide_platform = False
    CollisionGround(Player,Ground13)
    collide_platform = True in Player.collision

    CollisionGround(Player,Ground14)
    if not collide_platform:
      collide_platform = True in Player.collision

    if collide_platform == False:
      Player.InAir = True
      #Player.vy = -0.2

    if Player.InAir == True:
      Player.vy = Player.vy + Gravity
    Player.y += Player.vy


  if level == 8:
    screen.fill((0,255,255))
    screen.blit(Ground15.img,(Ground15.x,Ground15.y))
    screen.blit(Ground16.img,(Ground16.x,Ground16.y))
    screen.blit(Flag1.img,(Flag1.x,Ground16.y - Flag1.height))

    if Lakitu.Show == True:
      screen.blit(Lakitu.img,(Lakitu.x,Lakitu.y))
      Lakitu.UpdateHitbox()
      EnemyCollision(Lakitu)

    collide_platform = False
    CollisionGround(Player,Ground15)
    collide_platform = True in Player.collision

    CollisionGround(Player,Ground16)
    if not collide_platform:
      collide_platform = True in Player.collision

    if collide_platform == False:
      Player.InAir = True
      #Player.vy = -0.2

    if Player.InAir == True:
      Player.vy = Player.vy + Gravity
    Player.y += Player.vy

  if level == 9:
    screen.fill((0,50,50))
    screen.blit(Flag1.img,(Flag1.x,Ground18.y-Flag1.height))
    Lava = pygame.Rect(100,225,500,25)
    pygame.draw.rect(screen,[255,164,0],Lava)

    
    screen.blit(Ground18.img,(Ground18.x,Ground18.y))
    screen.blit(Ground17.img,(Ground17.x,Ground17.y))

    if DryBones.Show == True:
      screen.blit(DryBones.img,(DryBones.x,Ground19.y-DryBones.height))
      DryBones.hitbox = pygame.Rect(DryBones.x,Ground19.y-DryBones.height,DryBones.width,DryBones.height)
      EnemyCollision(DryBones)
      

    Ground19.UpdateHitbox()
    screen.blit(Ground19.img,(Ground19.x,Ground19.y))
    
    

    collide_platform = False
    CollisionGround(Player,Ground17)
    collide_platform = True in Player.collision

    CollisionGround(Player,Ground18)
    if not collide_platform:
      collide_platform = True in Player.collision
    CollisionGround(Player,Ground19)
    if not collide_platform:
      collide_platform = True in Player.collision

    if collide_platform == False:
      Player.InAir = True
      #Player.vy = -0.2

    if Player.InAir == True:
      Player.vy = Player.vy + Gravity
    Player.y += Player.vy
    
  if level == 10:
    screen.fill((0,0,0))
    screen.blit(Ground20.img,(Ground20.x,Ground20.y))
    screen.blit(Ground21.img,(Ground21.x,Ground21.y))
    Lava2 = pygame.Rect(0,225,500,25)
    pygame.draw.rect(screen,[255,164,0],Lava2)

    if Bowser.Show == True:
      screen.blit(Bowser.img,(Bowser.x,Bowser.y))
      Bowser.UpdateHitbox()
      Player.check_collision(Bowser.hitbox)
      if Player.collision[4] or Player.collision[5]:
        time.sleep(1)
        Player.x = 0
        Player.y = 20
      elif Player.collision[7] and Player.vy > 0:
        BowserHealth = BowserHealth - 1
        Player.vy = -2
        #Player.x -= 100
      if BowserHealth <= 0:
        Bowser.Defeat = True
        NumScore = NumScore + 2
        level = 11
        Player.x = 20
        Player.y = 20
      if level == 0 or level == 0.5:
        Player.x = 20
        Player.y = 20

    collide_platform = False
    CollisionGround(Player,Ground20)
    collide_platform = True in Player.collision

    CollisionGround(Player,Ground21)
    if not collide_platform:
      collide_platform = True in Player.collision

    if collide_platform == False:
      Player.InAir = True
      #Player.vy = -0.2

    if Player.InAir == True:
      Player.vy = Player.vy + Gravity
    Player.y += Player.vy

  if level == 11:
    screen.fill((50,50,50))
    screen.blit(EndFont,(70,20))

    screen.blit(Replay.img,(Replay.x,Replay.y))
    


  #For all levels
  if level >= 1 and level < 11:
    Rectangle = pygame.Rect(10,10,100,40)


    if Player.FacingRight == True:     
      screen.blit(Player.img,(Player.x,Player.y))
    else:
      screen.blit(Player.img_flip,(Player.x,Player.y))
      

    #Show the text
    pygame.draw.rect(screen,[150,150,150],Rectangle)
    ScoreText = ScoreFont.render("Score: "+ str(NumScore),False,(0,0,0))
    screen.blit(ScoreText,(20,20))
    
    if Player.y > 450:
      Player.x = 20
      Player.y = 20
    if Player.x <= 0:
      Player.x += 1.5
    if Player.x >= 450:
      Player.x -= 1.5

    Player.check_collision(Flag1.hitbox)
    if True in Player.collision:
      if level == 1:
        Player.x = 20
        Player.y = 20
        level = 2
      elif level == 2:
        Player.x = 20
        Player.y = 20
        level = 3
      elif level == 3:
        Player.x = 20
        Player.y = 20
        level = 4
      elif level == 4:
        Player.x = 20
        Player.y = 20
        level = 5
      elif level == 5 and Kong.Defeat == True:
        Player.x = 20
        Player.y = 20
        level = 6
      elif level == 6:
        Player.x = 20
        Player.y = 20
        level = 7
      elif level == 7:
        Player.x = 20
        Player.y = 20
        level = 8
      elif level == 8:
        Player.x = 20
        Player.y = 20
        level = 9
      elif level == 9:
        Player.x = 0
        Player.y = 20
        level = 10
        
    
  #Draws EVERYTHING
  pygame.display.flip()

#When loop is done, the game ends
pygame.quit()