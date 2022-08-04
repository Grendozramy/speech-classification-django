from django.http import HttpResponseRedirect
from .models import Department, Division, Interaction, User, WorkplaceUserNetwork
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create your views here.
def index(request):
    workplaceusernetwork_list = WorkplaceUserNetwork.objects.all()
    division_list = Division.objects.all()
    interaction_list = Interaction.objects.all()
    context = {
        'workplace_network': workplaceusernetwork_list,
        'divisions': division_list,
        'interactions': interaction_list
        }

    return render(request, 'workplace_user_network/index.html', context)

def create(request):
    workplaceusernetwork_list = WorkplaceUserNetwork.objects.all()
    user_list = User.objects.all()
    division_list = Division.objects.all()
    interaction_list = Interaction.objects.all()
    department_list = Department.objects.all()
    context = {
        'workplace_network': workplaceusernetwork_list,
        'users': user_list,
        'divisions': division_list,
        'interactions': interaction_list,
        'departments': department_list,
        }
    return render(request, 'workplace_user_network/workplace_network/create.html', context)

def store(request):
    workplacenetwork = WorkplaceUserNetwork.objects.create(
        from_user_id = request.POST['from_user_id'],
        to_user_id  = request.POST['to_user_id'],
        posting_division_id  = request.POST['posting_division_id'],
        comment_division_id  = request.POST['comment_division_id'],
        interaction_id  = request.POST['interaction_id'],
        posting_department_id  = request.POST['posting_department_id'],
        comment_department_id = request.POST['comment_department_id'],
        amount = request.POST['amount'])
    workplacenetwork.save()

    return HttpResponseRedirect(reverse('workplace_user_network:index'))

def detail(request, id):
    workplaceusernetwork_list = get_object_or_404(WorkplaceUserNetwork, id=id)
    user_list = User.objects.all()
    division_list = Division.objects.all()
    interaction_list = Interaction.objects.all()
    department_list = Department.objects.all()
    context = {
        'workplace_network': workplaceusernetwork_list,
        'users': user_list,
        'divisions': division_list,
        'interactions': interaction_list,
        'departments': department_list,
    }
    
    return render(request, 'workplace_user_network/workplace_network/detail.html', context)

def edit(request, id):
    workplaceusernetwork_list = get_object_or_404(WorkplaceUserNetwork, id=id)
    user_list = User.objects.all()
    division_list = Division.objects.all()
    interaction_list = Interaction.objects.all()
    department_list = Department.objects.all()
    context = {
        'workplace_network': workplaceusernetwork_list,
        'users': user_list,
        'divisions': division_list,
        'interactions': interaction_list,
        'departments': department_list,
    }
    
    return render(request, 'workplace_user_network/workplace_network/edit.html', context)


def update(request, id):
    workplaceusernetwork_list = get_object_or_404(WorkplaceUserNetwork, id=id)
    workplaceusernetwork_list.from_user_id = User.objects.get(id=request.POST['from_user_id'])
    workplaceusernetwork_list.to_user_id = User.objects.get(id=request.POST['to_user_id'])
    workplaceusernetwork_list.posting_division_id = Division.objects.get(id=request.POST['posting_division_id'])
    workplaceusernetwork_list.posting_department_id = Department.objects.get(id=request.POST['comment_division_id'])
    workplaceusernetwork_list.comment_division_id = Division.objects.get(id=request.POST['posting_department_id'])
    workplaceusernetwork_list.comment_department_id = Department.objects.get(id=request.POST['comment_department_id'])
    workplaceusernetwork_list.interaction_id  = Interaction.objects.get(id=request.POST['interaction_id'])
    workplaceusernetwork_list.amount = request.POST['amount']
    workplaceusernetwork_list.save()

    return HttpResponseRedirect(reverse('workplace_user_network:index'))

def delete(request, id):
    message = get_object_or_404(WorkplaceUserNetwork, id=id)
    message.delete()
    
    return HttpResponseRedirect(reverse('workplace_user_network:index'))
