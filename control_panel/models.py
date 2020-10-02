import os
import datetime

from django.db import models

from control_panel.cropper import crop
class siteTitleManager(models.Manager):
	def control_number(self):
		if len(site_title.objects.all())==0:
			site_title.objects.create()
		elif len(site_title.objects.all())>1:
			for obj in site_title.objects.all():
				if obj.id!=1:
					if obj.title_icon.path.find(
							'\\default.png')==-1 and obj.title_icon.path.find(
						'/default.png')==-1:
						if os.path.isfile(obj.title_icon.path):
							os.remove(obj.title_icon.path)
					obj.delete()
		return site_title.objects.filter(id=1).get()
	def change_title(self,title):
		site_title_obj=site_title.objects.filter(id=1).get()
		site_title_obj.title=title
		site_title_obj.save()
		return site_title_obj
	def change_icon(self,icon):
		site_title_obj=site_title.objects.filter(id=1).get()
		if site_title_obj.title_icon.path.find(
				'\\default.png')==-1 and site_title_obj.title_icon.path.find(
			'/default.png')==-1:
			if os.path.isfile(site_title_obj.title_icon.path):
				os.remove(site_title_obj.title_icon.path)
		site_title_obj.title_icon=icon
		site_title_obj.save()
		crop(site_title_obj.title_icon.path,(64,64))
		return site_title_obj
class site_title(models.Model):
	title=models.CharField(max_length=100)
	title_icon=models.ImageField(upload_to='title_ico/',
								 default='title_ico/default/default.png',
								 blank=True)
	objects=siteTitleManager()
class sitelogoManager(models.Manager):
	def control_number(self):
		if len(site_logo.objects.all())==0:
			site_logo.objects.create()
		elif len(site_logo.objects.all())>1:
			for obj in site_logo.objects.all():
				if obj.id!=1:
					obj.delete()
		return site_logo.objects.filter(id=1).get()
	def update_logo(self,logo):
		obj=site_logo.objects.filter(id=1).get()
		span=logo
		obj.title=span
		obj.save()
		return obj
	def get_logo(self):
		obj=site_logo.objects.filter(id=1).get()
		return obj.title
class site_logo(models.Model):
	title=models.CharField(max_length=100)
	objects=sitelogoManager()
class slideshowManager(models.Manager):
	def create_slide(self):
		slide=slideshow.objects.create(slide_title='title',
									   slide_body_text="slide body text")
		return slide
	def change_slide_img(self,id,img):
		if slideshow.objects.filter(id=id).exists():
			slide=slideshow.objects.filter(id=id).get()
		else:
			return None
		if slide.slide_img.path.find(
				'\\default.png')==-1 and slide.slide_img.path.find(
			'/default.png')==-1:
			if os.path.isfile(slide.slide_img.path):
				os.remove(slide.slide_img.path)
		slide.slide_img=img
		slide.save()
		crop(slide.slide_img.path,(1920,850))
		return slide
	def change_slide_title(self,id,title):
		if slideshow.objects.filter(id=id).exists():
			slide=slideshow.objects.filter(id=id).get()
		else:
			return None
		slide.slide_title=title
		slide.save()
		return slide
	def change_slide_body_text(self,id,text):
		if slideshow.objects.filter(id=id).exists():
			slide=slideshow.objects.filter(id=id).get()
		else:
			return None
		slide.slide_body_text=text
		slide.save()
		return slide
	def remove_slide(self,id):
		if slideshow.objects.filter(id=id).exists():
			slide=slideshow.objects.filter(id=id).get()
		else:
			return None
		if slide.slide_img.path.find(
				'\\default.png')==-1 and slide.slide_img.path.find(
			'/default.png')==-1:
			if os.path.isfile(slide.slide_img.path):
				os.remove(slide.slide_img.path)
		slide.delete()
		return slide
	def move_up(self,id):
		if slideshow.objects.filter(id=id).exists():
			slide=slideshow.objects.filter(id=id).get()
		else:
			return None
		slide_img_copy=slide.slide_img
		slide_title_copy=slide.slide_title
		slide_body_text_copy=slide.slide_body_text
		id_=int(id)-1
		while not slideshow.objects.filter(id=str(id_)).exists():
			id_-=1
		slide_=slideshow.objects.filter(id=str(id_)).get()
		slide.slide_img=slide_.slide_img
		slide.slide_title=slide_.slide_title
		slide.slide_body_text=slide_.slide_body_text
		slide.save()
		slide_.slide_img=slide_img_copy
		slide_.slide_title=slide_title_copy
		slide_.slide_body_text=slide_body_text_copy
		slide_.save()
		return slide
	def move_down(self,id):
		if slideshow.objects.filter(id=id).exists():
			slide=slideshow.objects.filter(id=id).get()
		else:
			return None
		slide_img_copy=slide.slide_img
		slide_title_copy=slide.slide_title
		slide_body_text_copy=slide.slide_body_text
		id_=int(id)+1
		while not slideshow.objects.filter(id=str(id_)).exists():
			id_+=1
		slide_=slideshow.objects.filter(id=str(id_)).get()
		slide.slide_img=slide_.slide_img
		slide.slide_title=slide_.slide_title
		slide.slide_body_text=slide_.slide_body_text
		slide.save()
		slide_.slide_img=slide_img_copy
		slide_.slide_title=slide_title_copy
		slide_.slide_body_text=slide_body_text_copy
		slide_.save()
		return slide
class slideshow(models.Model):
	slide_img=models.ImageField(upload_to='slides_img/',
								default='slides_img/default/default.png',
								blank=True)
	slide_title=models.TextField()
	slide_body_text=models.TextField()
	objects=slideshowManager()
