from classes import CookBook
from objects import cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}
    ingridient_list = []
    for dish in dishes:
        if dish  not in cook_book.dishes:
            print(f'Рецепта "{dish}" в книге рецептов нет')
        else: 
            for ingridient in cook_book.recipes[dish]:
                if ingridient['ingridient_name'] not in shop_dict:
                    shop_dict[ingridient['ingridient_name']] = {"measure":"", "quantity": 0}
                
                ingridient_list = [ingridient['ingridient_name'], ingridient['measure'] , \
                 int(ingridient['quantity']) * person_count]
                shop_dict[ingridient_list[0]]['quantity'] += ingridient_list[2]
                shop_dict[ingridient_list[0]]['measure'] = ingridient_list[1]  

    return print(shop_dict, '\n')
        



            



