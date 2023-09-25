import csv
import time
import random

class Inventory:
    def __init__(self, csv_filename):
        
        
        # Lê o arquivo CSV usando a codificação detectada
        with open(csv_filename, encoding="ISO-8859-1") as file:
            rows = list(csv.reader(file)) 
        
        # Separa o cabeçalho das linhas de dados
        self.header = rows[0]
        self.rows = rows[1:]
        
        # Renomeia as colunas 'id' e 'price'
        self.header[0] = 'id'
        self.header[-1] = 'price'
        
        # Converte as colunas 'id' e 'price' para tipo inteiro
        for row in self.rows:
            row[0] = int(row[0])
            row[-1] = int(float(row[-1]))
            
        # Cria um dicionário de mapeamento de id para linha e um conjunto de preços únicos
        self.id_to_row = {}
        self.prices = set()
            
        for row in self.rows:
            self.id_to_row[row[0]] = row
            self.prices.add(row[-1])
        
        # Ordena as linhas por preço
        self.rows_by_price = sorted(self.rows, key=lambda row: row[-1])
    
    # Retorna um laptop e suas características com base no ID do laptop
    def get_laptop_from_id(self, laptop_id):
        for row in self.rows:    
            if row[0] == laptop_id:
                return row
        return None
    #Big O: O(n) - Pior caso, onde n é o número de laptops no inventário. Isso ocorre quando o laptop desejado é o último na lista.
    #Big θ: O(n/2) - Caso médio, quando o laptop desejado está no início da lista.
    #Big Ω: O(1) - Melhor caso, quando o laptop desejado é o primeiro na lista.
    
    # Realiza a mesma tarefa que o método acima, mas de maneira mais rápida usando um dicionário
    def get_laptop_from_id_fast(self, laptop_id):
        if laptop_id in self.id_to_row:
            return self.id_to_row[laptop_id]
        return None
    #Big O: O(1) - dicionário Python, que é uma estrutura de dados de acesso rápido.
    #Big θ: O(1) - O acesso a um dicionário é uma operação constante.
    #Big Ω: O(1) - Também é constante no melhor caso.
        
    # Determina se um valor em dólares é igual ao preço de qualquer laptop
    # ou à soma dos preços de dois laptops
    def check_promotion_dollars(self, dollars):
        for row in self.rows:  
            if row[-1] == int(dollars):
                return True
            for other_row in self.rows:
                if other_row[-1] + row[-1] == int(dollars):
                    return True
        return False
    # Análise de Complexidade:
    # Big O: O(n^2) - Pior caso, onde n é o número de laptops no inventário. Isso ocorre quando nenhum laptop corresponde ao valor em dólares, 
    # e a função precisa verificar todas as combinações possíveis de laptops, resultando em dois loops aninhados.
    # Big θ: O(n^2) - Caso médio, pois, em média, metade dos laptops precisará ser verificada, resultando em dois loops aninhados.
    # Big Ω: O(1) - Melhor caso, quando o valor em dólares corresponde a um laptop diretamente, resultando em uma verificação rápida e uma operação constante.


    # Realiza a mesma tarefa que o método acima, mas de maneira mais rápida, usando conjuntos
    def check_promotion_dollars_fast(self, dollars):
        if dollars in self.prices:
            return True
        for price in self.prices:
            for other_price in self.prices:
                total = price + other_price
                if dollars == total:
                    return True
        return False
    # Análise de Complexidade:
    # Big O: O(n) - Pior caso, onde n é o número de preços de laptops únicos no inventário. O loop for que percorre self.prices requer O(n) operações.
    # Big θ: O(n) - Caso médio, pois, em média, o número de preços únicos em self.prices será proporcional a n, resultando em um loop de complexidade O(n).
    # Big Ω: O(1) - Melhor caso, quando dollars corresponde a um preço único de laptop em self.prices. Nesse caso, a função retorna imediatamente e requer uma operação constante.
    
    # Retorna o número de laptops que custam menos ou igual a um certo preço.
    # Também retorna o laptop mais caro com preço igual ou inferior ao mesmo preço
    def find_best_laptop_within_budget(self, budget):
        # Itera através do algoritmo de busca binária
        range_start = 0
        range_end = len(self.rows_by_price)
        while range_start < range_end:
            range_middle = (range_start + range_end) // 2
            price_check = self.rows_by_price[range_middle][-1]
            
            # Se o orçamento for igual ao preço na lista, retorne esse laptop
            if budget == price_check:
                top_laptop = range_middle + 1
                laptops_in_budget = self.rows_by_price[:top_laptop]
                print("Há {} laptops dentro do seu orçamento.".format(len(laptops_in_budget)))
                return laptops_in_budget[-1]
            
            # Atualiza o intervalo de busca binária até a convergência do intervalo 
            elif budget < price_check:
                range_end = range_middle   
            else:
                range_start = range_middle + 1
                
        # Após a convergência do intervalo, retorne o laptop mais caro acessível
        
        # Se o orçamento for <= preço na lista, então retorne o próximo laptop com preço mais baixo
        if budget <= self.rows_by_price[range_middle][-1]:
            if range_middle == 0:
                return print("Não há laptops dentro do seu orçamento.")
            top_laptop = range_middle
            laptops_in_budget = self.rows_by_price[:top_laptop]
            print("Há {} laptops dentro do seu orçamento.".format(len(laptops_in_budget)))
            return laptops_in_budget[-1]
        
        # Se o orçamento for > preço na lista, então retorne esse laptop
        else:
            top_laptop = range_middle + 1
            if top_laptop == 1:
                laptop = self.rows_by_price[range_middle]
                print("Há 1 laptop dentro do seu orçamento.")
                return laptop
            laptops_in_budget = self.rows_by_price[:top_laptop]
            print("Há {} laptops dentro do seu orçamento.".format(len(laptops_in_budget)))
            return laptops_in_budget[-1]
        #Big O: O(log n) - Pior caso, devido ao algoritmo de busca binária.
        #Big θ: O(log n) - Caso médio, pois o algoritmo de busca binária tem uma convergência rápida em média.
        #Big Ω: O(1) - Melhor caso, quando o orçamento corresponde ao preço de um laptop diretamente.
    
    # Retorna uma lista de laptops dentro de um intervalo de orçamento (preço mínimo e máximo).
    def find_laptops_within_budget_range(self, min_price, max_price):
        laptops_within_budget = []
        for row in self.rows_by_price:
            price = row[-1]
            if min_price <= price <= max_price:
                laptops_within_budget.append(row)
        return laptops_within_budget
    #Big O: O(n) - Pior caso, pois o método percorre todos os laptops no inventário.
    #Big θ: O(n/2) - Caso médio, pois, em média, metade dos laptops estará dentro do intervalo de preço.
    #Big Ω: O(1) - Melhor caso, quando nenhum laptop está dentro do intervalo de preço.

    # Retorna uma lista de laptops que atendem aos critérios de especificações fornecidos
    def find_laptops_by_specifications(self, **kwargs):
        matching_laptops = []
        for row in self.rows:
            is_match = True
            for key, value in kwargs.items():
                column_index = None
                if key == 'cpu':
                    column_index = 6
                elif key == 'ram':
                    column_index = 7
                elif key == 'storage':
                    column_index = 8
                elif key == 'graphics':
                    column_index = 9
                
                if column_index is not None and row[column_index] != value:
                    is_match = False
                    break
            
            if is_match:
                matching_laptops.append(row)
        
        return matching_laptops
    #Big O: O(n * k) - Pior caso, devido ao loop aninhado que verifica todos os critérios para todos os laptops no inventário.
    #Big θ: O(n * k) - Caso médio, pois em média, metade dos laptops precisará ser verificada em relação a cada critério.
    #Big Ω: O(n) - Melhor caso, quando apenas um critério é especificado e muitos laptops são descartados de imediato.


