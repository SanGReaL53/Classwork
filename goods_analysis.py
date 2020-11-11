def goods_analysis(*products, in_sale=None):
    if in_sale is None:
        p = [z for z in products if z['название'].lower().find('молоко') != -1]
        products = p
    else:
        products = [z for z in products if in_sale(z)]
    return sorted(products, key=lambda z: z['цена'])[:3]
