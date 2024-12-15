import requests


# Hàm đọc header của một URL
def get_headers(url):
    try:
        # Gửi yêu cầu GET tới URL
        response = requests.get(url)

        # Lấy các header từ phản hồi
        headers = response.headers

        print(f"Header của trang {url}:\n")
        # Duyệt qua và in từng header
        for key, value in headers.items():
            print(f"{key}: {value}")

    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi truy cập URL: {e}")


# URL cần đọc header
url = "https://www.google.com.vn/"
get_headers(url)
