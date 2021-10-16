def getMedian(arr1, arr2, n): 
	if n == 0: 
		return -1
	elif n == 1: 
		return (arr1[0]+arr2[1])/2
		
	elif n == 2: 
		return (max(arr1[0], arr2[0]) +
				min(arr1[1], arr2[1])) / 2
	
	else:
		m1 = median(arr1, n)
		m2 = median(arr2, n)
		if m1 > m2:
			if n % 2 == 0:
				return getMedian(arr1[:int(n / 2) + 1],
						arr2[int(n / 2) - 1:], int(n / 2) + 1)
			else:
				return getMedian(arr1[:int(n / 2) + 1], 
						arr2[int(n / 2):], int(n / 2) + 1)
		else:
			if n % 2 == 0:
				return getMedian(arr1[int(n / 2 - 1):],
						arr2[:int(n / 2 + 1)], int(n / 2) + 1)
			else:
				return getMedian(arr1[int(n / 2):], 
						arr2[0:int(n / 2) + 1], int(n / 2) + 1)

def median(arr, n):
	if n % 2 == 0:
		return (arr[int(n / 2)] +
				arr[int(n / 2) - 1]) / 2
	else:
		return arr[int(n/2)]

arr1 = [int(i) for i in input().split(" ")]
arr2 = [int(i) for i in input().split(" ")]
n = len(arr1)
print(int(getMedian(arr1,arr2,n)))


"""
Another Program
"""
# Python3 program to find compound 
# interest for given values. 

def compound_interest(principle, rate, time): 

	# Calculates compound interest 
	Amount = principle * (pow((1 + rate / 100), time)) 
	CI = Amount - principle 
	print("Compound interest is", CI) 

# Driver Code 
compound_interest(10000, 10.25, 5) 

# This code is contributed by Abhishek Agrawal. 
