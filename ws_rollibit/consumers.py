from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # 客户端尝试连接时调用
        print("连接成功")
        group = self.scope['url_route']['kwargs'].get("group")
        self.group_name = group  # 保存分组名称到实例变量
        print(self.group_name)
        self.accept()
        # 将客户端的链接对象加入到（内存 or redis）
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)

    def receive(self, text_data=None, bytes_data=None):
        async_to_sync(self.channel_layer.group_send)(
            self.group_name, {"type": "xx.oo", "message": text_data}
        )

    def xx_oo(self, event):
        self.send(text_data=json.dumps({
            'message': event['message']
        }))

    def disconnect(self, close_code):
        # 连接断开时调用
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)
