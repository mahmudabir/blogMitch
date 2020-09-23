from django import forms

from blog.models import *


class CreateBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "body", "image"]

        # This is also the way we can set html attributes from here and then just call the {{form}} from templates
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "name": "title",
                    "id": "id_title",
                }
            ),
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "name": "body",
                    "id": "id_body",
                }
            ),
        }


class UpdateBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "body", "image"]

    def save(self, commit=True):
        blog_post = self.instance
        blog_post.title = self.cleaned_data['title']
        blog_post.body = self.cleaned_data['body']

        if self.cleaned_data['image']:
            blog_post.image = self.cleaned_data['image']

        if commit:
            blog_post.save()
        return blog_post