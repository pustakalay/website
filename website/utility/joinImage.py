'''
Created on 27-Jan-2019

@author: Tanay
'''
import numpy as np
from PIL import Image
import os.path

def execute():
    BASE = os.path.dirname(os.path.abspath(__file__))
    mypath = os.path.abspath(os.path.join(BASE, '..'))
    list_im = [os.path.join(mypath, "media/Test-1-1.jpg"), os.path.join(mypath, "media/Test-2-1.jpg")]
    imgs    = [ Image.open(i) for i in list_im ]
    # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
    
    # save that beautiful picture
    imgs_comb = Image.fromarray( imgs_comb)
    imgs_comb.save( os.path.join(mypath, "media/Horizontal1.jpg") )
    
    list_im = [os.path.join(mypath, "media/Test-3-1.jpg"), os.path.join(mypath, "media/Test-4-1.jpg")]
    imgs    = [ Image.open(i) for i in list_im ]
    # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
    
    # save that beautiful picture
    imgs_comb = Image.fromarray( imgs_comb)
    imgs_comb.save( os.path.join(mypath, "media/Horizontal2.jpg") )   
    
    
    list_im = [os.path.join(mypath, "media/Horizontal1.jpg"), os.path.join(mypath, "media/Horizontal2.jpg")]
    imgs    = [ Image.open(i) for i in list_im ]
    # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1] 
    
    imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
    imgs_comb = Image.fromarray( imgs_comb)
    imgs_comb.save( os.path.join(mypath, "media/Result.jpg") )
