# Kafka streaming simulation placeholder
from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def send_event(event):
    producer.send('hr_events', event)
    producer.flush()

if __name__ == '__main__':
    sample_event = {'ID': 6, 'Event': 'New Hire', 'Date': '2025-06-21'}
    send_event(sample_event)
    print('Event sent')
