"""Publisher module."""
from typing import List
from subscriber import Subscriber
from abc import ABC, abstractmethod


class Publisher(ABC):
    """Abstract publisher."""

    @abstractmethod
    def attach(self, subscriber):
        """Attach a subscriber."""

    @abstractmethod
    def detach(self, subscriber):
        """Detach a subscriber."""

    @abstractmethod
    def notify(self, news_category, news_title):
        pass


class NewYorkTimesBreakingNews(Publisher):
    def __init__(self):
        # Subscribers
        self._subscribers: List[Subscriber] = []

    def attach(self, subscriber):
        self._subscribers.append(subscriber)

    def detach(self, subscriber):
        self._subscribers.remove(subscriber)

    def publish_news_item(self, news_category, news_title):
        """Publish a piece of news."""
        print(f"NYT: Breaking News: {news_title} [category={news_category}]")
        self.notify(news_category, news_title)

    def notify(self, news_category, news_title):
        """Notify all subscribers about a piece of news."""
        print(f"NYT: Notifying subscribers...")
        for subscriber in self._subscribers:
            subscriber.breaking_news(news_category, news_title)
