from django.urls import path
from .views import NewsList, PostDetail,NewsSearch, PostCreate,  PostUpdate, PostDelete,ArticleCreate,ArticleDelete,ArticleUpdate 

urlpatterns = [
   path('', NewsList.as_view(), name='news'), 
   path('<int:pk>', PostDetail.as_view(), name='post'),
   path('search', NewsSearch.as_view(), name='news_search'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('article/create/', ArticleCreate.as_view(), name='post_create'),
   path('article/<int:pk>/update/', ArticleUpdate.as_view(), name='post_update'),
   path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='post_delete')
]