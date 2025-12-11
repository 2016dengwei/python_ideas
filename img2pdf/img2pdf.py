# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 18:08:57 2025

@author: 2008d
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def image2pdf(path="C:\\book\\1000c\\"):

    page_width, page_height = A4
    p = canvas.Canvas(path+"1001.pdf", pagesize=A4)
        
    imgs = os.listdir(path)
    for img in imgs:
        if img.endswith('jpeg'):
            print(img)
            p.drawImage(path+img,0,0,page_width, page_height)
            p.showPage()    
    
    p.save()

if __name__=="__main__":
    image2pdf()

