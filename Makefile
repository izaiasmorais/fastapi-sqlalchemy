# Comandos do servidor
dev:
	uv run python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

start:
	uv run python -m uvicorn src.main:app --host 0.0.0.0 --port 8000

# Comandos do ambiente virtual
venv-init:
	uv venv
	@echo "Ambiente virtual criado! Para ativar manualmente: source .venv/bin/activate"
