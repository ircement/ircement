from PIL import Image
def crop(img_path,ref_res,exact=False):
	img=Image.open(img_path)
	w,h=img.size
	if not exact:
		w_h=ref_res[0]/ref_res[1]
		i_wh=w/h
		if w_h<i_wh:
			left=int((w-(h*w_h))/2)
			right=w-left
			top=0
			bottom=h
			img=img.crop((left,top,right,bottom))
		elif w_h>i_wh:
			left=0
			right=w
			top=int((h-(w*(1/w_h)))/2)
			bottom=h-top
			img=img.crop((left,top,right,bottom))
	else:
		left=int((w-ref_res[0])/2)
		right=w-left
		top=int((h-ref_res[1])/2)
		bottom=h-top
		img=img.crop((left,top,right,bottom))
	img.save(img_path)