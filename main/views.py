from django.shortcuts import render

from control_panel.models import *
def about_us(request):
	slideshow_array=list()
	for slide in slideshow.objects.all():
		slide.slide_body_text=slide.slide_body_text.split('\n')
		if '{' in slide.slide_title and '}' in slide.slide_title:
			slide_title_parts=slide.slide_title.split('}')
			title_parts=list()
			for slide_title_part in slide_title_parts:
				if '{' in slide_title_part:
					title_part={
						'title':slide_title_part.split('{')[0],
						'span':slide_title_part.split('{')[1]
						}
					title_parts.append(title_part)
				else:
					title_part={
						'title':slide_title_part,
						'span':''
						}
					title_parts.append(title_part)
			slideshow_arr={
				'object':slide,
				'title_parts':title_parts
				}
			slideshow_array.append(slideshow_arr)
		else:
			title_parts=list()
			title_part={
				'title':slide.slide_title,
				'span':''
				}
			title_parts.append(title_part)
			slideshow_arr={
				'object':slide,
				'title_parts':title_parts
				}
			slideshow_array.append(slideshow_arr)
	videos=video.objects.all()
	for _video in videos:
		_video.video_description=_video.video_description.split('\n')
	theme_name=''
	for theme in site_theme.objects.all():
		if theme.active:
			theme_name=theme.theme_name
			break
	pricing=our_pricing.objects.all()
	for i in range(len(pricing)):
		offers=list()
		_str=pricing[i].offers.split(',')
		for st in _str:
			offer={
				'offer':st.split(':')[0],
				'haveit':st.split(':')[1]
				}
			offers.append(offer)
		pricing[i].offers=offers
	counter_bg_img=mid_page.objects.all()[0].img
	counter_title=list()
	_str=mid_page.objects.all()[0].title.split('\n')
	for s in _str:
		str_=s.split('}')
		_line=list()
		for _s in str_:
			if '{' in _s:
				ct={
					'n_s':_s.split('{')[0],
					'span':_s.split('{')[1]
					}
				_line.append(ct)
			else:
				ct={
					'n_s':_s,
					'span':''
					}
				_line.append(ct)
		counter_title.append(_line)
	counter_des=mid_page.objects.all()[0].description.split('\n')
	counter_numbers_title_S=list()
	_str=mid_page.objects.all()[0].counter.split(',')
	for s in _str:
		counter={
			'title':s.split(':')[0],
			'num':s.split(':')[1]
			}
		counter_numbers_title_S.append(counter)
	if '|' in site_logo.objects.all()[0].title:
		_str=site_logo.objects.all()[0].title.split('|')
		_logo={
			'n_span':_str[0],
			'span':_str[1]
			}
	else:
		_str=site_logo.objects.all()[0].title
		_logo={
			'n_span':_str,
			'span':''
			}
	mid_page_img=mid_page_B.objects.all()[0].img
	mid_page_title=list()
	_str=mid_page_B.objects.all()[0].title.split('\n')
	for s in _str:
		str_=s.split('}')
		_line=list()
		for _s in str_:
			if '{' in _s:
				ct={
					'n_s':_s.split('{')[0],
					'span':_s.split('{')[1]
					}
				_line.append(ct)
			else:
				ct={
					'n_s':_s,
					'span':''
					}
				_line.append(ct)
		mid_page_title.append(_line)
	mid_page_des=mid_page_B.objects.all()[0].description.split('\n')
	work_process_=work_process.objects.all()
	for i in range(len(work_process_)):
		work_process_[i].description=work_process_[i].description.split('\n')
	news=our_news.objects.all()
	news_des_i=0
	for i in range(len(news)):
		news[i].description=news[i].description.split('\n')
		if len(news[i].description)>news_des_i:
			news_des_i=len(news[i].description)
	for i in range(len(news)):
		while len(news[i].description)<news_des_i:
			news[i].description.append('')
	return render(request,'main/about-us.html',{
					  'site_title':site_title.objects.all(),
					  'logo':_logo,
					  'slideshow':slideshow_array,
					  'videos':videos,
					  'services':services.objects.all(),
					  'work_samples':work_samples.objects.all(),
					  'work_process':work_process_,
					  'our_team':our_team.objects.all(),
					  'customers':our_customers.objects.all(),
					  'pricings':pricing,
					  'news':news,
					  'counter_bg_img':counter_bg_img,
					  'counter_title':counter_title,
					  'counter_des':counter_des,
					  'mid_page_img':mid_page_img,
					  'mid_page_title':mid_page_title,
					  'mid_page_des':mid_page_des,
					  'img_array':img_array.objects.all(),
					  'cntS':counter_numbers_title_S,
					  'style':'web_01/css/style'+theme_name+'.css',
					  'responsive':'web_01/css/responsive'+theme_name+'.css',
					  'page_name':'about us'
					  })
