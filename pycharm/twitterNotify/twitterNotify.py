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
    "consumer_key"        : "bRZQKVtNMNygCHHqKqwOWy2ul",
    "consumer_secret"     : "3QKm3Xakt45HdLPw2V4YdzB01xtgyTorGhD8C5qtkPH2mH8VgD",
    "access_token"        : "764871355359567876-yr7ZKWVavlrmt1DgSkhZsdN8KOJHYvS",
    "access_token_secret" : "VyOopFvaQeOzyrBawiJowntDCfd2xGRaNk69Pf9pYA7pw"
    }



  api = get_api(cfg)

  tweet = setTweet(url)
  print tweet
  status = api.update_status(status=tweet)
  # Yes, tweet is called 'status' rather confusing


if __name__ == "__main__":

  main()

