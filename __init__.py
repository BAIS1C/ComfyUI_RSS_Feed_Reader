from .RSSFeedtoPrompt import register

def initialize():
    node_classes = register()
    for node_name, node_class in node_classes.items():
        globals()[node_name] = node_class

initialize()

