from stream_connect.commons import ServiceMap
from confluent_kafka import KafkaError


class StreamPublisher(object):
    """
    generic class to publish messages into stream service
    """

    def __init__(self, service, host, topic, configurations={}):
        self.service = service
        self.host = host
        self.topic = topic
        self.configurations = configurations

    def publish(self, data, *args, **kwargs):
        executable_service = ServiceMap.get_stream_service(
            self.service)(self.host, self.topic, configurations=self.configurations)
        return executable_service.publish(data, *args, **kwargs)


class StreamConsumer(object):
    """
    generic class to consume messages from stream service
    """

    def __init__(self, service, host, topic, configurations={}):
        self.service = service
        self.host = host
        self.topic = topic
        self.configurations = configurations

    def consume(self):
        executable_service = ServiceMap.get_stream_service(
            self.service)(self.host, self.topic, configurations=self.configurations)
        return executable_service.consume()
