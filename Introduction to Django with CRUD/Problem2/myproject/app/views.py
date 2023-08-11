from django.shortcuts import render, redirect

data_dict = {}

data_dict = {
    "names": ["John", "Mary"],
    "ages" : [25, 34],
    "cities":["Chandrapur", "Haryana"]
}


# Create your views here.
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')
        
        names = data_dict.get('names', [])
        names.append(name)
        
        ages = data_dict.get('ages', [])
        ages.append(age)
        
        cities = data_dict.get('cities', [])
        cities.append(city)
        
        return redirect('read')
    
    return render(request, 'create.html')

def read(request):
    # Create a list of dictionaries where each dictionary represents an entry
    entries = []
    names = data_dict.get('names', [])
    ages = data_dict.get('ages', [])
    cities = data_dict.get('cities', [])
    
    for i in range(len(names)):
        entry = {
            'name': names[i],
            'age': ages[i],
            'city': cities[i],
        }
        entries.append(entry)
    
    return render(request, 'read.html', {'entries': entries})


def update(request):
    if request.method == 'POST':
        index = int(request.POST.get('index'))
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')
        
        names = data_dict.get('names', [])
        ages = data_dict.get('ages', [])
        cities = data_dict.get('cities', [])
        
        if 0 <= index < len(names):
            names[index] = name
            ages[index] = age
            cities[index] = city
        
        return redirect('read')
    
    return render(request, 'update.html', {'data': data_dict})


def delete(request):
    if request.method == 'POST':
        index = int(request.POST.get('index'))
        
        names = data_dict.get('names', [])
        ages = data_dict.get('ages', [])
        cities = data_dict.get('cities', [])
        
        if 0 <= index < len(names):
            del names[index]
            del ages[index]
            del cities[index]
        
        return redirect('read')
    
    return render(request, 'delete.html', {'data': data_dict})
