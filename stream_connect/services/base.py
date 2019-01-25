from abc import ABC, abstractmethod
from stream_connect.services.response import Response


class StreamConnectorBase(ABC):
    """
    base class to connect to streaming service
    """

    def __init__(self, host, topic, configurations={}):
        self.host = host
        self.topic = topic
        self.configurations = configurations
        self.response = Response()

    @abstractmethod
    def consume(self):
        pass

    @abstractmethod
    def publish(self, data):
        pass
