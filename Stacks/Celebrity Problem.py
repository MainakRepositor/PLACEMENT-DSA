# Python3 code
class Solution:

	# Function to find if there is a celebrity in the party or not.
	# return index if celebrity else return -1
	def celebrity(self, M, n):
		# code here
		i = 0
		j = n-1
		candidate = -1
		while(i < j):
			if M[j][i] == 1:
				j -= 1
			else:
				i += 1

		candidate = i
		for k in range(n):
			if candidate != k:
				if M[candidate][k] == 1 or M[k][candidate] == 0:
					return -1

		return candidate


n = 4
m = [[0, 0, 1, 0],
	[0, 0, 1, 0],
	[0, 0, 0, 0],
	[0, 0, 1, 0]]
ob = Solution()
print("Celebrity at index "+str(ob.celebrity(m, n)))
