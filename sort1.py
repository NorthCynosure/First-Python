def bubble_sort(alist):
    for i in range (len(alist) - 1):
    	swapped = False
    	for j in range(len(alist) - 1 - i):
    		if alist[j] > alist[j + 1]:
    			alist[j], alist[j + 1] = alist[j + 1], alist[j]
    			swapped = True
    	if swapped:
    		swapped = False
    		for j in range(len(alist) - 2 - i,0,-1):
    			


class Student(object):
    def __init__(self,name,classes):
        self.name = name
        self.classes = classes

    def __gt__(self,other):
    	return self.classes > other.classes

    def __lt__(self,other):
    	return self.classes < other.classes

    def __reper__(self):
    	return f'{self.name}:{self.age}'
		
'''蛤蛤'''



