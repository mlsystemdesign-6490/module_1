class Rectangle(object):
    '''
    initiating a rectange with length and breadth, getting area and perimeter
    '''
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def get_area(self):
        return self.length * self.breadth

    def get_perimeter(self):
        return (self.length+self.breadth)*2


r = Rectangle(160, 120)


print(f'Area of Rectangle: {r.get_area()} cm^2')
print(f'Perimeter of Rectangle:  {r.get_perimeter()} cm')

'''
Edit the class above to add cost for each unit area 

print(f'Total cost of Rectange:   $ {r.get_cost()} ')

where total cost = unit cost * area
'''