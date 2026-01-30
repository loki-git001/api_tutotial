from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
from rest_framework.reverse import reverse

# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={"base_template": "textarea.html"})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default="python")
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default="friendly")

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get("title", instance.title)
#         instance.code = validated_data.get("code", instance.code)
#         instance.linenos = validated_data.get("linenos", instance.linenos)
#         instance.language = validated_data.get("language", instance.language)
#         instance.style = validated_data.get("style", instance.style)
#         instance.save()
#         return instance


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(
        view_name="snippet-highlight", format="html"
    )

    owner_login = serializers.SerializerMethodField()

    def get_owner_login(self, obj):
        request = self.context.get("request")
        if not request:
            return None
        return reverse("snippet-owner-login", kwargs={"pk": obj.pk}, request=request)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            data.pop("owner_login", None)
        return data

    class Meta:
        model = Snippet
        fields = [
            "url",
            "id",
            "title",
            "code",
            "linenos",
            "language",
            "style",
            "owner",
            "highlight",
            "owner_login",
        ]
        extra_kwargs = {
            "url": {"help_text": "Link to the snippet detail view."},
            "title": {"help_text": "Title of the snippet (optional)."},
            "code": {"help_text": "The actual code content."},
            "linenos": {"help_text": "Show line numbers."},
            "language": {"help_text": "Programming language of the snippet."},
            "style": {"help_text": "Syntax highlighting style."},
            "owner": {"help_text": "Username of the snippet owner (readonly)."},
            "highlight": {"help_text": "Link to the highlighted HTML representation."},
            "owner_login": {"help_text": "Link to login as owner (if not logged in)."},
        }


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all()
    )

    class Meta:
        model = User
        fields = ["url", "id", "username", "snippets"]
        extra_kwargs = {
            "url": {"help_text": "Link to the user detail view."},
            "username": {"help_text": "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."},
            "snippets": {"help_text": "List of snippets owned by this user."},
        }
