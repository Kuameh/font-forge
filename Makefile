PY := .venv/bin/python

.PHONY: setup build specimen serve all clean

setup:  ## Create .venv and install the pinned toolchain
	python3 -m venv .venv
	$(PY) -m pip install -q --upgrade pip
	$(PY) -m pip install -q -r requirements.txt

build:  ## Build every family, or one: make build FAMILY=ForgeDemo
	$(PY) scripts/build.py $(FAMILY)
	$(PY) scripts/specimen.py
	$(PY) scripts/proof.py

specimen:  ## Regenerate specimen/index.html and specimen/proof.html from fonts/
	$(PY) scripts/specimen.py
	$(PY) scripts/proof.py

serve:  ## Specimen, proof and drawing sheet at http://localhost:8000/specimen/, /specimen/proof.html, /sheet/
	$(PY) -m http.server 8000

clean:  ## Remove build leftovers (not fonts/)
	rm -rf sources/*/instances master_ufo instance_ufo
