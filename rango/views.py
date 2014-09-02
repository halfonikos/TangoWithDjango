from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse 
from models import Category, Page
from forms import CategoryForm
from django.http.response import HttpResponseRedirect
from rango.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login

def index(request):
    context = RequestContext(request)
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': page_list} 
    
    for category in category_list:
        category.url = category.name.replace(' ','_')
    
    return render_to_response('rango/index.html',context_dict,context)

def add_category(request):
    context = RequestContext(request)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            url = reverse(index)
            return HttpResponseRedirect(url)
        else:
            print form.errors
        
    else:
        form=CategoryForm()
    
    return render_to_response('rango/add_category.html',{'form': form}, context)
    
def category(request, category_name_url):
    context = RequestContext(request)
    
    category_name = category_name_url.replace('_',' ')
    
    context_dict = {'category_name': category_name}
    
    try:
        category = Category.objects.get(name=category_name)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    
    return render_to_response('rango/category.html',context_dict, context)
def about(request):
    return render_to_response('rango/about.html')

def register(request):
    context = RequestContext(request)
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            #if 'picture' in request.FILES:
            #    profile.picture = request.FILES['picture']
            #
            #profile.save()
            
            registered = True
            
        else:
            print user_form.errors, profile_form.errors
        
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render_to_response(
        'rango/register.html',
        {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
        context)

def user_login(request):
    print "hello"
    context = RequestContext(request)
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user:
            
            if user.is_active:
                
                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                return HttpResponse("Your account is disabled")
            
        else:
            print "invalid login details: {0} {1}".format(username, password)
    else:
        print "hello"
        return render_to_response('rango/login.html',{},context)
              # render_to_response('rango/category.html',context_dict, context)