def contact_us(request):
	slideshow_array=list()
	for slide in slideshow.objects.all():
		slide.slide_body_text=slide.slide_body_text.split('\n')
		if '{' in slide.slide_title and '}' in slide.slide_title:
			slide_title_parts=slide.slide_title.split('}')
			title_parts=list()
			for slide_title_part in slide_title_parts:
				if '{' in slide_title_part:
					title_part={
						'title':slide_title_part.split('{')[0],
						'span':slide_title_part.split('{')[1]
						}
					title_parts.append(title_part)
				else:
					title_part={
						'title':slide_title_part,
						'span':''
						}
					title_parts.append(title_part)
			slideshow_arr={
				'object':slide,
				'title_parts':title_parts
				}
			slideshow_array.append(slideshow_arr)
		else:
			title_parts=list()
			title_part={
				'title':slide.slide_title,
				'span':''
				}
			title_parts.append(title_part)
			slideshow_arr={
				'object':slide,
				'title_parts':title_parts
				}
			slideshow_array.append(slideshow_arr)
	videos=video.objects.all()
	for _video in videos:
		_video.video_description=_video.video_description.split('\n')
	theme_name=''
	for theme in site_theme.objects.all():
		if theme.active:
			theme_name=theme.theme_name
			break
	pricing=our_pricing.objects.all()
	for i in range(len(pricing)):
		offers=list()
		_str=pricing[i].offers.split(',')
		for st in _str:
			offer={
				'offer':st.split(':')[0],
				'haveit':st.split(':')[1]
				}
			offers.append(offer)
		pricing[i].offers=offers
	counter_bg_img=mid_page.objects.all()[0].img
	counter_title=list()
	_str=mid_page.objects.all()[0].title.split('\n')
	for s in _str:
		str_=s.split('}')
		_line=list()
		for _s in str_:
			if '{' in _s:
				ct={
					'n_s':_s.split('{')[0],
					'span':_s.split('{')[1]
					}
				_line.append(ct)
			else:
				ct={
					'n_s':_s,
					'span':''
					}
				_line.append(ct)
		counter_title.append(_line)
	counter_des=mid_page.objects.all()[0].description.split('\n')
	counter_numbers_title_S=list()
	_str=mid_page.objects.all()[0].counter.split(',')
	for s in _str:
		counter={
			'title':s.split(':')[0],
			'num':s.split(':')[1]
			}
		counter_numbers_title_S.append(counter)
	if '|' in site_logo.objects.all()[0].title:
		_str=site_logo.objects.all()[0].title.split('|')
		_logo={
			'n_span':_str[0],
			'span':_str[1]
			}
	else:
		_str=site_logo.objects.all()[0].title
		_logo={
			'n_span':_str,
			'span':''
			}
	mid_page_img=mid_page_B.objects.all()[0].img
	mid_page_title=list()
	_str=mid_page_B.objects.all()[0].title.split('\n')
	for s in _str:
		str_=s.split('}')
		_line=list()
		for _s in str_:
			if '{' in _s:
				ct={
					'n_s':_s.split('{')[0],
					'span':_s.split('{')[1]
					}
				_line.append(ct)
			else:
				ct={
					'n_s':_s,
					'span':''
					}
				_line.append(ct)
		mid_page_title.append(_line)
	mid_page_des=mid_page_B.objects.all()[0].description.split('\n')
	work_process_=work_process.objects.all()
	for i in range(len(work_process_)):
		work_process_[i].description=work_process_[i].description.split('\n')
	news=our_news.objects.all()
	news_des_i=0
	for i in range(len(news)):
		news[i].description=news[i].description.split('\n')
		if len(news[i].description)>news_des_i:
			news_des_i=len(news[i].description)
	for i in range(len(news)):
		while len(news[i].description)<news_des_i:
			news[i].description.append('')
	return render(request,'main/contact-us.html',{
					  'site_title':site_title.objects.all(),
					  'logo':_logo,
					  'slideshow':slideshow_array,
					  'videos':videos,
					  'services':services.objects.all(),
					  'work_samples':work_samples.objects.all(),
					  'work_process':work_process_,
					  'our_team':our_team.objects.all(),
					  'customers':our_customers.objects.all(),
					  'pricings':pricing,
					  'news':news,
					  'counter_bg_img':counter_bg_img,
					  'counter_title':counter_title,
					  'counter_des':counter_des,
					  'mid_page_img':mid_page_img,
					  'mid_page_title':mid_page_title,
					  'mid_page_des':mid_page_des,
					  'img_array':img_array.objects.all(),
					  'cntS':counter_numbers_title_S,
					  'style':'web_01/css/style'+theme_name+'.css',
					  'responsive':'web_01/css/responsive'+theme_name+'.css',
					  'page_name':''
					  })