class videoManager(models.Manager):
	def create_video(self):
		_video=video.objects.create(video_title='title',
									video_description="video description")
		return _video
	def change_cover_img(self,id,img):
		if video.objects.filter(id=id).exists():
			_video=video.objects.filter(id=id).get()
		else:
			return None
		if _video.cover_img.path.find(
				'\\default.png')==-1 and _video.cover_img.path.find(
			'/default.png')==-1:
			if os.path.isfile(_video.cover_img.path):
				os.remove(_video.cover_img.path)
		_video.cover_img=img
		_video.save()
		crop(_video.cover_img.path,(450,400),True)
		return _video
	def change_video_title(self,id,title):
		if video.objects.filter(id=id).exists():
			_video=video.objects.filter(id=id).get()
		else:
			return None
		_video.video_title=title
		_video.save()
		return _video
	def change_video_description(self,id,text):
		if video.objects.filter(id=id).exists():
			_video=video.objects.filter(id=id).get()
		else:
			return None
		_video.video_description=text
		_video.save()
		return _video
	def change_video_url(self,id,url):
		if video.objects.filter(id=id).exists():
			_video=video.objects.filter(id=id).get()
		else:
			return None
		_video.video_url=url
		_video.save()
		return _video
	def flip(self,id):
		if video.objects.filter(id=id).exists():
			_video=video.objects.filter(id=id).get()
		else:
			return None
		_video.video_R_dir=not _video.video_R_dir
		_video.save()
		return _video
	def remove_video(self,id):
		if video.objects.filter(id=id).exists():
			_video=video.objects.filter(id=id).get()
		else:
			return None
		if _video.cover_img.path.find(
				'\\default.png')==-1 and _video.cover_img.path.find(
			'/default.png')==-1:
			if os.path.isfile(_video.cover_img.path):
				os.remove(_video.cover_img.path)
		_video.delete()
		return _video
	def move_up(self,id):
		if video.objects.filter(id=id).exists():
			_video=video.objects.filter(id=id).get()
		else:
			return None
		cover_img_copy=_video.cover_img
		video_title_copy=_video.video_title
		video_description_copy=_video.video_description1
		video_url_copy=_video.video_url
		video_R_dir_copy=_video.video_R_dir
		id_=int(id)-1
		while not video.objects.filter(id=str(id_)).exists():
			id_-=1
		_video_=video.objects.filter(id=str(id_)).get()
		_video.cover_img=_video_.cover_img
		_video.video_title=_video_.video_title
		_video.video_description=_video_.video_description
		_video.video_url=_video_.video_url
		_video.video_R_dir=_video_.video_R_dir
		_video.save()
		_video_.cover_img=cover_img_copy
		_video_.video_title=video_title_copy
		_video_.video_description=video_description_copy
		_video_.video_url=video_url_copy
		_video_.video_R_dir=video_R_dir_copy
		_video_.save()
		return _video
	def move_down(self,id):
		if video.objects.filter(id=id).exists():
			_video=video.objects.filter(id=id).get()
		else:
			return None
		cover_img_copy=_video.cover_img
		video_title_copy=_video.video_title
		video_description_copy=_video.video_description
		video_url_copy=_video.video_url
		video_R_dir_copy=_video.video_R_dir
		id_=int(id)+1
		while not video.objects.filter(id=str(id_)).exists():
			id_+=1
		_video_=video.objects.filter(id=str(id_)).get()
		_video.cover_img=_video_.cover_img
		_video.video_title=_video_.video_title
		_video.video_description=_video_.video_description
		_video.video_url=_video_.video_url
		_video.video_R_dir=_video_.video_R_dir
		_video.save()
		_video_.cover_img=cover_img_copy
		_video_.video_title=video_title_copy
		_video_.video_description=video_description_copy
		_video_.video_url=video_url_copy
		_video_.video_R_dir=video_R_dir_copy
		_video_.save()
		return _video
class video(models.Model):
	cover_img=models.ImageField(upload_to='video/cover_img/',
								default='video/cover_img/default/default.png',
								blank=True)
	video_title=models.CharField(max_length=191)
	video_description=models.TextField()
	video_url=models.URLField(
		default='https://www.youtube.com/embed/17MBllYf6OY',blank=True)
	video_R_dir=models.BooleanField(default=True)
	objects=videoManager()
class servicesManager(models.Manager):
	def create_service(self):
		service=services.objects.create(title='title',
										description="description")
		return service
	def change_service_img(self,id,img):
		if services.objects.filter(id=id).exists():
			_service=services.objects.filter(id=id).get()
		else:
			return None
		if _service.img.path.find(
				'\\default.png')==-1 and _service.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(_service.img.path):
				os.remove(_service.img.path)
		_service.img=img
		_service.save()
		crop(_service.img.path,(64,64))
		return _service
	def change_service_title(self,id,title):
		if services.objects.filter(id=id).exists():
			_service=services.objects.filter(id=id).get()
		else:
			return None
		_service.title=title
		_service.save()
		return _service
	def change_service_description(self,id,text):
		if services.objects.filter(id=id).exists():
			_service=services.objects.filter(id=id).get()
		else:
			return None
		_service.description=text
		_service.save()
		return _service
	def remove_service(self,id):
		if services.objects.filter(id=id).exists():
			_service=services.objects.filter(id=id).get()
		else:
			return None
		if _service.img.path.find(
				'\\default.png')==-1 and _service.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(_service.img.path):
				os.remove(_service.img.path)
		_service.delete()
		return _service
	def move_up(self,id):
		if services.objects.filter(id=id).exists():
			_service=services.objects.filter(id=id).get()
		else:
			return None
		img_copy=_service.img
		title_copy=_service.title
		description_copy=_service.description
		id_=int(id)-1
		while not services.objects.filter(id=str(id_)).exists():
			id_-=1
		_service_=services.objects.filter(id=str(id_)).get()
		_service.img=_service_.img
		_service.title=_service_.title
		_service.description=_service_.description
		_service.save()
		_service_.img=img_copy
		_service_.title=title_copy
		_service_.description=description_copy
		_service_.save()
		return _service
	def move_down(self,id):
		if services.objects.filter(id=id).exists():
			_service=services.objects.filter(id=id).get()
		else:
			return None
		img_copy=_service.img
		title_copy=_service.title
		description_copy=_service.description
		id_=int(id)+1
		while not services.objects.filter(id=str(id_)).exists():
			id_+=1
		_service_=services.objects.filter(id=str(id_)).get()
		_service.img=_service_.img
		_service.title=_service_.title
		_service.description=_service_.description
		_service.save()
		_service_.img=img_copy
		_service_.title=title_copy
		_service_.description=description_copy
		_service_.save()
		return _service
