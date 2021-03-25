## 6

REST框架包括用于处理的抽象`ViewSets`，允许开发人员专注于对API的状态和交互进行建模，并根据通用约定将URL构造自动处理。

`ViewSet`类是几乎同样的事情`View`类，但他们提供的操作，例如`retrieve`，或者`update`，而不是方法处理，如`get`或`put`。

当`ViewSet`类被实例化为一组视图时，通常仅在最后一刻才将类绑定到一组方法处理程序，通常是通过使用一个`Router`类来为您定义URL conf的复杂性。

## [重构以使用ViewSet](https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#refactoring-to-use-viewsets)

让我们采用当前的视图集，并将其重构为视图集。

首先，让我们将`UserList`and重构`UserDetail`为一个单一的`UserViewSet`。我们可以删除两个视图，并用一个类替换它们：

```
from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

在这里，我们使用了`ReadOnlyModelViewSet`该类来自动提供默认的“只读”操作。我们仍会像使用常规视图时一样完全设置`queryset`and`serializer_class`属性，但不再需要向两个单独的类提供相同的信息。

接下来我们要更换`SnippetList`，`SnippetDetail`和`SnippetHighlight`视图类。我们可以删除三个视图，然后再次将它们替换为一个类。

```
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
```

这次，我们使用了`ModelViewSet`该类，以获取完整的默认读写操作集。

请注意，我们还使用了`@action`装饰器来创建名为的自定义操作`highlight`。这个装饰可以用来添加不符合标准的任何自定义端点`create`/ `update`/`delete`风格。

默认情况下，使用`@action`装饰器的自定义操作将响应`GET`请求。`methods`如果我们想要一个响应`POST`请求的操作，则可以使用该参数。

默认情况下，自定义操作的URL取决于方法名称本身。如果要更改url的构造方式，则可以将其`url_path`作为修饰符关键字参数包含在内。

## [明确地将ViewSet绑定到URL](https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#binding-viewsets-to-urls-explicitly)

处理程序方法仅在定义URLConf时绑定到操作。为了了解实际情况，首先让我们从ViewSet显式创建一组视图。

在`snippets/urls.py`文件中，我们将`ViewSet`类绑定到一组具体视图中。

```
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
```

注意，我们如何`ViewSet`通过将http方法绑定到每个视图所需的操作来从每个类创建多个视图。

现在，我们已将资源绑定到具体视图中，可以照常向URL conf注册视图。

```
urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
])
```

## [使用路由器](https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#using-routers)

因为我们使用的是`ViewSet`类而不是`View`类，所以实际上我们不需要自己设计URL conf。使用`Router`类可以自动处理将资源连接到视图和url的约定。我们需要做的就是向路由器注册适当的视图集，然后让其余的工作完成。

这是我们重新连接的`snippets/urls.py`文件。

```
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
```

向路由器注册视图集类似于提供urlpattern。我们包含两个参数-视图的URL前缀和视图集本身。

`DefaultRouter`我们正在使用的类还会自动为我们创建API根视图，因此我们现在可以`api_root`从`views`模块中删除该方法。

## [视图与视图集之间的权衡](https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#trade-offs-between-views-vs-viewsets)

使用视图集可能是一个非常有用的抽象。它有助于确保URL约定在您的API之间保持一致，最大程度地减少需要编写的代码量，并允许您专注于API提供的交互和表示形式，而不是URL conf的细节。

这并不意味着它始终是正确的方法。在使用基于类的视图而不是基于函数的视图时，需要考虑一组类似的权衡取舍。与单独构建视图相比，使用视图集不那么明确。