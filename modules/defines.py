import tweepy

def twitter(post,media_ids):
    # all the keys we need for our twitter bot
    CONSUMER_KEY = 'UlOwhZzALkcTT8fgqw9kg'
    CONSUMER_SECRET = 'AjcxnNzzTxLTQXgXfzcjPhi9lFCCmhKE9SkOFCUBFc'
    ACCESS_KEY = '90204952-5toRkyt7xtZ5kjYTmCN5ttlQCFSCitAIGMMcug38M'
    ACCESS_SECRET = 'feBIelSYE9spdVxLR9H4USMIpGaOXPuNy7MNDlXjEXBtc'

    # talk to twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)


    media = api.media_upload(filename=media_ids)
    post_result = api.update_status(status=post, media_ids=[media.media_id])