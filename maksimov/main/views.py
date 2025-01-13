from django.shortcuts import render
from .hh_pars import get_vacancies
from .pretty_demand import first_table, second_table, third_table, four_table
from .pretty_next import first_table2, second_table2, third_table2, four_table2

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    context = {'first_table': first_table().get_string(),
               'second_table': second_table().get_string(),
               'third_table': third_table().get_string(),
               'four_table': four_table().get_string()
    }
    return render(request, 'main/about.html', context)

def skill(request):
    return render(request, 'main/skills.html')

def hh_p(request):
    vacancies = get_vacancies()
    return render(request, 'main/hh.html', {'vacancies': vacancies})

def geography(request):
    context2 = {'first_table': first_table2().get_string(),
               'second_table': second_table2().get_string(),
               'third_table': third_table2().get_string(),
               'four_table': four_table2().get_string()
               }
    return render(request, 'main/geography.html', context2)
