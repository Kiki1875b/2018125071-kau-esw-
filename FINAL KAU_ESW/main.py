from Joystick import Joystick
from Character import Character
from Enemy import Enemy
from PIL import Image, ImageDraw, ImageFont
from GameOver import GameOver
from GameStart import GameStart
from Bullet import Bullet
import time
import random
import numpy as np
from colorsys import hsv_to_rgb
import copy


my_image=Image.new("RGBA",(240,240))
my_draw = ImageDraw.Draw(my_image)

class Food:
    def __init__(self):
        self.score = 10
        self.position = (0,0,0,0)
        self.status = 'exist'
        self.state = None
        self.count = 0

    def make_food(self,draw):
        if(self.status == 'exist' and self.count == 0):
            position1 = (15,15,17,17)
            position2 = (215, 16, 217, 18)
            position3 = (215, 201, 217, 203)
            position4 = (15,201,17,203)
            num = random.randint(0,3)
            if(num == 0):
                self.position = position1
                draw.ellipse(tuple(self.position), outline=(255,255,255),fill = (255,255,0))
                self.count +=1
            elif(num ==1):
                self.position = position2
                draw.ellipse(tuple(self.position), outline=(255,255,255),fill = (255,255,0))
                self.count += 1
            elif(num ==2):
                self.position = position3
                draw.ellipse(tuple(self.position), outline=(255,255,255),fill = (255,255,0))

                self.count += 1
            else:
                self.position = position4
                draw.rectangle(tuple(self.position), outline=(255,255,255),fill = (255,255,0))
                self.count += 1

    def eat_food(self,character):
        eat = self.overlap(self.position, character.position)
        
        if eat:
            character.score += self.score
            self.status = 'nexist'
            self.count = 0
            self.status = 'exist'
            character.count += 1
            my_draw.rectangle(self.position, outline=(0,0,0),width=1)
            

    def overlap(self, position1, position2):
        return position2[2]> position1[0] >position2[0] and position2[3]>position1[1]>position2[1] 

