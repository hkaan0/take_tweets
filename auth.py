import tweepy

class TwitterAuth:
    def __init__(self):
        # API anahtarları ve access token'ları burada tanımla
        self.api_key = "4dIlCc04bBu3aKxNCqMM3NYEZ"
        self.api_secret_key = "1K50xReuPWSsMgDQZWI3ibmC3AEwxBcgBE7ktEOcLAnhj0wfiO"
        self.access_token = "914888095002218496-9KW7pVxxsGBxTASCCuCPwXuMLfPPZsv"
        self.access_token_secret = "RgYFvLkBhSoJypNXl2mtj8Z1xUhwSFxPwrMNBaZFlvkUd"
        
        # Bearer Token'ı burada tanımla
        self.bearer_token = "AAAAAAAAAAAAAAAAAAAAAEqDzgEAAAAAAi7i%2BvWmx9inrBfWWpLgc1Z6mMg%3DpW1srJQKmmZX5OQyclD9OH0HqwsQUL9VT1vtkXI1AMTIZia0lx"  # Buraya kendi bearer token'ını ekle
        
        # Kimlik doğrulama işlemi için OAuth1Handler kullan
        self.auth = tweepy.OAuthHandler(self.api_key, self.api_secret_key)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        
        # Tweepy API nesnesi oluştur
        self.api = tweepy.API(self.auth)
        
    def get_api(self):
        return self.api
    
    def get_client(self):
        # V2 API için Client nesnesi oluştur
        client = tweepy.Client(bearer_token=self.bearer_token)
        return client
    
    def verify_auth(self):
        try:
            # Kimlik doğrulamanın doğru olup olmadığını kontrol et
            self.api.verify_credentials()
            print("Kimlik doğrulama başarılı!")
        except tweepy.TweepError as e:
            print(f"Kimlik doğrulama hatası: {e}")


if __name__ == "__main__":
    twitter_auth = TwitterAuth()
    twitter_auth.verify_auth()