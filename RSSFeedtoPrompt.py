import feedparser
from comfyui.core.node import Node, Input, Output

class RSSFeedNode(Node):
    """
    RSS Feed Node for Comfy UI

    Fetches and parses RSS feeds, producing a script output containing news titles and descriptions.
    """
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

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("script_output",)
    FUNCTION = "execute"
    CATEGORY = "Data Fetching"

    def __init__(self):
        super().__init__()
        print("RSSFeedNode initialized")

    def execute(self, feed_url):
        try:
            print(f"Executing with feed_url: {feed_url}")
            result = self.fetch_and_parse_rss(feed_url)
            return (result,)
        except Exception as e:
            print(f"Error executing RSSFeedNode: {e}")
            return ("",)

    def fetch_and_parse_rss(self, feed_url):
        print(f"Fetching and parsing RSS feed from: {feed_url}")
        feed = feedparser.parse(feed_url)
        if feed.bozo:
            raise ValueError(f"Error parsing feed: {feed.bozo_exception}")

        prompts = []
        for entry in feed.entries:
            prompt = f"Imagine a scene where {entry.title} happens. {entry.summary}"
            prompts.append(prompt)

        return "\n".join(prompts)

def register():
    print("Registering RSSFeedNode")
    node = RSSFeedNode()
    ComfyUI.register_node(node)

NODE_CLASS_MAPPINGS = {
    "RSSFeedNode": RSSFeedNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RSSFeedNode": "RSS Feed to Prompt"
}
