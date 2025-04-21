# Apache Pulsar Stream Processing Pipeline

This project demonstrates a stream processing pipeline using **Apache Pulsar**. It includes four stages:

1. **Producer**: Sends a full sentence to the pipeline
2. **Splitter**: Splits sentences into words
3. **Processor**: Capitalizes each word
4. **Merger**: Collects capitalized words and reconstructs the final sentence

---

## 🚀 Getting Started

### 1. Start Pulsar in Standalone Mode
```bash
./bin/pulsar standalone
```

---

## 📦 Setup (One-Time Only)

### 2. Create Tenant and Namespace
```bash
bin/pulsar-admin tenants create demo-tenant \
  --admin-roles admin \
  --allowed-clusters standalone

bin/pulsar-admin namespaces create demo-tenant/demo-ns
```

### 3. Create Partitioned Topics
```bash
bin/pulsar-admin topics create-partitioned-topic persistent://demo-tenant/demo-ns/raw-topic --partitions 4
bin/pulsar-admin topics create-partitioned-topic persistent://demo-tenant/demo-ns/split-topic --partitions 4
bin/pulsar-admin topics create-partitioned-topic persistent://demo-tenant/demo-ns/merge-topic --partitions 4
```
![tenatns](https://github.com/user-attachments/assets/b682d5cd-99b7-4866-b914-362db38668e1)

---

## 🧩 Project Files and Flow

### 1. `producer.py`
- Reads a full paragraph (e.g., from `test_set.txt`)
- Sends the entire paragraph to `raw-topic`

### 2. `splitter.py`
- Consumes from `raw-topic`
- Splits paragraph into words
- Sends each word to `split-topic`

### 3. `processor.py`
- Consumes words from `split-topic`
- Capitalizes each word
- Sends each capitalized word to `merge-topic`
- Finally, sends a special message `"__END__"` to signal completion

### 4. `merger.py`
- Consumes from `merge-topic`
- Collects words until it sees `"__END__"`
- Joins words into a full sentence and prints the result

---
![arch_task4](https://github.com/user-attachments/assets/c02304a5-c866-4427-aec0-1483708e8b83)

## ✅ Running the Pipeline (IN ORDER)

> Open 4 terminal tabs or run each in background order:

1. Start merger (last step, but must be running first):
```bash
python3 merger.py
```

2. Start processor (uppercases the words):
```bash
python3 processor.py
```

3. Start splitter (splits the paragraph):
```bash
python3 splitter.py
```

4. Start the initial producer (sends paragraph):
```bash
python3 producer.py
```

---

## 🔚 Stopping the Pipeline

- The pipeline terminates automatically when `"__END__"` is received by the merger.
- To restart: re-run the producer or reset subscriptions.

---

## 💡 Notes
- You can scale each component by adding more consumers to handle partitioned topics.
- Adjust the number of partitions depending on message volume.

---

## 📂 Example File: ``
You can use  
```bash
curl https://www.gutenberg.org/files/1342/1342-0.txt -o "pride_and_prejudice.txt"
```
This should contain the pride and prejudice book you want to process through the system.
---

Happy Streaming! 🌊

