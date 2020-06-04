from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from xadmin.layout import Row, Fieldset, Container
from xadmin.filters import manager
from xadmin.filters import RelatedFieldListFilter
import xadmin

from .models import Post, Category, Tag
from .adminforms import PostAdminForm
from Blogz.base_admin import BaseOwnerAdmin


class PostInline:  # StackedInline
    form_layout = (
        Container(
            Row("title", "desc"),
        )
    )
    extra = 1
    model = Post

@xadmin.sites.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    # inlines = [PostInline, ]
    list_display = ('name', 'status', 'is_nav', 'created_time','post_count')
    fields = ('name', 'status', 'is_nav')

    def post_count(self, obj):
       return obj.post_set.count()

    post_count.short_description = '文章数量'


@xadmin.sites.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')

class CategoryOwnerFilter(RelatedFieldListFilter):
    """自定义过滤器只展示当前用户分类"""
    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        return field.name == 'category'

    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        # 重新获取lookup_choices,根据owner过滤
        self.lookup_choices = Category.objects.filter(owner=request.user).values_list('id', 'name')

# 注册过滤器
manager.register(CategoryOwnerFilter, take_priority=True)


@xadmin.sites.register(Post)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    # 展示字段
    list_display = [
        'title', 'category', 'status',
        'created_time', 'operator',
    ]
    list_display_links = []

    # 过滤器
    list_filter = ['category']
    #list_filter = [CategoryOwnerFilter]

    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = True


    from_layout = (
        Fieldset(
            '基础信息',
            Row("title", "category"),
            "status",
            "tag",
        ),
        Fieldset(
            '内容信息',
            'desc',
            'content',
        )
    )
    #filter_horizontal = ('tag', )
    filter_vertical = ('tag',)

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('xadmin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'


