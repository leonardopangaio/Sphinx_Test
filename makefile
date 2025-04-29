# Versão do Makefile
VERSION="2.8.0"
# Versão da aplicação
ver="v1.0"
SHELL := /bin/bash
.PHONY: help install_lib pyment sphinx

help: ## Mostra essa ajuda/descrição
	@grep -E '^[.a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

version: ## Mostra a versão do arquivo makefile
	@echo "A versão do Makefile é: $(VERSION)"
	@echo "A versão da aplicação é: $(ver)"


venv: ## Criação de ambiente virtual para Python
	@python3 -m venv venv

install_lib: venv requirements.txt ## Instalação das dependências
	@source venv/bin/activate \
		&& pip3 install --upgrade pip \
		&& pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir -r requirements.txt

run_python: venv requirements.txt install_lib ## Testa execução do script Python
	@source venv/bin/activate && python3 main.py

pyment: venv install_lib ## Geração das docstrings
	@source venv/bin/activate \
		&& pip3 install pyment \
		&& pyment -w -o reST main.py

sphinx-create: venv install_lib ## Geração da documentação do projeto
	@sudo apt-get install -y python3-sphinx \
		&& pip3 install sphinx_rtd_theme \
		&& mkdir -p docs/ \
		&& cd docs/ \
		&& sphinx-quickstart --ext-autodoc --ext-todo --ext-coverag \
		&& sed -i '1i import os\nimport sys\nsys.path.insert(0, os.path.abspath(".."))' conf.py \
		&& sed -i "s/^html_theme = '.*'/html_theme = 'sphinx_rtd_theme'/" conf.py \
		&& source ../venv/bin/activate \
		&& sphinx-apidoc -o . .. \
		&& echo -e " modules\n\nIndices and tables\n==================\n\n* :ref:\`genindex\`\n* :ref:\`modindex\`\n* :ref:\`search\`" >> index.rst \
		&& make html

sphinx-update: install_lib ## Atualização da documentação já gerada
	@cd docs/ \
		&& apt-get install -y python3-sphinx \
		&& pip3 install sphinx_rtd_theme \
		&& source ../venv/bin/activate \
		&& make html

requirements.txt: venv ## Gera o arquivo requirements.txt com as dependências
	@if [ ! -f requirements.txt ]; then \
			source venv/bin/activate \
			&& pip3 install pipreqs \
			&& pipreqs .; \
	fi

fix_reqs: venv ## Gera o requirements.txt baseado no que está instalado no venv
	@source venv/bin/activate \
		&& pip3 freeze > requirements.txt 