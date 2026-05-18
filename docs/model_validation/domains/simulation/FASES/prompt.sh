#!/bin/bash

# ============================================================
# CONTENT GENERATION — Simulation Domain
# Execucao automatizada com Claude Code
# ============================================================

PROJECT_ROOT="/home/guhaase/projetos/Graphenda"
MRL_ROOT="/home/guhaase/projetos/ModelRiskLab/mrl-content-files"
SPEC_DIR="$PROJECT_ROOT/build/docs/model_validation/domains/simulation/FASES"
DOMAIN_SPEC="$PROJECT_ROOT/build/docs/model_validation/domains/25-simulation.md"
LOG_DIR="$PROJECT_ROOT/logs/content-generation/simulation"
TOTAL_FASES=5

mkdir -p "$LOG_DIR"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; BLUE='\033[0;34m'; PURPLE='\033[0;35m'; NC='\033[0m'

log() { echo -e "${BLUE}[$(date +%H:%M:%S)]${NC} $1"; }
log_ok() { echo -e "${GREEN}[$(date +%H:%M:%S)] OK${NC} $1"; }
log_err() { echo -e "${RED}[$(date +%H:%M:%S)] ERR${NC} $1"; }
log_separator() { echo -e "${PURPLE}================================================================${NC}"; }

count_pending_checkboxes() { local n; n=$(grep -c '\- \[ \]' "$1" 2>/dev/null) || n=0; echo "$n"; }
count_completed_checkboxes() { local n; n=$(grep -c '\- \[x\]' "$1" 2>/dev/null) || n=0; echo "$n"; }

show_progress() {
    local pending=$(count_pending_checkboxes "$1") completed=$(count_completed_checkboxes "$1") total=$((pending + completed))
    [ "$total" -gt 0 ] && echo -e "${YELLOW}  Progresso: $completed/$total ($((completed * 100 / total))%)${NC}"
}

build_prompt() {
    local spec_file="$1" fase_num="$2"
    cat <<PROMPT
Voce e um pesquisador e redator tecnico especializado em simulacao, Monte Carlo, stress testing e model risk management.

## Contexto do projeto
- Projeto: ModelRiskLab — Plataforma de conteudo sobre Model Risk Management
- Diretorio de conteudo: $MRL_ROOT/content/en/
- Templates: $MRL_ROOT/templates/
- Especificacao do dominio: $DOMAIN_SPEC
- Dataset de referencia: Fama-French factors (Kenneth French) e yfinance para precos de ativos

## Tarefa
Execute COMPLETAMENTE a fase F$fase_num descrita na especificacao abaixo.
Apos completar cada criterio, edite o arquivo da especificacao em disco
trocando "- [ ]" por "- [x]" na linha correspondente.

## Regras
1. TODO conteudo deve ser baseado em PESQUISA REAL — use WebSearch e WebFetch
2. NAO invente dados, metricas ou referencias
3. Siga os templates e formatos especificados
4. Inclua frontmatter YAML valido em todos os arquivos .md
5. IMPORTANTE: Edite o arquivo $spec_file para marcar criterios completados
6. Se um criterio ja esta [x], pule-o
7. Para codigo Python: garanta sintaxe valida e funcional
8. Stack: numpy/scipy + mesa + SALib + arch
9. Dataset: Fama-French factors / yfinance para dados de mercado

## Conteudo ja gerado em fases anteriores
$(if [ "$fase_num" -gt 1 ]; then
    echo "Verifique o conteudo ja gerado em:"
    echo "- Guides: $MRL_ROOT/content/en/guides/simulation/"
    echo "- News: $MRL_ROOT/content/en/news/"
    echo "- Code: $MRL_ROOT/content/en/code-examples/simulation/"
    echo "- Reports: $MRL_ROOT/content/en/report-templates/simulation/"
fi)

## Arquivo da especificacao (edite os checkboxes NESTE arquivo)
Caminho: $spec_file

## Especificacao
$(cat "$spec_file")
PROMPT
}

if ! command -v claude &> /dev/null; then log_err "Claude Code CLI nao encontrado."; exit 1; fi

for i in $(seq 1 $TOTAL_FASES); do
    [ ! -f "$SPEC_DIR/CONTENT_GEN_F${i}.md" ] && log_err "CONTENT_GEN_F${i}.md nao encontrado" && exit 1
done
log_ok "Todos os arquivos de especificacao encontrados"

