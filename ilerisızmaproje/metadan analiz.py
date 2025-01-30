import tweepy

# Twitter API Kimlik Bilgileri
bearer_token = "AAAAAAAAAAAAAAAAAAAAAIYWygEAAAAAQKfJMCubQZ%2B2TF804jhKxJky4mw%3DLSnJJPqhSKNAbI1lZIGfgtYu7RHnlXccZd0mMMjYW1YYcupjin"

# Tweepy Client Bağlantısı
client = tweepy.Client(bearer_token=bearer_token)

# Tweet Metadata'sını Çekme
try:
    # Tweet ID (örnek bir tweet ID'si kullanılıyor)
    tweet_id = "1883470201074897336"
    
    # Tweet Bilgilerini Getir
    tweet = client.get_tweet(
        id=tweet_id, 
        tweet_fields=["created_at", "public_metrics", "source", "geo"]
    )

    # Metadata Bilgilerini Yazdır
    print("Tweet Metadata:")
    print(f"Tweet ID: {tweet.data.id}")
    print(f"Oluşturulma Tarihi: {tweet.data.created_at}")
    print(f"Kullanılan Cihaz: {tweet.data.source}")
    print(f"Beğeni Sayısı: {tweet.data.public_metrics['like_count']}")
    print(f"Retweet Sayısı: {tweet.data.public_metrics['retweet_count']}")
    print(f"Cevap Sayısı: {tweet.data.public_metrics['reply_count']}")
    print(f"Alıntı Sayısı: {tweet.data.public_metrics['quote_count']}")
    print(f"Konum: {tweet.data.geo if tweet.data.geo else 'Yok'}")
    
except tweepy.errors.TweepyException as e:
      print("Sorgu limitine ulaşıldı, 15 dakika bekleniyor...")
    # 15 dakika bekle
    # Daha sonra sorguyu tekrar çalıştırabilirsiniz