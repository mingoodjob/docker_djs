from rest_framework import serializers
from post.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'content', 'exposure', 'image', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
        # extra_kwargs = {
        #     'image': {'write_only': True}
        # }

    def create(self, validated_data):
        post = Post(**validated_data)
        post.save()
        return post

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.exposure = validated_data.get('exposure', instance.exposure)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance
