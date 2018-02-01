import midi

pattern = midi.Pattern()
track = midi.Track()
pattern.append(track)

start = 100

def generate(pitch_list, interval):
	headwait = 0
	startindex = 0
	strokes = []
	for i in range(16):
		if(pitch_list == 0):
			headwait+=interval
		else:
			startindex = i
			break
	
	tick = [interval] * 16
	for i in range(startindex, 15):
		if(pitch_list[i] != 0):
			for j in range(i + 1, 16):
				if(pitch_list[j] == 0):
					tick[i]+=interval
				else:
					break
	for i in range(startindex, 16):
		if(pitch_list[i] != 0):
			track.append(midi.NoteOnEvent(tick=startindex * interval, velocity=50, pitch=pitch_list[i]))
			track.append(midi.NoteOffEvent(tick=tick[i], pitch=pitch_list[i]))
			startindex = 0
				


generate([48, 0, 48, 0, 55, 0, 55, 0, 57, 0, 57, 0, 55, 0, 0, 0], 120)
generate([53, 0, 53, 0, 52, 0, 52, 0, 50, 0, 50, 0, 48, 0, 0, 0], 120)
generate([55, 0, 55, 0, 53, 0, 53, 0, 52, 0, 52, 0, 50, 0, 0, 0], 120)
generate([55, 0, 55, 0, 53, 0, 53, 0, 52, 0, 52, 0, 50, 0, 0, 0], 120)
generate([48, 0, 48, 0, 55, 0, 55, 0, 57, 0, 57, 0, 55, 0, 0, 0], 120)
generate([53, 0, 53, 0, 52, 0, 52, 0, 50, 0, 50, 0, 48, 0, 0, 0], 120)

print(pattern)
midi.write_midifile('test.mid', pattern)
