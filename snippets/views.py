from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse 
from django.shortcuts import render

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

# -----------------------#
#   PURE FUNCTION API   #
# -----------------------#

# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser


# @csrf_exempt
# def snippet_list(request):
#     '''List all code snippets, or create a new snippet'''

#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many = True)
#         return JsonResponse(serializer.data, safe = False)
#     elif request.method =='POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status = 400)
#     return HttpResponse(status=400)

# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         raise HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         snippet.delete()
#         return HttpResponse(status=204)
#     return HttpResponse(status=400)


# --------------------------------#
#       FUNCTION API :           #
#   REST FRAMEWORK & DECORATORS  #
# --------------------------------#

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status


# @api_view(["GET", "POST"])
# def snippet_list(request, format=None):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == "GET":
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "PUT", "DELETE"])
# def snippet_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         raise Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# --------------------------------#
#       CLASS BASED API :        #
#   REST FRAMEWORK & APIView     #
# --------------------------------#

# from rest_framework.views import APIView
# from django.http import Http404


# class SnippetList(APIView):
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# class SnippetDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk=pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk=pk)
#         serializer = SnippetSerializer(snippet, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# --------------------------------#
#   GENERIC CLASS BASED API :    #
#   REST FRAMEWORK & APIView     #
# --------------------------------#


from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly


# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

#     permission_classes = [permissions.IsAuthenti edOrReadOnly, IsOwnerOrReadOnly]


# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# # ----------------------#
# #   Hghlighted snippet  #
# # ----------------------#
# from rest_framework import renderers, generics

# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = [renderers.StaticHTMLRenderer]

#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)

# ----------------------#
#   Entry point to API  #
# ----------------------#

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


# @api_view(["GET"])
# def api_root(request, format=None):
#     return Response(
#         {
#             "users": reverse("user-list", request=request, format=format),
#             "snippets": reverse("snippet-list", request=request, format=format),
#         }
#     )



# ----------------------#
#   Implement viewsets  #
# ----------------------#

from rest_framework import viewsets


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary="List all users",
    operation_description="Return a list of all registered users.",
    responses={200: UserSerializer(many=True)}
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_summary="Retrieve a user",
    operation_description="Return key details of a specific user including their snippets.",
    responses={200: UserSerializer, 404: 'Not Found'}
))
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer


from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from .pagination import CustomPagination
from .filters import LanguageFilter
from rest_framework.filters import SearchFilter,   OrderingFilter


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary="List all snippets",
    operation_description="Return a list of all code snippets.",
    responses={200: SnippetSerializer(many=True)}
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_summary="Create a snippet",
    operation_description="Create a new code snippet.",
    responses={201: SnippetSerializer, 400: 'Bad Request'}
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_summary="Retrieve a snippet",
    operation_description="Return the code snippet, language, and style.",
    responses={200: SnippetSerializer, 404: 'Not Found'}
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_summary="Update a snippet",
    operation_description="Replace an existing snippet completely.",
    responses={200: SnippetSerializer, 400: 'Bad Request', 404: 'Not Found'}
))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_summary="Partially update a snippet",
    operation_description="Update one or more fields of an existing snippet.",
    responses={200: SnippetSerializer, 400: 'Bad Request', 404: 'Not Found'}
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_summary="Delete a snippet",
    operation_description="Remove a code snippet.",
    responses={204: 'No Content', 404: 'Not Found'}
))
class SnippetViewSet(viewsets.ModelViewSet):

    
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = CustomPagination
    filterset_class = LanguageFilter
    filter_backends = [SearchFilter,OrderingFilter]
    ordering_fields = ['id', 'title']
    search_fields = ['title', 'code']
    # filterset_fields = ['owner', 'linenos']

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Snippet.objects.filter(owner = self.request.user)
        return Snippet.objects.all()

    @swagger_auto_schema(
        operation_summary="Highlight snippet code",
        operation_description="Return the highlighted HTML representation of the snippet code."
    )
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.cache import never_cache

class OwnerOnlyLoginView(LoginView):

    template_name = "rest_framework/login.html"
    redirect_authenticated_user = False

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        self.snippet = get_object_or_404(Snippet, pk=kwargs["pk"])

        # Already logged in → redirect, do NOT logout
        if request.user.is_authenticated:
            if request.user != self.snippet.owner:
                return HttpResponse(status=status.HTTP_403_FORBIDDEN)
            return redirect(self.get_success_url())

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.get_user()

        # Ownership check BEFORE login
        if user != self.snippet.owner:
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)

        return super().form_valid(form)

    def get_success_url(self):
        return self.snippet.get_absolute_url() # type: ignore
