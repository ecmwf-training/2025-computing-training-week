# Génère un fichier PNG à partir d'un fichier Python en utilisant pygmentize

SOURCES := $(wildcard *.py)
PNGS := $(SOURCES:.py=.png)

all: $(PNGS)

%.png: %.py
	pygmentize -f png -l python -o $@ $<

clean:
	rm -f *.png
