import feedparser

class RSSFeedNode:
    """
    RSS Feed Node for Comfy UI

    Fetches and parses RSS feeds, producing a script output containing news titles and descriptions.
    """
    # Defining input types according to Comfy UI requirements
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

    # Output types as per Comfy UI's requirements
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("script_output",)

    # Specifying the function to call as an entry point
    FUNCTION = "execute"
    CATEGORY = "Data Fetching"

    def __init__(self):
        super().__init__()

    def execute(self, feed_url):
        # Implementation of the RSS feed fetching and parsing
        return (self.fetch_and_parse_rss(feed_url),)
    
    def fetch_and_parse_rss(self, feed_url):
        # Parsing the RSS feed using feedparser
        feed = feedparser.parse(feed_url)
        
        # Formatting the output as a script
        script_output = "News Update:\n"
        for entry in feed.entries:
            title = entry.title
            description = entry.description
            script_output += f"Title: {title}\nDescription: {description}\n\n"
        
        return script_output

# Registration for the node, make sure this matches how other nodes are registered
NODE_CLASS_MAPPINGS = {
    "RSSFeedNode": RSSFeedNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RSSFeedNode": "RSS Feed Reader"
}
