import tweepy
import json
from auth import TwitterAuth

# Twitter API authentication
auth = TwitterAuth()
client = auth.get_client()  # take Twitter API V2 object

def fetch_tweets_v2(hashtag, count=10):
    # fetching tweets with V2 API
    tweets = client.search_recent_tweets(query=hashtag, max_results=count)
    
    tweet_list = []
    for tweet in tweets.data:
        # will be saved as JSON with this format
        tweet_data = {
            'tweet_id': tweet.id,
            'created_at': tweet.created_at,
            'text': tweet.text,
            'user': tweet.author_id,
        }
        tweet_list.append(tweet_data)
    
    return tweet_list

def save_to_json(tweet_list, filename):
    # save tweets as JSON file
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(tweet_list, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    hashtag = "#Python"  # Tweets will fetching as a hashtag
    tweet_count = 10  # How many twetts will you fetch?

    tweets = fetch_tweets_v2(hashtag, tweet_count)
    save_to_json(tweets, f"{hashtag}_tweets.json")
    print(f"{len(tweets)} successfully saved to JSON file.")
