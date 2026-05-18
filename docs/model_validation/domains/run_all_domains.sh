#!/bin/bash

# ============================================================
# CONTENT GENERATION — Execucao de TODOS os 25 Dominios
# Executa cada prompt.sh em sequencia
# ============================================================

DOMAINS_DIR="/home/guhaase/projetos/Graphenda/build/docs/model_validation/domains"
LOG_DIR="/home/guhaase/projetos/Graphenda/logs/content-generation"
mkdir -p "$LOG_DIR"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
MASTER_LOG="$LOG_DIR/run_all_domains_${TIMESTAMP}.log"

# --- Cores ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'

# --- FUNCOES ---
log() { echo -e "${BLUE}[$(date +%H:%M:%S)]${NC} $1" | tee -a "$MASTER_LOG"; }
log_ok() { echo -e "${GREEN}[$(date +%H:%M:%S)] OK${NC} $1" | tee -a "$MASTER_LOG"; }
log_err() { echo -e "${RED}[$(date +%H:%M:%S)] ERR${NC} $1" | tee -a "$MASTER_LOG"; }
log_separator() { echo -e "${PURPLE}================================================================${NC}" | tee -a "$MASTER_LOG"; }
log_header() { echo -e "${CYAN}████████████████████████████████████████████████████████████████${NC}" | tee -a "$MASTER_LOG"; }

# --- LISTA DE DOMINIOS (em ordem de prioridade) ---
DOMAINS=(
    "01:linear-regression:Linear Regression:P0"
    "06:classification:Classification:P0"
    "21:anomaly-detection:Anomaly Detection:P0"
    "02:panel-data:Panel Data:P1"
    "03:time-series:Time Series:P1"
    "04:glm:GLM:P1"
    "05:survival:Survival:P1"
    "13:deep-learning-vision:Deep Learning Vision:P2"
    "15:deep-learning-sequential:Deep Learning Sequential:P2"
    "17:nlp-embeddings:NLP Embeddings:P2"
    "18:llm:LLM:P2"
    "22:causal-inference:Causal Inference:P2"
    "25:simulation:Simulation:P2"
    "07:regression-ml:Regression ML:P2"
    "08:ensemble:Ensemble:P2"
    "09:clustering:Clustering:P3"
    "10:dim-reduction:Dim Reduction:P3"
    "11:bayesian:Bayesian:P3"
    "12:reinforcement-learning:Reinforcement Learning:P3"
    "14:deep-learning-tabular:Deep Learning Tabular:P3"
    "16:nlp-classical:NLP Classical:P3"
    "19:generative:Generative:P3"
    "20:recommender:Recommender:P3"
    "23:graph-models:Graph Models:P3"
    "24:optimization:Optimization:P3"
)

