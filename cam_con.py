import numpy as np
import cv2

def receive_image(sock, MAX_PACKET_SIZE):
    # 接收开始信号
    while True:
        data, addr = sock.recvfrom(MAX_PACKET_SIZE)  # 从套接字接受数据，返回一对值，接收到的数据和发送者的地址
        try:
            if data.decode('utf-8') == "ok":  # 尝试将接受信号解码为utf-8,检查是否解码正确
                break
        except UnicodeDecodeError:
            continue

    # 接收图片大小
    data, addr = sock.recvfrom(MAX_PACKET_SIZE)  # 接受下一条信息，为图像的大小
    pic_length = int(data.decode('utf-8'))

    # 初始化图像数据缓冲区
    image_data = b''  # 初始化一个空的字节字符串 image_data，用于存储接收到的图像数据
    while len(image_data) < pic_length:  # 使用一个循环来接收图像数据，直到接收到的数据长度等于预期的图像大小
        data, addr = sock.recvfrom(MAX_PACKET_SIZE)
        image_data += data

    # 将图像数据转换为numpy数组并解码为图像
    image_array = np.frombuffer(image_data, dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)  # 解码为图像， cv2.IMREAD_COLOR指彩色图像

    return image