class services(models.Model):
	img=models.ImageField(upload_to='services/img/',
						  default='services/img/default/default.png'
						  ,blank=True)
	title=models.CharField(max_length=191)
	description=models.TextField()
	objects=servicesManager()
class workSamplesManager(models.Manager):
	def create_work_sample(self):
		work_sample=work_samples.objects.create(title='title',
												description="description")
		return work_sample
	def change_work_sample_img(self,id,img):
		if work_samples.objects.filter(id=id).exists():
			work_sample=work_samples.objects.filter(id=id).get()
		else:
			return None
		if work_sample.img.path.find(
				'\\default.png')==-1 and work_sample.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(work_sample.img.path):
				os.remove(work_sample.img.path)
		work_sample.img=img
		work_sample.save()
		crop(work_sample.img.path,(258,157))
		return work_sample
	def change_work_sample_title(self,id,title):
		if work_samples.objects.filter(id=id).exists():
			work_sample=work_samples.objects.filter(id=id).get()
		else:
			return None
		work_sample.title=title
		work_sample.save()
		return work_sample
	def change_work_sample_description(self,id,text):
		if work_samples.objects.filter(id=id).exists():
			work_sample=work_samples.objects.filter(id=id).get()
		else:
			return None
		work_sample.description=text
		work_sample.save()
		return work_sample
	def change_work_sample_url(self,id,url):
		if work_samples.objects.filter(id=id).exists():
			work_sample=work_samples.objects.filter(id=id).get()
		else:
			return None
		work_sample.url=url
		work_sample.save()
		return work_sample
	def remove_work_sample(self,id):
		if work_samples.objects.filter(id=id).exists():
			work_sample=work_samples.objects.filter(id=id).get()
		else:
			return None
		if work_sample.img.path.find(
				'\\default.png')==-1 and work_sample.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(work_sample.img.path):
				os.remove(work_sample.img.path)
		work_sample.delete()
		return work_sample
class work_samples(models.Model):
	img=models.ImageField(upload_to='work_samples/img/',
						  default='work_samples/img/default/default.png',
						  blank=True)
	title=models.CharField(max_length=191)
	description=models.TextField()
	url=models.URLField(blank=True)
	objects=workSamplesManager()
class workProcessManager(models.Manager):
	def create_process(self):
		w_p=work_process.objects.create(title='title',
										description='description')
		return w_p
	def change_img(self,id,img):
		if work_process.objects.filter(id=id).exists():
			w_p=work_process.objects.filter(id=id).get()
		else:
			return None
		if w_p.img.path.find(
				'\\default.png')==-1 and w_p.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(w_p.img.path):
				os.remove(w_p.img.path)
		w_p.img=img
		w_p.save()
		crop(w_p.img.path,(64,64),exact=True)
		return w_p
	def change_title(self,id,title):
		if work_process.objects.filter(id=id).exists():
			w_p=work_process.objects.filter(id=id).get()
		else:
			return None
		w_p.title=title
		w_p.save()
		return w_p
	def change_description(self,id,text):
		if work_process.objects.filter(id=id).exists():
			w_p=work_process.objects.filter(id=id).get()
		else:
			return None
		w_p.description=text
		w_p.save()
		return w_p
	def remove(self,id):
		if work_process.objects.filter(id=id).exists():
			w_p=work_process.objects.filter(id=id).get()
		else:
			return None
		if w_p.img.path.find(
				'\\default.png')==-1 and w_p.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(w_p.img.path):
				os.remove(w_p.img.path)
		w_p.delete()
		return w_p
	def move_up(self,id):
		if work_process.objects.filter(id=id).exists():
			w_p=work_process.objects.filter(id=id).get()
		else:
			return None
		img_copy=w_p.img
		title_copy=w_p.title
		description_copy=w_p.description
		id_=int(id)-1
		while not work_process.objects.filter(id=str(id_)).exists():
			id_-=1
		_w_p=work_process.objects.filter(id=str(id_)).get()
		w_p.img=_w_p.img
		w_p.title=_w_p.title
		w_p.description=_w_p.description
		w_p.save()
		_w_p.img=img_copy
		_w_p.title=title_copy
		_w_p.description=description_copy
		_w_p.save()
		return w_p
	def move_down(self,id):
		print('test')
		if work_process.objects.filter(id=id).exists():
			w_p=work_process.objects.filter(id=id).get()
		else:
			return None
		img_copy=w_p.img
		title_copy=w_p.title
		description_copy=w_p.description
		id_=int(id)+1
		while not work_process.objects.filter(id=str(id_)).exists():
			id_+=1
		print(id_)
		_w_p=work_process.objects.filter(id=str(id_)).get()
		w_p.img=_w_p.img
		w_p.title=_w_p.title
		w_p.description=_w_p.description
		w_p.save()
		_w_p.img=img_copy
		_w_p.title=title_copy
		_w_p.description=description_copy
		_w_p.save()
		return w_p
class work_process(models.Model):
	img=models.ImageField(upload_to='work_process/img/',
						  default='work_process/img/default/default.png',
						  blank=True)
	title=models.CharField(max_length=100)
	description=models.TextField(blank=True)
	objects=workProcessManager()
