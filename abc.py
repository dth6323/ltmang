import socket
import pickle
import struct
import threading

import cv2
import numpy as np
import keyboard  # Thư viện để nhận sự kiện nhấn phím

def send_command(client, action, position=None, key=None):
    command = {'action': action}
    if position:
        command['position'] = position
    if key:
        command['key'] = key  # Gửi thông tin phím nhấn
    client.sendall(pickle.dumps(command))

def mouse_event(event, x, y, flags, param):
    client = param['client']
    original_width, original_height = param['original_size']
    display_width, display_height = param['display_size']

    if event == cv2.EVENT_LBUTTONDOWN:  # Nhấp chuột trái
        send_command(client, 'click')
    elif event == cv2.EVENT_MOUSEMOVE:  # Di chuyển chuột
        x_original = int(x * (original_width / display_width))
        y_original = int(y * (original_height / display_height))
        send_command(client, 'move', position=(x_original, y_original))

def listen_for_keypresses(client):
    while True:
        key_event = keyboard.read_event()
        if key_event.event_type == keyboard.KEY_DOWN:  # Nếu nhấn phím
            send_command(client, 'keypress', key=key_event.name)

def receive_screen(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    print(f"Đã kết nối tới {ip}:{port}")

    data = b""
    payload_size = struct.calcsize("Q")
    display_width, display_height = 800, 600

    try:
        cv2.namedWindow("Man hinh", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Man hinh", display_width, display_height)

        original_size = None
        cv2.setMouseCallback("Man hinh", mouse_event, param={'client': client, 'display_size': (display_width, display_height)})

        # Tạo một luồng cho việc lắng nghe phím nhấn
        threading.Thread(target=listen_for_keypresses, args=(client,), daemon=True).start()

        while True:
            while len(data) < payload_size:
                data += client.recv(4096)

            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("Q", packed_msg_size)[0]

            while len(data) < msg_size:
                data += client.recv(4096)

            frame_data = data[:msg_size]
            data = data[msg_size:]

            try:
                screenshot = np.array(pickle.loads(frame_data))
                frame = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

                if original_size is None:
                    original_height, original_width = screenshot.shape[:2]
                    original_size = (original_width, original_height)
                    cv2.setMouseCallback("Man hinh", mouse_event, param={'client': client, 'original_size': original_size, 'display_size': (display_width, display_height)})

                frame_resized = cv2.resize(frame, (display_width, display_height))
                cv2.imshow("Man hinh", frame_resized)

            except pickle.UnpicklingError:
                print("")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as e:
        print(f"Lỗi: {e}")
    finally:
        client.close()
        cv2.destroyAllWindows()

receive_screen("192.168.18.101", 12345)
