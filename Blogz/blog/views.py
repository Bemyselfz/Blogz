from datetime import date
import json
from pprint import pprint

from django.shortcuts import render
from django.core.cache import cache
from django.db.models import Q ,F
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView

from .models import Post, Tag, Category
from config.models import SideBar


# 通用数据查询，如分类导航，侧边栏，底部导航等
class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sidebars':SideBar.get_all(),
        })
        context.update(Category.get_navs())
        return context

# 首页数据查询
class IndexView(CommonViewMixin, ListView):
    queryset = Post.latest_posts()
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'blog/list.html'

# 分类数据查询
class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            'Category':category,
        })

    def get_queryset(self):
        """ 重写queryset,根据分类过滤 """
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)

# 标签数据查询
class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag,pk=tag_id)
        context.update({
            'tag': tag
        })
        return context

    def get_queryset(self):
        """ 重写queryset,根据标签过滤 """
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag+_id')
        return queryset.filter(tag_id=tag_id)

# 首页数据查询
class PostListView(ListView):
    queryset = Post.latest_posts()
    paginate_by = 1
    context_object_name = 'post_list'
    template_name = 'blog/list.html'

# 文章详情页数据查询
class PostDetailView(CommonViewMixin, DetailView):
    queryset = Post.latest_posts()
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

    # get请求处理
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.handle_visited()
        return response

    # 文章的pv,uv处理
    def handle_visited(self):
        increase_pv = False
        increase_uv = False
        uid = self.request.uid
        pv_key = 'pv:%s:%s:' % (uid, self.request.path)
        uv_key = 'uv:%s:%s:%s' % (uid, str(date.today()), self.request.path)
        if not cache.get(pv_key):
            increase_pv = True
            cache.set(pv_key, 1, 1*60)  # 一分钟有效

        if not cache.get(uv_key):
            increase_uv = True
            cache.set(pv_key, 1, 24*60*60)  # 24小时有效

        if increase_pv and increase_uv:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv') + 1, uv=F('uv') + 1)
        elif increase_pv:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv') + 1)
        elif increase_uv:
            Post.objects.filter(pk=self.object.id).update(uv=F('uv') + 1)

# 搜索数据查询
class SearchView(IndexView):
    def get_context_data(self):
        context = super().get_context_data()
        context.update({
            'keyword':self.request.GET.get('keyword', '')
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get('keyword')
        if not keyword:
            return queryset
        return queryset.filter(Q(title__icontains=keyword) | Q(desc__icontains=keyword))

# 作者页数据查询
class AuthorView(IndexView):
    def get_queryset(self):
        queryset = super().get_queryset()
        author_id =self.kwargs.get('owner_id')
        return queryset.filter(owner_id=author_id)