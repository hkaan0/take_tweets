import tweepy
#authentication structure using OOP
class TwitterAuth:
    def __init__(self):
        #api and acces keys to reach twitter datas
        self.api_key = "YOUR API KEY"
        self.api_secret_key = "YOUR API SECRET KEY"
        self.access_token = "YOUR ACCESS TOKEN"
        self.access_token_secret = "YOUR ACCES TOKEN SECRET"
        self.bearer_token = "YOUR BEARER TOKEN"  
        
        #using OuthHandler function to validate your identification
        self.auth = tweepy.OAuthHandler(self.api_key, self.api_secret_key)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        
        # Tweepy object
        self.api = tweepy.API(self.auth)
    #get functions    
    def get_api(self):
        return self.api
    
    def get_client(self):
        # client object for Twitter V2 API
        client = tweepy.Client(bearer_token=self.bearer_token)
        return client
    
    
    # Control of authentication successfull or unsuccessfull
    def verify_auth(self):
        try:
            self.api.verify_credentials()
            print(" Successfull! ")
        except tweepy.TweepError as e:
            print(f"Unsuccessfull: {e}")

#To shown our verify_auth function we need to make if main structure
if __name__ == "__main__":
    twitter_auth = TwitterAuth()
    twitter_auth.verify_auth()


# I used OOP structure in this code because to make it reachable from another python file