def index(request):
	slideshow_array=list()
	for slide in slideshow.objects.all():
		slide.slide_body_text=slide.slide_body_text.split('\n')
		if '{' in slide.slide_title and '}' in slide.slide_title:
			slide_title_parts=slide.slide_title.split('}')
			title_parts=list()
			for slide_title_part in slide_title_parts:
				if '{' in slide_title_part:
					title_part={
						'title':slide_title_part.split('{')[0],
						'span':slide_title_part.split('{')[1]
						}
					title_parts.append(title_part)
				else:
					title_part={'title':slide_title_part,'span':''}
					title_parts.append(title_part)
			slideshow_arr={'object':slide,'title_parts':title_parts}
			slideshow_array.append(slideshow_arr)
		else:
			title_parts=list()
			title_part={
				'title':slide.slide_title,
				'span':''
				}
			title_parts.append(title_part)
			slideshow_arr={
				'object':slide,
				'title_parts':title_parts
				}
			slideshow_array.append(slideshow_arr)
	videos=video.objects.all()
	for _video in videos:
		_video.video_description=_video.video_description.split('\n')
	theme_name=''
	for theme in site_theme.objects.all():
		if theme.active:
			theme_name=theme.theme_name
			break
	pricing=our_pricing.objects.all()
	for i in range(len(pricing)):
		offers=list()
		_str=pricing[i].offers.split(',')
		for st in _str:
			offer={
				'offer':st.split(':')[0],
				'haveit':st.split(':')[1]
				}
			offers.append(offer)
		pricing[i].offers=offers
	counter_bg_img=mid_page.objects.all()[0].img
	counter_title=list()
	_str=mid_page.objects.all()[0].title.split('\n')
	for s in _str:
		str_=s.split('}')
		_line=list()
		for _s in str_:
			if '{' in _s:
				ct={
					'n_s':_s.split('{')[0],
					'span':_s.split('{')[1]
					}
				_line.append(ct)
			else:
				ct={
					'n_s':_s,
					'span':''
					}
				_line.append(ct)
		counter_title.append(_line)
	counter_des=mid_page.objects.all()[0].description.split('\n')
	counter_numbers_title_S=list()
	_str=mid_page.objects.all()[0].counter.split(',')
	for s in _str:
		counter={
			'title':s.split(':')[0],
			'num':s.split(':')[1]
			}
		counter_numbers_title_S.append(counter)
	if '|' in site_logo.objects.all()[0].title:
		_str=site_logo.objects.all()[0].title.split('|')
		_logo={
			'n_span':_str[0],
			'span':_str[1]
			}
	else:
		_str=site_logo.objects.all()[0].title
		_logo={
			'n_span':_str,
			'span':''
			}
	mid_page_img=mid_page_B.objects.all()[0].img
	mid_page_title=list()
	_str=mid_page_B.objects.all()[0].title.split('\n')
	for s in _str:
		str_=s.split('}')
		_line=list()
		for _s in str_:
			if '{' in _s:
				ct={
					'n_s':_s.split('{')[0],
					'span':_s.split('{')[1]
					}
				_line.append(ct)
			else:
				ct={
					'n_s':_s,
					'span':''
					}
				_line.append(ct)
		mid_page_title.append(_line)
	mid_page_des=mid_page_B.objects.all()[0].description.split('\n')
	work_process_=work_process.objects.all()
	for i in range(len(work_process_)):
		work_process_[i].description=work_process_[i].description.split('\n')
	news=our_news.objects.all()
	news_des_i=0
	for i in range(len(news)):
		news[i].description=news[i].description.split('\n')
		if len(news[i].description)>news_des_i:
			news_des_i=len(news[i].description)
	for i in range(len(news)):
		while len(news[i].description)<news_des_i:
			news[i].description.append('')
	return render(request,'main/index.html',
				  {
					  'site_title':site_title.objects.all(),
					  'logo':_logo,
					  'slideshow':slideshow_array,
					  'videos':videos,
					  'services':services.objects.all(),
					  'work_samples':work_samples.objects.all(),
					  'work_process':work_process_,
					  'our_team':our_team.objects.all(),
					  'customers':our_customers.objects.all(),
					  'pricings':pricing,
					  'news':news,
					  'counter_bg_img':counter_bg_img,
					  'counter_title':counter_title,
					  'counter_des':counter_des,
					  'mid_page_img':mid_page_img,
					  'mid_page_title':mid_page_title,
					  'mid_page_des':mid_page_des,
					  'img_array':img_array.objects.all(),
					  'cntS':counter_numbers_title_S,
					  'style':'web_01/css/style'+theme_name+'.css',
					  'responsive':'web_01/css/responsive'+theme_name+'.css',
					  'page_name':''
					  })
