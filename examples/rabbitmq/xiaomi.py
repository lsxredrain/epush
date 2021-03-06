#!/usr/bin/env python
#coding:utf-8

import pika
import json

HOST = 'localhost'
USERNAME = 'hisir'
PASSWORD = 'hisir123'


class Xiaomi():
    def __init__(self):
        credentials = pika.PlainCredentials(USERNAME, PASSWORD)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST, credentials=credentials))
        self.channel = self.connection.channel()

    def notification_send(self):
        data = {'push_method': 'notification_send',
                'title': 'Test  中文',
                'description': 'Content',
                'registration_id': 'go6VssZlTDDypm+hxYdaxycXtqM7M9NsTPbCjzyIyh0='}
        self.in_mq(data)

    def all(self):
        data = {'push_method':'all',
                'title':'Test中文',
                'description':'Test'}
        self.in_mq(data)

    def end(self):
        self.channel.close()
        self.connection.close()

    def in_mq(self, data):
        self.channel.basic_publish(exchange='',
                routing_key='xiaomi_c',
                body=json.dumps(data))



if __name__ == "__main__":
    xiaomi = Xiaomi()

    xiaomi.notification_send()
    #xiaomi.all()

    xiaomi.end()
