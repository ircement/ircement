from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import (
	render,
	redirect,
	)

from .models import *
def index(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	return render(request,'control_panel/index.html',{
		'messages':messages,
		'page_name':''
		})
def users(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	users=User.objects.all()
	return render(request,'control_panel/users.html',
				  {
					  'users':users,
					  'messages':messages,
					  'page_name':'users'
					  })
def change_user_data(request,id):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	if not User.objects.filter(id=id).exists():
		return redirect('/control_panel/auth/users/')
	if request.method=='POST':
		if request.POST.get('first-name') is not None:
			if not request.user.is_superuser:
				message={
					'type':'error',
					'body':'You Don\'t Have Permission To Change Users Data.'
					}
				messages.append(message)
			else:
				user_to_change=User.objects.get(id=id)
				first_name=request.POST.get('first-name')
				last_name=request.POST.get('last-name')
				email=request.POST.get('email')
				username=request.POST.get('username')
				if email is not None and email!='':
					if '@' not in email or '.' not in email:
						message={
							'type':'error',
							'body':' Email Is Not Valid.'
							}
						messages.append(message)
					else:
						if User.objects.filter(
								email=email).exists() and User.objects.get(
							email=email).email!=user_to_change.email:
							message={
								'type':'error',
								'body':' Email Is Used.'
								}
							messages.append(message)
				if username is not None and username!='':
					if User.objects.filter(
							username=username).exists() and User.objects.get(
						username=username).username!=user_to_change.username:
						message={
							'type':'error',
							'body':' Username Is Used.'
							}
						messages.append(message)
				allow_to_update_user=True
				for message in messages:
					if message.get('type')=='error':
						allow_to_update_user=False
				if allow_to_update_user:
					if first_name is not None and first_name!='':
						user_to_change.first_name=first_name
					if last_name is not None and last_name!='':
						user_to_change.last_name=last_name
					if email is not None and email!='':
						user_to_change.email=email
					if username is not None and username!='':
						user_to_change.username=username
					user_to_change.save()
					if first_name=='' and last_name=='' and email=='' and\
							username=='':
						message={
							'type':'info',
							'body':' There Were No Changes To Save.'
							}
					else:
						message={
							'type':'success',
							'body':' User Was Updated Successfully.'
							}
					messages.append(message)
		elif request.POST.get('delete') is not None:
			if not request.user.is_superuser:
				message={
					'type':'error',
					'body':'You Don\'t Have Permission To Change Users Data.'
					}
				messages.append(message)
			else:
				user_to_delete=User.objects.get(id=id)
				user_to_delete.delete()
		elif request.POST.get('Ignore') is not None:
			print('Ignore')
			return redirect('/control_panel/auth/users/')
		else:
			if not request.user.is_superuser:
				message={
					'type':'error',
					'body':'You Don\'t Have Permission To Change Users Data.'
					}
				messages.append(message)
			else:
				user_to_change=User.objects.get(id=id)
				is_active=request.POST.get('is-active') is not None
				is_staff_status=request.POST.get('is-staff-status') is not None
				is_superuser_status=request.POST.get(
					'is-superuser-status') is not None
				if user_to_change.is_active==is_active and\
						user_to_change.is_staff==is_staff_status and\
						user_to_change.is_superuser==is_superuser_status:
					message={
						'type':'info',
						'body':' There Were No Changes To Save.'
						}
					messages.append(message)
				else:
					message={
						'type':'success',
						'body':' User Was Updated Successfully.'
						}
					messages.append(message)
				user_to_change.is_active=is_active
				user_to_change.is_staff=is_staff_status
				user_to_change.is_superuser=is_superuser_status
				user_to_change.save()
	try:
		user_to_change=User.objects.get(id=id)
		return render(request,'control_panel/change-user-data.html',
					  {
						  'user_to_change':user_to_change,
						  'messages':messages,
						  'page_name':'user data'
						  })
	except:
		return redirect('/control_panel/auth/users/')
def create_new_user(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	if request.method=='POST':
		if not request.user.is_superuser:
			message={
				'type':'error',
				'body':'You Don\'t Have Permission To Add New User.'
				}
			messages.append(message)
		else:
			first_name=request.POST.get('first-name')
			last_name=request.POST.get('last-name')
			email=request.POST.get('email')
			username=request.POST.get('username')
			password=request.POST.get('password')
			re_password=request.POST.get('re-password')
			is_active=False
			is_staff_status=False
			is_superuser_status=False
			if request.POST.get('is-active') is not None:
				is_active=True
			if request.POST.get('is-staff-status') is not None:
				is_staff_status=True
			if request.POST.get('is-superuser-status') is not None:
				is_superuser_status=True
			if first_name is None or first_name=='':
				message={'type':'error','body':' First Name Field Is Empty.'}
				messages.append(message)
			if last_name is None or last_name=='':
				message={'type':'error','body':' Last Name Field Is Empty.'}
				messages.append(message)
			if email is None or email=='':
				message={'type':'error','body':' Email Field Is Empty.'}
				messages.append(message)
			else:
				if '@' not in email or '.' not in email:
					message={'type':'error','body':' Email Is Not Valid.'}
					messages.append(message)
				else:
					if User.objects.filter(email=email).exists():
						message={'type':'error','body':' Email Is Used.'}
						messages.append(message)
			if username is None or username=='':
				message={'type':'error','body':' Username Field Is Empty.'}
				messages.append(message)
			else:
				if User.objects.filter(username=username).exists():
					message={'type':'error','body':' Username Is Used.'}
					messages.append(message)
			if password is None or password=='':
				message={'type':'error','body':' Password Field Is Empty.'}
				messages.append(message)
			else:
				if len(password)<8:
					message={'type':'warning','body':' Password Is Weak.'}
					messages.append(message)
			if re_password is None or re_password=='':
				message={
					'type':'error',
					'body':' Repeat Password Field Is Empty, You Have To '
						   'Repeat The Password In This Field.'
					}
				messages.append(message)
			else:
				if re_password!=password:
					message={
						'type':'error',
						'body':' The Two Password Fields Didn’t Match.'
						}
					messages.append(message)
			allow_to_create_user=True
			for message in messages:
				if message.get('type')=='error':
					allow_to_create_user=False
			if allow_to_create_user:
				user=User.objects.create_user(
					first_name=first_name,
					last_name=last_name,
					email=email,
					username=username,
					password=password,
					is_active=is_active,
					is_staff=is_staff_status,
					is_superuser=is_superuser_status,
					)
				user.save()
				message={
					'type':'success',
					'body':' User Was Created Successfully.'
					}
				messages.append(message)
	return render(request,'control_panel/create-new-user.html',
				  {
					  'messages':messages,
					  'page_name':'add user'
					  })
def site_title_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	site_title.objects.control_number()
	site_logo.objects.control_number()
	if request.method=="POST":
		title=request.POST.get('title')
		title_ico=request.FILES.get('title-ico')
		logo_span=request.POST.get('logo_span')
		logo_n_span=request.POST.get('logo_n_span')
		logo=site_logo.objects.get_logo()
		if title:
			site_title.objects.change_title(title)
			message={
				'type':'success',
				'body':' Your Site Title Was Updated'
				}
			messages.append(message)
		if title_ico:
			site_title.objects.change_icon(title_ico)
			message={
				'type':'success',
				'body':' Your Site Title Icon Was Updated'
				}
			messages.append(message)
		if logo_span or logo_n_span:
			site_logo.objects.update_logo(logo_n_span+'|'+logo_span)
			message={
				'type':'success',
				'body':' Your Site Logo Was Updated'
				}
			messages.append(message)
		if len(messages)<1:
			message={
				'type':'info',
				'body':' There Were No Changes To Save.'
				}
			messages.append(message)
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
	return render(request,'control_panel/site-title.html',
				  {
					  'messages':messages,
					  'site_title':site_title.objects.all(),
					  'logo':_logo,
					  'page_name':'site title'
					  })
def slideshow_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	if request.method=='POST':
		if request.POST.get('Add-new-slide') is not None:
			slideshow.objects.create_slide()
		elif request.POST.get('remove-slide') is not None:
			id=request.POST.get('remove-slide')
			slideshow.objects.remove_slide(id)
		elif request.POST.get('save') is not None:
			slide_img=request.FILES.get('slide-img')
			slide_title=request.POST.get('slide-title')
			slide_body_text=request.POST.get('slide-body-text')
			id=request.POST.get('save')
			if slide_img:
				slideshow.objects.change_slide_img(id,slide_img)
				message={
					'type':'success',
					'body':' Slide Image Was Updated'
					}
				messages.append(message)
			if slide_title!='':
				slideshow.objects.change_slide_title(id,slide_title)
				message={
					'type':'success',
					'body':' Slide Title Was Updated'
					}
				messages.append(message)
			if slide_body_text!='':
				slideshow.objects.change_slide_body_text(id,slide_body_text)
				message={'type':'success','body':' Slide Body Text Was Updated'}
				messages.append(message)
			if len(messages)<1:
				message={'type':'info','body':' There Were No Changes To Save.'}
				messages.append(message)
		elif request.POST.get('m-u') is not None:
			id=request.POST.get('m-u')
			slideshow.objects.move_up(id)
		elif request.POST.get('m-d') is not None:
			id=request.POST.get('m-d')
			slideshow.objects.move_down(id)
	slideshow_array=list()
	for slide in slideshow.objects.all():
		slide.slide_body_text={
			'str_list':slide.slide_body_text.split('\n'),
			'str':slide.slide_body_text
			}
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
	return render(request,'control_panel/slideshow.html',
				  {
					  'messages':messages,
					  'slideshow':slideshow_array,
					  'page_name':'slideshow'
					  })
def video_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	if request.method=='POST':
		if request.POST.get('Add-new-video') is not None:
			video.objects.create_video()
		elif request.POST.get('remove-video') is not None:
			id=request.POST.get('remove-video')
			video.objects.remove_video(id)
		elif request.POST.get('save') is not None:
			cover_img=request.FILES.get('cover-img')
			video_title=request.POST.get('video-title')
			video_description=request.POST.get('video-description')
			video_url=request.POST.get('video-url')
			id=request.POST.get('save')
			if cover_img:
				video.objects.change_cover_img(id,cover_img)
				message={
					'type':'success',
					'body':' Video Cover Image Was Updated'
					}
				messages.append(message)
			if video_title!='':
				video.objects.change_video_title(id,video_title)
				message={'type':'success','body':' Video Title Was Updated'}
				messages.append(message)
			if video_description!='':
				video.objects.change_video_description(id,video_description)
				message={
					'type':'success',
					'body':' Video Description Was Updated'
					}
				messages.append(message)
			if video_url!='':
				video.objects.change_video_url(id,video_url)
				message={'type':'success','body':' Video url Was Updated'}
				messages.append(message)
			if len(messages)<1:
				message={'type':'info','body':' There Were No Changes To Save.'}
				messages.append(message)
		elif request.POST.get('m-u') is not None:
			id=request.POST.get('m-u')
			video.objects.move_up(id)
		elif request.POST.get('m-d') is not None:
			id=request.POST.get('m-d')
			video.objects.move_down(id)
		elif request.POST.get('r-l') is not None:
			id=request.POST.get('r-l')
			video.objects.flip(id)
	return render(request,'control_panel/video.html',
				  {
					  'messages':messages,
					  'videos':video.objects.all(),
					  'page_name':'video'
					  })
def our_services_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	if request.method=='POST':
		if request.POST.get('Add-new-service') is not None:
			services.objects.create_service()
		elif request.POST.get('remove-service') is not None:
			id=request.POST.get('remove-service')
			services.objects.remove_service(id)
		elif request.POST.get('save') is not None:
			img=request.FILES.get('service-img')
			title=request.POST.get('service-title')
			description=request.POST.get('service-description')
			id=request.POST.get('save')
			if img:
				services.objects.change_service_img(id,img)
				message={
					'type':'success',
					'body':' Service Image Was Updated'
					}
				messages.append(message)
			if title!='':
				services.objects.change_service_title(id,title)
				message={
					'type':'success',
					'body':' Service Title Was Updated'
					}
				messages.append(message)
			if description!='':
				services.objects.change_service_description(id,description)
				message={
					'type':'success',
					'body':' Service Description Was Updated'
					}
				messages.append(message)
			if len(messages)<1:
				message={
					'type':'info',
					'body':' There Were No Changes To Save.'
					}
				messages.append(message)
		elif request.POST.get('m-u') is not None:
			id=request.POST.get('m-u')
			services.objects.move_up(id)
		elif request.POST.get('m-d') is not None:
			id=request.POST.get('m-d')
			services.objects.move_down(id)
	return render(request,'control_panel/our-services.html',
				  {
					  'messages':messages,
					  'services':services.objects.all(),
					  'page_name':'our services'
					  })
def work_samples_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	if request.method=='POST':
		if request.POST.get('Add-new-work-sample') is not None:
			work_samples.objects.create_work_sample()
		elif request.POST.get('remove-work-sample') is not None:
			id=request.POST.get('remove-work-sample')
			work_samples.objects.remove_work_sample(id)
		elif request.POST.get('save') is not None:
			id=request.POST.get('save')
			img=request.FILES.get('work-sample-img')
			title=request.POST.get('work-sample-title')
			description=request.POST.get('work-sample-description')
			url=request.POST.get('work-sample-url')
			if img:
				work_samples.objects.change_work_sample_img(id,img)
				message={
					'type':'success',
					'body':' Work Sample Image Was Updated'
					}
				messages.append(message)
			if title!='':
				work_samples.objects.change_work_sample_title(id,title)
				message={
					'type':'success',
					'body':' Work Sample Title Was Updated'
					}
				messages.append(message)
			if description!='':
				work_samples.objects.change_work_sample_description(id,
																	description)
				message={
					'type':'success',
					'body':' Work Sample Description Was Updated'
					}
				messages.append(message)
			if url!='':
				work_samples.objects.change_work_sample_url(id,url)
				message={
					'type':'success',
					'body':' Work Sample url Was Updated'
					}
				messages.append(message)
			if len(messages)<1:
				message={
					'type':'info',
					'body':' There Were No Changes To Save.'
					}
				messages.append(message)
	return render(request,'control_panel/work-samples.html',
				  {
					  'messages':messages,
					  'work_samples':work_samples.objects.all(),
					  'page_name':'work samples'
					  })
def work_process_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	if request.method=='POST':
		if request.POST.get('Add-new') is not None:
			work_process.objects.create_process()
		elif request.POST.get('remove') is not None:
			id=request.POST.get('remove')
			work_process.objects.remove(id)
		elif request.POST.get('save') is not None:
			img=request.FILES.get('image')
			title=request.POST.get('title')
			description=request.POST.get('description')
			id=request.POST.get('save')
			if img:
				work_process.objects.change_img(id,img)
				message={
					'type':'success',
					'body':' Service Image Was Updated'
					}
				messages.append(message)
			if title!='':
				work_process.objects.change_title(id,title)
				message={
					'type':'success',
					'body':' Service Title Was Updated'
					}
				messages.append(message)
			if description!='':
				work_process.objects.change_description(id,description)
				message={
					'type':'success',
					'body':' Service Description Was Updated'
					}
				messages.append(message)
			if len(messages)<1:
				message={
					'type':'info',
					'body':' There Were No Changes To Save.'
					}
				messages.append(message)
		elif request.POST.get('m-u') is not None:
			id=request.POST.get('m-u')
			work_process.objects.move_up(id)
		elif request.POST.get('m-d') is not None:
			id=request.POST.get('m-d')
			work_process.objects.move_down(id)
	return render(request,'control_panel/work-process.html',
				  {
					  'messages':messages,
					  'work_process':work_process.objects.all(),
					  'page_name':'work process'
					  })
def our_team_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	if request.method=='POST':
		if request.POST.get('Add-mem') is not None:
			our_team.objects.create_team_member()
		elif request.POST.get('remove-mem') is not None:
			id=request.POST.get('remove-mem')
			our_team.objects.remove_member(id)
		elif request.POST.get('save') is not None:
			id=request.POST.get('save')
			img=request.FILES.get('img')
			title=request.POST.get('title')
			description=request.POST.get('description')
			facebook=request.POST.get('facebook')
			twitter=request.POST.get('twitter')
			instagram=request.POST.get('instagram')
			telegram=request.POST.get('telegram')
			if img:
				our_team.objects.change_team_member_img(id,img)
				message={
					'type':'success',
					'body':' Work Sample Image Was Updated'
					}
				messages.append(message)
			if title!='':
				our_team.objects.change_team_member_title(id,title)
				message={
					'type':'success',
					'body':'  Name Was Updated'
					}
				messages.append(message)
			if description!='':
				our_team.objects.change_team_member_description(id,
																description)
				message={
					'type':'success',
					'body':' Description Was Updated'
					}
				messages.append(message)
			if facebook!='':
				our_team.objects.change_team_member_facebook(id,facebook)
				message={
					'type':'success',
					'body':' facebook Was Updated'
					}
				messages.append(message)
			if twitter!='':
				our_team.objects.change_team_member_twitter(id,twitter)
				message={
					'type':'success',
					'body':' twitter Was Updated'
					}
				messages.append(message)
			if instagram!='':
				our_team.objects.change_team_member_instagram(id,instagram)
				message={
					'type':'success',
					'body':' instagram Was Updated'
					}
				messages.append(message)
			if telegram!='':
				our_team.objects.change_team_member_telegram(id,telegram)
				message={
					'type':'success',
					'body':' telegram Was Updated'
					}
				messages.append(message)
			if len(messages)<1:
				message={
					'type':'info',
					'body':' There Were No Changes To Save.'
					}
				messages.append(message)
	return render(request,'control_panel/our-team.html',{
		'messages':messages,
		'our_team':our_team.objects.all(),
		'page_name':'our team'
		})
def our_customers_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	if request.method=='POST':
		if request.POST.get('Add-customer') is not None:
			our_customers.objects.create_customer()
		elif request.POST.get('remove-customer') is not None:
			id=request.POST.get('remove-customer')
			our_customers.objects.remove_customer(id)
		elif request.POST.get('save') is not None:
			id=request.POST.get('save')
			img=request.FILES.get('img')
			name=request.POST.get('name')
			job=request.POST.get('job')
			description=request.POST.get('description')
			if img:
				our_customers.objects.change_customer_img(id,img)
				message={
					'type':'success',
					'body':' Image Was Updated'
					}
				messages.append(message)
			if name!='':
				our_customers.objects.change_customer_name(id,name)
				message={
					'type':'success',
					'body':'  Name Was Updated'
					}
				messages.append(message)
			if job!='':
				our_customers.objects.change_customer_job(id,job)
				message={
					'type':'success',
					'body':'  Job Was Updated'
					}
				messages.append(message)
			if description!='':
				our_customers.objects.change_customer_description(id,
																  description)
				message={
					'type':'success',
					'body':' Description Was Updated'
					}
				messages.append(message)
			if len(messages)<1:
				message={
					'type':'info',
					'body':' There Were No Changes To Save.'
					}
				messages.append(message)
	return render(request,'control_panel/our-customers.html',
				  {
					  'messages':messages,
					  'our_customers':our_customers.objects.all(),
					  'page_name':'our customers'
					  })
def our_pricing_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	if request.method=='POST':
		if request.POST.get('Add-new') is not None:
			our_pricing.objects.create_pricing()
		elif request.POST.get('remove') is not None:
			id=request.POST.get('remove')
			our_pricing.objects.remove(id)
		elif request.POST.get('save') is not None:
			id=request.POST.get('save')
			img=request.FILES.get('img')
			title=request.POST.get('title')
			price=request.POST.get('price')
			offers=list()
			i=1
			while request.POST.get('offer'+str(i)) is not None:
				offers.append(request.POST.get('offer'+str(i)))
				i+=1
			offers_val=list()
			i=1
			while True:
				if request.POST.get('offer_val'+str(i)) is not None:
					ov={
						'val':request.POST.get('offer_val'+str(i)),
						'index':i
						}
					offers_val.append(ov)
				if request.POST.get('offer_val'+str(i)) is None and i>50:
					break
				i+=1
			for i,offer in enumerate(offers_val):
				if offer['index']!=i+1:
					ov={
						'val':'off',
						'index':i+1
						}
					offers_val.insert(i,ov)
			link=request.POST.get('link')
			if img:
				our_pricing.objects.change_pricing_img(id,img)
				message={
					'type':'success',
					'body':' Image Was Updated'
					}
				messages.append(message)
			if title:
				our_pricing.objects.change_pricing_title(id,title)
				message={
					'type':'success',
					'body':'  Title Was Updated'
					}
				messages.append(message)
			if price:
				our_pricing.objects.change_pricing_price(id,price)
				message={
					'type':'success',
					'body':'  Price Was Updated'
					}
				messages.append(message)
			if offers:
				for i,offer in enumerate(offers):
					if offer!='':
						our_pricing.objects.rename_offer(i,offer)
						message={
							'type':'success',
							'body':' Offer ('+str(i)+') Was Updated To '
													 '<'+offer+'>'
							}
						messages.append(message)
			if link:
				our_pricing.objects.change_pricing_link(id,link)
				message={
					'type':'success',
					'body':' Link Was Updated'
					}
				messages.append(message)
			ov=list()
			for i in range(len(offers_val)):
				if offers_val[i]['val']=='on':
					ov.append('True')
				else:
					ov.append('False')
			our_pricing.objects.update_offer_val(id,ov)
			message={
				'type':'success',
				'body':' Changes Was Saved Successfully.'
				}
			messages.append(message)
			if len(messages)<1:
				message={
					'type':'info',
					'body':' There Were No Changes To Save.'
					}
				messages.append(message)
		elif request.POST.get('Add-offer') is not None:
			our_pricing.objects.add_offer()
		elif request.POST.get('remove-offer') is not None:
			index=request.POST.get('remove-offer')
			our_pricing.objects.remove_offer(index)
		elif request.POST.get('m-u') is not None:
			id=request.POST.get('m-u')
			our_pricing.objects.move_up(id)
		elif request.POST.get('m-d') is not None:
			id=request.POST.get('m-d')
			our_pricing.objects.move_down(id)
	prices=our_pricing.objects.all()
	for i in range(len(prices)):
		offers=list()
		_str=prices[i].offers.split(',')
		for s in _str:
			offer={
				'name':s.split(':')[0],
				'val':s.split(':')[1]
				}
			offers.append(offer)
		prices[i].offers=offers
	return render(request,'control_panel/our-pricing.html',
				  {
					  'messages':messages,
					  'prices':prices,
					  'page_name':'pricing'
					  })
def our_news_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	if request.method=='POST':
		if request.POST.get('Add-new') is not None:
			our_news.objects.create_news()
		elif request.POST.get('remove') is not None:
			id=request.POST.get('remove')
			our_news.objects.remove(id)
		elif request.POST.get('save') is not None:
			id=request.POST.get('save')
			img=request.FILES.get('img')
			name=request.POST.get('name')
			date=request.POST.get('date')
			topic_A=request.POST.get('topic_A')
			topic_B=request.POST.get('topic_B')
			description=request.POST.get('description')
			link=request.POST.get('link')
			if img:
				our_news.objects.change_news_img(id,img)
				message={
					'type':'success',
					'body':' Image Was Updated'
					}
				messages.append(message)
			if name:
				our_news.objects.change_news_name(id,name)
				message={
					'type':'success',
					'body':'  Name Was Updated'
					}
				messages.append(message)
			if date:
				if our_news.objects.change_news_date(id,date):
					message={
						'type':'success',
						'body':'  date Was Updated'
						}
				else:
					message={
						'type':'error',
						'body':'  date Was Not valid'
						}
				messages.append(message)
			if topic_A:
				our_news.objects.change_news_topic_A(id,topic_A)
				message={
					'type':'success',
					'body':'  topic_A Was Updated'
					}
				messages.append(message)
			if topic_B:
				our_news.objects.change_news_topic_B(id,topic_B)
				message={
					'type':'success',
					'body':'  topic_B Was Updated'
					}
				messages.append(message)
			if description:
				our_news.objects.change_news_description(id,description)
				message={
					'type':'success',
					'body':'  description Was Updated'
					}
				messages.append(message)
			if link:
				our_news.objects.change_news_link(id,link)
				message={
					'type':'success',
					'body':' Link Was Updated'
					}
				messages.append(message)
			if len(messages)<1:
				message={
					'type':'info',
					'body':' There Were No Changes To Save.'
					}
				messages.append(message)
		elif request.POST.get('m-u') is not None:
			id=request.POST.get('m-u')
			our_news.objects.move_up(id)
		elif request.POST.get('m-d') is not None:
			id=request.POST.get('m-d')
			our_news.objects.move_down(id)
	return render(request,'control_panel/our-news.html',{
		'messages':messages,
		'news':our_news.objects.all(),
		'page_name':'news'
		})
def footer_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	return render(request,'control_panel/footer.html',{
		'messages':messages,
		'page_name':'footer'
		})
def img_array_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	if request.method=='POST':
		if request.POST.get('Add-new') is not None:
			img_array.objects.create_img()
		elif request.POST.get('remove') is not None:
			id=request.POST.get('remove')
			img_array.objects.remove(id)
		elif request.POST.get('save') is not None:
			id=request.POST.get('save')
			img=request.FILES.get('img')
			if img:
				img_array.objects.change_img(id,img)
				message={
					'type':'success',
					'body':' Image Was Updated'
					}
				messages.append(message)
			if len(messages)<1:
				message={
					'type':'info',
					'body':' There Were No Changes To Save.'
					}
				messages.append(message)
	return render(request,'control_panel/img-array.html',{
		'messages':messages,
		'img_array':img_array.objects.all(),
		'page_name':'img_array'
		})
def themes_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	if request.method=='POST':
		if request.POST.get('active') is not None:
			id=request.POST.get('active')
			site_theme.objects.active_theme(id)
		elif request.POST.get('remove') is not None:
			id=request.POST.get('remove')
			site_theme.objects.remove_theme(id)
		elif request.POST.get('add') is not None:
			color=str(request.POST.get('color_m')).replace('#','')
			color_ba=str(request.POST.get('color_ba')).replace('#','')
			site_theme.objects.create_theme(color,color_ba)
			message={
				'type':'success',
				'body':'  Theme Was Created.'
				}
			messages.append(message)
	default=True
	if len(site_theme.objects.all())!=0:
		for obj in site_theme.objects.all():
			if obj.active:
				default=False
				break
	return render(request,'control_panel/themes.html',{
		'messages':messages,
		'themes':site_theme.objects.all(),
		'default_theme':default,
		'page_name':'themes'
		})
def pe_index_(request):
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	if request.method=='POST':
		if request.POST.get('Add-new-option') is not None:
			main_pages.objects.add_option(1)
		elif request.POST.get('remove-option') is not None:
			index=request.POST.get('remove-option')
			main_pages.objects.remove_option(1,int(index))
		elif request.POST.get('save') is not None:
			id=request.POST.get('save')
			img=request.FILES.get('img')
			if img:
				img_array.objects.change_img(id,img)
				message={
					'type':'success',
					'body':' Image Was Updated'
					}
				messages.append(message)
			if len(messages)<1:
				message={
					'type':'info',
					'body':' There Were No Changes To Save.'
					}
				messages.append(message)
	options=main_pages.objects.get_options(1,True)
	slideshow_array=list()
	for slide in slideshow.objects.all():
		slide.slide_body_text={
			'str_list':slide.slide_body_text.split('\n'),
			'str':slide.slide_body_text
			}
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
	return render(request,'control_panel/pe-index.html',{
		'messages':messages,
		'options':options,
		'slideshow':slideshow_array,
		'page_name':'pe_index'
		})
def pe_about_us_(request):
	if not request.user.is_staff:
		return redirect('/')
	return render(request,'control_panel/pe-about-us.html',
				  {
					  'page_name':'pe_about_us'
					  })
def pe_our_services_(request):
	if not request.user.is_staff:
		return redirect('/')
	return render(request,'control_panel/pe-our-services.html',
				  {
					  'page_name':'pe_our_services'
					  })
def pe_our_pricing_(request):
	if not request.user.is_staff:
		return redirect('/')
	return render(request,'control_panel/pe-our-pricing.html',
				  {
					  'page_name':'pe_our_pricing'
					  })
def pe_our_team_(request):
	if not request.user.is_staff:
		return redirect('/')
	return render(request,'control_panel/pe-our-team.html',
				  {
					  'page_name':'pe_our_team'
					  })
def pe_contact_us_(request):
	if not request.user.is_staff:
		return redirect('/')
	return render(request,'control_panel/pe-contact-us.html',
				  {
					  'page_name':'pe_contact_us'
					  })
def logout(request):
	if not request.user.is_staff:
		return redirect('/')
	if not request.user.is_staff:
		return redirect('/')
	messages=list()
	auth.logout(request)
	return render(request,'control_panel/logout.html',{
		'messages':messages,
		'page_name':'logout'
		})
