class Rectangle(object):
    '''
    initiating a rectange with length and breadth, getting area and perimeter
    '''
    def __init__(self,length,breadth,cost):
        self.length = length
        self.breadth = breadth
        self.cost = cost
    def get_area(self):
        return self.length * self.breadth

    def get_perimeter(self):
        return (self.length+self.breadth)*2

    def get_cost(self):
        area = self.get_area()
        return (area*self.cost)


r = Rectangle(160, 120,50)


print(f'Area of Rectangle: {r.get_area()} cm^2')
print(f'Perimeter of Rectangle:  {r.get_perimeter()} cm')
print(f'Total cost of Rectange: $ {r.get_cost()}' )
'''
Edit the class above to add cost for each unit area 

print(f'Total cost of Rectange:  {r.get_cost()} ')

where total cost = unit cost * area
'''