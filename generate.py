import os
import glob

slideshow_dir = "images/slideshow/"
gallery_dir = "images/gallery/"


with open('templates/slideshow_template.html', 'r') as myfile:
    slideshow_template = myfile.read()
with open('templates/gallery_template.html', 'r') as myfile:
    gallery_template = myfile.read()
with open(slideshow_dir + 'slideshow_text.txt', 'r') as myfile:
	slideshow_text = [line.rstrip('\n') for line in myfile]
	slideshow_text = [line.split(', ') for line in slideshow_text]


slideshow_str = ""
active = " active" # To set the first item as active
for infile in glob.glob(slideshow_dir + "*.jpg"):

	# Include description form text file.
	title = ""
	description = ""
	filename = infile.split('/')[-1].split('.')[0] # Removes extension
	for item in slideshow_text:
		if item[0].split('.')[0] == filename: # Removes extension, if used.
			title = item[1]
			description = item[2]

	slideshow_item = slideshow_template.format(active, infile, title, description)
	slideshow_str += slideshow_item
	active = ""


gallery_str = ""
for infile in glob.glob(gallery_dir + "*.jpg"):
	gallery_item = gallery_template.format(infile, infile)
	gallery_str += gallery_item


with open('templates/index_template.html', 'r') as myfile:
    html_template = myfile.read()
html_str = html_template.format(slideshow_str, gallery_str)
html_file = open("index.html","w")
html_file.write(html_str)
html_file.close()