def our_services(request):
	slideshow_array=list()
	for slide in slideshow.objects.all():
		slide.slide_body_text=slide.slide_body_text.split('\n')
		if '{' in slide.slide_title and '}' in slide.slide_title:
			slide_title_parts=slide.slide_title.split('}')
			title_parts=list()
			for slide_title_part in slide_title_parts:
				if '{' in slide_title_part:
					title_part={
						'title':slide_title_part.split('{')[0],
						'span':slide_title_part.split('{')[1]
						}
					title_parts.append(title_part)
				else:
					title_part={
						'title':slide_title_part,
						'span':''
						}
					title_parts.append(title_part)
			slideshow_arr={
				'object':slide,
				'title_parts':title_parts
				}
			slideshow_array.append(slideshow_arr)
		else:
			title_parts=list()
			title_part={
				'title':slide.slide_title,
				'span':''
				}
			title_parts.append(title_part)
			slideshow_arr={
				'object':slide,
				'title_parts':title_parts
				}
			slideshow_array.append(slideshow_arr)
	videos=video.objects.all()
	for _video in videos:
		_video.video_description=_video.video_description.split('\n')
	theme_name=''
	for theme in site_theme.objects.all():
		if theme.active:
			theme_name=theme.theme_name
			break
	pricing=our_pricing.objects.all()
	for i in range(len(pricing)):
		offers=list()
		_str=pricing[i].offers.split(',')
		for st in _str:
			offer={
				'offer':st.split(':')[0],
				'haveit':st.split(':')[1]
				}
			offers.append(offer)
		pricing[i].offers=offers
	counter_bg_img=mid_page.objects.all()[0].img
	counter_title=list()
	_str=mid_page.objects.all()[0].title.split('\n')
	for s in _str:
		str_=s.split('}')
		_line=list()
		for _s in str_:
			if '{' in _s:
				ct={
					'n_s':_s.split('{')[0],
					'span':_s.split('{')[1]
					}
				_line.append(ct)
			else:
				ct={
					'n_s':_s,
					'span':''
					}
				_line.append(ct)
		counter_title.append(_line)
	counter_des=mid_page.objects.all()[0].description.split('\n')
	counter_numbers_title_S=list()
	_str=mid_page.objects.all()[0].counter.split(',')
	for s in _str:
		counter={
			'title':s.split(':')[0],
			'num':s.split(':')[1]
			}
		counter_numbers_title_S.append(counter)
	if '|' in site_logo.objects.all()[0].title:
		_str=site_logo.objects.all()[0].title.split('|')
		_logo={
			'n_span':_str[0],
			'span':_str[1]
			}
	else:
		_str=site_logo.objects.all()[0].title
		_logo={
			'n_span':_str,
			'span':''
			}
	mid_page_img=mid_page_B.objects.all()[0].img
	mid_page_title=list()
	_str=mid_page_B.objects.all()[0].title.split('\n')
	for s in _str:
		str_=s.split('}')
		_line=list()
		for _s in str_:
			if '{' in _s:
				ct={
					'n_s':_s.split('{')[0],
					'span':_s.split('{')[1]
					}
				_line.append(ct)
			else:
				ct={
					'n_s':_s,
					'span':''
					}
				_line.append(ct)
		mid_page_title.append(_line)
	mid_page_des=mid_page_B.objects.all()[0].description.split('\n')
	work_process_=work_process.objects.all()
	for i in range(len(work_process_)):
		work_process_[i].description=work_process_[i].description.split('\n')
	news=our_news.objects.all()
	news_des_i=0
	for i in range(len(news)):
		news[i].description=news[i].description.split('\n')
		if len(news[i].description)>news_des_i:
			news_des_i=len(news[i].description)
	for i in range(len(news)):
		while len(news[i].description)<news_des_i:
			news[i].description.append('')
	return render(request,'main/our-services.html',{
					  'site_title':site_title.objects.all(),
					  'logo':_logo,
					  'slideshow':slideshow_array,
					  'videos':videos,
					  'services':services.objects.all(),
					  'work_samples':work_samples.objects.all(),
					  'work_process':work_process_,
					  'our_team':our_team.objects.all(),
					  'customers':our_customers.objects.all(),
					  'pricings':pricing,
					  'news':news,
					  'counter_bg_img':counter_bg_img,
					  'counter_title':counter_title,
					  'counter_des':counter_des,
					  'mid_page_img':mid_page_img,
					  'mid_page_title':mid_page_title,
					  'mid_page_des':mid_page_des,
					  'img_array':img_array.objects.all(),
					  'cntS':counter_numbers_title_S,
					  'style':'web_01/css/style'+theme_name+'.css',
					  'responsive':'web_01/css/responsive'+theme_name+'.css',
					  'page_name':''
					  })
