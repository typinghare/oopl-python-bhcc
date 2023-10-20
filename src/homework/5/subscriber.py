class Subscriber:
    """Base subscriber class."""

    def breaking_news(self, news_category: str, news_title: str):
        """Called when publishers to which this subscriber subscribes publishes news."""
        pass


class BusinessNewsSubscriber(Subscriber):
    def breaking_news(self, news_category: str, news_title: str):
        """Prints when the news category is business."""
        if news_category == "business":
            print(f"SUBSCRIBER: Business Breaking: {news_title}")


class PoliticsNewsSubscriber(Subscriber):
    def breaking_news(self, news_category: str, news_title: str):
        """Prints when the news category is politics."""
        if news_category == "politics":
            print(f"SUBSCRIBER: Politics Breaking: {news_title}")


class KeyWordSubscriber(Subscriber):
    def __init__(self, keyword: str):
        # The keyword to match news titles
        self.keyword = keyword

    def breaking_news(self, news_category: str, news_title: str):
        """Prints when the news tiles contain the keyword."""
        if news_title.lower().find(self.keyword) != -1:
            print(f"SUBSCRIBER: Filter [{self.keyword}]: {news_title}")
