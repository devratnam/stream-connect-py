from connector import StreamPublisher, StreamConsumer
host = 'host'
topic = "topic"
con_topic = [topic]
data = {
"source_number": "test",
"agn_uuid": "testid",
"status": "Created",
"products": [
    {
        "product_dlv_sku": "string",
        "product_scannable_id": "string",
        "combo": True,
        "total_quantity": 0,
        "child_products": [
            {
                "product_dlv_sku": "string",
                "product_scannable_id": "string",
                "combo": False,
                "total_quantity": 0
            }   
        ]
    }
]}

s = StreamPublisher("KAFKA", host, topic, configurations={})
s.publish(data)

# s = StreamConsumer("KAFKA", host, con_topic, configurations={})
# s.consume()