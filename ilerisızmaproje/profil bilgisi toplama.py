import tweepy

# Twitter API anahtarlarını buraya ekle
consumer_key = "JufwEqDvTaGkRRGA4V86zJUPy"
consumer_secret = "5xpbUlNrHH1fdhw5VJLepQq89iXKR40hisatiNrIlfsDLN8liA"
access_token = "1005929869929263105-rTpLdn6iSKk2UwnuiFCqcInJeFnDua"
access_token_secret = "u38lb7rgUXYFgE57pO55kj7LlkSqPXionTr1ImKVMaePw"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAIYWygEAAAAAQKfJMCubQZ%2B2TF804jhKxJky4mw%3DLSnJJPqhSKNAbI1lZIGfgtYu7RHnlXccZd0mMMjYW1YYcupjin"

# API'yi ayarla
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
client = tweepy.Client(bearer_token=bearer_token)


# Bir kullanıcı bilgisi al
user = client.get_user(username="keyvanarasteh")
print(f"Kullanıcı Adı: {user.data.name}")
print(f"Kullanıcı Tanıtımı: {user.data.description}")