class ourTeamManager(models.Manager):
	def create_team_member(self):
		mem=our_team.objects.create(title='title',
									description="description")
		return mem
	def change_team_member_img(self,id,img):
		if our_team.objects.filter(id=id).exists():
			mem=our_team.objects.filter(id=id).get()
		else:
			return None
		if mem.img.path.find(
				'\\default.png')==-1 and mem.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(mem.img.path):
				os.remove(mem.img.path)
		mem.img=img
		mem.save()
		crop(mem.img.path,(280,291))
		return mem
	def change_team_member_title(self,id,title):
		if our_team.objects.filter(id=id).exists():
			mem=our_team.objects.filter(id=id).get()
		else:
			return None
		mem.title=title
		mem.save()
		return mem
	def change_team_member_description(self,id,text):
		if our_team.objects.filter(id=id).exists():
			mem=our_team.objects.filter(id=id).get()
		else:
			return None
		mem.description=text
		mem.save()
		return mem
	def change_team_member_facebook(self,id,url):
		if our_team.objects.filter(id=id).exists():
			mem=our_team.objects.filter(id=id).get()
		else:
			return None
		mem.facebook=url
		mem.save()
		return mem
	def change_team_member_twitter(self,id,url):
		if our_team.objects.filter(id=id).exists():
			mem=our_team.objects.filter(id=id).get()
		else:
			return None
		mem.twitter=url
		mem.save()
		return mem
	def change_team_member_instagram(self,id,url):
		if our_team.objects.filter(id=id).exists():
			mem=our_team.objects.filter(id=id).get()
		else:
			return None
		mem.instagram=url
		mem.save()
		return mem
	def change_team_member_telegram(self,id,url):
		if our_team.objects.filter(id=id).exists():
			mem=our_team.objects.filter(id=id).get()
		else:
			return None
		mem.telegram=url
		mem.save()
		return mem
	def remove_member(self,id):
		if our_team.objects.filter(id=id).exists():
			mem=our_team.objects.filter(id=id).get()
		else:
			return None
		if mem.img.path.find(
				'\\default.png')==-1 and mem.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(mem.img.path):
				os.remove(mem.img.path)
		mem.delete()
		return mem
class our_team(models.Model):
	img=models.ImageField(upload_to='our_team/img/',
						  default='our_team/img/default/default.png',
						  blank=True)
	title=models.CharField(max_length=100)
	description=models.CharField(max_length=100)
	facebook=models.URLField(blank=True)
	twitter=models.URLField(blank=True)
	instagram=models.URLField(blank=True)
	telegram=models.URLField(blank=True)
	objects=ourTeamManager()
class ourCustomersManager(models.Manager):
	def create_customer(self):
		customer=our_customers.objects.create(name='name',job='job',
											  description='description')
		return customer
	def change_customer_img(self,id,img):
		if our_customers.objects.filter(id=id).exists():
			customer=our_customers.objects.filter(id=id).get()
		else:
			return None
		if customer.img.path.find(
				'\\default.png')==-1 and customer.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(customer.img.path):
				os.remove(customer.img.path)
		customer.img=img
		customer.save()
		crop(customer.img.path,(54,54))
		return customer
	def change_customer_name(self,id,name):
		if our_customers.objects.filter(id=id).exists():
			customer=our_customers.objects.filter(id=id).get()
		else:
			return None
		customer.name=name
		customer.save()
		return customer
	def change_customer_job(self,id,job):
		if our_customers.objects.filter(id=id).exists():
			customer=our_customers.objects.filter(id=id).get()
		else:
			return None
		customer.job=job
		customer.save()
		return customer
	def change_customer_description(self,id,text):
		customer=self.filter(id=id).get()
		customer.description=text
		customer.save()
		return customer
	def remove_customer(self,id):
		if our_customers.objects.filter(id=id).exists():
			customer=our_customers.objects.filter(id=id).get()
		else:
			return None
		if customer.img.path.find(
				'\\default.png')==-1 and customer.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(customer.img.path):
				os.remove(customer.img.path)
		customer.delete()
		return customer
class our_customers(models.Model):
	img=models.ImageField(upload_to='customers/img/',
						  default='customers/img/default/default.png',
						  blank=True)
	name=models.CharField(max_length=100,blank=True)
	job=models.CharField(max_length=100,blank=True)
	description=models.TextField()
	objects=ourCustomersManager()
class themeManager(models.Manager):
	def create_theme(self,color,color_ba):
		theme_num=0
		while os.path.isfile(
				'static/web_01/css/style-theme'+str(theme_num)+'.css'):
			theme_num+=1
		theme=site_theme.objects.create(theme_name='-theme'+str(theme_num),
										color=color,color_ba=color_ba)
		style=open('static/web_01/css/style-base.css','r')
		responsive=open('static/web_01/css/responsive-base.css','r')
		code=style.read().replace('#69b8d1','#'+str(color))
		code=code.replace('#a4bfd2','#'+str(color_ba))
		code_r=responsive.read().replace('#69b8d1','#'+str(color))
		style.close()
		responsive.close()
		style=open('static/web_01/css/style-theme'+str(theme_num)+'.css','w+')
		responsive=open(
			'static/web_01/css/responsive-theme'+str(theme_num)+'.css','w+')
		style.write(code)
		responsive.write(code_r)
		style.close()
		responsive.close()
		return theme
	def active_theme(self,id):
		for obj in site_theme.objects.all():
			obj=site_theme.objects.filter(id=obj.id).get()
			obj.active=False
			obj.save()
		if int(id)!=-1:
			if site_theme.objects.filter(id=id).exists():
				theme=site_theme.objects.filter(id=id).get()
			else:
				return None
			theme.active=True
			theme.save()
			return theme
		return None
	def remove_theme(self,id):
		if site_theme.objects.filter(id=id).exists():
			theme=site_theme.objects.filter(id=id).get()
		else:
			return None
		if os.path.isfile(
				'static/web_01/css/style'+str(theme.theme_name)+'.css'):
			os.remove('static/web_01/css/style'+str(theme.theme_name)+'.css')
		if os.path.isfile(
				'static/web_01/css/responsive'+str(theme.theme_name)+'.css'):
			os.remove(
				'static/web_01/css/responsive'+str(theme.theme_name)+'.css')
		theme.delete()
		return theme
