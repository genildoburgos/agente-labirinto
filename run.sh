#!/bin/bash

# Define o diretório atual do script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/.venv"

# Verifica se o ambiente virtual existe. Se não existir, cria.
if [ ! -d "$VENV_DIR" ]; then
    echo "Ambiente virtual não encontrado. Criando..."
    python3 -m venv "$VENV_DIR"
    if [ $? -ne 0 ]; then
        echo "Erro: Falha ao criar o ambiente virtual. Verifique se o pacote python3-venv está instalado."
        exit 1
    fi
fi

# Garante que as dependências estejam instaladas
echo "Verificando dependências..."
"$VENV_DIR/bin/pip" install -r "$SCRIPT_DIR/requirements.txt" --quiet

# Função para exibir ajuda
show_help() {
    echo "Uso: ./run.sh [demo|evaluate]"
    echo ""
    echo "Opções:"
    echo "  demo      Executa a demonstração do A* (abre a interface gráfica do Pygame)"
    echo "  evaluate  Executa a avaliação estatística (compara A* e Aleatório)"
    echo ""
    echo "Se nenhum argumento for passado, um menu interativo será exibido."
}

# Executa o código Python no ambiente virtual
run_mode() {
    local mode=$1
    if [ "$mode" = "demo" ]; then
        echo -e "\nIniciando a demonstração do A*..."
        "$VENV_DIR/bin/python3" "$SCRIPT_DIR/main.py" --mode demo
    elif [ "$mode" = "evaluate" ]; then
        echo -e "\nIniciando a avaliação dos agentes..."
        "$VENV_DIR/bin/python3" "$SCRIPT_DIR/main.py" --mode evaluate
    else
        show_help
    fi
}

# Trata os argumentos
if [ $# -eq 1 ]; then
    run_mode "$1"
elif [ $# -gt 1 ]; then
    show_help
else
    # Menu interativo caso não passe nenhum parâmetro
    echo "============================================="
    echo "            AGENTE LABIRINTO - MENU          "
    echo "============================================="
    echo "1) Executar Demonstração (A* Gráfico)"
    echo "2) Executar Avaliação Estatística (A* vs. Aleatório)"
    echo "3) Sair"
    echo "============================================="
    read -p "Escolha uma opção [1-3]: " option
    case $option in
        1) run_mode "demo" ;;
        2) run_mode "evaluate" ;;
        *) echo "Saindo..."; exit 0 ;;
    esac
fi
