from PIL import Image, ImageEnhance 
im = Image.open("/home/ubuntu/Desktop/1011sd.png")
enhancer = ImageEnhance.Contrast(im)
enhanced_im = enhancer.enhance(1.50)
enhanced_im.save("/home/ubuntu/Desktop/1011sd1.png")