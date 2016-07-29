import os
import sys
import json
import pika

conn = pika.BlockingConnection()
ch = conn.channel()


#
# Helpers
#
def callback(ch, method, properties, body):
    jdata = json.dumps(body)
    print(' ----> Received {}'.format(body))

    # push_message()
    return True

#
# Start
#
ch.basic_consume(callback, queue='scrappers', no_ack=True)
print('----> Waiting for messages. To exit press CTRL+C')
ch.start_consuming()
