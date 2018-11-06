## Portfolio website which auto-generates HTML


### Customisation:

Do these steps once.

1. Download repository.
2. Edit templates/index_template.html as follows:
    - l7: author
    - l11: title
    - l31: email
      - It is strongly suggested to obfuscate this using the tool [here.](https://www.albionresearch.com/misc/obfuscator.php) If used, replace the entire line 31 with the output from the second window of this tool.
3. (optional) Add favicon to images/fav.png
4. (optional) Remove line 4 from templates/index_template.html which blocks search engines crawling the site.


### Add Photos:

Do this each time photos are to be added:

1. Add gallery photos in images/gallery
2. Add slideshow photos in images/slideshow
3. (optional) Edit images/slideshow/slideshow_text to show headings over images.
4. Open Terminal (Mac) and navigate to the folder containing this file.
    - If you are unsure how to do this, in the Terminal window type `cd`, press spacebar, drag the folder onto the terminal window (which will complete the command) and press enter.
5. Run the site generator with the command `python3 generator.py`
6. The site is done! Open index.html to view the output. Copy the contents of the folder to your hosting service as necessary.

### TODO:
Check favicon best practices.
Automate config step - pull info from config file, though obfuscating email is then tricky for the user.
