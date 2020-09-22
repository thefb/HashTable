# Capacidade do array interno
INITIAL_CAPACITY = 50

# Estrutura de dados em nós - essencialmente um nó de listas conectadas


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return "<Node: (%s, %s), next %s>" % (self.key, self.value, self.next != None)

    def __repr__(self):
        return str(self)

# tabela hash com elos separados


class HashTable:
    # inicializa a tabela hash
    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    # Gera um valor hash para uma determinada chave
    # input: key - String
    # Output: Index de 0 até a capacidade maxima
    def hash(self, key):
        hashsum = 0
        # para cada caractere na chave
        for idx, c in enumerate(key):   
            # adiciona (index + tamanho da chave) ** (valor ordinario do caractere atual)
            hashsum += (idx + len(key)) ** ord(c)
            # faz uma divisão em modulo para manter a soma de todos os hash's entre [0, (capacidade maxima - 1)]
            hashsum = hashsum % self.capacity
        return hashsum

    # Insere na tabela uma chave e seu valor
    def insert(self, key, value):
        # aumenta o tamanho da tabela.
        self.size += 1
        # calcula o index da chave
        index = self.hash(key)
        # vai até o nó correspondente
        node = self.buckets[index]
        # se o bucket estiver vazio
        if node is None:
            # cria um nó, insere-o e retorna
            self.buckets[index] = Node(key, value)
            return
        # Itera ate o final da lista de determinado index
        prev = node
        while node is not None:
            prev = node
            node = node.next
        # adiciona um novo nó no final da lista com a cahve e valor fornecido
        prev.next = Node(key, value)

    # encontra na tabela a chave solicitada e retorna seus valores associados
    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            return result