
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .search_engine import search_rank

class SearchView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        q=request.GET.get('q','')
        ranked=search_rank(Product.objects.all(),q)
        return Response({'query':q,'results':[{'id':p.id,'product_name':p.product_name,'category':p.category,'relevance_score':s,'rank_reason':r} for s,r,p in ranked[:20]]})
