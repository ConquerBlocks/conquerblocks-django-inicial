from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField('Imagen de perfil', upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField('Biografía', max_length=500, blank=True)
    birth_date = models.DateField('Fecha de nacimiento', null=True, blank=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return self.user.username

    def follow(self, profile):
        follow, created = Follow.objects.get_or_create(follower=self, following=profile)
        return created

    def unfollow(self, profile):
        if Follow.objects.filter(follower=self, following=profile).count():
          Follow.objects.filter(follower=self, following=profile).delete()
          return True
        return False

    def like_post(self, post):
      post.like(self.user)

    def unlike_post(self, post):
      post.unlike(self.user)


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, verbose_name='¿Quien sigue?', on_delete=models.CASCADE, related_name='follower_set')
    following = models.ForeignKey(UserProfile, verbose_name='¿A quien sigue?', on_delete=models.CASCADE, related_name='following_set')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='¿Desde cuando lo sigue?')

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower} follows {self.following}"

    class Meta:
        verbose_name = 'Seguidor'
        verbose_name_plural = 'Seguidores'
