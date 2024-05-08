import tweepy
import pandas as pd
import time


client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
    wait_on_rate_limit=True,
)



def extract_tweet(row):
    try:
        response = client.get_user(username=row["id"])
        id = response.data.id

        tweets = tweepy.Paginator(client.get_users_tweets,
            id=id,
            tweet_fields=["context_annotations", "id", "created_at", "geo", "text"],
            max_results=100,
        ).flatten(limit=3200)

        # Pulling information from tweets iterable object and adding relevant tweet information in our data frame
        user_tweets = []
        for tweet in tweets:
            user_tweets.append(
                {
                    "Created at": tweet.created_at,
                    "User ID": tweet.id,
                    "Text": tweet.text,
                }
        return user_tweets
    except ValueError:
        pass


def main():
    parser = argparse.ArgumentParser(description='Extract tweets from Twitter user timeline')
    parser.add_argument('file_path', type=str, help='Path to the file containing candidates info')
    args = parser.parse_args()
    cands = pd.read_csv(args.file_path)

    for n, row in cands.iterrows():
        print(f"Extracting tweets for {row["CAND_NAME"]}...")
        df_user_tweets = pd.DataFrame(extract_tweets(row["id"]))
        df_user_tweets.to_csv("./output/" + row["filename"])
        time.sleep(10)


if __name__ == "__main__":
    main()

