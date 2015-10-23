import threading

connect  =[[0,1,0,0,0,0,0,0,0,1],
           [1,0,1,0,0,0,0,0,0,0],
           [0,1,0,1,0,0,0,0,0,0],
           [0,0,1,0,1,0,0,0,0,0],
           [0,0,0,1,0,1,0,0,0,0],
           [0,0,0,0,1,0,1,0,0,0],
           [0,0,0,0,0,1,0,1,0,0],
           [0,0,0,0,0,0,1,0,1,0],
           [0,0,0,0,0,0,0,1,0,1],
           [1,0,0,0,0,0,0,0,1,0]]

#node[Black_hole,next node,safe or out]
node = [[0 for i in range(3)] for j in range(10)]
node [9][0] = "B"

def agent ():
	print (node[9][0])


if __name__ == '__main__' :
	agent1 = threading.Thread(target=agent, name="agent1", args=())
	agent1.start()
	agent()
