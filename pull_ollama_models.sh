#!/usr/bin/env bash
set -euo pipefail

models=(
  "llama3.1:8b"
  "mistral:7b"
  "qwen2.5:7b"
  "qwen2.5:14b"
  "granite3.3:8b"
  "gemma2:2b"
  "deepseek-r1:8b"
)

for m in "${models[@]}"; do
  echo "pulling $m"
  ollama pull "$m"
done