laptops = Inventory('laptops.csv')
#Gerando uma lista de 10.000 números de identificação aleatórios
random_ids = [random.randint(0, 1320) for _ in range(10000)]

#Pegando o tempo do método da lista de listas
total_time_no_dict=0
for random_id in random_ids:
    
    start = time.time()
    laptops.get_laptop_from_id(random_id)
    end = time.time()
    total_time_no_dict += end - start


# Pegando o tempo do método do dicionário
total_time_dict=0
for random_id in random_ids:
    
    start = time.time()
    laptops.get_laptop_from_id_fast(random_id)
    end = time.time()
    total_time_dict += end - start

print("tempo do método da lista de listas é : ",total_time_no_dict)
print("tempo do método do dicionário é : ",total_time_dict)

#Gerando uma lista de 100 valores de ofertas promocionais aleatórias
random_prices = [random.randint(100, 5000) for i in range(100)]
#Pegando o tempo do método de conjuntos de dados
total_time_no_set = 0
for random_price in random_prices:
    
    start = time.time()
    laptops.check_promotion_dollars(random_price)
    end = time.time()
    total_time_no_set += end - start


#Pegando o tempo do método sets
total_time_set = 0
for random_price in random_prices:
    
    start = time.time()
    laptops.check_promotion_dollars_fast(random_price)
    end = time.time()
    total_time_set += end - start

print("tempo do método é : ",total_time_no_set)
print("tempo do método do  conjuntos é : ",total_time_set)

print(laptops.find_best_laptop_within_budget(1000))
print(laptops.find_best_laptop_within_budget(100))

print(laptops.find_laptops_within_budget_range(1000,1010))


criteria = {
    'ram': '8GB',
    'storage': '128GB SSD',
    'graphics': 'Intel Iris Plus Graphics 640'
}
laptops_with_specifications = laptops.find_laptops_by_specifications(**criteria)
for laptop in laptops_with_specifications:
    print("Laptop disponível com as especificações desejadas:")
    print(laptop)