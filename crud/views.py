from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from crud import models
from crud import forms
import requests
# Create your views here.
class Test:

    def first_page(self):

        # models.MyModel.objects.all() SELECT * FROM tabel_name
        # models.MyModel.objects.filter(color = 123, speed = 123) SELECT * FROM table_name WHERE color = '123' AND speed = '123'

        cars = models.MyModel.objects.all()

        for car in cars:
            car.tags = car.tags.split(',')

        data = {
            "title": "First Page (READ)",
            "form": forms.MyForm,
            "cars": cars
        }

        # name, surname, skills[array], education[array], socail_networds[array], hashtags[array] 

        return render(self, 'index.html', data)

    # def second_page(self):
    #     return render(self, 'second.html')

    def save_my_model(self):
        if self.method == 'POST':
            color = self.POST.get('color')
            speed = self.POST.get('speed')
            model = self.POST.get('model')
            tags = self.POST.get('tags')
            models.MyModel(color=color, speed=speed, model=model, tags=tags).save()
            return redirect('/')

    def delete_model(request):
        if request.method == 'GET':
            id_delete = request.GET.get('pk')
            car = models.MyModel.objects.get(id=id_delete)
            car.delete()

            # return render(request, 'index.html', id_delete)
            # color = self.POST.get('color')
            # speed = self.POST.get('speed')
            # model = self.POST.get('model')
            # tags = self.POST.get('tags')
            # models.MyModel(color=color, speed=speed, model=model, tags=tags).save()
            return redirect('/')

    def edit_model(request):
        if request.method == 'GET':
            id_update = request.GET.get('pk')
            car = models.MyModel.objects.get(id=id_update)

            str1 = ""  
                
                # traverse in the string   
            for c in car.tags:  
                str1 += c   
            
            # return string   
            car.tags = str1

            data = {                
                "car": car
            }
            return render(request, 'second.html', data)

    def update_model(request):
        if request.method == 'POST':
            id_update = request.POST.get('pk')
            car = models.MyModel.objects.get(id=id_update)
            car.color = request.POST.get('color')
            car.speed = request.POST.get('speed')
            car.model = request.POST.get('model')
            car.tags = request.POST.get('tags')
            car.save()

            return redirect('/')

    def getBooks(request):

        books = models.Book.objects.all()
        data = {            
            "books": books
        }

        return render(request, 'books.html', data)

        # name, surname, skills[array], education[array], socail_networds[array], hashtags[array] 

            
            # color = self.POST.get('color')
            # speed = self.POST.get('speed')
            # model = self.POST.get('model')
            # tags = self.POST.get('tags')
            # models.MyModel(color=color, speed=speed, model=model, tags=tags).save()
           

# def myparser(request, inst_account):
#     instagram_account = requests.get('https://www.instagram.com/'+inst_account+'/?__a=1').json()
#     description = instagram_account['graphql']['user']['biography']
#     account = instagram_account['graphql']['user']['username']
#     followers = instagram_account['graphql']['user']['edge_followed_by']['count']
#     following = instagram_account['graphql']['user']['edge_follow']['count']
#     posts = instagram_account['graphql']['user']['edge_owner_to_timeline_media']['count']

#     output = "<h1>"+account+"</h1> <p>"+description+"</p> <ul><li> Followers: "+str(followers)+"</li><li> Following: "+str(following)+"</li><li> Posts: "+str(posts)+"</li></ul>"
    
#     models.Account(account_username=account, account_description=description, account_followers=followers, account_following=following, account_posts=posts).save()
    
#     return output


# def enter_account(request):
#     if request.method == 'POST':
#         account = request.POST.get('account')
#         out = myparser(request, account)
#         return HttpResponse(out)
