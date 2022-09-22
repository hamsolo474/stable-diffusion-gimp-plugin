# Stable Diffusion Gimp Plugin
A simple interface based on this repository: https://github.com/sddebz/stable-diffusion-krita-plugin

Requires Gimp 2.x (I havent tested it on 2.99)


Follow the installation instructions here
https://github.com/sddebz/stable-diffusion-krita-plugin


### Plugin installation

1. Open GIMP and go into Edit > Preferences > Folders > Plug-ins 
2. Go to that folder, for me it was C:\Users\USERNAME\Appdata\Roaming\GIMP\2.10\plug-ins
3. Copy from this repository contents of folder `gimp_plugin` into that folder
4. Restart GIMP


#### Troublehooting:

Look into parent repository https://github.com/sddebz/stable-diffusion-krita-plugin for instructions. This repository uses slightly changed code, but most parameters including those for low VRAM usage should still work.

### Usage
With an Image open, go to Image > stable-diffusion > txt2img
