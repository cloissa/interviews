# 	Flag ← True
# 	repeat while Flag ← True: 
# 		Flag ← False
# 		for all items in list
# 			if list[item] > list[item+1]
# 				temp = list[item]
# 				list[item] = list[item+1]
# 				list = temp
# 				temp = True
# 	 Until EndofArray
# return dataset


def bubblesort(dataset): 
	cont = True
	while cont:
		cont = False
		for item in range(len(dataset)-1):
			if dataset[item] > dataset[item+1]:
				temp = dataset[item]
				dataset[item] = dataset[item+1]
				dataset = temp
				cont = True
	return dataset


# Procedure InsertionSort (List, First, Last)
#     For CurrentPointer <- First + 1 To Last
#         CurrentValue <- List[CurrentPointer]
#         Pointer <- CurrentPointer − 1
#         While List[Pointer] > CurrentValue AND Pointer > 0
#             List[Pointer+1] <- List[Pointer]
#             Pointer <- Pointer − 1
#         EndWhile
#         List[Pointer+1] <- CurrentValue
#     EndFor
# EndProcedure


def insertsort(dataset, first, last):
	for item in range(1, len(dataset)):
		value = dataset[item]
		position = item
		
		while dataset[item] > value and (position > 0):
			dataset[position] = dataset[position-1]
			position = position-1
	
	dataset[position] = value


# def quicksort(myList, start, end):
#     if start < end:
#         # partition the list
#         pivot = partition(myList, start, end)
#         # sort both halves
#         quicksort(myList, start, pivot-1)
#         quicksort(myList, pivot+1, end)
#     return myList

def partition(dataset, start, end):
	pivot = dataset[start]
	left = start+1
	right = end
	done = False
	while not done:
		while left <= right and dataset[left] <= pivot:
			left += 1
		while dataset[right] >= pivot and right >= left:
			right -= 1
		if right < left:
			done = True
		else:
			temp = dataset[left]
			dataset[left] = dataset[right]
			dataset[right] = temp
	temp = dataset[start]
	dataset[start] = dataset[right]
	dataset[right] = temp
	return right
 

def quicksort(dataset, start, end):
	if start < end:
		pivot = partition(dataset, start, end)
		quicksort(dataset, start, pivot-1)
		quicksort(dataset, pivot+1, end)
	return dataset	

dataset = [1,6,9,3,34,9,2,0,67,433,45,6]
print(quicksort(dataset, 0, len(dataset)))
