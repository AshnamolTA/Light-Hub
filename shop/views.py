from django.shortcuts import render,redirect,get_object_or_404

# from django.forms import BaseModelForm

# from django.http import HttpResponse

from django.urls import reverse_lazy

from django.views.generic import View,FormView,TemplateView,DetailView

from django.contrib.auth import authenticate,login,logout

from shop.forms import SignUpForm,SignInForm,UserProfileForm


from shop import views

from shop.models import Light,UserProfile,Category,WishListItem,Shape


class SignUpView(View):

    template_name="signup.html"

    form_class=SignUpForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=self.form_class(request.POST)

        if form_instance.is_valid():

            form_instance.save()

            print("Account Created")

            return redirect("signin")
        
        else:

            print("Failed To Create Account")
            
            
            return render(request,"login.html",{"form":form_instance})

        

class SignInView(FormView):

    template_name="login.html"

    form_class=SignInForm

    def post(self,request,*args,**kwargs):
        
        form_instance=self.form_class(request.POST)

        if form_instance.is_valid():

            uname=form_instance.cleaned_data.get("username")

            pwd=form_instance.cleaned_data.get("password")

            user_object=authenticate(username=uname,password=pwd)

            if user_object:

                login(request,user_object)

                return redirect("index")
            
        return render(request,self.template_name,{"form":form_instance})
    
class LogoutView(View):

    def get(self,request,*arga,**kwargs):
         
         logout(request)

         return redirect("signin")
    


class UserProfileEditView(View):

    template_name="profile_edit.html"

    form_class=UserProfileForm

    def get(self,request,*args,**kwargs):

        user_profile_instance=request.user.profile

        form_instance=self.form_class(instance=user_profile_instance)

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        user_profile_instance=request.user.profile

        form_instance=self.form_class(request.POST,instance=user_profile_instance,files=request.FILES)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("index")

        return render(request,self.template_name,{"form":form_instance})
    
        
class IndexView(TemplateView):

    template_name="index.html"

    def get(self,request,*args,**kwargs):

        qs=Category.objects.all()

        return render(request,self.template_name,{"data":qs})



class CategoryDetailView(TemplateView):

    template_name="category_light.html"

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Category.objects.get(id=id)

        return render(request,self.template_name,{"category":qs})
    

            


class LightListView(TemplateView):

    template_name="light.html"

    def get(self,request,*args,**kwargs):

        qs=Light.objects.all()

        return render(request,self.template_name,{"light":qs})
    
class LightDetailView(View):

    template_name="light_detail.html"

    def get(self,request,*args,**kwargs):
        

        id=kwargs.get("pk")

        
        qs=Light.objects.get(id=id)

        return render(request,self.template_name,{"data":qs})
    





class AddToWishlistItemView(View):

    def Post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        light_object=get_object_or_404(Light,id=id)

        # shape_name=request.POST.get("name")
        # shape_obj=Shape.objects.get(name=shape_name)

        
        

        request.user.basket.basket_item.create(light_object=light_object)

        print("item add to wishlist")

        return redirect("light_detail")
            






    

        
    

