import tweepy

def twitter(post,media_ids):
    # all the keys we need for our twitter bot
    CONSUMER_KEY = 'CONSUMER_KEY'
    CONSUMER_SECRET = 'CONSUMER_SECRET'
    ACCESS_KEY = 'ACCESS_KEY'
    ACCESS_SECRET = 'ACCESS_SECRET'

    # talk to twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)


    media = api.media_upload(filename=media_ids)
    post_result = api.update_status(status=post, media_ids=[media.media_id])

driver