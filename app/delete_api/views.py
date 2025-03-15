from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from .models import Data

class ItemDeleteView(APIView):
     def delete(self, request, item_id):
        try:
          #Retrieve Iten by ID
          item = Data.objects.get(id=item_id)

        except Data.DoesNotExist:

          return Response({"msg": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        #Delete the item from the database 
        item.delete()
        #Return a 284 response
        return Response({"msg": "Delete "})