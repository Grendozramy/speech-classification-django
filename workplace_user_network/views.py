from __future__ import division
from .models import Division, Interaction, WorkplaceUserNetwork
from django.shortcuts import render

# Create your views here.
def index(request):
    workplaceusernetwork_list = WorkplaceUserNetwork.objects.all()
    division_list = Division.objects.all()
    interaction_list = Interaction.objects.all()
    context = {
        'workplace_user_network': workplaceusernetwork_list,
        'division': division_list,
        'interaction': interaction_list
        }

    return render(request, 'workplace_user_network/index.html', context)
