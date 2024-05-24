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
        try:
            return (self.fetch_and_parse_rss(feed_url),)
        except Exception as e:
            print(f"Error executing ComfyUI_RSS_Feed_Reader: {e}")
            return ("",)

    def fetch_and_parse_rss(self, feed_url):
        feed = feedparser.parse(feed_url)
        if feed.bozo:
            raise ValueError(f"Error parsing feed: {feed.bozo_exception}")

        script_output = "News Update:\n"
        for entry in feed.entries:
            title = entry.title
            description = entry.description
            script_output += f"Title: {title}\nDescription: {description}\n\n"

        return script_output

# Register the node
def register():
    from ComfyUI import node_manager
    node_manager.register_node(ComfyUI_RSS_Feed_Reader)

register()

# Node class mappings and display name mappings
NODE_CLASS_MAPPINGS = {
    "ComfyUI_RSS_Feed_Reader": ComfyUI_RSS_Feed_Reader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUI_RSS_Feed_Reader": "ComfyUI_RSS_Feed_Reader"
}
