class FormatFile:
    def __init__(self, name):
        self.name = name


    def readfile(self):
        with open(self.name) as f:
            data = f.readlines()
        self.data = data
        
  
    def getlines(self):
        lines_list = []

        for line in self.data:
            line = line.replace('\n', '')
            lines_list.append(line)

        lines_list.append('')

        self.lines = lines_list
        

    def formatlines(self):
        recip = []
        recipes_list = []

        for line in (self.lines):
            if line != '':
                recip.append(line)
            else:
                recipes_list.append(recip)
                recip = []
        self.rcpslist = recipes_list
        
    
    def createdict(self):
        cook_book = {}
        ingridients = []
        ingridient_dict = {}
        split_string = []
        dish_list = []

        for recip in self.rcpslist:
            for index, element in enumerate(recip):
                if index == 0:
                    cook_book[element] = []
                elif index not in [0,1]: 
                    split_string = element.split(' | ')
                    ingridient_dict['ingridient_name'] = split_string[0]
                    ingridient_dict['quantity'] = split_string[1]
                    ingridient_dict['measure'] = split_string[2]
                    ingridients.append(ingridient_dict)
                    ingridient_dict = {}
            
            cook_book[recip[0]] = ingridients
            dish_list.append(recip[0])
            ingridients = []

        self.recipes = cook_book
        self.dishes = dish_list


class CookBook(FormatFile):
    def __init__(self, name):
        super().__init__(name)
        self.readfile()
        self.getlines()
        self.formatlines()
        self.createdict()
    
    def __str__(self):
        return f"В книге есть следующие рецепты: \n{', '.join(self.dishes)}"
    
    
class SortFile(FormatFile):
    def __init__(self, name):
        super().__init__(name)
        self.readfile()

    def srt(self, files):
        order_list = []
        for file in files:
            order_list.append(len(file.data))
            order_list = sorted(order_list)
        self.order = order_list
        self.files = files

    def wrtfile(self):
        with open (self.name, 'a') as f:
            for l in self.order:
                for file in self.files:
                    if l == len(file.data):
                        f.write(file.name)
                        f.write('\n')
                        f.write(str(len(file.data)))
                        f.write('\n')
                        for i in range(l):
                            f.write(file.data[i])
                        f.write('\n')

