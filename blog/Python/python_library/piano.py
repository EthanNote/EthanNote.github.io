import pygame
import time
import wave

class player:
	def __init__(self, keymap=None):
		pygame.mixer.init()
		self.keymap=keymap
		if self.keymap==None:
			self.keymap = {
			0: 'a2',1: 'a2m',2: 'b2',3: 'c2',4: 'c2m',5: 'd2',6: 'd2m',7: 'e2',8: 'f2',9: 'f2m',10:'g2',11:'g2m',			
			12:'a3',13:'a3m',14:'b3',15:'c3',16:'c3m',17:'d3',18:'d3m',19:'e3',20:'f3',21:'f3m',22:'g3',23:'g3m',
			24:'a4',25:'a4m',26:'b4',27:'c4',28:'c4m',29:'d4',30:'d4m',31:'e4',32:'f4',33:'f4m',34:'g4',35:'g4m',
			36:'a5',37:'a5m',38:'b5',39:'c5',40:'c5m',41:'d5',42:'d5m',43:'e5',44:'f5',45:'f5m',46:'g5',47:'g5m',
			48:'a6',49:'a6m',50:'b6',51:'c6',52:'c6m',53:'d6',54:'d6m',55:'e6',56:'f6',57:'f6m',58:'g6',59:'g6m'
			}
		
		self.keys=[None]*60
		for i in range(len(self.keymap.keys())):
			self.keys[i]=pygame.mixer.Sound('piano88/'+self.keymap[i]+'.wav')

	def play(self, keys, interval):
		for k in keys:
			if k>=0 and k<len(self.keys):
				self.keys[k].play()		
				print(self.keymap[k])
			elif k==-1:
				print('empty')
			else:
				print('index out of range')
			time.sleep(interval)
			
p=player()
p.play(range(16), 0.5)
input('over')
