make lint:
	uv run ruff check brain_games
    
prompt:
	uv add prompt

random:
	uv add random
	
install:
	uv sync

brain-games:
	uv run brain-games
	
build:
	uv build

package-install:
	uv tool install ~/dist/*.whl
