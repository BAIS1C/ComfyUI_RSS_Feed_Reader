import feedparser

class RSSFeedNode:
    """
    RSS Feed Node

    Fetches and parses RSS feeds, producing a script output containing news titles and descriptions.
    """
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("script_output",)
    FUNCTION = "execute"
    CATEGORY = "Data Fetching"

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "feed_url": ("STRING", {
                    "multiline": False, 
                    "dynamicPrompts": False, 
                    "default": "http://example.com/rss"
                }),
            },
        }

    def execute(self, feed_url):
        # Fetch and parse the RSS feed
        return (self.fetch_and_parse_rss(feed_url),)
    
    def fetch_and_parse_rss(self, feed_url):
        # Parse the RSS feed
        feed = feedparser.parse(feed_url)
        
        # Initialize a script output
        script_output = "News Update:\n"
        
        # Loop through the entries in the feed
        for entry in feed.entries:
            title = entry.title
            description = entry.description
            
            # Append each news item to the script
            script_output += f"Title: {title}\nDescription: {description}\n\n"
        
        return script_output

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "RSSFeedNode": RSSFeedNode
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "RSSFeedNode": "RSS Feed Reader"
}