DEST_DIRS=("$MRL_ROOT/content/en/guides/simulation" "$MRL_ROOT/content/en/news" "$MRL_ROOT/content/en/code-examples/simulation/modeling" "$MRL_ROOT/content/en/code-examples/simulation/validation" "$MRL_ROOT/content/en/code-examples/simulation/visualization" "$MRL_ROOT/content/en/report-templates/simulation" "$MRL_ROOT/content/pt/guides/simulation" "$MRL_ROOT/content/pt/code-examples/simulation/modeling" "$MRL_ROOT/content/pt/code-examples/simulation/validation" "$MRL_ROOT/content/pt/code-examples/simulation/visualization" "$MRL_ROOT/content/pt/report-templates/simulation")
for dir in "${DEST_DIRS[@]}"; do [ ! -d "$dir" ] && mkdir -p "$dir"; done
log_ok "Diretorios de destino verificados"

log_separator
log "CONTENT GENERATION — Simulation Domain"
log "Fases: $TOTAL_FASES | Logs: $LOG_DIR"
log_separator

START=${1:-1}; END=${2:-$TOTAL_FASES}; [ $# -eq 1 ] && END=$START
[ "$START" -eq "$END" ] && log "Executando apenas fase F$START" || log "Executando fases F$START a F$END"

for i in $(seq $START $END); do
    SPEC_FILE="$SPEC_DIR/CONTENT_GEN_F${i}.md"
    LOG_FILE="$LOG_DIR/F${i}_${TIMESTAMP}.log"
    LOG_LATEST="$LOG_DIR/F${i}_latest.log"

    log_separator; log "Fase F$i"; show_progress "$SPEC_FILE"

    PENDING=$(count_pending_checkboxes "$SPEC_FILE")
    [ "$PENDING" -eq 0 ] && log_ok "Fase F$i ja esta completa. Pulando." && continue

    log "Pendentes: $PENDING criterios | Log: $LOG_FILE"
    PROMPT=$(build_prompt "$SPEC_FILE" "$i")

    MAX_RETRIES=3; RETRY=0
    while [ "$RETRY" -lt "$MAX_RETRIES" ]; do
        log "Tentativa $((RETRY + 1))/$MAX_RETRIES"
        cd "$PROJECT_ROOT"
        echo "$PROMPT" | claude --dangerously-skip-permissions 2>&1 | tee "$LOG_FILE"
        ln -sf "$LOG_FILE" "$LOG_LATEST"

        NEW_PENDING=$(count_pending_checkboxes "$SPEC_FILE")
        [ "$NEW_PENDING" -eq 0 ] && log_ok "Fase F$i COMPLETA!" && break
        [ "$NEW_PENDING" -lt "$PENDING" ] && log "Progresso: $PENDING -> $NEW_PENDING" && PENDING=$NEW_PENDING
        RETRY=$((RETRY + 1))
    done

    FINAL_PENDING=$(count_pending_checkboxes "$SPEC_FILE")
    [ "$FINAL_PENDING" -gt 0 ] && log_err "Fase F$i INCOMPLETA ($FINAL_PENDING pendentes)"
    show_progress "$SPEC_FILE"
done

log_separator; log "RESUMO — CONTENT GENERATION: Simulation"; log_separator
for i in $(seq 1 $TOTAL_FASES); do
    SPEC_FILE="$SPEC_DIR/CONTENT_GEN_F${i}.md"
    PENDING=$(count_pending_checkboxes "$SPEC_FILE"); COMPLETED=$(count_completed_checkboxes "$SPEC_FILE")
    [ "$PENDING" -eq 0 ] && echo -e "  ${GREEN}OK${NC} F$i - Completa ($COMPLETED criterios)" || echo -e "  ${RED}--${NC} F$i - Pendente ($PENDING/$((PENDING + COMPLETED)) criterios)"
done
log_separator

log "Arquivos gerados:"; echo ""
echo -e "${YELLOW}  Guides:${NC}"; ls "$MRL_ROOT/content/en/guides/simulation/" 2>/dev/null || echo "    (nenhum)"
echo -e "${YELLOW}  News:${NC}"; ls "$MRL_ROOT/content/en/news/" 2>/dev/null | grep -i "monte-carlo\|var-cvar\|agent-based\|basel.*stress\|convergence.*monte\|variance-reduction\|validating-simulation" || echo "    (nenhum novo)"
echo -e "${YELLOW}  Code Examples:${NC}"; find "$MRL_ROOT/content/en/code-examples/simulation/" -name "*.py" 2>/dev/null | while read f; do echo "    $(echo $f | sed "s|$MRL_ROOT/content/en/code-examples/||")"; done
echo -e "${YELLOW}  Report Templates:${NC}"; ls "$MRL_ROOT/content/en/report-templates/simulation/" 2>/dev/null || echo "    (nenhum)"
echo ""; log_separator
