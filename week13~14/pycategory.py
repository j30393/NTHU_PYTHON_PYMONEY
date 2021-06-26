class Categories:
    def __init__(self):
        self.categories = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', [
            'bus', 'railway']], 'income', ['salary', 'bonus']]
        self.cate_list = ''
    def view(self,catego,num):
        if(catego == None):
            return
        if type(catego) == type([]):
            for child in catego:
                self.view(child,num + 4)
        else:
            self.cate_list += ' '*num
            self.cate_list += '-' 
            self.cate_list += catego
            self.cate_list += '\n'
    
    def get_cate_list(self):
        return self.cate_list
            
    def is_category_valid(self, target):
        """check if the category is in self._categories or not"""
        def check_category_valid(target, categories_list):
            for i in categories_list:
                if type(i) == list:
                    if check_category_valid(target, i):
                        return True
                else:
                    if i == target:
                        return True
            return False

        return check_category_valid(target, self.categories)
        
                    
    def find_subcategories(self, category):
        def find_subcategories_gen(category, categories, found=False):
            if type(categories) == list:
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child, found)
                    if child == category and index + 1 < len(categories) \
                        and type(categories[index + 1]) == list:
                        # When the target category is found,
                        # recursively call this generator on the subcategories
                        # with the flag set as True.
                        yield from find_subcategories_gen(category, categories[index+1], True)
            else:
                if categories == category or found:
                    yield categories

        gen = find_subcategories_gen(category,self.categories)
        ans=[i for i in gen]
        return ans
