# Sphinx_Test

Este arquivo tem como objetivo a informar os passos que foram realizados para conseguir instalar o Sphinx e executar ele a fim de gerar a documentação de forma automática com base no código fonte analisado pela ferramenta.

## Etapa Principal

1. Instalação do módulo, pode ser via pip com o comando `pip3 install sphinx`, contudo para o exemplo a instalação foi realizada diretamente no sistema operacional com o comando `apt-get install -y python3-sphinx`.

2. Neste caso, para simplicidade, eu criei uma pasta docs dentro do projeto em si, mas nada impede que criemos uma pasta separada para ser tratado em repositório/pipeline separado.

3. Criação do projeto Sphinx, neste caso é necessário estar dentro da pasta onde a documentação Sphinx será gerada, e para isto utilizei o seguinte comando `sphinx-quickstart --ext-autodoc --ext-todo --ext-coverag`

> :memo: **Note:** Nesta etapa tive dificuldades, pois em todos os vídeos e documentações que vi, a simples execução do comando `sphinx-quickstart` era o suficiente, contigo para versões atuais, esse comando vai gerar o projeto sem nenhuma configuração existente.

4. Nesta etapa deveremos alterar o arquivo `conf.py`, descomentando as linhas referentes a importação de duas bibliotecas e a definição de caminho.

5. Para realizar a geração da documentação, utilizei o comando `sphinx-apidoc -o . ..` para que o Sphinx gere a documentação base (`index.rst` e demais arquivos).

6. Execução do `make html` para que o Sphinx gere o site com a documentação.

## Extras

Caso seja um código que não tenha nenhum docstring, podemos utilizar a lib pyment.

O comando de exemplo que foi utilizado durante a apresentação é o `pyment -w main.py`.

## Observações

Para que o Sphinx funcione de forma nativa e não seja necessário a utilização de módulo externo para interpretar as docstrings, elas devem ser escritas utilizando a linguagem reStructuredText.

Também é possível utilizar o Sphinx para validar a cobertura de documentação, então invés de utilizar o docstr-coverage para realizar essa validação, podemos utilizar o próprio Sphinx com o comando `sphinx-build -b coverage ./ ./_build/` ou de forma mais simplificada o `make coverage`, onde ele vai gerar um arquivo .txt com o relatório do que ele analisou.

## Referências

- https://eikonomega.medium.com/getting-started-with-sphinx-autodoc-part-1-2cebbbca5365
- https://youtu.be/b4iFyrLQQh4?si=p0sYW1x_8ES567oN
