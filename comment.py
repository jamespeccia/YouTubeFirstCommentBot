def comment(api, video_id, comment_text):
    try:
        response = api.commentThreads().insert(part="snippet",
                                               body={
                                                   "snippet": {
                                                       "videoId": video_id,
                                                       "topLevelComment": {
                                                           "snippet": {
                                                               "textOriginal": comment_text
                                                           }
                                                       }
                                                   }
                                               }
                                               )
        response.execute()
        return True
    except Exception as e:
        print("An error occurred:")
        print(e)
    return False
