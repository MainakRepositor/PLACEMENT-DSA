# Function for binary search in ascending part
def ascendingBinarySearch(arr, low, high, key):
	
	while low <= high:
		mid = low + (high - low) // 2
		
		if arr[mid] == key:
			return mid
		
		if arr[mid] > key:
			high = mid - 1
		else:
			low = mid + 1
			
	return -1

# Function for binary search in descending part of array
def descendingBinarySearch(arr, low, high, key):
	
	while low <= high:
		mid = low + (high - low) // 2
		
		if arr[mid] == key:
			return mid
		
		if arr[mid] < key:
			high = mid - 1
		else:
			low = mid + 1
			
	return -1

# Find bitonic point
def findBitonicPoint(arr, n, l, r):
	
	bitonicPoint = 0
	mid = (r + l) // 2
	
	if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
		return mid
	
	elif arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
		bitonicPoint = findBitonicPoint(arr, n, mid, r)
	else:
		bitonicPoint = findBitonicPoint(arr, n, l, mid)
		
	return bitonicPoint

# Function to search key in bitonic array
def searchBitonic(arr, n, key, index):
	
	if key > arr[index]:
		return -1
	elif key == arr[index]:
		return index
	else:
		temp = ascendingBinarySearch(arr, 0, index-1, key)
		if temp != -1:
			return temp
		
		# search in right of k
		return descendingBinarySearch(arr, index+1, n-1, key)
	
# Driver code
def main():
	arr = [-8, 1, 2, 3, 4, 5, -2, -3]
	key = 1
	n = len(arr)
	l = 0
	r = n - 1
	
	# Function call
	index = findBitonicPoint(arr, n, l, r)
	
	x = searchBitonic(arr, n, key, index)
	
	if x == -1:
		print("Element Not Found")
	else:
		print("Element Found at index", x)
		
main()