class site_theme(models.Model):
	active=models.BooleanField(default=False)
	theme_name=models.CharField(max_length=21)
	color=models.CharField(max_length=6)
	color_ba=models.CharField(max_length=6)
	objects=themeManager()
class ourPricingManager(models.Manager):
	def create_pricing(self):
		pricings=our_pricing.objects.all()
		if len(pricings)>0:
			offers=our_pricing.objects.all()[0].offers
		else:
			offers="offerA:True,offerB:False,offerC:False"
		pricing=our_pricing.objects.create(title='title',price='10',
										   offers=offers)
		return pricing
	def change_pricing_img(self,id,img):
		if our_pricing.objects.filter(id=id).exists():
			pricing=our_pricing.objects.filter(id=id).get()
		else:
			return None
		if pricing.img.path.find(
				'\\default.png')==-1 and pricing.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(pricing.img.path):
				os.remove(pricing.img.path)
		pricing.img=img
		pricing.save()
		crop(pricing.img.path,(64,64))
		return pricing
	def change_pricing_title(self,id,title):
		if our_pricing.objects.filter(id=id).exists():
			pricing=our_pricing.objects.filter(id=id).get()
		else:
			return None
		pricing.title=title
		pricing.save()
		return pricing
	def change_pricing_price(self,id,price):
		if our_pricing.objects.filter(id=id).exists():
			pricing=our_pricing.objects.filter(id=id).get()
		else:
			return None
		pricing.price=price
		pricing.save()
		return pricing
	def add_offer(self):
		pricing=our_pricing.objects.all()
		for i in range(len(pricing)):
			pricing[i].offers+=',offer:False'
			pricing[i].save()
		return pricing
	def rename_offer(self,index,name):
		pricing=our_pricing.objects.all()
		for i in range(len(pricing)):
			offers=pricing[i].offers.split(',')
			offers[int(index)]=name+':'+offers[int(index)].split(':')[1]
			offers_str=''
			for j,offer in enumerate(offers):
				if offer is not None:
					if j==0:
						offers_str+=offer
					else:
						offers_str+=','+offer
			pricing[i].offers=offers_str
			pricing[i].save()
		return pricing
	def update_offer_val(self,id,ov):
		pricing=our_pricing.objects.filter(id=id).get()
		offers=pricing.offers.split(',')
		for i in range(len(offers)):
			try:
				offers[i]=offers[i].split(':')[0]+':'+str(ov[i])
			except:
				offers[i]=offers[i].split(':')[0]+':False'
		offers_str=''
		for offer in offers:
			if offers_str=='':
				offers_str+=offer
			else:
				offers_str+=','+offer
		pricing.offers=offers_str
		pricing.save()
		return pricing
	def remove_offer(self,index):
		pricing=our_pricing.objects.all()
		for i in range(len(pricing)):
			offers=pricing[i].offers.split(',')
			if len(offers)<2:
				return pricing
			offers[int(index)]=None
			offers_str=''
			for j,offer in enumerate(offers):
				if offer is not None and offer!='':
					if offers_str=='':
						offers_str+=offer
					else:
						offers_str+=','+offer
			pricing[i].offers=offers_str
			pricing[i].save()
		return pricing
	def change_pricing_link(self,id,link):
		if our_pricing.objects.filter(id=id).exists():
			pricing=our_pricing.objects.filter(id=id).get()
		else:
			return None
		pricing.link=link
		pricing.save()
		return pricing
	def remove(self,id):
		if our_pricing.objects.filter(id=id).exists():
			price=our_pricing.objects.filter(id=id).get()
		else:
			return None
		if price.img.path.find(
				'\\default.png')==-1 and price.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(price.img.path):
				os.remove(price.img.path)
		price.delete()
		return price
	def move_up(self,id):
		if our_pricing.objects.filter(id=id).exists():
			pricing=our_pricing.objects.filter(id=id).get()
		else:
			return None
		img_copy=pricing.img
		title_copy=pricing.title
		price_copy=pricing.price
		offers_copy=pricing.offers
		link_copy=pricing.link
		id_=int(id)-1
		while not our_pricing.objects.filter(id=str(id_)).exists():
			id_-=1
		_pricing=our_pricing.objects.filter(id=str(id_)).get()
		pricing.img=_pricing.img
		pricing.title=_pricing.title
		pricing.price=_pricing.price
		pricing.offers=_pricing.offers
		pricing.link=_pricing.link
		pricing.save()
		_pricing.img=img_copy
		_pricing.title=title_copy
		_pricing.price=price_copy
		_pricing.offers=offers_copy
		_pricing.link=link_copy
		_pricing.save()
		return pricing
	def move_down(self,id):
		if our_pricing.objects.filter(id=id).exists():
			pricing=our_pricing.objects.filter(id=id).get()
		else:
			return None
		img_copy=pricing.img
		title_copy=pricing.title
		price_copy=pricing.price
		offers_copy=pricing.offers
		link_copy=pricing.link
		id_=int(id)+1
		while not our_pricing.objects.filter(id=str(id_)).exists():
			id_+=1
		_pricing=our_pricing.objects.filter(id=str(id_)).get()
		pricing.img=_pricing.img
		pricing.title=_pricing.title
		pricing.price=_pricing.price
		pricing.offers=_pricing.offers
		pricing.link=_pricing.link
		pricing.save()
		_pricing.img=img_copy
		_pricing.title=title_copy
		_pricing.price=price_copy
		_pricing.offers=offers_copy
		_pricing.link=link_copy
		_pricing.save()
