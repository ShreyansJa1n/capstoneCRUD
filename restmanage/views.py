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
            return render(request, 'index.html', {"msg": "Record entered successfully", "dish": d})
        elif request.POST['button'] == "See the record" or request.POST['button'] == "See another record":
            idf = request.POST['id']
            d = dish.objects.get(pk=idf)
            v = vegetables.objects.filter(vegedish=idf)
            vegenames = []
            for i in range(len(v)):
                vegenames.append(v[i].vegename)
            return render(request, 'select.html', {"dish": d, "vegetables": vegenames})

        elif request.POST['button'] == "Update the record":
            idf = request.POST['id']
            name = request.POST['name']
            ing = request.POST['ingredients']
            price = int(request.POST['price'])
            calories = request.POST['calories']
            typev = request.POST['type']
            chef = request.POST['Chef']
            vegetable = request.POST.getlist('vegetables')
            try:
                date = request.POST['date']
                print('date', str(date))
            except:
                date = ''
            try:
                img = request.FILES['image']
            except:
                img = ''
            d = dish.objects.get(pk=idf)
            v = vegetables.objects.filter(vegedish=idf).delete()

            if(img != ''):
                if(date != ''):
                    d.name = name
                    d.ing = ing
                    d.price = price
                    d.calories = calories
                    d.chef = chef
                    d.image = img
                    if typev == "Vegetarian":
                        d.typev = True
                    else:
                        d.typev = False
                    d.save()
                else:
                    d.name = name
                    d.ing = ing
                    d.price = price
                    d.calories = calories
                    d.chef = chef
                    d.dateAdded = date
                    d.image = img
                    if typev == "Vegetarian":
                        d.typev = True
                    else:
                        d.typev = False
                    d.save()
            else:
                if(date != ''):
                    d.name = name
                    d.ing = ing
                    d.price = price
                    d.calories = calories
                    d.chef = chef
                    if typev == "Vegetarian":
                        d.typev = True
                    else:
                        d.typev = False
                    d.save()
                else:
                    d.name = name
                    d.ing = ing
                    d.price = price
                    d.calories = calories
                    d.chef = chef
                    d.dateAdded = date
                    if typev == "Vegetarian":
                        d.typev = True
                    else:
                        d.typev = False
                    d.save()
            for i in vegetable:
                v = vegetables.objects.create(vegename=str(i), vegedish=d)
                v.save()

            return render(request, 'index.html', {'msg': 'Updated successfully', 'dish': d})

        elif request.POST['button'] == "See all the records":
            d = dish.objects.all()
            return render(request, 'allrecords.html', {'dish': d})

        # elif request.POST['button'] == "See all the records":
        #     d = dish.objects.all()
        #     return render(request, 'allrecords.html', {'dish': d})


class showrec(View):
    def get(self, request, pk):
        d = dish.objects.get(pk=pk)
        v = vegetables.objects.filter(vegedish=pk)
        vegenames = []
        for i in range(len(v)):
            vegenames.append(v[i].vegename)
        return render(request, 'select.html', {"dish": d, "vegetables": vegenames})
