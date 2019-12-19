import dateutil.parser
import httplib2
from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow


def new_channel(response):
    for channel in response['items']:
        result = dict()
        result['id'] = channel['id']
        result['username'] = channel['snippet']['title']
        return result
    return None


class YouTube:
    CLIENT_SECRETS_FILE = "key/client_secrets.json"
    CLIENT_ID = "CLIENT_ID_HERE"
    CLIENT_SECRET = "CLIENT_SECRET_HERE"
    YOUTUBE_READONLY_SCOPE = 'https://www.googleapis.com/auth/youtube.force-ssl'
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    def __init__(self):
        flow = OAuth2WebServerFlow(client_id=self.CLIENT_ID,
                                   client_secret=self.CLIENT_SECRET,
                                   scope=self.YOUTUBE_READONLY_SCOPE)

        storage = Storage("keys/oauth2.json")
        self.credentials = storage.get()

        if self.credentials is None or self.credentials.invalid:
            flags = argparser.parse_args()
            self.credentials = run_flow(flow, storage, flags)

        self.api = build(self.YOUTUBE_API_SERVICE_NAME, self.YOUTUBE_API_VERSION,
                         http=self.credentials.authorize(httplib2.Http()))

    def get_channel(self, id):
        response = self.api.channels().list(
            id=id,
            part="snippet",
            fields='items(id,snippet(title))'
        ).execute()
        return new_channel(response)

    def get_latest_upload(self, channel, start_time):
        channels = self.api.channels().list(
            id=channel['id'],
            part="contentDetails,snippet",
            fields="items(id,contentDetails(relatedPlaylists(uploads)),snippet(title))"
        )

        channels = channels.execute()

        uploads_list_id = channels["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

        latest_upload = self.api.playlistItems().list(
            playlistId=uploads_list_id,
            part="snippet",
            fields='items(id,snippet(title,publishedAt,resourceId(videoId)))',
            maxResults=1
        )

        latest_upload = latest_upload.execute()
        try:
            latest_upload = latest_upload["items"][0]
        except:
            return None

        time_published = dateutil.parser.parse(latest_upload['snippet']['publishedAt']).timestamp()

        if time_published >= start_time:
            video = dict()
            video['id'] = latest_upload["snippet"]["resourceId"]["videoId"]
            video['time_published'] = latest_upload["snippet"]["publishedAt"]
            video['title'] = latest_upload["snippet"]["title"]
            video['channel_title'] = channels["items"][0]["snippet"]["title"]
            return video
        else:
            return None