class our_pricing(models.Model):
	img=models.ImageField(upload_to='our_pricing/img/',
						  default='our_pricing/img/default/default.png',
						  blank=True)
	title=models.CharField(max_length=100)
	price=models.CharField(max_length=100)
	offers=models.TextField(blank=True)
	link=models.URLField(blank=True)
	objects=ourPricingManager()
class ourNewsManager(models.Manager):
	def create_news(self):
		news=our_news.objects.create(name='name',
									 topic_A='topic A',topic_B='topic B',
									 description='description')
		return news
	def change_news_img(self,id,img):
		if our_news.objects.filter(id=id).exists():
			news=our_news.objects.filter(id=id).get()
		else:
			return None
		if news.img.path.find(
				'\\default.png')==-1 and news.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(news.img.path):
				os.remove(news.img.path)
		news.img=img
		news.save()
		crop(news.img.path,(286,171))
		return news
	def change_news_name(self,id,name):
		if our_news.objects.filter(id=id).exists():
			news=our_news.objects.filter(id=id).get()
		else:
			return None
		news.name=name
		news.save()
		return news
	def change_news_date(self,id,date):
		if our_news.objects.filter(id=id).exists():
			news=our_news.objects.filter(id=id).get()
		else:
			return False
		try:
			str_=str(date).split('/')
			date=datetime.date(int(str_[2]),int(str_[0]),int(str_[1]))
			news.date=date
		except:
			return False
		news.save()
		return True
	def change_news_topic_A(self,id,topic_A):
		if our_news.objects.filter(id=id).exists():
			news=our_news.objects.filter(id=id).get()
		else:
			return None
		news.topic_A=topic_A
		news.save()
		return news
	def change_news_topic_B(self,id,topic_B):
		if our_news.objects.filter(id=id).exists():
			news=our_news.objects.filter(id=id).get()
		else:
			return None
		news.topic_B=topic_B
		news.save()
		return news
	def change_news_description(self,id,description):
		if our_news.objects.filter(id=id).exists():
			news=our_news.objects.filter(id=id).get()
		else:
			return None
		news.description=description
		news.save()
		return news
	def change_news_link(self,id,link):
		if our_news.objects.filter(id=id).exists():
			news=our_news.objects.filter(id=id).get()
		else:
			return None
		news.link=link
		news.save()
		return news
	def remove(self,id):
		if our_news.objects.filter(id=id).exists():
			news=our_news.objects.filter(id=id).get()
		else:
			return None
		if news.img.path.find(
				'\\default.png')==-1 and news.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(news.img.path):
				os.remove(news.img.path)
		news.delete()
		return news
	def move_up(self,id):
		if our_news.objects.filter(id=id).exists():
			news=our_news.objects.filter(id=id).get()
		else:
			return None
		img_copy=news.img
		name_copy=news.name
		date_copy=news.date
		topic_A_copy=news.topic_A
		topic_B_copy=news.topic_B
		des_copy=news.description
		link_copy=news.link
		id_=int(id)-1
		while not our_news.objects.filter(id=str(id_)).exists():
			id_-=1
		_news=our_news.objects.filter(id=str(id_)).get()
		news.img=_news.img
		news.name=_news.name
		news.date=_news.date
		news.topic_A=_news.topic_A
		news.topic_B=_news.topic_B
		news.description=_news.description
		news.link=_news.link
		news.save()
		_news.img=img_copy
		_news.name=name_copy
		_news.date=date_copy
		_news.topic_A=topic_A_copy
		_news.topic_B=topic_B_copy
		_news.description=des_copy
		_news.link=link_copy
		_news.save()
		return news
	def move_down(self,id):
		if our_news.objects.filter(id=id).exists():
			news=our_news.objects.filter(id=id).get()
		else:
			return None
		img_copy=news.img
		name_copy=news.name
		date_copy=news.date
		topic_A_copy=news.topic_A
		topic_B_copy=news.topic_B
		des_copy=news.description
		link_copy=news.link
		id_=int(id)+1
		while not our_news.objects.filter(id=str(id_)).exists():
			id_+=1
		_news=our_news.objects.filter(id=str(id_)).get()
		news.img=_news.img
		news.name=_news.name
		news.date=_news.date
		news.topic_A=_news.topic_A
		news.topic_B=_news.topic_B
		news.description=_news.description
		news.link=_news.link
		news.save()
		_news.img=img_copy
		_news.name=name_copy
		_news.date=date_copy
		_news.topic_A=topic_A_copy
		_news.topic_B=topic_B_copy
		_news.description=des_copy
		_news.link=link_copy
		_news.save()
		return news
class our_news(models.Model):
	img=models.ImageField(upload_to='our_news/img/',
						  default='our_news/img/default/default.png',
						  blank=True)
	name=models.CharField(max_length=100)
	date=models.DateField(('Date'),default=datetime.date.today)
	topic_A=models.CharField(max_length=100)
	topic_B=models.CharField(max_length=100)
	description=models.TextField()
	link=models.URLField(blank=True)
	objects=ourNewsManager()
