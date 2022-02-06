from abc import ABCMeta, abstractclassmethod
from hashlib import new
from typing import Any, List


# Topic
class NewsAgency:
    def __init__(self) -> None:
        self.__subscribers: List = list()
        self.__last_news: Any = None

    def subscribe(self, subscriber: Any) -> None:
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Any = None) -> Any:
        if not subscriber:
            return self.__subscribers.pop()
        else:
            return self.__subscribers.remove(subscriber)

    def notify_all(self):
        for subscriber in self.__subscribers:
            subscriber.notify()

    def add_news(self, news: Any) -> None:
        self.__last_news = news

    def show_last_news(self) -> str:
        return f"Breaking News: {self.__last_news}"

    def subscribers(self) -> Any:
        return [type(value).__name__ for value in self.__subscribers]


# Observer Interface
class SubscriptionType(metaclass=ABCMeta):
    @abstractclassmethod
    def notify(self):
        pass


# Observer A
class SMSSubscriber(SubscriptionType):
    def __init__(self, news_agency) -> None:
        self.news_agency = news_agency
        self.news_agency.subscribe(self)

    def notify(self):
        print(f"{type(self).__name__} {self.news_agency.show_last_news()}")


# Observer B
class EmailSubscriber(SubscriptionType):
    def __init__(self, news_agency) -> None:
        self.news_agency = news_agency
        self.news_agency.subscribe(self)

    def notify(self):
        print(f"{type(self).__name__} {self.news_agency.show_last_news()}")


# Observer N
class AnySubscriber(SubscriptionType):
    def __init__(self, news_agency) -> None:
        self.news_agency = news_agency
        self.news_agency.subscribe(self)

    def notify(self):
        print(f"{type(self).__name__} {self.news_agency.show_last_news()}")


# Client
if __name__ == "__main__":
    news_agency = NewsAgency()

    SMSSubscriber(news_agency=news_agency)
    EmailSubscriber(news_agency=news_agency)
    AnySubscriber(news_agency=news_agency)

    print(f"\nSubscribers: {news_agency.subscribers()}\n")

    news_agency.add_news("Bitcoin DROPPED!!!")
    news_agency.notify_all()

    print(f"\nUnsubscribed: {type(news_agency.unsubscribe()).__name__}\n")
    print(f"Subiscribers: {news_agency.subscribers()}\n")
