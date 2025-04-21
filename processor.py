
import pulsar

client = pulsar.Client("pulsar://localhost:6650")
# Consumer to recive the splitted messages
consumer = client.subscribe("persistent://demo-tenant/demo-ns/split-topic",subscription_name="word-processor")

#producer to send messages to merge
producer = client.create_producer('persistent://demo-tenant/demo-ns/merge-topic')

print("Capitalizing the words ! ")

try:
        while True:
                msg = consumer.receive()
                words=msg.data().decode('utf-8')

                processed_words=words.upper()
                producer.send(processed_words.encode('utf-8'))
                consumer.acknowledge(msg)
except Exception as e:
        print("Error:",e)
        consumer.negative_acknowledge(msg)
finally:
        client.close()

