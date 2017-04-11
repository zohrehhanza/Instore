from blog.adonis_crawler import list_products
from blog.IGA_crawler import list_products_1

import pickle

final_list = list_products + list_products_1
with open(file_products, 'wb') as f:
    pickle.dump(final_list, f)
