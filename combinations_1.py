# Reimplement a DFS in loop with stack without recursion

o = []	
def get_combinations(a, l):
	combinations(0, a, l, [])


def combinations(curr_depth, a, l, c):
	if curr_depth == l:
		print(c)		
		o.append(c.copy())# very important, otherwise, a pointer to c is appended which changes by the stack operation
		#print(o)
		return
	else:
		#print(a[curr_idx])
		#c.append(a[curr_idx])
		for child_idx in range(len(a)):		
			c.append(a[child_idx])
			combinations(curr_depth+1, a, l, c)
			c.pop()
		#curr_depth += 1
		
a = range(10)

#a = range(3)
#a = [0.1, 0.2, 0.3]
get_combinations(a, 2)		
print(o)
print(len(o))
		