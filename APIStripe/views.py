from django.shortcuts import render

def buy(request, id): 

    return render(request, 'main/form.html', {
            'title':'Registration'
        })

def item(request, id): 

    item = None

    return render(request, 'APIStripe/item.html', {
            'title':'Item with id: ' + str(id),
            'item' : item
        })
