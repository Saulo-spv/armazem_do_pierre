from enum import Enum

# Classe base para produtos
class product:
    def __init__(self, name, price, brand, bar_code):
        self.price = price
        self.name = name
        self.brand = brand
        self.bar_code = bar_code

    def get_bar_code(self):
        return self.bar_code
    
    def describe(self):
        print(f"Product Name: {self.name}")
        print(f"Product Price: {self.price}")
        print(f"Product Brand: {self.brand}")
        print(f"Product Bar Code: {self.bar_code}")


# Classe para produtos do tipo shampoo
class shampoo(product):
    def __init__(self, name, anti_dandruff, price, brand, bar_code):
        super().__init__(name, price, brand, bar_code)
        self.anti_dandruff = anti_dandruff
    
    def describe(self):
        print(f"Product Name: {self.name}")
        print(f"Anti-Dandruff: {self.anti_dandruff}")
        print(f"Product Price: {self.price}")
        print(f"Product Brand: {self.brand}")
        print(f"Product Bar Code: {self.bar_code}")


# Classe para produtos do tipo perfume
class perfume(product):
    def __init__(self, name, price, brand, bar_code):
        super().__init__(name, price, brand, bar_code)


# Classe para produtos do tipo brinquedo
class toy(product):
    def __init__(self, name, price, brand, bar_code):
        super().__init__(name, price, brand, bar_code)


# Enumeração para marcas
class Brand(Enum):
    SHAMPOO = 'Clear'
    PERFUME = 'Jequiti'
    TOY = 'Mattel'


class ProductNotExistsError(Exception):
    def __init__(self):
        message = message="O produto não está cadastrado."
        super().__init__(message)


class ProductNotInStockError(Exception):
    def __init__(self):
        message = "O produto não está em estoque."
        super().__init__(message)


# Classe para o inventário
class Inventario:
    def __init__(self):
        # Inicializa listas vazias para cada tipo de produto
        self.shampoo_stock = {}
        self.perfume_stock = {}
        self.toy_stock = {}


    def add_shampoo(self, shampoo):
        # Adiciona um objeto de shampoo ao estoque de shampoos
        try:
            try:
                self.shampoo_stock[shampoo.bar_code] += 1
            except KeyError:
                raise ProductNotExistsError()
        except ProductNotExistsError:
            self.shampoo_stock[shampoo.bar_code] = 1


    def add_perfume(self, perfume):
        # Adiciona um objeto de perfume ao estoque de perfumes
        try:
            try:
                self.perfume_stock[perfume.bar_code] += 1
            except KeyError:
                raise ProductNotExistsError()
        except ProductNotExistsError:
            self.perfume_stock[perfume.bar_code] = 1


    def add_toy(self, toy):
        # Adiciona um objeto de brinquedo ao estoque de brinquedos
        try:
            try:
                self.toy_stock[toy.bar_code] += 1
            except KeyError:
                raise ProductNotExistsError()
        except ProductNotExistsError:
            self.toy_stock[toy.bar_code] = 1
            

    # Retorna a lista de produtos no estoque
    def list_shampoos(self):
        return self.shampoo_stock

    def list_perfumes(self):
        return self.perfume_stock
    
    def list_toys(self):
        return self.toy_stock
    

    # Vende produto no estoque
    def sell_product(self, bar_code):
        try:
            if bar_code in self.shampoo_stock:
                if self.shampoo_stock[bar_code] < 1:
                    raise ProductNotInStockError()
                else:
                    self.shampoo_stock[bar_code] -= 1
            elif bar_code in self.perfume_stock:
                if self.perfume_stock[bar_code] < 1:
                    raise ProductNotInStockError()
                else:
                    self.perfume_stock[bar_code] -= 1
            elif bar_code in self.toy_stock:
                if self.toy_stock[bar_code] < 1:
                    raise ProductNotInStockError()
                else:
                    self.toy_stock[bar_code] -= 1
            else:
                raise ProductNotExistsError()
        except ProductNotInStockError:
            print("Não é possível realizar a venda desse produto.")
             

if __name__ == '__main__':
    # Criar uma instância do Inventario
    inventario = Inventario()

    # Cria produtos
    shampoo_clearmen = shampoo('ClearMen - Cristiano Ronaldo', True, 32, Brand.SHAMPOO.value, '12345')
    perfume_eliana = perfume('Eliana', 145, Brand.PERFUME.value, '12346')
    toy_mattel = toy('HotWheels', 507, Brand.TOY.value, '12347')

    # Descrição do produto
    perfume_eliana.describe()

    # Adicionar shampoos ao estoque
    inventario.add_shampoo(shampoo_clearmen)

    # Adicionar perfumes ao estoque
    inventario.add_perfume(perfume_eliana)

    # Adicionar brinquedos ao estoque
    inventario.add_toy(toy_mattel)

    # Vende produto
    inventario.sell_product('12345')

    # Lista estoque de shampoo
    print(inventario.list_shampoos())