import os, re, readchar, random, time, timeout_decorator, sys

# flow: lane animation --> car move --> game

end_program = 0
loc = 22
l_loc = 22-10
r_loc = 22+10
SPEED = 0.05

blank_row = '                                    '
a_row = '                                    '
b_row = '                                    '
c_row = '                                    '
d_row = '                                    '
e_row = '                                    '

def lane_overwrite(row, l_loc, r_loc):
	r_list = list(row)
	r_list[l_loc] = 'l'
	r_list[r_loc] = 'l'
	return "".join(r_list)

def e_overwrite(e_row, num):
	e_list = list(e_row)
	
	if e_list[num] == 'l': # collision check
		os.system('clear')
		for i in range(3):
			print('')
		print('         GAME  OVER   ')
		for i in range(4):
			print('')
		exit()
	else:
		e_list[num] = 'O' # overwrite
		e_row = "".join(e_list)
		return e_row

@timeout_decorator.timeout(SPEED)
def key_get():
	global loc, end_program
	key = readchar.readkey()
	if key=='f':
		loc = loc+1
	if key=='s':
		loc = loc-1
	if key=='q':
		end_program = 1

def init():
	os.system('clear')
	for i in range(4):
		print(lane_overwrite(blank_row, l_loc, r_loc))
	print(e_overwrite(lane_overwrite(blank_row, l_loc, r_loc), loc))

	print('')
	print('           TYPE ANY KEY           ')
	print('')
	key = readchar.readkey()
	return


def play(rand_num):
	global loc, blank_row, a_row, b_row, c_row, d_row, e_row, l_loc, r_loc
	os.system('clear')
	
	if rand_num == 0:
		a_row = lane_overwrite(a_row, l_loc, r_loc)
	if rand_num == 1:
		l_loc = min(l_loc + 1, r_loc - 2)
		a_row = lane_overwrite(a_row, l_loc, r_loc)
	if rand_num == 2:
		l_loc = max(l_loc - 1, 0)
		a_row = lane_overwrite(a_row, l_loc, r_loc)
	if rand_num == 3:
		r_loc = min(r_loc + 1, 33)
		a_row = lane_overwrite(a_row, l_loc, r_loc)
	if rand_num == 4:
		r_loc = max(r_loc - 1, l_loc + 2)
		a_row = lane_overwrite(a_row, l_loc, r_loc)
	
	print(a_row)
	print(b_row)
	print(c_row)
	print(d_row)
	print(e_overwrite(e_row, loc))
	
	# need to make it interruption
	try:
		key = key_get() # this has a problem
	except:
		pass
	
	if end_program == 1:
		exit()
	
	e_row = d_row
	d_row = c_row
	c_row = b_row
	b_row = a_row
	a_row = blank_row


if __name__=='__main__':
	init()
	rand_num = 0
	while True:
		play(rand_num)
		rand_num = random.randint(0,4)