class midPageManager(models.Manager):
	def create_news(self):
		news=our_news.objects.create(name='name',
									 topic_A='topic A',topic_B='topic B',
									 description='description')
		return news
	def change_news_img(self,id,img):
		if our_pricing.objects.filter(id=id).exists():
			pricing=our_pricing.objects.filter(id=id).get()
		else:
			return None
		if pricing.img.path.find(
				'\\default.png')==-1 and pricing.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(pricing.img.path):
				os.remove(pricing.img.path)
		pricing.img=img
		pricing.save()
		return pricing
	def change_news_name(self,id,title):
		if our_pricing.objects.filter(id=id).exists():
			pricing=our_pricing.objects.filter(id=id).get()
		else:
			return None
		pricing.title=title
		pricing.save()
		return pricing
	def change_news_date(self,id,price):
		if our_pricing.objects.filter(id=id).exists():
			pricing=our_pricing.objects.filter(id=id).get()
		else:
			return None
		pricing.price=price
		pricing.save()
		return pricing
	def change_news_topic_A(self,id,offers):
		if our_pricing.objects.filter(id=id).exists():
			pricing=our_pricing.objects.filter(id=id).get()
		else:
			return None
		pricing.offers=offers
		pricing.save()
		return pricing
	def change_news_topic_B(self,id,offers):
		if our_pricing.objects.filter(id=id).exists():
			pricing=our_pricing.objects.filter(id=id).get()
		else:
			return None
		pricing.offers=offers
		pricing.save()
		return pricing
	def change_news_description(self,id,offers):
		if our_pricing.objects.filter(id=id).exists():
			pricing=our_pricing.objects.filter(id=id).get()
		else:
			return None
		pricing.offers=offers
		pricing.save()
		return pricing
	def change_news_link(self,id,link):
		if our_pricing.objects.filter(id=id).exists():
			pricing=our_pricing.objects.filter(id=id).get()
		else:
			return None
		pricing.link=link
		pricing.save()
		return pricing
	def remove_news(self,id):
		if our_pricing.objects.filter(id=id).exists():
			price=our_pricing.objects.filter(id=id).get()
		else:
			return None
		if price.img.path.find(
				'\\default.png')==-1 and price.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(price.img.path):
				os.remove(price.img.path)
		price.delete()
		return price
class mid_page(models.Model):
	img=models.ImageField(upload_to='mid_page/img/',
						  default='mid_page/img/default/default.png',
						  blank=True)
	title=models.TextField()
	description=models.TextField()
	counter=models.TextField()
	objects=midPageManager()
class midPageBManager(models.Manager):
	def create_news(self):
		news=our_news.objects.create(name='name',
									 topic_A='topic A',topic_B='topic B',
									 description='description')
		return news
	def change_news_img(self,id,img):
		if our_pricing.objects.filter(id=id).exists():
			pricing=our_pricing.objects.filter(id=id).get()
		else:
			return None
		if pricing.img.path.find(
				'\\default.png')==-1 and pricing.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(pricing.img.path):
				os.remove(pricing.img.path)
		pricing.img=img
		pricing.save()
		return pricing
	def change_news_name(self,id,title):
		if our_pricing.objects.filter(id=id).exists():
			pricing=our_pricing.objects.filter(id=id).get()
		else:
			return None
		pricing.title=title
		pricing.save()
		return pricing
	def change_news_date(self,id,price):
		if our_pricing.objects.filter(id=id).exists():
			pricing=our_pricing.objects.filter(id=id).get()
		else:
			return None
		pricing.price=price
		pricing.save()
		return pricing
	def change_news_topic_A(self,id,offers):
		if our_pricing.objects.filter(id=id).exists():
			pricing=our_pricing.objects.filter(id=id).get()
		else:
			return None
		pricing.offers=offers
		pricing.save()
		return pricing
	def change_news_topic_B(self,id,offers):
		if our_pricing.objects.filter(id=id).exists():
			pricing=our_pricing.objects.filter(id=id).get()
		else:
			return None
		pricing.offers=offers
		pricing.save()
		return pricing
	def change_news_description(self,id,offers):
		if our_pricing.objects.filter(id=id).exists():
			pricing=our_pricing.objects.filter(id=id).get()
		else:
			return None
		pricing.offers=offers
		pricing.save()
		return pricing
	def change_news_link(self,id,link):
		if our_pricing.objects.filter(id=id).exists():
			pricing=our_pricing.objects.filter(id=id).get()
		else:
			return None
		pricing.link=link
		pricing.save()
		return pricing
	def remove_news(self,id):
		if our_pricing.objects.filter(id=id).exists():
			price=our_pricing.objects.filter(id=id).get()
		else:
			return None
		if price.img.path.find(
				'\\default.png')==-1 and price.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(price.img.path):
				os.remove(price.img.path)
		price.delete()
		return price
class mid_page_B(models.Model):
	img=models.ImageField(upload_to='mid_page_B/img/',
						  default='mid_page_B/img/default/default.png',
						  blank=True)
	title=models.TextField()
	description=models.TextField()
	objects=midPageBManager()
class imgArrayManager(models.Manager):
	def create_img(self):
		img=img_array.objects.create()
		return img
	def change_img(self,id,new_img):
		if img_array.objects.filter(id=id).exists():
			img=img_array.objects.filter(id=id).get()
		else:
			return None
		if img.img.path.find(
				'\\default.png')==-1 and img.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(img.img.path):
				os.remove(img.img.path)
		img.img=new_img
		img.save()
		crop(img.img.path,(183,44),True)
		return img
	def remove(self,id):
		if img_array.objects.filter(id=id).exists():
			img=img_array.objects.filter(id=id).get()
		else:
			return None
		if img.img.path.find(
				'\\default.png')==-1 and img.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(img.img.path):
				os.remove(img.img.path)
		img.delete()
		return img
class img_array(models.Model):
	img=models.ImageField(upload_to='img_array/img/',
						  default='img_array/img/default/default.png',
						  blank=True)
	objects=imgArrayManager()
