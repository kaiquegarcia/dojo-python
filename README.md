# Coding Dojo Python

Um repositório pronto para prover um espaço legal para coding dojos em Python!

Especialmente feito a pedido do [Eber Santana](https://www.linkedin.com/in/ebersantana/). Espero que goste, meu caro! Use com moderação, haha.

## Guia de uso

Para cada evento de coding dojo, é necessário criar uma pasta com um nome único. O nome dessa pasta será o nome do pacote python usado no código, então evite o uso de caracteres que não sejam letras alfanuméricas em caixa baixa (lowercase, `a-z0-9`).

Minha sugestão é: se for fazer várias edições de coding dojo, coloque o nome `edicaoXXX``, onde XXX é o número da edição. Se quiser mapear os tópicos de cada edição, coloque em algum outro arquivo de documentação uma lista mapeando cada pacote a um assunto. Por exemplo:

- [example1](./example1/README.md): Desafio do Código Morse

## Escrevendo o desafio

Após criar a pasta do desafio, coloque a descrição em um arquivo `README.md` (como feito no [exemplo](./example1/README.md)) e implemente um esboço vazio de testes. Note que essa parte depende de como está a maturidade de testes do time que irá ser desafiado. Se as pessoas envolvidas já sabem escrever os testes, somente o README basta! Deixa a estrutura de testes com eles. Caso seja algo novo para qualquer pessoa envolvida, vale a pena já deixar o arquivo pronto com todos os testes escritos nas primeiras edições. Depois você começa a só deixar as funções vazias... E, por fim, apenas a classe vazia, deixando a responsabilidade sobre refletir os casos a serem provados pelos envolvidos. No meu exemplo, eu usei o pacote `unittest` do Python para escrever tudo. Mas o ideal é que isso seja aberto para que todos decidam que pacote utilizar, talvez até importar.

```python
import unittest

class SuaClasseTest(unittest.TestCase):
    def setUp(self):
        self.algumaPropriedade = algumaCoisa()

    def seusTestes(self):
        self.assertEqual(self.algumaPropriedade.algumaCoisa(), "resultado-esperado")
```

Falando especificamente sobre python, é importante criar um arquivo vazio `__init__.py` dentro da pasta do desafio, pois é esse arquivo que determina que aquela pasta é um pacote python. Sem isso, você não conseguirá importar o arquivo de solução nos arquivos de teste.

## Solucionando o desafio

Note que os testes não rodarão por dois motivos:

1. o código de solução ainda nem existe, não tem como nenhum teste passar ou algo foi feito errado;
2. o teste espera respostas válidas.

Dito isso, o primeiro passo é escrever outro arquivo python no mesmo diretório do desafio. O indicado é solucionar um teste por vez, mas algumas vezes alguém vai conseguir solucionar todos ou vários com uma implementação só. Se você é o sensei da edição, por favor, tente manter a galera focada em solucionar testes e não em implementar o recurso inteiro de uma vez só. A ideia é: terminou o código que resolve o teste? Roda pra ver (código de execução de testes mais abaixo).

Então, aos poucos (baby steps), todos os testes serão resolvidos e o código estará finalizado. Daí a importância de testes bem escritos abordando todas as possibilidades que julgarem necessárias.

Enfim, para que os testes funcionem, após a escrita do arquivo, é preciso adicionar a importação no arquivo de teste:

```python
from edicaoXXX.arquivoSolucao import oQuePrecisarNosTestes
```

Não esqueçam desse detalhe, hehe.

## Executando os testes

Abra um terminal no diretório raiz do repositório e execute o comando a seguir:
```bash
python -m unittest edicaoXXX/arquivo_de_teste.py
```

Onde `edicaoXXX` é a pasta do desafio e `arquivo_de_teste.py` é o nome do arquivo onde estão os testes que quer executar.

Se quiser rodar todos os testes em um comando só, é importante mencionar que os mesmos devem ter o nome terminando com `_tests` ou você deverá modificar o comando para o término em comum:

```bash
python -m unittest discover -s edicaoXXX -p "*_tests.py"
```

No caso do exemplo feito nesse repositório, você pode fazer qualquer um dos comandos a seguir para testar:

- Testes de encode:
  ```bash
  python -m unittest example1/encode_tests.py
  ```
- Testes de decode:
  ```bash
  python -m unittest example1/decode_tests.py
  ```
- Todos os testes:
  ```bash
  python -m unittest discover -s example1 -p "*_tests.py"
  ```


E é isso, agora você está pronto para desenrolar os coding dojos em Python!

Qualquer dúvida, você pode encontrar algumas formas de contato [aqui](https://kaiquegarcia.dev/).