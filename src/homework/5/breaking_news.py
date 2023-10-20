"""Publisher module."""
from typing import List
from subscriber import Subscriber


class Publisher:
    def __init__(self):
        # Subscribers
        self._subscriber_list: List[Subscriber] = []

    def attach(self, subscriber):
        """Attach a subscriber."""
        self._subscriber_list.append(subscriber)

    def detach(self, subscriber):
        """Detach a subscriber."""
        self._subscriber_list.remove(subscriber)


class NewYorkTimesBreakingNews(Publisher):
    def publish_news_item(self, news_category, news_title):
        """Publish a piece of news."""
        print(f"NYT: Breaking News: {news_title} [category={news_category}]")
        self.notify(news_category, news_title)

    def notify(self, news_category, news_title):
        """Notify all subscribers about a piece of news."""
        print(f"NYT: Notifying subscribers...")
        for subscriber in self._subscriber_list:
            subscriber.breaking_news(news_category, news_title)
