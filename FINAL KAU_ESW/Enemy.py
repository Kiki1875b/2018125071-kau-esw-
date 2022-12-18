
import random
import numpy as np

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

class Enemy:
    def __init__(self, spawn_position):
        self.appearance = 'circle'
        self.spawn_position = spawn_position
        self.state = 'alive'
        self.speed = 10
        self.dead_position = np.array([0,0,0,0])
        self.position = np.array([spawn_position[0],spawn_position[1],spawn_position[2],spawn_position[3]])
        self.outline = "#000000"
        self.direction ={'up':False, 'down':False, 'left':False,'right':False}
        num = random.randint(0,3)
        if num == 0:
            self.direction['up'] = True
        elif num == 1: 
            self.direction['down'] = True
        elif num == 2:
            self.direction['left'] = True
        else:
            self.direction['right'] = True


        

    def move(self):
        if(self.spawn_position == (120,120,130,130)):

            if self.direction['up']:
                a = self.position 
                center_x = round((a[0]+5)/10)
                center_y = round((a[1])/10)
                b = mat_matrix[center_y-1,center_x]
                if(b == 1):
                    self.direction['up'] = False
                    self.direction['right'] = True
                else:
                    self.position[1] -= self.speed
                    self.position[3] -= self.speed
            elif self.direction['down']:
                a = self.position 
                center_x = round((a[0]+5)/10)
                center_y = round((a[1])/10)
                b = mat_matrix[center_y+1,center_x]
                if(b == 1):
                    self.direction['down'] = False
                    self.direction['left'] = True
                else:
                    self.position[1]+= self.speed
                    self.position[3]+= self.speed
            elif self.direction['left']:
                a = self.position 
                center_x = round(a[0]/10)
                center_y = round((a[1]+5)/10)
                b = mat_matrix[center_y,center_x-1]
                if(b == 1):
                    self.direction['left'] = False
                    self.direction['up'] = True
                else:
                    self.position[0] -= self.speed
                    self.position[2] -= self.speed
            elif self.direction['right']:
                a = self.position + 10
                center_x = round(a[2]/10)
                center_y = round((a[1]+5)/10)
                b = mat_matrix[center_y,center_x]
                if(b == 1):
                    self.direction['right'] = False
                    self.direction['down'] = True
                else:
                    self.position[0] += self.speed
                    self.position[2] += self.speed
        elif(self.spawn_position == (90,170,100,180)):           #enemy 2 
            if self.direction['up']:
                a = self.position 
                center_x = round((a[0]+5)/10)
                center_y = round((a[1])/10)
                b = mat_matrix[center_y-1,center_x]
                if(b == 1):
                    self.direction['up'] = False
                    self.direction['right'] = True
                else:
                    if (self.position[0] == 10 and self.position[1]==180):
                        self.direction['right'] = True
                        self.direction['up'] = False
                    self.position[1] -= self.speed
                    self.position[3] -= self.speed
            elif self.direction['down']:
                a = self.position 
                center_x = round((a[0]+5)/10)
                center_y = round((a[1])/10)
                b = mat_matrix[center_y+1,center_x]
                if(b == 1):
                    self.direction['down'] = False
                    self.direction['left'] = True
                else:
                    self.position[1]+= self.speed
                    self.position[3]+= self.speed
            elif self.direction['left']:
                a = self.position 
                center_x = round(a[0]/10)
                center_y = round((a[1]+5)/10)
                b = mat_matrix[center_y,center_x-1]
                if(b == 1):
                    self.direction['left'] = False
                    self.direction['up'] = True
                else:
                    self.position[0] -= self.speed
                    self.position[2] -= self.speed
            elif self.direction['right']:
                a = self.position + 10
                center_x = round(a[2]/10)
                center_y = round((a[1]+5)/10)
                b = mat_matrix[center_y,center_x]
                if(b == 1):
                    self.direction['right'] = False
                    self.direction['down'] = True
                else:
                    self.position[0] += self.speed
                    self.position[2] += self.speed
        elif(self.spawn_position == (90,50,100,60)):           #enemy 3
            if self.direction['up']:
                a = self.position 
                center_x = round((a[0]+5)/10)
                center_y = round((a[1])/10)
                b = mat_matrix[center_y-1,center_x]
                if(b == 1):
                    self.direction['up'] = False
                    self.direction['right'] = True
                else:
                    if (self.position[0] == 10 and self.position[1]==180):
                        self.direction['right'] = True
                        self.direction['up'] = False
                    self.position[1] -= self.speed
                    self.position[3] -= self.speed
            elif self.direction['down']:
                a = self.position 
                center_x = round((a[0]+5)/10)
                center_y = round((a[1])/10)
                b = mat_matrix[center_y+1,center_x]
                if(b == 1):
                    self.direction['down'] = False
                    self.direction['left'] = True
                else:
                    self.position[1]+= self.speed
                    self.position[3]+= self.speed
            elif self.direction['left']:
                a = self.position 
                center_x = round(a[0]/10)
                center_y = round((a[1]+5)/10)
                b = mat_matrix[center_y,center_x-1]
                if(b == 1):
                    self.direction['left'] = False
                    self.direction['up'] = True
                else:
                    self.position[0] -= self.speed
                    self.position[2] -= self.speed
            elif self.direction['right']:
                a = self.position + 10
                center_x = round(a[2]/10)
                center_y = round((a[1]+5)/10)
                b = mat_matrix[center_y,center_x]
                if(b == 1):
                    self.direction['right'] = False
                    self.direction['down'] = True
                else:
                    if(self.position[0]==90 and self.position[1]==10):
                        self.direction['right'] = False
                        self.direction['down'] = True
                    self.position[0] += self.speed
                    self.position[2] += self.speed   
        elif(self.spawn_position == (140,50,150,60)):           #enemy 4
            if self.direction['up']:
                a = self.position 
                center_x = round((a[0]+5)/10)
                center_y = round((a[1])/10)
                b = mat_matrix[center_y-1,center_x]
                if(b == 1):
                    self.direction['up'] = False
                    self.direction['right'] = True
                else:
                    if (self.position[0] == 10 and self.position[1]==180):
                        self.direction['right'] = True
                        self.direction['up'] = False
                    self.position[1] -= self.speed
                    self.position[3] -= self.speed
            elif self.direction['down']:
                a = self.position 
                center_x = round((a[0]+5)/10)
                center_y = round((a[1])/10)
                b = mat_matrix[center_y+1,center_x]
                if(b == 1):
                    self.direction['down'] = False
                    self.direction['left'] = True
                else:
                    if(self.position[0]==210 and self.position[1]==50):
                        self.direction['down'] = False
                        self.direction['left'] = True
                    self.position[1]+= self.speed
                    self.position[3]+= self.speed
            elif self.direction['left']:
                a = self.position 
                center_x = round(a[0]/10)
                center_y = round((a[1]+5)/10)
                b = mat_matrix[center_y,center_x-1]
                if(b == 1):
                    self.direction['left'] = False
                    self.direction['up'] = True
                else:
                    self.position[0] -= self.speed
                    self.position[2] -= self.speed
            elif self.direction['right']:
                a = self.position + 10
                center_x = round(a[2]/10)
                center_y = round((a[1]+5)/10)
                b = mat_matrix[center_y,center_x]
                if(b == 1):
                    self.direction['right'] = False
                    self.direction['down'] = True
                else:
                    if(self.position[0]==90 and self.position[1]==10):
                        self.direction['right'] = False
                        self.direction['down'] = True
                    self.position[0] += self.speed
                    self.position[2] += self.speed      
        elif(self.spawn_position == (140,170,150,180)):           #enemy 5
            if self.direction['up']:
                a = self.position 
                center_x = round((a[0]+5)/10)
                center_y = round((a[1])/10)
                b = mat_matrix[center_y-1,center_x]
                if(b == 1):
                    self.direction['up'] = False
                    self.direction['right'] = True
                else:
                    if (self.position[0] == 10 and self.position[1]==180):
                        self.direction['right'] = True
                        self.direction['up'] = False
                    self.position[1] -= self.speed
                    self.position[3] -= self.speed
            elif self.direction['down']:
                a = self.position 
                center_x = round((a[0]+5)/10)
                center_y = round((a[1])/10)
                b = mat_matrix[center_y+1,center_x]
                if(b == 1):
                    self.direction['down'] = False
                    self.direction['left'] = True
                else:
                    self.position[1]+= self.speed
                    self.position[3]+= self.speed
            elif self.direction['left']:
                a = self.position 
                center_x = round(a[0]/10)
                center_y = round((a[1]+5)/10)
                b = mat_matrix[center_y,center_x-1]
                if(b == 1):
                    self.direction['left'] = False
                    self.direction['up'] = True
                else:
                    if(self.position[0]==140 and self.position[1]==220):
                        self.direction['left'] = False
                        self.direction['up']=True
                    self.position[0] -= self.speed
                    self.position[2] -= self.speed
            elif self.direction['right']:
                a = self.position + 10
                center_x = round(a[2]/10)
                center_y = round((a[1]+5)/10)
                b = mat_matrix[center_y,center_x]
                if(b == 1):
                    self.direction['right'] = False
                    self.direction['down'] = True
                else:
                    if(self.position[0]==90 and self.position[1]==10):
                        self.direction['right'] = False
                        self.direction['down'] = True
                    self.position[0] += self.speed
                    self.position[2] += self.speed
        elif(self.spawn_position == (110, 90, 120, 100)):   #Enemy 6
            self.direction['left'] = True
            if self.direction['right']:
                a = self.position + 10
                center_x = round(a[2]/10)
                center_y = round((a[1]+5)/10)
                b = mat_matrix[center_y,center_x]
                if(b == 1):
                    self.direction['right'] = False
                    self.direction['left'] = True
                else:
                    self.position[0] += self.speed
                    self.position[2] += self.speed
            elif self.direction['left']:
                a = self.position 
                center_x = round(a[0]/10)
                center_y = round((a[1]+5)/10)
                b = mat_matrix[center_y,center_x-1]
                if(b == 1):
                    self.direction['left'] = False
                    self.direction['right'] = True
                else:
                    self.position[0] -= self.speed
                    self.position[2] -= self.speed
            
        elif(self.spawn_position == (150, 130, 160, 140)): #Enemy 7
            self.direction['right'] = True
            if self.direction['left']:
                a = self.position 
                center_x = round(a[0]/10)
                center_y = round((a[1]+5)/10)
                b = mat_matrix[center_y,center_x-1]
                if(b == 1):
                    self.direction['left'] = False
                    self.direction['right'] = True
                else:
                    self.position[0] -= self.speed
                    self.position[2] -= self.speed
            elif self.direction['right']:
                a = self.position + 10
                center_x = round(a[2]/10)
                center_y = round((a[1]+5)/10)
                b = mat_matrix[center_y,center_x]
                if(b == 1):
                    self.direction['right'] = False
                    self.direction['left'] = True
                else:
                    self.position[0] += self.speed
                    self.position[2] += self.speed

            
        