.PHONY: all bandit pylint flake8 clean

SCRIPTS = \
    scripts/ColorFilter.py \
    scripts/ImageProcessor.py \
    scripts/NumPyCreator.py \
    scripts/ScrapBooker.py \

all: black bandit pylint flake8

install:
	uv sync

black:
	@black ${SCRIPTS} || true

bandit:
	@bandit ${SCRIPTS} || true

pylint:
	@pylint ${SCRIPTS} || true

flake8:
	@flake8 ${SCRIPTS} || true

clean:
	@rm -rf dist/ build/ __pycache__/ *.spec site/ image_processor_output.png
