def goods_analysis(*products, in_sale=None):
    if in_sale is None:
        products = [z for z in products if z['название'].lower().find('молоко') != -1]
    else:
        products = [z for z in products if in_sale(z)]
    return sorted(products, key=lambda z : z['цена'])[:3]

