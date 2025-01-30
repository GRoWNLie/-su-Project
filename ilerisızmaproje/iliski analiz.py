import tweepy

# Twitter API Ayarları

consumer_key = "JufwEqDvTaGkRRGA4V86zJUPy"
consumer_secret = "5xpbUlNrHH1fdhw5VJLepQq89iXKR40hisatiNrIlfsDLN8liA"
access_token = "1005929869929263105-rTpLdn6iSKk2UwnuiFCqcInJeFnDua"
access_token_secret = "u38lb7rgUXYFgE57pO55kj7LlkSqPXionTr1ImKVMaePw"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAIYWygEAAAAAQKfJMCubQZ%2B2TF804jhKxJky4mw%3DLSnJJPqhSKNAbI1lZIGfgtYu7RHnlXccZd0mMMjYW1YYcupjin"

client = tweepy.Client(bearer_token=bearer_token)
# Kullanıcı Bilgisi Alma
try:
    user = client.get_user(username="elonmusk")
    followers = client.get_users_followers(user.data.id, max_results=10)

    for follower in followers.data:
        print(f"Takipçi: {follower.username}")
except tweepy.errors.TooManyRequests as e:
    print("Sorgu limitine ulaşıldı, 15 dakika bekleniyor...")
except tweepy.errors.Forbidden as e:
    print("Yetkilendirme hatası: Projenizle doğru anahtarları kullandığınızdan emin olun.")