def our_team_(request):
	slideshow_array=list()
	for slide in slideshow.objects.all():
		slide.slide_body_text=slide.slide_body_text.split('\n')
		if '{' in slide.slide_title and '}' in slide.slide_title:
			slide_title_parts=slide.slide_title.split('}')
			title_parts=list()
			for slide_title_part in slide_title_parts:
				if '{' in slide_title_part:
					title_part={
						'title':slide_title_part.split('{')[0],
						'span':slide_title_part.split('{')[1]
						}
					title_parts.append(title_part)
				else:
					title_part={
						'title':slide_title_part,
						'span':''
						}
					title_parts.append(title_part)
			slideshow_arr={
				'object':slide,
				'title_parts':title_parts
				}
			slideshow_array.append(slideshow_arr)
		else:
			title_parts=list()
			title_part={
				'title':slide.slide_title,
				'span':''
				}
			title_parts.append(title_part)
			slideshow_arr={
				'object':slide,
				'title_parts':title_parts
				}
			slideshow_array.append(slideshow_arr)
	videos=video.objects.all()
	for _video in videos:
		_video.video_description=_video.video_description.split('\n')
	theme_name=''
	for theme in site_theme.objects.all():
		if theme.active:
			theme_name=theme.theme_name
			break
	pricing=our_pricing.objects.all()
	for i in range(len(pricing)):
		offers=list()
		_str=pricing[i].offers.split(',')
		for st in _str:
			offer={
				'offer':st.split(':')[0],
				'haveit':st.split(':')[1]
				}
			offers.append(offer)
		pricing[i].offers=offers
	counter_bg_img=mid_page.objects.all()[0].img
	counter_title=list()
	_str=mid_page.objects.all()[0].title.split('\n')
	for s in _str:
		str_=s.split('}')
		_line=list()
		for _s in str_:
			if '{' in _s:
				ct={
					'n_s':_s.split('{')[0],
					'span':_s.split('{')[1]
					}
				_line.append(ct)
			else:
				ct={
					'n_s':_s,
					'span':''
					}
				_line.append(ct)
		counter_title.append(_line)
	counter_des=mid_page.objects.all()[0].description.split('\n')
	counter_numbers_title_S=list()
	_str=mid_page.objects.all()[0].counter.split(',')
	for s in _str:
		counter={
			'title':s.split(':')[0],
			'num':s.split(':')[1]
			}
		counter_numbers_title_S.append(counter)
	if '|' in site_logo.objects.all()[0].title:
		_str=site_logo.objects.all()[0].title.split('|')
		_logo={
			'n_span':_str[0],
			'span':_str[1]
			}
	else:
		_str=site_logo.objects.all()[0].title
		_logo={
			'n_span':_str,
			'span':''
			}
	mid_page_img=mid_page_B.objects.all()[0].img
	mid_page_title=list()
	_str=mid_page_B.objects.all()[0].title.split('\n')
	for s in _str:
		str_=s.split('}')
		_line=list()
		for _s in str_:
			if '{' in _s:
				ct={
					'n_s':_s.split('{')[0],
					'span':_s.split('{')[1]
					}
				_line.append(ct)
			else:
				ct={
					'n_s':_s,
					'span':''
					}
				_line.append(ct)
		mid_page_title.append(_line)
	mid_page_des=mid_page_B.objects.all()[0].description.split('\n')
	work_process_=work_process.objects.all()
	for i in range(len(work_process_)):
		work_process_[i].description=work_process_[i].description.split('\n')
	news=our_news.objects.all()
	news_des_i=0
	for i in range(len(news)):
		news[i].description=news[i].description.split('\n')
		if len(news[i].description)>news_des_i:
			news_des_i=len(news[i].description)
	for i in range(len(news)):
		while len(news[i].description)<news_des_i:
			news[i].description.append('')
	return render(request,'main/our-team.html',{
					  'site_title':site_title.objects.all(),
					  'logo':_logo,
					  'slideshow':slideshow_array,
					  'videos':videos,
					  'services':services.objects.all(),
					  'work_samples':work_samples.objects.all(),
					  'work_process':work_process_,
					  'our_team':our_team.objects.all(),
					  'customers':our_customers.objects.all(),
					  'pricings':pricing,
					  'news':news,
					  'counter_bg_img':counter_bg_img,
					  'counter_title':counter_title,
					  'counter_des':counter_des,
					  'mid_page_img':mid_page_img,
					  'mid_page_title':mid_page_title,
					  'mid_page_des':mid_page_des,
					  'img_array':img_array.objects.all(),
					  'cntS':counter_numbers_title_S,
					  'style':'web_01/css/style'+theme_name+'.css',
					  'responsive':'web_01/css/responsive'+theme_name+'.css',
					  'page_name':''
					  })
