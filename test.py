#!/usr/bin/python
import itertools

error_char = 'X'
good_char = 'o'

def print2D(string, n, k):
	for i in range(0, n*k, k):
		print string[i:i+k]

def calcSum(n,k):
	total = 0
	
	n_vals = range(n-(n-2)-1, n-0)
	k_vals = range(k-(k-2)-1, k-0)
	
	for n_val in n_vals:
		for k_val in k_vals:
			total += n_val * k_val
			
	return total

def computeErrorProb(n,k):
	total_permutations = 0
	total_undec = 0
	
	# Make all permutations of n*k bit block with 4 errors
	permutations = set(itertools.permutations(error_char*4 + (n*k-4)*good_char))
	total_permutations = len(permutations)
	
	print "--- Undetectable errors ---"
	for perm in permutations:
		error_indices = list([])
		
		for i in range(0,n*k):
			if perm[i] == error_char:
				error_indices.append(i)
				
		# Determine if these errors are undetectable - vertices in a rectangle
		# 	fix tomorrow
		# Checks - 0 and 1 in same row, 0 and 2 in same col, 1 and 3 in same col, 
		if error_indices[0]/n == error_indices[1]/n and error_indices[0]%n == error_indices[2]%n and error_indices[1]%n == error_indices[3]%n and error_indices[2]/n == error_indices[3]/n:
			total_undec += 1
			print2D(perm,n,k)
			print ''
									
	print "Total unique permutations: " + str(total_permutations)
	print "Total undetectable errors: " + str(total_undec)
	print "Sum(k-p-1)(n-q-1): " + str(calcSum(n,k))
	print "nk(nk-1)(nk-2)(nk-3) = " + str(n*k*(n*k - 1)*(n*k - 2)*(n*k - 3))

if __name__ == "__main__":
	computeErrorProb(3,4)
