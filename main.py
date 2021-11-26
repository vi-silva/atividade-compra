from carrinho import Carrinho, Cliente, Produto


class Utilidades:
    @staticmethod
    def entrada_tratada_int(mensagem):
        while True:
            try:
                return int(input(mensagem))
            except:
                print('Informe um valor numérico')
    @staticmethod
    def entrada_tratada_float(mensagem):
        while True:
            try:
                return float(input(mensagem))
            except:
                print('Informe um valor numérico')

class Aplicacao:
    comandos = [
        (0, 'Informar cliente'),
        (1, 'Adicionar produto'),
        (2, 'Incrementar item'),
        (3, 'Decrementar item'),
        (4, 'Remover item'),
        (5, 'Exibir resumo')
    ]

    def __init__(self):
        self._carrinho = Carrinho()

    def executar(self):
        while True:
            self._exibir_menu()
            comando = input('> Selecione uma opcao acima: ')
            deve_sair = self.executar_comando(comando)
            if deve_sair:
                break

    def executar_comando(self, comando):
        if comando == '0':
            self._inserir_cliente()
        elif comando == '1':
            self._adicionar_produto()
            self._exibir_itens()
        elif comando == '2':
            self._incrementar_item()
            self._exibir_itens()
        elif comando == '3':
            self._decrementar_item()
            self._exibir_itens()
        elif comando == '4':
            self._remover_items()
            self._exibir_itens()
        elif comando == '5':
            self._exibir_resumo()
        else:
            return True

    def _inserir_cliente(self):
        nome = input('> Informe seu nome: ')
        identidade = input('> Informe seu identidade: ')
        cliente = Cliente(nome, identidade)
        self._carrinho.cliente = cliente

    def _adicionar_produto(self):
        print('Informe os dados: ')
        descricao = input('Descricao: ')
        codigo = input('Codigo: ')
        valor_unitario = Utilidades.entrada_tratada_float('Valor unitário: ')
        quantidade = Utilidades.entrada_tratada_int('Quantidade: ')
        desconto = Utilidades.entrada_tratada_int('Desconto: ')
        produto = Produto(codigo=codigo, descricao=descricao, desconto=desconto,
                          valor_unitario=valor_unitario, quantidade=quantidade)
        self._carrinho.add_item(produto)

    def _incrementar_item(self):
        codigo = input('Codigo: ')
        quantidade = Utilidades.entrada_tratada_int('Quantidade: ')
        self._carrinho.incrementar_item(codigo, quantidade)

    def _decrementar_item(self):
        codigo = input('Código: ')
        quantidade = Utilidades.entrada_tratada_int('Quantidade: ')
        self._carrinho.decrementar_item(codigo, quantidade)

    def _remover_items(self):
        codigo = input('Código: ')
        self._carrinho.remover_item(codigo)

    def _exibir_itens(self):
        self._carrinho.exibir_itens()

    def _exibir_resumo(self):
        self._carrinho.exibir_resumo()

    def _exibir_menu(self):
        for op in Aplicacao.comandos:
            opcao, descricao = op
            print(f'[{opcao}] - {descricao}')

app = Aplicacao()

app.executar()
