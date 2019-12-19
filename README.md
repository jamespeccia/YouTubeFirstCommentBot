# YouTubeFirstCommentBot
Leaves first comment on any new YouTube video

### Prerequisites

1. Use Google API Console to create OAuth 2.0 credentials:
   1. Visit the [developer console](https://console.developers.google.com)
   1. Create a new project
   1. Open the [API Manager](https://console.developers.google.com/apis/)
   1. Enable *YouTube Data API v3*
   1. Go to [Credentials](https://console.developers.google.com/apis/credentials)
   1. Configure the OAuth consent screen and create *OAuth client ID* credentials 
   1. Use Application Type *Other* and provide a client name (e.g. *Python*)
   1. Confirm and download the generated credentials as JSON file
1. Store the file in the application folder as *key/client_secrets.json*

In api.py, set the following to match your OAuth2.0 credentials:

  >CLIENT_SECRETS_FILE = "key/client_secrets.json"<br/>
  >CLIENT_ID = "CLIENT_ID_HERE"<br/>
  >CLIENT_SECRET = "CLIENT_SECRET_HERE"<br/>

In run.py, set the channel ID to watch and comment:

  >CHANNEL = "CHANNEL_ID_HERE"<br/>
  >COMMENT_TEXT = "COMMENT_HERE"<br/>
  
## Final Notes
Run minutes before you know someone is supposed to upload or you could surpass your quota for calls for the day.
You could also set a timer to wait x seconds per upload check, although the comment will most likely not be the first.

## Author
James Peccia
