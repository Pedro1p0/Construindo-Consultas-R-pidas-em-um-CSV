# Projeto Building Fast Queries on a CSV

Este projeto é uma extensão do projeto guiado da Dataquest "Building Fast Queries on a CSV". O objetivo é implementar funcionalidades adicionais, realizar uma análise de complexidade das soluções implementadas e criar um vídeo explicativo sobre o projeto.
# Equipe
- Pedro Henrique Bezerra Fernandes
- Pedro Vitor Bezerra Clemente
## Funcionalidades Adicionais

### Consulta por Faixa de Preço
Foi implementada a funcionalidade de consultar laptops dentro de uma faixa de preço especificada, permitindo que o usuário encontre laptops com preços entre um valor mínimo e máximo.

Exemplo de uso:
```python
laptops.find_laptops_within_budget_range(min_price=1000, max_price=1500)
```
Consulta por Especificações

Também foi adicionada a capacidade de buscar laptops com base em especificações desejadas, como quantidade de RAM, capacidade de armazenamento e placa gráfica.

Exemplo de uso:

```python

criteria = {
    'ram': '8GB',
    'storage': '256GB SSD',
    'graphics': 'NVIDIA GeForce GTX 1650'
}
laptops.find_laptops_by_specifications(**criteria)
```

Análise de Complexidade
Função get_laptop_from_id

    Big O: O(n)
    Big θ: O(n/2)
    Big Ω: O(1)

Função get_laptop_from_id_fast

    Big O: O(1)
    Big θ: O(1)
    Big Ω: O(1)

Função check_promotion_dollars

    Big O: O(n^2)
    Big θ: O(n^2)
    Big Ω: O(1)

Função check_promotion_dollars_fast

    Big O: O(n)
    Big θ: O(n)
    Big Ω: O(1)

Função find_best_laptop_within_budget

    Big O: O(log n)
    Big θ: O(log n)
    Big Ω: O(1)

Função find_laptops_within_budget_range

    Big O: O(n)
    Big θ: O(n/2)
    Big Ω: O(1)

Função find_laptops_by_specifications

    Big O: O(n * k)
    Big θ: O(n * k)
    Big Ω: O(n)

Documentação e Comentários

O código está bem documentado com comentários explicativos que detalham as diferentes partes do código e sua funcionalidade.
Vídeo Explicativo

[Assista ao vídeo explicativo sobre o projeto aqui](https://www.loom.com/share/3a02b42907a84b95a88c07914549951c)
Conclusão

Este projeto estendeu o projeto guiado da Dataquest, adicionando funcionalidades adicionais úteis para consultar laptops com base em preço e especificações. Além disso, foi realizada uma análise de complexidade para cada função implementada, fornecendo insights sobre o desempenho dessas operações em relação ao tamanho do conjunto de dados. O código também foi devidamente documentado e comentado para facilitar a compreensão.



