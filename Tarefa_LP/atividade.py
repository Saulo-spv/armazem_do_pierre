from enum import Enum

# Classe base para produtos
class product:
    def __init__(self, name, price, brand):
        self.price = price
        self.name = name
        self.brand = brand

    def bar_code(self, bar_code):
        return f'The bar code of {self.name} is {bar_code}'

# Classe para produtos do tipo shampoo
class shampoo(product):
    def __init__(self, name, anti_dandruff, price, brand):
        super().__init__(name, price, brand)
        self.anti_dandruff = anti_dandruff

# Classe para produtos do tipo perfume
class perfume(product):
    def __init__(self, name, price, brand):
        super().__init__(name, price, brand)

# Classe para produtos do tipo brinquedo
class toy(product):
    def __init__(self, name, price, brand):
        super().__init__(name, price, brand)

# Enumeração para marcas
class Brand(Enum):
    SHAMPOO = 'Clear'
    PERFUME = 'Jequiti'
    TOY = 'Mattel'

# Classe para o inventário
class Inventario:
    def __init__(self):
        # Inicializa listas vazias para cada tipo de produto
        self.shampoo_stock = []
        self.perfume_stock = []
        self.toy_stock = []

    def add_shampoo(self, shampoo):
        # Adiciona um objeto de shampoo ao estoque de shampoos
        self.shampoo_stock.append(shampoo)

    def add_perfume(self, perfume):
        # Adiciona um objeto de perfume ao estoque de perfumes
        self.perfume_stock.append(perfume)

    def add_toy(self, toy):
        # Adiciona um objeto de brinquedo ao estoque de mochilas
        self.toy_stock.append(toy)

    def list_shampoos(self):
        # Retorna a lista de shampoos disponíveis no estoque
        return self.shampoo_stock

    def list_perfumes(self):
        # Retorna a lista de perfumes disponíveis no estoque
        return self.perfume_stock

    def list_toys(self):
        # Retorna a lista de brinquedos disponíveis no estoque
        return self.toy_stock

# Dicionário de produtos
products = {
    'shampoo' : ['ClearMen - Cristiano Ronaldo', 32, Brand.SHAMPOO],
    'perfume' : ['Eliana', 145, Brand.PERFUME],
    'toy' : ['HotWheels', 507, Brand.TOY]
}

# Lista de produtos
list_of_products = []

# Preenche a lista de produtos com base no dicionário
for item in products:
    name = products[item][0]
    price = products[item][1]

    if item == 'shampoo':
        product_instance = shampoo(name, True, price, Brand.SHAMPOO.value)
    elif item == 'perfume':
        product_instance = perfume(name, price, Brand.PERFUME.value)
    elif item == 'toy':
        product_instance = toy(name, price, Brand.TOY.value)

    list_of_products.append(product_instance)

# Exibe informações dos produtos
for product in list_of_products:
    print(f"Product Name: {product.name}")
    print(f"Product Price: {product.price}")
    print(f"Product Brand: {product.brand}")
    print(f"Product Bar Code: {product.bar_code('12345')}")


print("#"*40)

# Criar uma instância do Inventario
inventario = Inventario()

# Adicionar shampoos ao estoque
inventario.add_shampoo(list_of_products[0])

# Adicionar perfumes ao estoque
inventario.add_perfume(list_of_products[1])

# Adicionar brinquedos ao estoque
inventario.add_toy(list_of_products[2])

# Listar shampoos disponíveis no estoque
print("Shampoos no estoque:")
shampoos_no_estoque = inventario.list_shampoos()
for shampoo in shampoos_no_estoque:
    print(f" - {shampoo.name}")

# Listar perfumes disponíveis no estoque
print("\nPerfumes no estoque:")
perfumes_no_estoque = inventario.list_perfumes()
for perfume in perfumes_no_estoque:
    print(f" - {perfume.name}")

# Listar mochilas disponíveis no estoque
print("\nMochilas no estoque:")
brinquedos_no_estoque = inventario.list_toys()
for toy in brinquedos_no_estoque:
    print(f" - {toy.name}")