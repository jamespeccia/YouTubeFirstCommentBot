import time

from api import YouTube
from comment import comment

CHANNEL = "CHANNEL_ID_HERE"
COMMENT_TEXT = "COMMENT_HERE"


def main():
    print("Starting...")
    youtube = YouTube()

    channel = youtube.get_channel(CHANNEL)

    print("Waiting for new videos...")
    start_time = time.asctime()

    while True:
        upload = youtube.get_latest_upload(channel, start_time)
        if upload:
            try:
                url = 'https://youtube.com/watch?v={}'.format(upload['id'])
                print("{} | {} uploaded a new video titled \"{}\"".format(time.asctime(), upload['channel_title'],
                                                                          upload['title'], url))
                if comment(youtube.api, upload['id'], COMMENT_TEXT):
                    print("{} | \"{}\" was commented on {}'s new video \"{}\"".format(time.asctime(), COMMENT_TEXT,
                                                                                      upload['channel_title'],
                                                                                      upload['title']))
                start_time = time.time()

            except Exception as e:
                # If it reaches the 100 seconds api threshold, wait for 100 seconds
                print("Error: Too many requests:\n{}".format(e))
                print("Waiting 100 seconds..")
                time.sleep(100)


if __name__ == '__main__':
    main()
