import os
import sys
import json
import pika

conn = pika.BlockingConnection()
ch = conn.channel()
ch.queue_declare(queue='scrappers')

#
# Publish
#
message = '{"name": "Another one"}'
print('----> Publishing message {}\n '.format(message))
ch.basic_publish(exchange='',
                routing_key='scrappers',
                body='message')

conn.close()