class mainPagesManager(models.Manager):
	def add_option(self,id):
		if main_pages.objects.filter(id=id).exists():
			page=main_pages.objects.filter(id=id).get()
		else:
			return None
		if page.b_title=='':
			page.b_title+='background title'
		else:
			page.b_title+=',background title'
		if page.title=='':
			page.title+='title'
		else:
			page.title+=',title'
		if page.description=='':
			page.description+='description'
		else:
			page.description+=',description'
		if page.options=='':
			page.options+='None'
		else:
			page.options+=',None'
		page.save()
		return page
	def change_page_name(self,id,name):
		if main_pages.objects.filter(id=id).exists():
			page=main_pages.objects.filter(id=id).get()
		else:
			return None
		page.page_name=name
		page.save()
		return page
	def change_b_title(self,id,index,b_title):
		if main_pages.objects.filter(id=id).exists():
			page=main_pages.objects.filter(id=id).get()
		else:
			return None
		
		return page
	def change_title(self,id,index,new_img):
		if main_pages.objects.filter(id=id).exists():
			img=main_pages.objects.filter(id=id).get()
		else:
			return None
		if img.img.path.find(
				'\\default.png')==-1 and img.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(img.img.path):
				os.remove(img.img.path)
		img.img=new_img
		img.save()
		crop(img.img.path,(183,44),True)
		return img
	def change_description(self,id,index,description):
		if main_pages.objects.filter(id=id).exists():
			img=main_pages.objects.filter(id=id).get()
		else:
			return None
		if img.img.path.find(
				'\\default.png')==-1 and img.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(img.img.path):
				os.remove(img.img.path)
		img.img=new_img
		img.save()
		crop(img.img.path,(183,44),True)
		return img
	def change_option(self,id,index,description):
		if main_pages.objects.filter(id=id).exists():
			img=main_pages.objects.filter(id=id).get()
		else:
			return None
		if img.img.path.find(
				'\\default.png')==-1 and img.img.path.find(
			'/default.png')==-1:
			if os.path.isfile(img.img.path):
				os.remove(img.img.path)
		img.img=new_img
		img.save()
		crop(img.img.path,(183,44),True)
		return img
	def get_options(self,id,single_des=False):
		if main_pages.objects.filter(id=id).exists():
			page=main_pages.objects.filter(id=id).get()
		else:
			return None
		options=list()
		b_title_str=page.b_title.split(',')
		title_str=page.title.split(',')
		description_str=page.description.split(',')
		options_str=page.options.split(',')
		for i,option_str in enumerate(options_str):
			if option_str != '':
				if single_des:
					option={
						'b_title':b_title_str[i],
						'title':title_str[i],
						'description':description_str[i],
						'option':option_str
						}
				else:
					option={
						'b_title':b_title_str[i],
						'title':title_str[i],
						'description':description_str[i].split('\n'),
						'option':option_str
						}
				options.append(option)
		return options
	def remove_option(self,id,index):
		if main_pages.objects.filter(id=id).exists():
			page=main_pages.objects.filter(id=id).get()
		else:
			return None
		b_title=page.b_title.split(',')
		b_title.pop(index)
		b_title_str=''
		for b_t in b_title:
			if b_title_str=='':
				b_title_str+=b_t
			else:
				b_title_str+=','+b_t
		page.b_title=b_title_str
		title=page.title.split(',')
		title.pop(index)
		title_str=''
		for t in title:
			if title_str=='':
				title_str+=t
			else:
				title_str+=','+t
		page.title=title_str
		description=page.description.split(',')
		description.pop(index)
		description_str=''
		for d in description:
			if description_str=='':
				description_str+=d
			else:
				description_str+=','+d
		page.description=description_str
		options=page.options.split(',')
		options.pop(index)
		options_str=''
		for o in options:
			if options_str=='':
				options_str+=o
			else:
				options_str+=','+o
		page.options=options_str
		page.save()
		return page
	def m_u(self,id,index):
		if main_pages.objects.filter(id=id).exists():
			page=main_pages.objects.filter(id=id).get()
		else:
			return None
		b_title=page.b_title.split(',')
		copy=b_title[index]
		b_title[index]=b_title[index-1]
		b_title[index-1]=copy
		b_title_str=''
		for b_t in b_title:
			if b_title_str=='':
				b_title_str+=b_t
			else:
				b_title_str+=','+b_t
		page.b_title=b_title_str
		title=page.title.split(',')
		copy=title[index]
		title[index]=title[index-1]
		title[index-1]=copy
		title_str=''
		for t in title:
			if title_str=='':
				title_str+=t
			else:
				title_str+=','+t
		page.title=title_str
		description=page.description.split(',')
		copy=description[index]
		description[index]=description[index-1]
		description[index-1]=copy
		description_str=''
		for d in description:
			if description_str=='':
				description_str+=d
			else:
				description_str+=','+d
		page.description=description_str
		options=page.options.split(',')
		copy=options[index]
		options[index]=options[index-1]
		options[index-1]=copy
		options_str=''
		for o in options:
			if options_str=='':
				options_str+=o
			else:
				options_str+=','+o
		page.options=options_str
		page.save()
		return page
	def m_d(self,id,index):
		if main_pages.objects.filter(id=id).exists():
			page=main_pages.objects.filter(id=id).get()
		else:
			return None
		b_title=page.b_title.split(',')
		copy=b_title[index]
		b_title[index]=b_title[index+1]
		b_title[index+1]=copy
		b_title_str=''
		for b_t in b_title:
			if b_title_str=='':
				b_title_str+=b_t
			else:
				b_title_str+=','+b_t
		page.b_title=b_title_str
		title=page.title.split(',')
		copy=title[index]
		title[index]=title[index+1]
		title[index+1]=copy
		title_str=''
		for t in title:
			if title_str=='':
				title_str+=t
			else:
				title_str+=','+t
		page.title=title_str
		description=page.description.split(',')
		copy=description[index]
		description[index]=description[index+1]
		description[index+1]=copy
		description_str=''
		for d in description:
			if description_str=='':
				description_str+=d
			else:
				description_str+=','+d
		page.description=description_str
		options=page.options.split(',')
		copy=options[index]
		options[index]=options[index+1]
		options[index+1]=copy
		options_str=''
		for o in options:
			if options_str=='':
				options_str+=o
			else:
				options_str+=','+o
		page.options=options_str
		page.save()
		return page
class main_pages(models.Model):
	page_name=models.CharField(max_length=100)
	b_title=models.TextField(blank=True)
	title=models.TextField(blank=True)
	description=models.TextField(blank=True)
	options=models.TextField(blank=True)
	objects=mainPagesManager()
