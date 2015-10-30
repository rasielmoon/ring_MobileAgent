import threading

connect  =[[0,1,0,0,0,0,0,0,0,1], #0
           [1,0,1,0,0,0,0,0,0,0], #1
           [0,1,0,1,0,0,0,0,0,0], #2
           [0,0,1,0,1,0,0,0,0,0], #3
           [0,0,0,1,0,1,0,0,0,0], #4
           [0,0,0,0,1,0,1,0,0,0], #5
           [0,0,0,0,0,1,0,1,0,0], #6
           [0,0,0,0,0,0,1,0,1,0], #7
           [0,0,0,0,0,0,0,1,0,1], #8
           [1,0,0,0,0,0,0,0,1,0]] #9

#node[Black_hole,next node,safe or out]
node = [[0 for i in range(3)] for j in range(10)]
node [9][0] = "B"
next_node = 0
now_node =0

def find_next(now_node):
	hoge = now_node
	flg = 0
	while flg == 0 :
		if connect[now_node][hoge] == 1 :
			next_node = hoge
			flg = 1
		else :
			hoge = hoge + 1
		
			if hoge == 10:
				hoge = 0
			print hoge
#	print "end find"
	return next_node

def agent (s):
	end_flg = 0
	now_node = s
	while end_flg == 0 :
		if node[now_node][0] == "B":
			print "find out"
			end_flg = 1
		else :
			now_node = find_next(now_node)	


if __name__ == '__main__' :
#	agent1 = threading.Thread(target=agent, name="agent1", args=())
#	agent1.start()
	s = 0
	now_node = s
	agent(now_node)
