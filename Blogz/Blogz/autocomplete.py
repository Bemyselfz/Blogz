from dal import autocomplete

from blog.models import Category, Tag


# 分类自动补全
class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated(): # 判断用户是否登陆，如果未登录，返回空queryset
            return Category.objects.none()

        qs = Category.objects.filter(owner=self.request.user)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs

# 标签自动补全
# class TagAutocomplete(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         if not self.request.user.is_authenticated():
#             return Tag.objects.none()
#
#         qs = Tag.objects.filter(owner=self.request.user)
#
#         if self.q:
#             qs = qs.filter(name__istartswith=self.q)
#         return qs