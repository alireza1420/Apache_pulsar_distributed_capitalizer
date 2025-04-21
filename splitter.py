
import pulsar

client = pulsar.Client('pulsar://localhost:6650')

# Subscribe to raw-topic
consumer = client.subscribe(
    'persistent://demo-tenant/demo-ns/raw-topic',
    subscription_name='splitter'
)

# Create a producer for split-topic (just once!)
producer = client.create_producer(
    'persistent://demo-tenant/demo-ns/split-topic'
)

print("Splitter is running and waiting for messages...")

try:
    while True:
        msg = consumer.receive()
        sentence = msg.data().decode('utf-8')

        print("Received message:", sentence)

        words = sentence.split()  # split into words

        for word in words:
            print(f"Sending word: {word}")
            producer.send(word.encode('utf-8'))

        consumer.acknowledge(msg)

except Exception as e:
    print("Error:", e)
    consumer.negative_acknowledge(msg)

finally:
    client.close()

