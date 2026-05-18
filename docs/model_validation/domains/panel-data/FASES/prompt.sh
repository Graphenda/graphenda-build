#!/bin/bash

# ============================================================
# CONTENT GENERATION — Panel Data Models Domain
# Execucao automatizada com Claude Code
# ============================================================

# --- CONFIGURACOES ---
PROJECT_ROOT="/home/guhaase/projetos/Graphenda"
MRL_ROOT="/home/guhaase/projetos/ModelRiskLab/mrl-content-files"
SPEC_DIR="$PROJECT_ROOT/build/docs/model_validation/domains/panel-data/FASES"
DOMAIN_SPEC="$PROJECT_ROOT/build/docs/model_validation/domains/02-panel-data.md"
LOG_DIR="$PROJECT_ROOT/logs/content-generation/panel-data"
TOTAL_FASES=5

# --- DIRETORIO DE LOG ---
mkdir -p "$LOG_DIR"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# --- Cores para output ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m'

# --- FUNCOES DE LOG ---
log() {
    echo -e "${BLUE}[$(date +%H:%M:%S)]${NC} $1"
}

log_ok() {
    echo -e "${GREEN}[$(date +%H:%M:%S)] OK${NC} $1"
}

log_err() {
    echo -e "${RED}[$(date +%H:%M:%S)] ERR${NC} $1"
}

log_separator() {
    echo -e "${PURPLE}================================================================${NC}"
}

# --- FUNCOES AUXILIARES ---
count_pending_checkboxes() {
    local file="$1"
    local n
    n=$(grep -c '\- \[ \]' "$file" 2>/dev/null) || n=0
    echo "$n"
}

count_completed_checkboxes() {
    local file="$1"
    local n
    n=$(grep -c '\- \[x\]' "$file" 2>/dev/null) || n=0
    echo "$n"
}

show_progress() {
    local file="$1"
    local pending=$(count_pending_checkboxes "$file")
    local completed=$(count_completed_checkboxes "$file")
    local total=$((pending + completed))
    if [ "$total" -gt 0 ]; then
        local pct=$((completed * 100 / total))
        echo -e "${YELLOW}  Progresso: $completed/$total ($pct%)${NC}"
    fi
}

# --- GERADOR DE PROMPT ---
build_prompt() {
    local spec_file="$1"
    local fase_num="$2"

    cat <<PROMPT
Voce e um pesquisador e redator tecnico especializado em econometria e model risk management.

## Contexto do projeto
- Projeto: ModelRiskLab — Plataforma de conteudo sobre Model Risk Management
- Diretorio de conteudo: $MRL_ROOT/content/en/
- Templates: $MRL_ROOT/templates/
- Especificacao do dominio: $DOMAIN_SPEC

## Tarefa
Execute COMPLETAMENTE a fase F$fase_num descrita na especificacao abaixo.
Siga todas as etapas de implementacao com atencao.
Apos completar cada criterio, edite o arquivo da especificacao em disco
trocando "- [ ]" por "- [x]" na linha correspondente.

## Regras
1. TODO conteudo deve ser baseado em PESQUISA REAL — use WebSearch e WebFetch
2. NAO invente dados, metricas ou referencias — busque fontes reais
3. Siga os templates e formatos especificados
4. Inclua frontmatter YAML valido em todos os arquivos .md
5. IMPORTANTE: Apos completar cada criterio de aceite, use a ferramenta Edit
   para editar o arquivo $spec_file e trocar "- [ ]" por "- [x]" no criterio
   correspondente. Voce DEVE editar o arquivo .md em disco.
6. Se um criterio de aceite ja esta marcado como [x], pule-o
7. Execute as verificacoes listadas em cada etapa
8. Para codigo Python: garanta que a sintaxe e valida e o codigo e funcional
9. Para dados em painel: use o dataset Grunfeld (statsmodels) como referencia principal

## Conteudo ja gerado em fases anteriores
$(if [ "$fase_num" -gt 1 ]; then
    echo "Verifique o conteudo ja gerado em:"
    echo "- Guides: $MRL_ROOT/content/en/guides/panel-data/"
    echo "- News: $MRL_ROOT/content/en/news/"
    echo "- Code: $MRL_ROOT/content/en/code-examples/panel-data/"
    echo "- Reports: $MRL_ROOT/content/en/report-templates/panel-data/"
fi)

## Arquivo da especificacao (edite os checkboxes NESTE arquivo)
Caminho: $spec_file

## Especificacao
$(cat "$spec_file")
PROMPT
}

# --- VERIFICACAO DE PRE-REQUISITOS ---
if ! command -v claude &> /dev/null; then
    log_err "Claude Code CLI nao encontrado. Instale com: npm install -g @anthropic-ai/claude-code"
    exit 1
fi

for i in $(seq 1 $TOTAL_FASES); do
    if [ ! -f "$SPEC_DIR/CONTENT_GEN_F${i}.md" ]; then
        log_err "Arquivo de especificacao nao encontrado: CONTENT_GEN_F${i}.md"
        exit 1
    fi
done

log_ok "Todos os arquivos de especificacao encontrados"

