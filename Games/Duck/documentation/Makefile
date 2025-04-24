.Phony: all clean

# get all .drawio files in folder and create list of .png target files
DRAWIOS := $(wildcard *.drawio)
PNGS := $(DRAWIOS:.drawio=.png)

all: generate

# target of generate is list of all .png files, based on exisiting .drawio files
generate: $(PNGS)

# create .png file for each .drawio file with draw.io application
%.png: %.drawio
	/Applications/draw.io.app/Contents/MacOS/draw.io -x -f png -o $@ $<

# clean all generated .png files
clean:
	rm -f $(PNGS) 

