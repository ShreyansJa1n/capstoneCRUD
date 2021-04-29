from django.shortcuts import render
from django.views import View
from .models import dish, vegetables
# Create your views here.


class HomePage(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        if request.POST['button'] == "Add the record":
            name = request.POST['name']
            ing = request.POST['ingredients']
            price = int(request.POST['price'])
            calories = request.POST['calories']
            typev = request.POST['type']
            chef = request.POST['Chef']
            vegetable = request.POST.getlist('vegetables')
            date = request.POST['date']
            img = request.FILES['image']
            print(vegetable)
            if typev == "Vegetarian":
                typevbool = True
            else:
                typevbool = False

            d = dish.objects.create(name=name, ing=ing, price=price,
                                    calories=calories, typev=typevbool, chef=chef, dateAdded=date, image=img)
            d.save()
            for i in vegetable:
                v = vegetables.objects.create(vegename=str(i), vegedish=d)
                v.save()

            print(name, ing, price, calories, typev,
                  chef, vegetables, date, img)
            return render(request, 'index.html')
        elif request.POST['button'] == "See the record":
            idf = request.POST['id']
            d = dish.objects.get(pk=idf)
            v = vegetables.objects.filter(vegedish=idf)
            vegenames = []
            for i in range(len(v)):
                vegenames.append(v[i].vegename)
            return render(request, 'select.html', {"dish": d, "vegetables": vegenames})