def pricing(request):
	slideshow_array=list()
	for slide in slideshow.objects.all():
		slide.slide_body_text=slide.slide_body_text.split('\n')
		if '{' in slide.slide_title and '}' in slide.slide_title:
			slide_title_parts=slide.slide_title.split('}')
			title_parts=list()
			for slide_title_part in slide_title_parts:
				if '{' in slide_title_part:
					title_part={
						'title':slide_title_part.split('{')[0],
						'span':slide_title_part.split('{')[1]
						}
					title_parts.append(title_part)
				else:
					title_part={
						'title':slide_title_part,
						'span':''
						}
					title_parts.append(title_part)
			slideshow_arr={
				'object':slide,
				'title_parts':title_parts
				}
			slideshow_array.append(slideshow_arr)
		else:
			title_parts=list()
			title_part={
				'title':slide.slide_title,
				'span':''
				}
			title_parts.append(title_part)
			slideshow_arr={
				'object':slide,
				'title_parts':title_parts
				}
			slideshow_array.append(slideshow_arr)
	videos=video.objects.all()
	for _video in videos:
		_video.video_description=_video.video_description.split('\n')
	theme_name=''
	for theme in site_theme.objects.all():
		if theme.active:
			theme_name=theme.theme_name
			break
	pricing=our_pricing.objects.all()
	for i in range(len(pricing)):
		offers=list()
		_str=pricing[i].offers.split(',')
		for st in _str:
			offer={
				'offer':st.split(':')[0],
				'haveit':st.split(':')[1]
				}
			offers.append(offer)
		pricing[i].offers=offers
	counter_bg_img=mid_page.objects.all()[0].img
	counter_title=list()
	_str=mid_page.objects.all()[0].title.split('\n')
	for s in _str:
		str_=s.split('}')
		_line=list()
		for _s in str_:
			if '{' in _s:
				ct={
					'n_s':_s.split('{')[0],
					'span':_s.split('{')[1]
					}
				_line.append(ct)
			else:
				ct={
					'n_s':_s,
					'span':''
					}
				_line.append(ct)
		counter_title.append(_line)
	counter_des=mid_page.objects.all()[0].description.split('\n')
	counter_numbers_title_S=list()
	_str=mid_page.objects.all()[0].counter.split(',')
	for s in _str:
		counter={
			'title':s.split(':')[0],
			'num':s.split(':')[1]
			}
		counter_numbers_title_S.append(counter)
	if '|' in site_logo.objects.all()[0].title:
		_str=site_logo.objects.all()[0].title.split('|')
		_logo={
			'n_span':_str[0],
			'span':_str[1]
			}
	else:
		_str=site_logo.objects.all()[0].title
		_logo={
			'n_span':_str,
			'span':''
			}
	mid_page_img=mid_page_B.objects.all()[0].img
	mid_page_title=list()
	_str=mid_page_B.objects.all()[0].title.split('\n')
	for s in _str:
		str_=s.split('}')
		_line=list()
		for _s in str_:
			if '{' in _s:
				ct={
					'n_s':_s.split('{')[0],
					'span':_s.split('{')[1]
					}
				_line.append(ct)
			else:
				ct={
					'n_s':_s,
					'span':''
					}
				_line.append(ct)
		mid_page_title.append(_line)
	mid_page_des=mid_page_B.objects.all()[0].description.split('\n')
	work_process_=work_process.objects.all()
	for i in range(len(work_process_)):
		work_process_[i].description=work_process_[i].description.split('\n')
	news=our_news.objects.all()
	news_des_i=0
	for i in range(len(news)):
		news[i].description=news[i].description.split('\n')
		if len(news[i].description)>news_des_i:
			news_des_i=len(news[i].description)
	for i in range(len(news)):
		while len(news[i].description)<news_des_i:
			news[i].description.append('')
	return render(request,'main/pricing.html',{
					  'site_title':site_title.objects.all(),
					  'logo':_logo,
					  'slideshow':slideshow_array,
					  'videos':videos,
					  'services':services.objects.all(),
					  'work_samples':work_samples.objects.all(),
					  'work_process':work_process_,
					  'our_team':our_team.objects.all(),
					  'customers':our_customers.objects.all(),
					  'pricings':pricing,
					  'news':news,
					  'counter_bg_img':counter_bg_img,
					  'counter_title':counter_title,
					  'counter_des':counter_des,
					  'mid_page_img':mid_page_img,
					  'mid_page_title':mid_page_title,
					  'mid_page_des':mid_page_des,
					  'img_array':img_array.objects.all(),
					  'cntS':counter_numbers_title_S,
					  'style':'web_01/css/style'+theme_name+'.css',
					  'responsive':'web_01/css/responsive'+theme_name+'.css',
					  'page_name':''
					  })
