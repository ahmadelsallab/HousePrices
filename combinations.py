# Reimplement a DFS in loop with stack without recursion

o = []	
def get_combinations(a):
	combinations(0, a, [])


def combinations(curr_depth, a, c):
	if curr_depth == len(a):
		print(c)		
		o.append(c.copy())# very important, otherwise, a pointer to c is appended which changes by the stack operation
		#print(o)
		return
	else:
		#print(a[curr_idx])
		#c.append(a[curr_idx])
		for child_idx in range(len(a)):		
			c.append(a[child_idx])
			combinations(curr_depth+1, a, c)
			c.pop()
		#curr_depth += 1
		
#a = range(10)
#a = range(3)
a = [0.1, 0.2, 0.3]
get_combinations(a)		
print(o)
print(len(o))
		