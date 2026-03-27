#!/bin/bash
set -e

# ANSI colors
ORANGE='\033[0;33m'
CYAN='\033[0;36m'
GREEN='\033[0;32m'
BOLD='\033[1m'
RESET='\033[0m'

if [ -f .env ]; then
  while IFS='=' read -r key value; do
    [[ "$key" =~ ^#.*$ || -z "$key" ]] && continue
    value="${value%\"}"
    value="${value#\"}"
    [ -z "${!key}" ] && export "$key=$value"
  done < .env
fi

# Validate required env variables
MISSING=()
[ -z "$SERVICE_NAME" ] && MISSING+=("SERVICE_NAME")
[ -z "$HOST_IP" ]      && MISSING+=("HOST_IP")
[ -z "$PORT" ]         && MISSING+=("PORT")

if [ ${#MISSING[@]} -gt 0 ]; then
  printf "\n"
  printf "${ORANGE}${BOLD}⚠️  Warning:${RESET}${ORANGE} Missing required environment variable(s): %s${RESET}\n" "${MISSING[*]}"
  printf "${ORANGE}   Check your .env file or system environment variables.${RESET}\n"
  printf "\n"
  exit 1
fi

# Prints a box row: visible text for padding calc, colored text for display
# Box is 80 cols: │ + 78 chars + │
box_row() {
  local visible="$1"
  local colored="$2"
  local pad=$(( 79 - ${#visible} ))
  printf "${BOLD}${CYAN}│${RESET}${colored}%${pad}s${BOLD}${CYAN}│${RESET}\n" ""
}

BORDER="───────────────────────────────────────────────────────────────────────────────"
printf "\n"
printf "${BOLD}${CYAN}┌${BORDER}┐${RESET}\n"
box_row "  🤖  Starting service: ${SERVICE_NAME}" "  ${BOLD}${GREEN}▶  Starting service:${RESET} ${BOLD}${SERVICE_NAME}${RESET}"
box_row "  Host  →  ${HOST_IP}" "  ${CYAN}Host${RESET}  →  ${HOST_IP}"
box_row "  Port  →  ${PORT}" "  ${CYAN}Port${RESET}  →  ${PORT}"
printf "${BOLD}${CYAN}└${BORDER}┘${RESET}\n"
printf "\n"

uv run uvicorn main:create_service --host "$HOST_IP" --port "$PORT" --factory
