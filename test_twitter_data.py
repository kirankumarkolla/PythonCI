import twitter_data

class test_twitter_data:
    def test_get_tweets(self):
        assert "Success" == twitter_data.get_tweets('Balck lives matter','D:\\Python\\output',10)
        