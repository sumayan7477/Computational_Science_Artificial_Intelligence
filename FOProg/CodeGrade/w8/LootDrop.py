# import random
# def get_loots(loot_list,num):
#     random.seed(1)
#     gen_list=[]
#     for i in range(num):
#         gen_list.append(random.choice(loot_list))
#     return gen_list

# def get_count(gen_list):
#     summary = []
#     summary_items =[]
#     for item  in gen_list:
#         if item not in summary_items:
#             count = gen_list.count(item)
#             summary.append(f"{item}: {count}")
#             summary_items.append(item)
#     text=""
#     for item in summary:
#         text += item +"\n"
#     text= text.strip()
#     return text


import random
LOOT_DROPS = ["Wooden Sword", "Magic Potion", "Gold Coins", "Diamond", "Nothing"]
def get_loots(loot_list,num):
    random.seed(1)
    gen_list=[]
    for i in range(num):
        gen_list.append(random.choice(loot_list))
    return gen_list 

def get_count(gen_list):
    summary = ""
    
    for item  in LOOT_DROPS:
        count = gen_list.count(item)
        summary+= f"{item}: {count}\n"
    return summary.strip()