TOTAL=${#DOMAINS[@]}

# --- SELECAO DE DOMINIOS ---
# Uso:
#   ./run_all_domains.sh                  # Executa todos
#   ./run_all_domains.sh 3                # Executa apenas os 3 primeiros
#   ./run_all_domains.sh --domain glm     # Executa apenas o dominio 'glm'
#   ./run_all_domains.sh --priority P0    # Executa apenas dominios P0
#   ./run_all_domains.sh --from 10        # Executa a partir do 10o dominio
#   ./run_all_domains.sh --list           # Lista dominios e sai

FILTER_DOMAIN=""
FILTER_PRIORITY=""
START_FROM=1
LIMIT=$TOTAL

if [ "$1" == "--list" ]; then
    echo ""
    echo "Dominios disponiveis (em ordem de execucao):"
    echo ""
    IDX=1
    for entry in "${DOMAINS[@]}"; do
        IFS=':' read -r num slug name prio <<< "$entry"
        printf "  %2d. [%s] %-30s (%s)\n" "$IDX" "$prio" "$name" "$slug"
        IDX=$((IDX + 1))
    done
    echo ""
    exit 0
fi

if [ "$1" == "--domain" ] && [ -n "$2" ]; then
    FILTER_DOMAIN="$2"
elif [ "$1" == "--priority" ] && [ -n "$2" ]; then
    FILTER_PRIORITY="$2"
elif [ "$1" == "--from" ] && [ -n "$2" ]; then
    START_FROM="$2"
elif [ -n "$1" ] && [[ "$1" =~ ^[0-9]+$ ]]; then
    LIMIT="$1"
fi

# --- VERIFICACAO ---
if ! command -v claude &> /dev/null; then
    log_err "Claude Code CLI nao encontrado. Instale com: npm install -g @anthropic-ai/claude-code"
    exit 1
fi

# --- INICIO ---
log_header
log "CONTENT GENERATION — ALL DOMAINS"
log "Total de dominios: $TOTAL"
log "Timestamp: $TIMESTAMP"
log "Master log: $MASTER_LOG"
log_header
echo ""

# --- Contadores ---
COMPLETED=0
FAILED=0
SKIPPED=0
IDX=0

START_TIME=$(date +%s)

for entry in "${DOMAINS[@]}"; do
    IFS=':' read -r num slug name prio <<< "$entry"
    IDX=$((IDX + 1))

    # Filtros
    if [ -n "$FILTER_DOMAIN" ] && [ "$slug" != "$FILTER_DOMAIN" ]; then
        continue
    fi
    if [ -n "$FILTER_PRIORITY" ] && [ "$prio" != "$FILTER_PRIORITY" ]; then
        continue
    fi
    if [ "$IDX" -lt "$START_FROM" ]; then
        continue
    fi
    if [ "$((COMPLETED + FAILED + SKIPPED))" -ge "$LIMIT" ] && [ -z "$FILTER_DOMAIN" ] && [ -z "$FILTER_PRIORITY" ]; then
        break
    fi

    SCRIPT="$DOMAINS_DIR/$slug/FASES/prompt.sh"

    log_separator
    log "[$IDX/$TOTAL] Dominio: $name ($slug) [$prio]"

    # Verificar se o script existe
    if [ ! -f "$SCRIPT" ]; then
        log_err "Script nao encontrado: $SCRIPT"
        FAILED=$((FAILED + 1))
        continue
    fi

    # Verificar se ja esta completo (todos os checkboxes marcados)
    FASES_DIR="$DOMAINS_DIR/$slug/FASES"
    TOTAL_PENDING=0
    for f in "$FASES_DIR"/CONTENT_GEN_F*.md; do
        if [ -f "$f" ]; then
            P=$(grep -c '\- \[ \]' "$f" 2>/dev/null) || P=0
            TOTAL_PENDING=$((TOTAL_PENDING + P))
        fi
    done

    if [ "$TOTAL_PENDING" -eq 0 ]; then
        log_ok "Dominio $name ja esta completo. Pulando."
        SKIPPED=$((SKIPPED + 1))
        continue
    fi

    log "Criterios pendentes: $TOTAL_PENDING"
    log "Executando: $SCRIPT"

    # Executar
    DOMAIN_START=$(date +%s)
    cd "$DOMAINS_DIR/$slug/FASES"
    bash prompt.sh 2>&1 | tee -a "$MASTER_LOG"
    EXIT_CODE=$?
    DOMAIN_END=$(date +%s)
    DOMAIN_DURATION=$(( DOMAIN_END - DOMAIN_START ))

    # Verificar resultado
    NEW_PENDING=0
    for f in "$FASES_DIR"/CONTENT_GEN_F*.md; do
        if [ -f "$f" ]; then
            P=$(grep -c '\- \[ \]' "$f" 2>/dev/null) || P=0
            NEW_PENDING=$((NEW_PENDING + P))
        fi
    done

    if [ "$NEW_PENDING" -eq 0 ]; then
        log_ok "Dominio $name COMPLETO (${DOMAIN_DURATION}s)"
        COMPLETED=$((COMPLETED + 1))
    elif [ "$NEW_PENDING" -lt "$TOTAL_PENDING" ]; then
        log "Dominio $name PARCIAL: $TOTAL_PENDING -> $NEW_PENDING pendentes (${DOMAIN_DURATION}s)"
        COMPLETED=$((COMPLETED + 1))
    else
        log_err "Dominio $name SEM PROGRESSO (${DOMAIN_DURATION}s)"
        FAILED=$((FAILED + 1))
    fi

    echo ""
done

# --- RESUMO FINAL ---
END_TIME=$(date +%s)
TOTAL_DURATION=$(( END_TIME - START_TIME ))
HOURS=$((TOTAL_DURATION / 3600))
MINUTES=$(( (TOTAL_DURATION % 3600) / 60 ))
SECONDS=$((TOTAL_DURATION % 60))

log_header
log "RESUMO FINAL — CONTENT GENERATION"
log_header
echo "" | tee -a "$MASTER_LOG"

for entry in "${DOMAINS[@]}"; do
    IFS=':' read -r num slug name prio <<< "$entry"
    FASES_DIR="$DOMAINS_DIR/$slug/FASES"

    PENDING=0
    DONE=0
    for f in "$FASES_DIR"/CONTENT_GEN_F*.md; do
        if [ -f "$f" ]; then
            P=$(grep -c '\- \[ \]' "$f" 2>/dev/null) || P=0
            D=$(grep -c '\- \[x\]' "$f" 2>/dev/null) || D=0
            PENDING=$((PENDING + P))
            DONE=$((DONE + D))
        fi
    done

    TOTAL_CRITERIA=$((PENDING + DONE))
    if [ "$PENDING" -eq 0 ] && [ "$TOTAL_CRITERIA" -gt 0 ]; then
        printf "  ${GREEN}OK${NC} %-30s [%s] %d/%d criterios\n" "$name" "$prio" "$DONE" "$TOTAL_CRITERIA" | tee -a "$MASTER_LOG"
    elif [ "$TOTAL_CRITERIA" -eq 0 ]; then
        printf "  ${YELLOW}--${NC} %-30s [%s] sem criterios\n" "$name" "$prio" | tee -a "$MASTER_LOG"
    else
        printf "  ${RED}--${NC} %-30s [%s] %d/%d criterios (%d pendentes)\n" "$name" "$prio" "$DONE" "$TOTAL_CRITERIA" "$PENDING" | tee -a "$MASTER_LOG"
    fi
done

echo "" | tee -a "$MASTER_LOG"
log "Executados: $((COMPLETED + FAILED)) | Completos: $COMPLETED | Falhas: $FAILED | Pulados: $SKIPPED"
log "Tempo total: ${HOURS}h ${MINUTES}m ${SECONDS}s"
log "Master log: $MASTER_LOG"
log_header
