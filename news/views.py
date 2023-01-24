from django.shortcuts import render
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializers import PostSerializer


class PostPagination(PageNumberPagination):
    """
    Pagination class.
    
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000



class PostListView(generics.ListAPIView):
    """
    Lists of posts
    
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['published']

    # Filter by name (DRF basic)
    # filterset_fields = ['name']   

    def get_queryset(self):
        """
        Function: filter by name with query
    
        """
        query = super().get_queryset()

        name = self.request.GET.get("name")

        if name:
            query = query.filter(name__icontains=name)

        
        return query
    

class PostCreateView(APIView):
    """
    Create new post.

    """

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostUpdateDelete(APIView):
    """
    Retrieve, Update or Delete a post instance.
    """
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post_id = self.get_object(pk)
        serializer = PostSerializer(post_id)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post_id = self.get_object(pk)
        serializer = PostSerializer(post_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
