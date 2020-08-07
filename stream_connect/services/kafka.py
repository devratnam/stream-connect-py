import json

from stream_connect.services.base import StreamConnectorBase
from confluent_kafka import Producer, Consumer, KafkaError
from stream_connect.errors import ERROR_CODES


class KafkaConnector(StreamConnectorBase):
    """
    kafka stream connector service
    """

    def publish(self, data, *args, **kwargs):
        config = self.configurations
        config.update({'bootstrap.servers': self.host})
        producer = Producer(producer = Producer(config))
        producer.poll(0)
        _data = json.dumps(data)
        producer.produce(
            self.topic, _data.encode('utf-8'), *args, **kwargs, callback=self.delivery_status)
        producer.flush()

    def consume(self):
        credential_dict = self.get_credential_dict()
        consumer = Consumer(credential_dict)
        consumer.subscribe(self.topic)
        message = consumer.poll(1.0)
        if message.error():
            raise KafkaError(ERROR_CODES["KafkaConsumerError"].format(message.error()))
        return message

    def delivery_status(self, error, message):
        """ 
        Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush().
        """
        if error:
            self.response.errors.append(KafkaError(ERROR_CODES["KafkaProducerError"].format(error)))
        else:
            self.response.success = True
            self.response.message = 'Message delivered to {} [{}]'.format(message.topic(), message.partition())

    def get_credential_dict(self):
        credential_dict = {
            'bootstrap.servers': self.host,
            'auto.offset.reset': 'earliest',
        }
        credential_dict.update(self.configurations)
        return credential_dict
