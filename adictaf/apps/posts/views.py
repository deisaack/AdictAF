from .models import Post


posts= Post.objects.update_or_create(
    id=obj['media_id'],
    defaults={
        'comments': objcomment_count,
        'likes': like_count,
    }
)