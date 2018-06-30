# Reimplement a DFS in loop with stack without recursion

o = []	
def get_valid_weights(a, l):
	get_valid_weights_(0, a, l-1, [])


def get_valid_weights_(curr_depth, a, l, c):
	if curr_depth == l:
		if sum(c) <= 1:
			c.append(1-sum(c))
			print(c)		
			o.append(c.copy())# very important, otherwise, a pointer to c is appended which changes by the stack operation
			c.pop()
			#print(o)
		return
	else:
		#print(a[curr_idx])
		#c.append(a[curr_idx])
		for child_idx in range(len(a)):		
			c.append(a[child_idx])
			get_valid_weights_(curr_depth+1, a, l, c)
			c.pop()
		#curr_depth += 1
		
import numpy as np
res = 0.1
l = 10
a = np.multiply(range(l+1), res)


#a = range(3)
#a = [0.1, 0.2, 0.3]
get_valid_weights(a, 2)		
print(o)
print(len(o))
		