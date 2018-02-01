import midi
import random
import numpy
class MatSound:
	def __init__(self, interval=120, velocity=100):
		self.interval = interval
		self.velocity = velocity		
		self.chapterlength = 16
		self.pattern = midi.Pattern()
		self.track = midi.Track()
		self.pattern.append(self.track)

	def generateChapter(self, pitch_list):
		headwait = 0
		startindex = 0
		strokes = []
		for i in range(self.chapterlength):
			if(pitch_list[i] == 0):
				headwait+=self.interval
			else:
				startindex = i
				break
	
		tick = [self.interval] * self.chapterlength
		for i in range(startindex, self.chapterlength - 1):
			if(pitch_list[i] != 0):
				for j in range(i + 1, self.chapterlength):
					if(pitch_list[j] == 0):
						tick[i]+=self.interval
					else:
						break
		for i in range(startindex, self.chapterlength):
			if(pitch_list[i] != 0):
				self.track.append(midi.NoteOnEvent(tick=startindex * self.interval, 
									   velocity=self.velocity, pitch=pitch_list[i]))
				self.track.append(midi.NoteOffEvent(tick=tick[i], pitch=pitch_list[i]))
				startindex = 0

	def generate(self, mat):
		for row in mat:
			self.generateChapter(row)

	def save(self, fname):
		midi.write_midifile(fname, self.pattern)

	@staticmethod
	def CreateSound(mat, fname, interval=120, velocity=100, chapterlength = 16):
		ms=MatSound(interval, velocity)
		ms.chapterlength=chapterlength
		ms.generate(mat)
		ms.save(fname)

#test
if(__name__ == '__main__'):
	while(True):
		mat=numpy.zeros((16,16), dtype=int)

		for i in range(16):
			selectCount=random.randint(2,4)
			selectedKeys=[0]
			for c in range(selectCount):
				key=0;
				while(key in selectedKeys or  key % 12 in [1, 3, 6, 8 ,10]):
					key=int(numpy.random.randn()*10+60)
				selectedKeys.append(key)

			for j in range(16):
				index=random.randint(1, len(selectedKeys)-1)
				if(random.randint(0,100)%2==0 and j%4!=0):
					index=0
				while(j%4==0 and index==0):
					index=random.randint(1, len(selectedKeys)-1)
				mat[i][j]=selectedKeys[index]

				r=j%4
				if(mat[i][j]>mat[i][j-r]):
					t=mat[i][j]
					mat[i][j]=mat[i][j-r]
					mat[i][j-r]=t
				if(i>0 and random.randint(0,2)==0):
					mat[i][j]=mat[i-1][j]

		print(mat)
		MatSound.CreateSound(mat, 'noisy.mid', 60)
		input('Create Next')
			
