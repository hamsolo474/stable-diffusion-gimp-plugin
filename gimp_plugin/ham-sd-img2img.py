from __future__ import with_statement
from __future__ import absolute_import
from gimpfu import *
import urllib2
import json
import os

methods = [u'Euler a', u'Euler', u'LMS', u'Heun', u'DPM2', u'DPM2 a', u'DDIM', u'PLMS']

def img2img(timg, tdraw, src, mal, pprompt, nprompt, method='Euler a', steps=30, cfg=7, tiling=False, gfpgan=True, w=512, h=512, seed = -1):
    sdic = {True: 'Selection', False: 'Whole Image'}
    mdic = {True: 'Merged',    False: 'Active Layer'}
    if mdic[mal] == 'Merged':
        pdb.file_png_save_defaults(timg, tdraw, r'')
        pass

    elif mdic[mal] == 'Active Layer':
        pass

    if sdic[src] == 'Selection':
        src_path  = ''
        mask_path = ''
        
    elif sdic[src] == 'Whole Image':
        src_path  = ''
        mask_path = ''
    mask_path = r"C:\Users\ham\sd\stable-diffusion\repositories\stable-diffusion\outputs\krita-in\moon_mask.png"
    src_path = r"C:\Users\ham\sd\stable-diffusion\repositories\stable-diffusion\outputs\krita-in\moon_src.png"
    params = {'mode': 0, 
              'src_path':           src_path, 
              'mask_path':          mask_path, #'C:\\Users\\ham\\sd\\stable-diffusion\\repositories\\stable-diffusion\\outputs\\krita-in\\1663841661_mask.png', 
              u'prompt':            pprompt, 
              u'negative_prompt':   nprompt, 
              u'sampler_name':      method, 
              u'steps':             steps, 
              u'cfg_scale':         cfg, 
              u'batch_count':       1, 
              u'batch_size':        1, 
              u'base_size':         w, 
              u'max_size':          704, 
              u'seed':              seed, 
              u'tiling':            tiling, 
              u'use_gfpgan':        gfpgan, 
              u'face_restorer':   u'CodeFormer', 
              u'codeformer_weight': 0.5, 
              'upscaler_name':      'None'}
    url = u"http://127.0.0.1:8000/img2img"
    handle(url, params, timg)


def handle(url, params, timg):
    try:
        fp = post(url, params)
        layer = pdb.gimp_file_load_layer(timg, fp)
        pdb.gimp_image_insert_layer(timg, layer, None, 0)
        os.remove(fp)
    except urllib2.URLError:
        pdb.gimp_message(f'Could not connect to stable-diffusion running at {url}')
    

def post(url, body):
        req = urllib2.Request(url)
        req.add_header(u'Content-Type', u'application/json')
        body = json.dumps(body)
        body_encoded = body.encode(u'utf-8')
        req.add_header(u'Content-Length', unicode(len(body_encoded)))
        res = urllib2.urlopen(req, body_encoded)
        return json.loads(res.read())[u'outputs'][0] 
        #{'outputs': ['C:\\Users\\ham\\sd\\stable-diffusion\\repositories\\stable-diffusion\\outputs\\krita-out\\1663833125_0.png'], 'info': '{"prompt": "road", "negative_prompt": "sky", "seed": 2627372744, "width": 512, "height": 512, "sampler": "PLMS", "cfg_scale": 7.5, "steps": 20}'}

register(
 u"Ham-Gimp-Stable-diffusion",                  # Name
    u"",                                        # Blurb
    u"Links to stable diffusion",               # help
    u"hamsolo474",                              # Author
    u"Licenced the same as Stable-Diffusion",   # Copyright
    u"2022",                                    # Date
    u"<Image>/Image/Stable-Diffusion/img2img",  # Menu path
    u"",                                        # Image types
    [                                           # Gui Params
        (PF_TOGGLE, u"merged", u"Merged (True) or Active layer (False)?", False),
        (PF_TOGGLE, u"selection", u"Whole canvas (True) or Selection (False)", False),
        (PF_STRING, u"Pprompt", u"Positive Prompt", u''),
        (PF_STRING, u"Nprompt", u"Negative Prompt", u''),
        (PF_STRING, u"method", u"Sampling Method", u'Euler a'),
        #(list, 'method', 'Sampling Method', methods[0], methods),
        (PF_SLIDER, u"ss", u"Sampling Steps", 30,(1,150,1)),
        (PF_ADJUSTMENT, u"cfg", u"CFG", 7,(1,15,0.5)),
        (PF_TOGGLE, u"tiling", u"Tiling", False),
        (PF_TOGGLE, u"gfpgan", u"Use GFPGAN", True),
        (PF_ADJUSTMENT, u"w", u"Width", 512,(64,2048,64)),
        (PF_ADJUSTMENT, u"h", u"Height", 512,(64,2048,64)),
        (PF_INT, u"seed", u"Seed", -1)
    ],
    [],                                         # Results
    img2img)                                    # Function

main()