import pulsar

client = pulsar.Client('pulsar://localhost:6650')

file_path = "pride_and_prejudice.txt"

with open(file_path, "r") as input_file:
    text = input_file.read()

    # Send the full text or lines to raw-topic
    producer = client.create_producer('persistent://demo-tenant/demo-ns/raw-topic')
    producer.send(text.encode('utf-8'))  # One message, full content

client.close()

