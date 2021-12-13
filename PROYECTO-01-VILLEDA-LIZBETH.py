#Importamos los datos de Lifestore
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
# Productos con mas ventas | Se crean listas vacías

lista_ventas = []
lista_busquedas = []
lista_ventas_totales = []

# Lista vacía con los id de los productos y el número de productos
for num_producto in range(len(lifestore_products)):
    id_producto = lifestore_products[num_producto][0]
    lista_interna = [id_producto, 0]
    
    lista_ventas.append(lista_interna)
    #lista_ventas[[id_producto, número de productos]]

    lista_busquedas.append(lista_interna)
    #lista_busquedas[[id_producto, número de productos]]

# Lista vacía con las id de productos, número de productos y el promedio
for num_producto in range(len(lifestore_products)):
    id_producto = lifestore_products[num_producto][0]
    lista_interna = [id_producto, 0, 0]
    
    lista_ventas_totales.append(lista_interna)
    #lista_ventas_totales[[id_producto, número de productos, promedio de reseña]]

#Lista con la cantidad de productos vendidos según el producto 

for venta in lifestore_sales:
    producto_vendido = venta[1]
    devuelto = venta[4]
    
    if not devuelto:
        lista_ventas[producto_vendido - 1][1] += 1
    lista_ventas_totales[producto_vendido - 1][1] += 1

#Ventas totales | Mayor a menor 

copia_lista_ventas = lista_ventas.copy()
lista_ventas_ordenada = []

for i in range(len(lista_ventas)-1):
  venta_max = copia_lista_ventas[0][1]
  posicion_max = 0

  for j in range(len(copia_lista_ventas)-1): 
    venta_sig = copia_lista_ventas[j+1][1]
    
    if venta_sig >= venta_max:
      venta_max = venta_sig
      posicion_max = j+1
  
  lista_ventas_ordenada.append(copia_lista_ventas[posicion_max])
  copia_lista_ventas.pop(posicion_max)

lista_ventas_ordenada.append(copia_lista_ventas[0])

# Productos con mas búsquedas | Lista con la cantidad de productos buscados según el producto
for busqueda in lifestore_searches:
    producto_buscado = busqueda[1]
    lista_busquedas[producto_buscado - 1][1] += 1

#Mayor a menor
copia_lista_busquedas = lista_busquedas.copy()
lista_busqueda_ordenada = []

for i in range(len(lista_busquedas)-1):
  busqueda_max = copia_lista_busquedas[0][1]
  posicion_max = 0

  for j in range(len(copia_lista_busquedas)-1):
    busqueda_sig = copia_lista_busquedas[j+1][1]

    if busqueda_sig >= busqueda_max:
      busqueda_max = busqueda_sig
      posicion_max = j+1
  
  lista_busqueda_ordenada.append(copia_lista_busquedas[posicion_max])
  copia_lista_busquedas.pop(posicion_max)

lista_busqueda_ordenada.append(copia_lista_busquedas[0])

# Reseñas | Mayor a menor

aumento = 0
for producto in lifestore_products:
  suma_review = 0
  id_producto = producto[0]

  while (lifestore_sales[aumento][1] == id_producto) and (aumento < len(lifestore_sales)-1):
    suma_review += lifestore_sales[aumento][2]
    aumento += 1
  
  productos_vendidos = lista_ventas_totales[id_producto-1][1]

  if productos_vendidos > 0:
   lista_ventas_totales[id_producto-1][2] = suma_review/productos_vendidos

copia_lista_reviews = lista_ventas_totales.copy()
lista_reviews_ordenada = []

for i in range(len(lista_ventas_totales)-1):
  review_max = copia_lista_reviews[0][2]
  posicion_max = 0

  for j in range(len(copia_lista_reviews)-1):
    review_sig = copia_lista_reviews[j+1][2]

    if review_sig >= review_max:
      review_max = review_sig
      posicion_max = j+1
  
  lista_reviews_ordenada.append(copia_lista_reviews[posicion_max])
  copia_lista_reviews.pop(posicion_max)

lista_reviews_ordenada.append(copia_lista_reviews[0])

# Bienvenida al usuario | Solo se permitirá el ingreso a la base de datos de Life Store a un usuario verificado por la empresa.
#En este caso los datos para ingresar serán los siguientes:
#USUARIO: adminlifestore
#CONTRASEÑA: lifestore01
limpiarPantalla = '\n' * 10
separado = ['|', '⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯', '|']
separador = separado[0] + separado[1] + separado[2]

