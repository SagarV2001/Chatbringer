from django.db import models
from django.db.models import Q
class User(models.Model):
    username = models.CharField(max_length=50,primary_key=True)
    email = models.CharField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=50,blank=False)
    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)
    def __str__(self):
        return self.username
    def get_friends(self):
        friendships = Friendship.objects.filter(Q(user1__username=self.username)|Q(user2__username=self.username))
        return [friendship.user1 if friendship.user2.username==self.username else friendship.user2 for friendship in friendships]
    def is_friend(self,selected_username):
        return Friendship.objects.filter(Q(user1__username=self.username,user2__username=selected_username) | Q(user2__username=self.username,user1__username=selected_username)).exists()
    def is_requested(self,selected_username):
        return FriendRequest.objects.filter(Q(from_user=self.username,to_user=selected_username)).exists()
    def get_friend_requests(self):
        return FriendRequest.objects.filter(Q(to_user=self.username))
    def send_friend_request(self,selected_username):
        try:
            selected_user = User.objects.get(username=selected_username)
            if self.is_requested(selected_username):
                print('Already requested.')
            elif self.is_friend(selected_username):
                print('Already Friend.')
            else:
                FriendRequest.objects.create(from_user=self,to_user=selected_user)
                print('Request Sent.')
        except Exception:
            print("Person doesn't exist.")
    def accept_friend_request(self,selected_username):
        try:
            if self.is_friend(selected_username):
                print('Already friend.')
            else:
                selected_user = User.objects.get(username=selected_username)
                Friendship.objects.create(user1=self,user2=selected_user)
                print('Accepted friend.')
            FriendRequest.objects.get(from_user=selected_username, to_user=self.username).delete()
            print('Request deleted after accepting/already friend.')
        except Exception:
            print("Person doesn't exist.")

    def reject_friend_request(self,selected_username):
        try:
            selected_user = User.objects.get(username=selected_username)
            if self.is_friend(selected_username):
                print('Is a Friend.')
            else:
                request_instance = FriendRequest.objects.get(from_user=selected_user, to_user=self)
                request_instance.delete()
                print('Request deleted.')
        except Exception:
            print("Person doesn't exist.")

    def remove_friend(self,selected_username):
        try:
            user2 = User.objects.get(username=selected_username)
            if self.is_friend(selected_username):
                friend_instance = Friendship.objects.get(user1=self,user2=user2)
                friend_instance.delete()
                print('friend deleted')
            else:
                print('Not a friend')
        except Exception:
            print("Person doesn't exist")

class Friendship(models.Model):
    user1 = models.ForeignKey(User, related_name='user1_friendships', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='user2_friendships', on_delete=models.CASCADE)
    def __str__(self):
        return f"Friendship between {self.user1} and {self.user2}"

class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='sent_friend_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_friend_requests', on_delete=models.CASCADE)
    def __str__(self):
        return f"Friend request sent to {self.from_user} to {self.to_user}"

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.sender} to {self.receiver} at {self.timestamp}"