def main():
    joystick = Joystick()                             
    mat_matrix = np.asarray(dtype = np.dtype('uint8'),a=
            [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,0,0,1],
            [1,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1],
            [1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,0,0,1],
            [1,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1],
            [1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,0,0,1],
            [1,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])

    my_image=Image.new("RGBA",(240,240))
    my_draw = ImageDraw.Draw(my_image)
    for i in range(24):
        for j in range(24):
            if(mat_matrix[i][j] == 1):
                new_map = np.asarray(dtype = np.dtype('uint8'),a=
                [[255,255,255,255,255,255,255,255,255,255],
                [255,255,255,255,255,255,255,255,255,255],
                [255,255,255,255,255,255,255,255,255,255],
                [255,255,255,255,255,255,255,255,255,255],
                [255,255,255,255,255,255,255,255,255,255],
                [255,255,255,255,255,255,255,255,255,255],
                [255,255,255,255,255,255,255,255,255,255],
                [255,255,255,255,255,255,255,255,255,255],
                [255,255,255,255,255,255,255,255,255,255],
                [255,255,255,255,255,255,255,255,255,255]])
                test_draw = Image.fromarray(new_map,mode='L').convert('1')
                my_draw.bitmap(((j)*10,(i)*10), test_draw, fill = None)
            else:
                new_map = np.asarray(dtype = np.dtype('uint8'),a=
                [[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]])
                test_draw = Image.fromarray(new_map,mode='L').convert('1')
                my_draw.bitmap(((j)*10,(i)*10), test_draw, fill = None)
    joystick.disp.image(my_image)
           
    fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)
    fnt2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
    back = Image.open('/home/kau-esw/TA-ESW/MY_PRJ/prj_pac.png')
    back.paste(my_image,(240,240))

    instruction = Image.open('TA-ESW/MY_PRJ/ins_pac.png')
    

    joystick = Joystick()
    my_circle = Character(joystick.width, joystick.height)
    enemy_1 = Enemy((120,120,130,130))
    enemy_2 = Enemy((90,170,100,180))
    enemy_3 = Enemy((90,50,100,60))
    enemy_4 = Enemy((140,50,150,60))
    enemy_5 = Enemy((140,170,150,180))
    enemy_6 = Enemy((110, 90, 120, 100))
    enemy_7 = Enemy((150, 130, 160, 140))
    enemylist = [enemy_1,enemy_2,enemy_3,enemy_4,enemy_5]
    bullets =[]
    food = Food()
    gamestart = GameStart()
    gameover = GameOver()
    start_time = 0
    time_now = 0
    speed_count = 0
    respawn_count = 0
    while(gamestart.state == False):
            rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
            joystick.disp.image(back)
            if not joystick.button_A.value: # A pressed
                game_start_time = time.time()
                gamestart.state == True
                break
            if not joystick.button_B.value:
                gamestart.instruction = True
                break
    
    while(gamestart.instruction == True):
        instruction.paste(my_image,(240,240))
        joystick.disp.image(instruction)
        if not joystick.button_A.value:
            game_start_time = time.time()
            gamestart.instruction = False
            break




    while True:
        """
        respawn_count += 1
        if(respawn_count >100): # 죽은 적들 부활 시간
            for enemy in enemylist:
                enemy.state = 'alive'
                respawn_count = 0
        """

        game_end_time = time.time()
        total_game_time = game_end_time - game_start_time

        if(total_game_time > 30 and speed_count == 0): #30초 이후 게임 난이도 증가 
            enemylist.append(enemy_6)
            enemylist.append(enemy_7)
            speed_count += 1
        gameover.check(my_circle)==True

        if(gameover.state == True):#게임 오버
            break
        background = copy.deepcopy(my_image)
        
        count = 0
        command = {'move': False, 'up_pressed': False , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False}
        
        if not joystick.button_U.value:  # up pressed
            command['up_pressed'] = True
            command['move'] = True

        if not joystick.button_D.value:  # down pressed
            command['down_pressed'] = True
            command['move'] = True

        if not joystick.button_L.value:  # left pressed
            command['left_pressed'] = True
            command['move'] = True

        if not joystick.button_R.value:  # right pressed
            command['right_pressed'] = True
            command['move'] = True
        if not joystick.button_A.value: # A pressed
            if(my_circle.count >= 4):
                my_circle.count -= 4
                start_time = time.time()
                for enemy in enemylist:
                    enemy.speed = 0
        if not joystick.button_B.value:
            if(my_circle.count >= 1):
                my_circle.count -= 1
                bullet = Bullet(my_circle.position+4, command)
                bullets.append(bullet)
        for bullet in bullets:
            bullet.collision_check(enemylist)
            bullet.move()
            
    
        if(start_time != 0): #5초동안 적들 움직임 멈춤
            etime = time.time()
            time_now = etime - start_time
        if(time_now > 5):
            for enemy in enemylist:
                enemy.speed = 10
                    
        
        now_draw = ImageDraw.Draw(background)
        
        my_circle.move(command)
        
        
        now_draw.ellipse(tuple(my_circle.position), outline = my_circle.outline, fill = (255,255,0))
        if(enemy_1.state == 'alive'):
            now_draw.ellipse(tuple(enemy_1.position), outline = enemy_1.outline, fill = (128, 0, 128))
        if(enemy_2.state == 'alive'):
            now_draw.ellipse(tuple(enemy_2.position), outline = enemy_2.outline, fill = (0, 0, 255))
        if(enemy_3.state == 'alive'):
            now_draw.ellipse(tuple(enemy_3.position), outline = enemy_3.outline, fill = (255, 105, 180))
        if(enemy_4.state == 'alive'):
            now_draw.ellipse(tuple(enemy_4.position), outline = enemy_4.outline, fill = (128,128,128))
        if(enemy_5.state == 'alive'):
            now_draw.ellipse(tuple(enemy_5.position), outline = enemy_5.outline, fill = (255, 0, 0))
        if(total_game_time>30):
            if(enemy_6.state == 'alive'):
                now_draw.ellipse(tuple(enemy_6.position), outline = enemy_6.outline, fill = (64, 238, 238))
            if(enemy_7.state == 'alive'):
                now_draw.ellipse(tuple(enemy_7.position), outline = enemy_7.outline, fill = (205, 133, 63))
        for bullet in bullets:
            if bullet.state != 'hit':
                now_draw.rectangle(tuple(bullet.position), outline = bullet.outline, fill = (255, 255, 255))
            else:
                bullet.position = np.array([0,0,0,0])
                bullets.remove(bullet)
        for enemy in enemylist:
            if (enemy.state != 'alive'):
                enemy.position = enemy.dead_position


                

        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        now_draw.text((40, 150), "score:{0}".format(my_circle.score), font=fnt, fill=rcolor)
        now_draw.text((140, 150), "TIME: {0}".format(int(total_game_time)), font=fnt, fill=rcolor)
        now_draw.text((40, 110), "A: {0}/4".format(my_circle.count), font=fnt, fill=rcolor)
        now_draw.text((150, 110), "B: {0}/1".format(my_circle.count), font=fnt, fill=rcolor)
        now_draw.text((90, 70), "LIFE: {0}/1".format(my_circle.life), font=fnt, fill=rcolor)
        score = my_circle.score
        
        
        
        count = 1
        for enemy in enemylist:
            my_circle.check_hit(enemy)
        if count != 0:
            enemy_1.move()
            enemy_2.move()
            enemy_3.move()
            enemy_4.move()
            enemy_5.move()
            if(total_game_time>30):
                enemy_6.move()
                enemy_7.move()
                
            if (food.status == 'exist'):
                now_draw.ellipse(food.position, outline=(255,255,255),fill =(255,255,255))
                food.make_food(now_draw)
                food.eat_food(my_circle)
            if(food.count == 0):
                food.status == 'exist'
        joystick.disp.image(background)
        
    while (gameover.state == True):
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        now_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(0, 0, 0, 100))
        now_draw.text((35, 100), "GAME OVER", font=fnt2, fill=rcolor)
        now_draw.text((35, 150), 'SCORE:{0}'.format(score), font=fnt, fill=rcolor)
        now_draw.text((20, 200), 'press A to replay, B to end', font=fnt, fill=rcolor)
        joystick.disp.image(background)
        if not joystick.button_A.value:
            main()
        if not joystick.button_B.value:
            break
            
            


if __name__ == '__main__':
    main()