print(separador+"\n")
print(1*"\t"+"  Te damos la bienvenida a Life Store"+"\n")
print(separador+"\n")
print('>Favor de solicitar el usuario y contraseña a un administrador de Life Store')
if __name__ == "__main__":
    USUARIO = 'adminlifestore'
    CONTRASENA = 'lifestore01'
 #Se ingresa un usuario y contraseña validado por Life Store
    username = input('Ingrese su nombre de usuario:\n > ')
    password = input('Ingrese la contraseña:\n > ')

    if username == USUARIO:
        if password == CONTRASENA:
            print("Te damos la bienvenida a Life Store")
        else:
            print("Contraseña erronea")
    else:
        print('El usuario no existe')

    if password == "lifestore01":
         print("Eliga una opción")
         print("1. Productos con más búsquedas \n"+ 
            "2. Productos con menos búsquedas \n"+
            "3. 5 Productos con mejores reseñas \n"+
            "4. 5 Productos con peores reseñas \n"+
            "5. Productos con más ventas por mes \n"+
            "6. Productos con menos ventas por mes \n"
            "0. Salir del menú"+"\n")

    eleccion = int(input("Eliga una opción: "))

    while eleccion != 0:
      print(limpiarPantalla)
      if eleccion > 0 and eleccion < 7:
        
        # Productos con mas búsquedas
        if eleccion == 1:
          print("Número"+"| ID producto"+"\t"+"| Num. busqueda")
          print(separador)
          for i in range(10):
            id_producto = lista_busqueda_ordenada[i][0]
            num_busqueda = lista_busqueda_ordenada[i][1]
            print("\t"+str(i+1)+2*"\t"+str(id_producto)+3*"\t"+str(num_busqueda))

        # Productos con menos búsquedas
        elif eleccion == 2:
          print("Número"+"| ID producto"+"\t"+"| Num. busquedas")
          print(separador)
          for i in range(1,20):
            id_producto = lista_busqueda_ordenada[-i][0]
            num_busqueda = lista_busqueda_ordenada[-i][1]
            print("\t"+str(len(lifestore_products)-i+1)+2*"\t"+str(id_producto)+3*"\t"+str(num_busqueda))

        # Productos con mejores reseñas
        elif eleccion == 3:
          print("   Número"+"| ID producto"+"\t"+"| Promedio reviews")
          print(separador)
          for i in range(5):
            id_producto = lista_reviews_ordenada[i][0]
            num_review = lista_reviews_ordenada[i][2]
            print("\t"+str(i+1)+2*"\t"+str(id_producto)+3*"\t"+str(num_review))
        
        # Productos con peores reseñas
        elif eleccion == 4:
          print("Número"+"| ID producto"+"\t"+"| Promedio reviews")
          print(separador)
          cantidad = 1
          num = 1
          while cantidad < 6:
            if lista_reviews_ordenada[-num][1] != 0:
              id_producto = lista_reviews_ordenada[-cantidad][0]
              num_review = lista_reviews_ordenada[-cantidad][2]
              print("\t"+str(len(lifestore_products)-cantidad+1)+2*"\t"+str(id_producto)+3*"\t"+str(num_review))  
              
              cantidad += 1
            num += 1
        elif eleccion == 5:
          anio = input("¿De qué año desea ver el listado? (2020): " )
          mes = input("¿De qué mes desea ver el listado? (01 (enero),02 (febrero), 03(marzo) etc.): ")
          lista_ventas_mes = []
          for num_producto in range(len(lifestore_products)):
            id_producto = lifestore_products[num_producto][0]
            lista_interna = [id_producto, 0, 0]

            lista_ventas_mes.append(lista_interna)
            #lista_ventas_mes[[id_producto, número de productos, mes]]
          
          #Lista con la cantidad de productos vendidos según el producto
          vv = 0
          for venta in lifestore_sales:
              producto_vendido = venta[1]
              devuelto = venta[4]
              
              if not devuelto:
                if venta[3][3:5] == mes and venta[3][6:10] == anio:
                  vv += 1
                  lista_ventas_mes[producto_vendido - 1][1] += 1
          
          if vv == 0:
            print("No hay ventas en ese mes y año específico")
            break

          # Mayor a menor
          copia_lista_ventas_mes = lista_ventas_mes.copy()
          lista_ventas_mes_ordenada = []

          for i in range(len(lista_ventas_mes)-1):

              venta_max = copia_lista_ventas_mes[0][1]
              posicion_max = 0
              for j in range(len(copia_lista_ventas_mes)-1): 
                  venta_sig = copia_lista_ventas_mes[j+1][1]
                  
                  if venta_sig >= venta_max:
                      venta_max = venta_sig
                      posicion_max = j+1
              
              lista_ventas_mes_ordenada.append(copia_lista_ventas_mes[posicion_max])
              copia_lista_ventas_mes.pop(posicion_max)

          lista_ventas_mes_ordenada.append(copia_lista_ventas_mes[0])

          print("| Número"+"| ID producto"+"\t"+"| Num. ventas"+"\t"+"| Mes"+"| Año")
          print(separador)
          for i in range(15):
            id_producto = lista_ventas_mes_ordenada[i][0]
            num_venta = lista_ventas_mes_ordenada[i][1]
            print("\t"+str(i+1)+2*"\t"+str(id_producto)+5*"\t"+str(num_venta)+3*"\t"+str(mes)+"\t"+str(anio)) 

        elif eleccion == 6:
          anio = input("¿De qué año desea ver el listado? (2020): " )
          mes = input("¿De qué mes desea ver el listado? (01 (enero),02 (febrero), 03(marzo) etc.): ")
          lista_ventas_mes = []
          for num_producto in range(len(lifestore_products)):
            id_producto = lifestore_products[num_producto][0]
            lista_interna = [id_producto, 0, 0]

            lista_ventas_mes.append(lista_interna)
            #lista_ventas_mes[[id_producto, número de productos, mes]]
      
          #Lista con la cantidad de productos vendidos según el producto
          vv = 0
          for venta in lifestore_sales:
              producto_vendido = venta[1]
              devuelto = venta[4]
              
              if not devuelto:
                if venta[3][3:5] == mes and venta[3][6:10] == anio:
                  vv += 1
                  lista_ventas_mes[producto_vendido - 1][1] += 1
          
          if vv == 0:
            print("No hay ventas en ese mes y año específico")
            break

          # Ventas por mes
          copia_lista_ventas_mes = lista_ventas_mes.copy()
          lista_ventas_mes_ordenada = []

          for i in range(len(lista_ventas_mes)-1):

              venta_max = copia_lista_ventas_mes[0][1]
              posicion_max = 0
              for j in range(len(copia_lista_ventas_mes)-1): 
                  venta_sig = copia_lista_ventas_mes[j+1][1]
                  
                  if venta_sig >= venta_max:
                      venta_max = venta_sig
                      posicion_max = j+1
              
              lista_ventas_mes_ordenada.append(copia_lista_ventas_mes[posicion_max])
              copia_lista_ventas_mes.pop(posicion_max)

          lista_ventas_mes_ordenada.append(copia_lista_ventas_mes[0])

          print("| Número"+"| ID producto"+"\t"+"| Num. ventas"+"\t"+"| Mes"+"| Año")
          print(separador)
          for i in range(1,11):
            id_producto = lista_ventas_mes_ordenada[-i][0]
            num_venta = lista_ventas_mes_ordenada[-i][1]
            print("\t"+str(i)+2*"\t"+str(id_producto)+5*"\t"+str(num_venta)+3*"\t"+str(mes)+"\t"+str(anio)) 

        # Saber el nombre del producto   
        nombre = input("¿Deseas conocer el nombre del producto? (si/no): ")
        if nombre == "si":
          num_producto = int(input("Escribe el Número del producto: "))
          if eleccion == 1 or eleccion == 2:
            id_producto = lista_ventas_ordenada[num_producto-1][0]
          if eleccion == 3 or eleccion == 4:
            id_producto = lista_busqueda_ordenada[num_producto-1][0]
          if eleccion == 5 or eleccion == 6:
            id_producto = lista_reviews_ordenada[num_producto-1][0]
          print("| ID del producto "+"| Nombre")
          print(separador)
          print("\t "+str(id_producto)+"\t "+str(lifestore_products[id_producto-1][1]))

        
        print("1. Productos con más búsquedas \n"+
        "2. Productos con menos búsquedas \n"+
        "3. 5 Productos con mejores reseñas \n"+
        "4. 5 Productos con peores reseñas \n"+
        "5. Productos con más ventas por mes \n"+
        "6. Productos con menos ventas por mes \n"
        "0. Salir del menú"+"\n")
        
        eleccion = int(input("Eliga una opción: "))  
      else:
        print("Elige una opción válida")
        print("1. Productos con más búsquedas \n"+
        "2. Productos con menos búsquedas \n"+
        "3. 5 Productos con mejores reseñas \n"+
        "4. 5 Productos con peores reseñas \n"+
        "5. Productos con más ventas por mes \n"+
        "6. Productos con menos ventas por mes \n"
        "0. Salir del menú"+"\n")
        
        eleccion = int(input("Eliga una opción: "))
 
# Fin de interacción con el usuario