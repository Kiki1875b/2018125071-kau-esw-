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

class Character:
    def __init__(self, width, height):
        self.appearance = 'circle'
        self.state = None
        self.position = np.array([110 , 110 , 120, 120])
        self.outline = "#FFFFFF"
        self.speed = 10
        self.direction ={'up':False, 'down':False, 'left':False,'right':False}
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.score = 0
        self.count = 0
        self.hit_status = 'False'
        self.life = 2
    
    def check_hit(self, enemy):
        hit = self.overlap(self.position, enemy.position)
        if hit:
            self.life -= 1
            self.position = np.array([110 , 110 , 120, 120])
            if self.life == -1:
                print("game over")
    
    def overlap(self, position1, position2):
        return position2[2]>position1[0]+5>position2[0] and position2[3]>position1[1]+5>position2[1]



    def move(self, command = None):
        if command['move'] == False:
            self.state = None
            self.outline = "#FFFFFF" 
        
        else:
            self.state = 'move'
            self.outline = "#FF0000" 

            if command['up_pressed']:
                a = self.position 
                center_x = round((a[0]+5)/10)
                center_y = round((a[1])/10)
                center_x2 = round(a[0]/10)
                center_x3 = round(a[2]/10)
                
                self.direction['up'] = True
                b = mat_matrix[center_y-1,center_x]
              

                if(self.direction['up'] == True):
                    if(b==1):
                        self.position[1] = self.position[1]
                        self.position[3] = self.position[3]
                        self.direction['up'] = False
                    else:
                        prev_pos = [self.position[0],self.position[1],self.position[2],self.position[3]]
                        self.position[1] -= self.speed
                        self.position[3] -= self.speed
                        

            if command['down_pressed']:
                self.direction['down'] = True
                a = self.position 
                center_x = round((a[0]+5)/10)
                center_y = round((a[3])/10)

                
                b = mat_matrix[center_y+1,center_x]
            
            
                if (self.direction['down'] == True):
                    if(b==1):
                        self.position[1] = self.position[1]
                        self.position[3] = self.position[3]
                        self.direction['down'] = False
                    else:
                        prev_pos = [self.position[0],self.position[1],self.position[2],self.position[3]]
                        self.position[1] += self.speed
                        self.position[3] += self.speed
                        

            if command['left_pressed']:
                self.direction['left'] = True
                a = self.position 
                center_x = round((a[0])/10)
                center_y = round((a[1]+5)/10)
                
               
                b = mat_matrix[center_y,center_x-1]
                
            
                if(self.direction['left'] == True): 
                    if(b==1):
                        self.position[0] = self.position[0]
                        self.position[2] = self.position[2]
                        self.direction['left'] = False
                    else:
                        prev_pos = [self.position[0],self.position[1],self.position[2],self.position[3]]
                        self.position[0] -= self.speed
                        self.position[2] -= self.speed
                        
            if command['right_pressed']:
                self.direction['right'] = True
                a = self.position 
                center_x = round(a[2]/10)
                center_y = round((a[1]+10)/10)
               
            
                b = mat_matrix[center_y,center_x]
                
                
                if(self.direction['right']==True):
                    if(b==1 ):
                        self.position[0] = self.position[0]
                        self.position[2] = self.position[2]
                        self.direction['right'] = False
                    else:
                        prev_pos = [self.position[0],self.position[1],self.position[2],self.position[3]]
                        self.position[0] += self.speed
                        self.position[2] += self.speed
                        
