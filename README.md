# Controle de Treinamento MTB Caminho da Fé

Sistema completo para acompanhar seu treinamento de MTB.

## Rodando localmente

1. Clone o projeto
2. Ajuste seu CLIENT_ID e CLIENT_SECRET
3. Rode:

```bash
docker build -t treino_mtb .
docker run -p 8501:8501 treino_mtb
