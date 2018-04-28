import sys
import threading
from shop.models import Product,Category
from server import Server
pic = [
    [1,'Electronic','IPhone X','IPhone_X','products/2018/04/19/iphonex.jpg','IPhone X',1299,100,0],
    [2,'Bath','Loma Moisturizing Shampoo','Loma_M_Shampoo','products/2018/04/19/Loma_Moisturizing_Shampoo.jpg','Loma Moisturizing Shampoo 1000ml',29.9,200,1],
    [3,'Shoes','NB M998','NB_M998','products/2018/04/19/M998wtp.jpg','New Balance Sport Shoes M998',89,100,1],
    [4,'Bath','Moroccan','Moroccan','products/2018/04/19/Moroccan.jpg','Moroccan Argan Oil',12.99,500,1],
    [5,'Shoes','Adidas xr1','Adidas_xr1','products/2018/04/19/NMD_xr1.jpg','Adidas Sports Shoes xr1',79,200,1],
    [6,'Electronic','Samsung S9','Samsung_S9','products/2018/04/19/S9.jpg','Samsung Galaxy S9',1099,150,0],
    ]
server = Server()

for pic in pic:
    try:
        p = Product.objects.get(pid = pic[0])
    except:
        p = Product()
        p.pid = pic[0]
        category = pic[1]
        try:
            c = Category.objects.get(name=category)
        except:
            c = Category.objects.create(name = category,slug = category)
        p.category = c
        p.name = pic[2]
        p.slug = pic[3]
        p.image = pic[4]
        p.description = pic[5]
        p.price = pic[6]
        p.stock = pic[7]
        p.whnum = pic[8]
        p.save()
        print("fin")
    else:
        continue
server.close()
    
