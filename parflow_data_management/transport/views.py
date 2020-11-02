from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from parflow_data_management.transport.tasks import generate_key_and_passphrase
from .models.key_pair import KeyPair

def keygen_view(request):
    return render(request, "basicbutton.html")


@api_view(['POST'])
def start_keygen(request):
    # Create an empty row to be populated by the
    # generate_key_and_passphrase function
    key_pair = KeyPair.objects.create()

    # Pass in the ID so we can populate the row
    generate_key_and_passphrase.delay(request.user.id, key_pair.id)

    # Propogate the ID to the user
    return Response(data=str(key_pair.id))