# --- VERIFICAR DIRETORIOS DE DESTINO ---
DEST_DIRS=(
    "$MRL_ROOT/content/en/guides/panel-data"
    "$MRL_ROOT/content/en/news"
    "$MRL_ROOT/content/en/code-examples/panel-data/modeling"
    "$MRL_ROOT/content/en/code-examples/panel-data/validation"
    "$MRL_ROOT/content/en/code-examples/panel-data/visualization"
    "$MRL_ROOT/content/en/report-templates/panel-data"
)

for dir in "${DEST_DIRS[@]}"; do
    if [ ! -d "$dir" ]; then
        log "Criando diretorio: $dir"
        mkdir -p "$dir"
    fi
done

log_ok "Diretorios de destino verificados"

# --- INICIO DA EXECUCAO ---
log_separator
log "CONTENT GENERATION — Panel Data Models Domain"
log "Fases: $TOTAL_FASES"
log "Logs: $LOG_DIR"
log_separator

# Selecionar fase(s) para executar
START=${1:-1}
END=${2:-$TOTAL_FASES}

# Se apenas 1 argumento, executar apenas essa fase
if [ $# -eq 1 ]; then
    END=$START
fi

if [ "$START" -eq "$END" ]; then
    log "Executando apenas fase F$START"
else
    log "Executando fases F$START a F$END"
fi

for i in $(seq $START $END); do
    SPEC_FILE="$SPEC_DIR/CONTENT_GEN_F${i}.md"
    LOG_FILE="$LOG_DIR/F${i}_${TIMESTAMP}.log"
    LOG_LATEST="$LOG_DIR/F${i}_latest.log"

    log_separator
    log "Fase F$i"
    show_progress "$SPEC_FILE"

    PENDING=$(count_pending_checkboxes "$SPEC_FILE")
    if [ "$PENDING" -eq 0 ]; then
        log_ok "Fase F$i ja esta completa. Pulando."
        continue
    fi

    log "Pendentes: $PENDING criterios de aceite"
    log "Log: $LOG_FILE"

    # Gerar prompt
    PROMPT=$(build_prompt "$SPEC_FILE" "$i")

    # Executar com Claude Code
    MAX_RETRIES=3
    RETRY=0

    while [ "$RETRY" -lt "$MAX_RETRIES" ]; do
        log "Tentativa $((RETRY + 1))/$MAX_RETRIES"

        cd "$PROJECT_ROOT"
        echo "$PROMPT" | claude --dangerously-skip-permissions 2>&1 | tee "$LOG_FILE"

        # Criar symlink para latest
        ln -sf "$LOG_FILE" "$LOG_LATEST"

        # Verificar progresso
        NEW_PENDING=$(count_pending_checkboxes "$SPEC_FILE")
        if [ "$NEW_PENDING" -eq 0 ]; then
            log_ok "Fase F$i COMPLETA!"
            break
        elif [ "$NEW_PENDING" -lt "$PENDING" ]; then
            log "Progresso parcial: $PENDING -> $NEW_PENDING pendentes"
            PENDING=$NEW_PENDING
            RETRY=$((RETRY + 1))
        else
            log_err "Sem progresso. Tentando novamente..."
            RETRY=$((RETRY + 1))
        fi
    done

    FINAL_PENDING=$(count_pending_checkboxes "$SPEC_FILE")
    if [ "$FINAL_PENDING" -gt 0 ]; then
        log_err "Fase F$i INCOMPLETA ($FINAL_PENDING pendentes)"
    fi

    show_progress "$SPEC_FILE"
done

# --- RESUMO ---
log_separator
log "RESUMO — CONTENT GENERATION: Panel Data Models"
log_separator

for i in $(seq 1 $TOTAL_FASES); do
    SPEC_FILE="$SPEC_DIR/CONTENT_GEN_F${i}.md"
    PENDING=$(count_pending_checkboxes "$SPEC_FILE")
    COMPLETED=$(count_completed_checkboxes "$SPEC_FILE")

    if [ "$PENDING" -eq 0 ]; then
        echo -e "  ${GREEN}OK${NC} F$i - Completa ($COMPLETED criterios)"
    else
        echo -e "  ${RED}--${NC} F$i - Pendente ($PENDING/$((PENDING + COMPLETED)) criterios)"
    fi
done

log_separator

# --- VERIFICACAO FINAL DE ARQUIVOS GERADOS ---
log "Arquivos gerados:"
echo ""

echo -e "${YELLOW}  Guides:${NC}"
ls "$MRL_ROOT/content/en/guides/panel-data/" 2>/dev/null || echo "    (nenhum)"

echo -e "${YELLOW}  News:${NC}"
ls "$MRL_ROOT/content/en/news/" 2>/dev/null | grep -i "panel\|fixed-effect\|random-effect\|hausman\|arellano\|nickell\|gmm" || echo "    (nenhum novo)"

echo -e "${YELLOW}  Code Examples:${NC}"
find "$MRL_ROOT/content/en/code-examples/panel-data/" -name "*.py" 2>/dev/null | while read f; do echo "    $(echo $f | sed "s|$MRL_ROOT/content/en/code-examples/||")"; done
[ $? -ne 0 ] && echo "    (nenhum)"

echo -e "${YELLOW}  Report Templates:${NC}"
ls "$MRL_ROOT/content/en/report-templates/panel-data/" 2>/dev/null || echo "    (nenhum)"

echo ""
log_separator
