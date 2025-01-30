from api.models import CategoryResource, CourseRecourse
from tastypie.api import Api
from django.urls import path, include


# api/v1/categories
# api/v1/courses

api = Api(api_name='v1')
api.register(CategoryResource())
api.register(CourseRecourse())

urlpatterns = [
    path('', include(api.urls), name='index')
]
