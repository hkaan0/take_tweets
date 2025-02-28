import tweepy
import json
from auth import TwitterAuth

# Twitter API kimlik doğrulaması
auth = TwitterAuth()
client = auth.get_client()  # V2 API Client nesnesini al

def fetch_tweets_v2(hashtag, count=10):
    # V2 API ile tweetleri çek
    tweets = client.search_recent_tweets(query=hashtag, max_results=count)
    
    tweet_list = []
    for tweet in tweets.data:
        tweet_data = {
            'tweet_id': tweet.id,
            'created_at': tweet.created_at,
            'text': tweet.text,
            'user': tweet.author_id,
        }
        tweet_list.append(tweet_data)
    
    return tweet_list

def save_to_json(tweet_list, filename):
    # Tweetleri JSON formatında kaydet
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(tweet_list, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    hashtag = "#Python"  # Burada istediğin hashtag'i verebilirsin
    tweet_count = 10  # Çekilecek tweet sayısı

    tweets = fetch_tweets_v2(hashtag, tweet_count)
    save_to_json(tweets, f"{hashtag}_tweets.json")
    print(f"{len(tweets)} tweet başarıyla JSON dosyasına kaydedildi!")
