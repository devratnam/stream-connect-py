from enum import Enum
from stream_connect.services.kafka import KafkaConnector


class ServiceMap(Enum):

    KAFKA = KafkaConnector

    @staticmethod
    def get_stream_service(service):
        _stream_service = None
        for each in ServiceMap:
            if each.name == service:
                _stream_service = each.value
                break
        return _stream_service
