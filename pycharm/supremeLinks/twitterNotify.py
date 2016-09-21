import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

url = ''

#ulr is a str
def setTweet(url):
  return url

# url = setTweet('test')
# print url

def main():
  # Fill in the values noted in previous step here
  cfg = {
    "consumer_key"        : "MP7JLFytogwkk8L7MqS1Lwajw",
    "consumer_secret"     : "6uAj4y7UUjjSVE0PwZ4HSsKPYQwSux0xhAV8RouSE8x9GteqOc",
    "access_token"        : "345817124-r3qWVN0wF574Y9CniR1PodIBPTv6Hj3kD17h71mp",
    "access_token_secret" : "4WBy3uHUjW7gFxl61sxXe1m66cMCLrEpTYDc1radxwvGr"
    }



  api = get_api(cfg)

  tweet = setTweet(url)
  print tweet
  status = api.update_status(status=tweet)
  # Yes, tweet is called 'status' rather confusing


if __name__ == "__main__":

  main()

