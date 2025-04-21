
import pulsar

client = pulsar.Client("pulsar://localhost:6650")

# Subscribe to the merge-topic (where uppercased words are published)
consumer = client.subscribe(
    "persistent://demo-tenant/demo-ns/merge-topic",
    subscription_name="merger"
)

result = []

print("Merging capitalized words...")

try:
    while True:
        msg = consumer.receive()
        word = msg.data().decode('utf-8')

        print(f"Received: {word}")
        result.append(word)

        consumer.acknowledge(msg)


    # Final merged sentence
    final_sentence = " ".join(result)
    print("\n✅ Final Merged Sentence:\n")
    print(final_sentence)

except Exception as e:
    print("Error in merger:", e)
    consumer.negative_acknowledge(msg)

finally:
    client.close()
