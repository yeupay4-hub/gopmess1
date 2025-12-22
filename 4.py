import requests
import os
import re
import json
import random
import base64
import uuid
import time
from datetime import datetime

try:
    from pystyle import Add,Center,Anime,Colors,Colorate,Write,System
except:
    os.system('pip install pystyle requests colorama beautifulsoup4 selenium mechanize webdriver_manager')
    from pystyle import Add,Center,Anime,Colors,Colorate,Write,System

banners = f"""⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⡋⠉⠙⠒⢤⡀⠀⠀⠀⠀⠀⢠⠖⠉⠉⠙⠢⡄⠀
⠀⠀⠀⠀⠀⠀⢀⣼⣟⡒⠒⠀⠀⠀⠀⠀⠙⣆⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠹⡄
⠀⠀⠀⠀⠀⠀⣼⠷⠖⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⢷
⠀⠀⠀⠀⠀⠀⣷⡒⠀⠀⢐⣒⣒⡒⠀⣐⣒⣒⣧⠀⠀⡇⠀⢠⢤⢠⡠⠀⠀⢸
⠀⠀⠀⠀⠀⢰⣛⣟⣂⠀⠘⠤⠬⠃⠰⠑⠥⠊⣿⠀⢴⠃⠀⠘⠚⠘⠑⠐⠀⢸
⠀⠀⠀⠀⠀⢸⣿⡿⠤⠀⠀⠀⠀⠀⢀⡆⠀⠀⣿⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⣸
⠀⠀⠀⠀⠀⠈⠿⣯⡭⠀⠀⠀⠀⢀⣀⠀⠀⠀⡟⠀⠀⢸⠀⠀⠀⠀⠀⠀⢠⠏
⠀⠀⠀⠀⠀⠀⠀⠈⢯⡥⠄⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠳⢄⣀⣀⣀⡴⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⡦⣄⣀⣀⣀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⠛⠃⠀⠀⠀⢹⠳⡶⣤⡤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⢴⣿⣿⣿⡟⡷⢄⣀⣀⣀⡼⠳⡹⣿⣷⠞⣳⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢰⡯⠭⠹⡟⠿⠧⠷⣄⣀⣟⠛⣦⠔⠋⠛⠛⠋⠙⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⠭⠉⠀⢠⣤⠀⠀⠀⠘⡷⣵⢻⠀⠀⠀⠀⣼⠀⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡇⣿⠍⠁⠀⢸⣗⠂⠀⠀⠀⣧⣿⣼⠀⠀⠀⠀⣯⠀⢸⠀
-----------------------------------------------------------------
       Tool Gộp Mess V1.0 By Mdung & CteVcl
=====================================================================
➩ Telegram: https;//t.me/ctevclwar
➩ FaceBook 1: https://www.facebook.com/daikafi5
➩ FaceBook 2: https://www.facebook.com/profile.php?id=61570431072611
=====================================================================
"""

def clear():
    if platform[0:3]=='lin':
        os.system('clear')
    else:
        os.system('cls')

def banner():
    print('\x1b[0m',end='')
    clear()
    a=Colorate.Horizontal(Colors.red_to_purple, banners)
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
    print()

banner()

def doi_giay(value):
    print(f'Doi {value} giay...')
    time.sleep(value)

def kiem_tra_cookie(cookie):
    try:
        if 'c_user=' not in cookie:
            return {"status": "failed", "msg": "Cookie khong chua user_id"}
        
        user_id = cookie.split('c_user=')[1].split(';')[0]
        url = f"https://graph2.facebook.com/v3.3/{user_id}/picture?redirect=0"
        response = requests.get(url, timeout=30)
        check_data = response.json()

        if not check_data.get('data', {}).get('height') or not check_data.get('data', {}).get('width'):
            return {"status": "failed", "msg": "Cookie khong hop le"}

        headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi-VN,vi;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"0.1.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }

        profile_response = requests.get(f'https://m.facebook.com/profile.php?id={user_id}', headers=headers, timeout=30)
        name = profile_response.text.split('<title>')[1].split('<')[0].strip()

        return {
            "status": "success",
            "name": name,
            "user_id": user_id,
            "msg": "successful"
        }
    except Exception as e:
        return {"status": "failed", "msg": f"Loi xay ra: {str(e)}"}

def generate_vietnamese_names():
    ho = [
        'Nguyễn', 'Trần', 'Lê', 'Phạm', 'Hoàng', 'Vũ', 'Đặng', 'Bùi', 'Đỗ', 'Hồ',
        'Ngô', 'Dương', 'Lý', 'Võ', 'Đinh', 'Tô', 'Lâm', 'Phan', 'Trương', 'Huỳnh',
        'Cao', 'Đoàn', 'Lưu', 'Mai', 'Tăng', 'Hà', 'Trịnh', 'Đào', 'Bành', 'Lục',
        'La', 'Quách', 'Tạ', 'Thái', 'Đàm', 'Bế', 'Châu', 'Hứa', 'Kiều', 'Ninh',
        'Vương', 'Triệu', 'Hàn', 'Tôn', 'Lương', 'Khương', 'Tần', 'Hình', 'Từ', 'Văn',
        'Phùng', 'Hồng', 'Nghiêm', 'Tống', 'Hùng', 'Lai', 'Cung', 'Bạc', 'Điền', 'Chương',
        'Thạch', 'Đường', 'Đoạn', 'Lã', 'Thẩm', 'Liễu', 'Bạch', 'Sơn', 'Tào', 'Âu',
        'Lỗ', 'Tư', 'Lạc', 'Hạ', 'Khoa', 'Nông', 'Phí', 'Mạch', 'Khâu', 'Chử',
        'Tiền', 'Đới', 'Tiêu', 'Cát', 'Viên', 'Đồng', 'Trà', 'Hữu', 'Khúc', 'Tề',
        'Phương', 'Bì', 'Hầu', 'Sầm', 'Nguyến', 'Trấn', 'Lề', 'Phậm', 'Hoẳng', 'Vụ',
        'Đằng', 'Ngỗ', 'Dưởng', 'Lỷ', 'Vổ', 'Đình', 'Tổ', 'Lầm', 'Phấn', 'Trưởng',
        'Huýnh', 'Cảo', 'Đoản', 'Lứu', 'Mại', 'Tẳng', 'Hả', 'Trình', 'Đảo', 'Bảnh',
        'Lục', 'Lả', 'Quạch', 'Tả', 'Thải', 'Đảm', 'Bể', 'Chấu', 'Hử', 'Kiểu',
        'Nình', 'Vưỡng', 'Triểu', 'Hản', 'Tốn', 'Lường', 'Khưỡng', 'Tẫn', 'Hĩnh', 'Tử',
        'Vắn', 'Phứng', 'Hổng', 'Nghiếm', 'Tống', 'Hững', 'Lại', 'Cứng', 'Bạc', 'Điển',
        'Chưỡng', 'Thạch', 'Đường', 'Đoạn', 'Lã', 'Thẩm', 'Liễu', 'Bạch', 'Sơn', 'Tảo',
        'Âu', 'Lỗ', 'Tứ', 'Lạc', 'Hạ', 'Khoa', 'Nông', 'Phí', 'Mạch', 'Khâu',
        'Chử', 'Tiền', 'Đới', 'Tiêu', 'Cát', 'Viên', 'Đồng', 'Trà', 'Hữu', 'Khúc',
        'Tề', 'Phương', 'Bì', 'Hầu', 'Sầm', 'Nguyến', 'Trấn', 'Lề', 'Phậm', 'Hoẳng',
        'Vụ', 'Đằng', 'Ngỗ', 'Dưởng', 'Lỷ', 'Vổ', 'Đình', 'Tổ', 'Lầm', 'Phấn',
        'Trưởng', 'Huýnh', 'Cảo', 'Đoản', 'Lứu', 'Mại', 'Tẳng', 'Hả', 'Trình', 'Đảo',
        'Bảnh', 'Lục', 'Lả', 'Quạch', 'Tả', 'Thải', 'Đảm', 'Bể', 'Chấu', 'Hử',
        'Kiểu', 'Nình', 'Vưỡng', 'Triểu', 'Hản', 'Tốn', 'Lường', 'Khưỡng', 'Tẫn', 'Hĩnh',
        'Tử', 'Vắn', 'Phứng', 'Hổng', 'Nghiếm', 'Tống', 'Hững', 'Lại', 'Cứng', 'Bạc',
        'Điển', 'Chưỡng', 'Thạch', 'Đường', 'Đoạn', 'Lã', 'Thẩm', 'Liễu', 'Bạch', 'Sơn',
        'Tảo', 'Âu', 'Lỗ', 'Tứ', 'Lạc', 'Hạ', 'Khoa', 'Nông', 'Phí', 'Mạch',
        'Khâu', 'Chử', 'Tiền', 'Đới', 'Tiêu', 'Cát', 'Viên', 'Đồng', 'Trà', 'Hữu',
        'Khúc', 'Tề', 'Phương', 'Bì', 'Hầu', 'Sầm', 'Nguyến', 'Trấn', 'Lề', 'Phậm',
        'Hoẳng', 'Vụ', 'Đằng', 'Ngỗ', 'Dưởng', 'Lỷ', 'Vổ', 'Đình', 'Tổ', 'Lầm',
        'Phấn', 'Trưởng', 'Huýnh', 'Cảo', 'Đoản', 'Lứu', 'Mại', 'Tẳng', 'Hả', 'Trình',
        'Đảo', 'Bảnh', 'Lục', 'Lả', 'Quạch', 'Tả', 'Thải', 'Đảm', 'Bể', 'Chấu',
        'Hử', 'Kiểu', 'Nình', 'Vưỡng', 'Triểu', 'Hản', 'Tốn', 'Lường', 'Khưỡng', 'Tẫn',
        'Hĩnh', 'Tử', 'Vắn', 'Phứng', 'Hổng', 'Nghiếm', 'Tống', 'Hững', 'Lại', 'Cứng',
        'Bạc', 'Điển', 'Chưỡng', 'Thạch', 'Đường', 'Đoạn', 'Lã', 'Thẩm', 'Liễu', 'Bạch',
        'Sơn', 'Tảo', 'Âu', 'Lỗ', 'Tứ', 'Lạc', 'Hạ', 'Khoa', 'Nông', 'Phí',
        'Mạch', 'Khâu', 'Chử', 'Tiền', 'Đới', 'Tiêu', 'Cát', 'Viên', 'Đồng', 'Trà',
        'Hữu', 'Khúc', 'Tề', 'Phương', 'Bì', 'Hầu', 'Sầm', 'Nguyến', 'Trấn', 'Lề',
        'Phậm', 'Hoẳng', 'Vụ', 'Đằng', 'Ngỗ', 'Dưởng', 'Lỷ', 'Vổ', 'Đình', 'Tổ',
        'Lầm', 'Phấn', 'Trưởng', 'Huýnh', 'Cảo', 'Đoản', 'Lứu', 'Mại', 'Tẳng', 'Hả',
        'Trình', 'Đảo', 'Bảnh', 'Lục', 'Lả', 'Quạch', 'Tả', 'Thải', 'Đảm', 'Bể',
        'Chấu', 'Hử', 'Kiểu', 'Nình', 'Vưỡng', 'Triểu', 'Hản', 'Tốn', 'Lường', 'Khưỡng',
        'Tẫn', 'Hĩnh', 'Tử', 'Vắn', 'Phứng', 'Hổng', 'Nghiếm', 'Tống', 'Hững', 'Lại',
        'Cứng', 'Bạc', 'Điển', 'Chưỡng', 'Thạch', 'Đường', 'Đoạn', 'Lã', 'Thẩm', 'Liễu',
        'Bạch', 'Sơn', 'Tảo', 'Âu', 'Lỗ', 'Tứ', 'Lạc', 'Hạ', 'Khoa', 'Nông',
        'Phí', 'Mạch', 'Khâu', 'Chử', 'Tiền', 'Đới', 'Tiêu', 'Cát', 'Viên', 'Đồng',
        'Trà', 'Hữu', 'Khúc', 'Tề', 'Phương', 'Bì', 'Hầu', 'Sầm'
    ]
    ten_dem = [
        'Văn', 'Thị', 'Ngọc', 'Minh', 'Hồng', 'Anh', 'Hải', 'Bích', 'Đức', 'Lan',
        'Phong', 'Mai', 'Hương', 'Tuấn', 'Quỳnh', 'Hoa', 'Linh', 'Khoa', 'Như', 'Phúc',
        'Thanh', 'Tâm', 'Duy', 'Hạnh', 'Hằng', 'Khánh', 'Bảo', 'Trung', 'Nga', 'Nhật',
        'Thủy', 'Yến', 'Xuân', 'Sơn', 'Tùng', 'Phương', 'Diệu', 'Kiên', 'Trí', 'Vĩnh',
        'Huyền', 'Thảo', 'Đạt', 'Cường', 'Hòa', 'Khởi', 'Long', 'Nam', 'Quân', 'Việt',
        'Bình', 'Châu', 'Đông', 'Hiếu', 'Hiệp', 'Huy', 'Khai', 'Nhi', 'Quý', 'Thắng',
        'Ái', 'Ân', 'Băng', 'Cẩm', 'Cúc', 'Dung', 'Đan', 'Điệp', 'Giang', 'Hiền',
        'Hoài', 'Hợp', 'Kim', 'Liên', 'Liễu', 'Loan', 'Mẫn', 'Ngân', 'Nhiên', 'Oanh',
        'Phượng', 'Thắm', 'Thiên', 'Thục', 'Thu', 'Tuyết', 'Uyên', 'Vân', 'Vy', 'Yên',
        'Đào', 'Đoan', 'Hậu', 'Lệ', 'Mỹ', 'Nhàn', 'Quyên', 'Sương', 'Thoa', 'Thúy',
        'Tiên', 'Trang', 'Trinh', 'Tú', 'Vắn', 'Thĩ', 'Ngọc', 'Mình', 'Hổng', 'Ánh',
        'Hải', 'Bịch', 'Đức', 'Làn', 'Phóng', 'Mãi', 'Hương', 'Tuấn', 'Quỷnh', 'Hoà',
        'Lình', 'Khoá', 'Như', 'Phức', 'Thảnh', 'Tẩm', 'Dũy', 'Hạnh', 'Hằng', 'Khánh',
        'Bảo', 'Trúng', 'Ngã', 'Nhật', 'Thủy', 'Yến', 'Xuẫn', 'Sơn', 'Túng', 'Phương',
        'Diệu', 'Kiền', 'Trí', 'Vĩnh', 'Huyền', 'Thảo', 'Đạt', 'Cường', 'Hoà', 'Khởi',
        'Long', 'Nam', 'Quần', 'Việt', 'Bình', 'Chấu', 'Đông', 'Hiệu', 'Hiệp', 'Hũy',
        'Khải', 'Nhĩ', 'Quý', 'Thắng', 'Ái', 'Ân', 'Băng', 'Cẩm', 'Cúc', 'Dũng', 'Đan',
        'Điệp', 'Giang', 'Hiền', 'Hoài', 'Hợp', 'Kim', 'Liên', 'Liễu', 'Loan', 'Mẫn',
        'Ngân', 'Nhiên', 'Oanh', 'Phượng', 'Thắm', 'Thiên', 'Thục', 'Thu', 'Tuyết', 'Uyên',
        'Vân', 'Vỹ', 'Yên', 'Đào', 'Đoan', 'Hậu', 'Lệ', 'Mỹ', 'Nhàn', 'Quyên', 'Sương',
        'Thoa', 'Thúy', 'Tiên', 'Trang', 'Trình', 'Tú', 'Văn', 'Thị', 'Ngọc', 'Minh',
        'Hồng', 'Anh', 'Hải', 'Bích', 'Đức', 'Lan', 'Phong', 'Mai', 'Hương', 'Tuấn',
        'Quỳnh', 'Hoa', 'Linh', 'Khoa', 'Như', 'Phúc', 'Thanh', 'Tâm', 'Duy', 'Hạnh',
        'Hằng', 'Khánh', 'Bảo', 'Trung', 'Nga', 'Nhật', 'Thủy', 'Yến', 'Xuân', 'Sơn',
        'Tùng', 'Phương', 'Diệu', 'Kiên', 'Trí', 'Vĩnh', 'Huyền', 'Thảo', 'Đạt', 'Cường',
        'Hòa', 'Khởi', 'Long', 'Nam', 'Quân', 'Việt', 'Bình', 'Châu', 'Đông', 'Hiếu',
        'Hiệp', 'Huy', 'Khai', 'Nhi', 'Quý', 'Thắng', 'Ái', 'Ân', 'Băng', 'Cẩm', 'Cúc',
        'Dung', 'Đan', 'Điệp', 'Giang', 'Hiền', 'Hoài', 'Hợp', 'Kim', 'Liên', 'Liễu',
        'Loan', 'Mẫn', 'Ngân', 'Nhiên', 'Oanh', 'Phượng', 'Thắm', 'Thiên', 'Thục', 'Thu',
        'Tuyết', 'Uyên', 'Vân', 'Vy', 'Yên', 'Đào', 'Đoan', 'Hậu', 'Lệ', 'Mỹ', 'Nhàn',
        'Quyên', 'Sương', 'Thoa', 'Thúy', 'Tiên', 'Trang', 'Trinh', 'Tú', 'Vắn', 'Thĩ',
        'Ngọc', 'Mình', 'Hổng', 'Ánh', 'Hải', 'Bịch', 'Đức', 'Làn', 'Phóng', 'Mãi',
        'Hương', 'Tuấn', 'Quỷnh', 'Hoà', 'Lình', 'Khoá', 'Như', 'Phức', 'Thảnh', 'Tẩm',
        'Dũy', 'Hạnh', 'Hằng', 'Khánh', 'Bảo', 'Trúng', 'Ngã', 'Nhật', 'Thủy', 'Yến',
        'Xuẫn', 'Sơn', 'Túng', 'Phương', 'Diệu', 'Kiền', 'Trí', 'Vĩnh', 'Huyền', 'Thảo',
        'Đạt', 'Cường', 'Hoà', 'Khởi', 'Long', 'Nam', 'Quần', 'Việt', 'Bình', 'Chấu',
        'Đông', 'Hiệu', 'Hiệp', 'Hũy', 'Khải', 'Nhĩ', 'Quý', 'Thắng', 'Ái', 'Ân',
        'Băng', 'Cẩm', 'Cúc', 'Dũng', 'Đan', 'Điệp', 'Giang', 'Hiền', 'Hoài', 'Hợp',
        'Kim', 'Liên', 'Liễu', 'Loan', 'Mẫn', 'Ngân', 'Nhiên', 'Oanh', 'Phượng', 'Thắm',
        'Thiên', 'Thục', 'Thu', 'Tuyết', 'Uyên', 'Vân', 'Vỹ', 'Yên', 'Đào', 'Đoan',
        'Hậu', 'Lệ', 'Mỹ', 'Nhàn', 'Quyên', 'Sương', 'Thoa', 'Thúy', 'Tiên', 'Trang',
        'Trình', 'Tú'
    ]
    ten = [
        'An', 'Bình', 'Cường', 'Duy', 'Hà', 'Hùng', 'Hương', 'Khang', 'Lan', 'Linh',
        'Mai', 'Minh', 'Nam', 'Ngọc', 'Phúc', 'Phong', 'Quân', 'Quỳnh', 'Sơn', 'Thảo',
        'Tâm', 'Thanh', 'Thịnh', 'Trang', 'Trí', 'Tuấn', 'Tùng', 'Vân', 'Việt', 'Vỹ',
        'Xuân', 'Yến', 'Bảo', 'Châu', 'Đạt', 'Đông', 'Hải', 'Hoa', 'Khoa', 'Hân',
        'Hiếu', 'Hiệp', 'Huy', 'Khai', 'Long', 'Nhi', 'Phương', 'Quý', 'Thắng', 'Anh',
        'Ân', 'Băng', 'Cẩm', 'Cúc', 'Dung', 'Đan', 'Điệp', 'Giang', 'Hiền', 'Hoài',
        'Hòa', 'Hợp', 'Kim', 'Liên', 'Liễu', 'Loan', 'Mẫn', 'Ngân', 'Nhiên', 'Oanh',
        'Phượng', 'Thắm', 'Thiên', 'Thục', 'Thu', 'Tuyết', 'Uyên', 'Vân', 'Yên', 'Đào',
        'Đoan', 'Hậu', 'Lệ', 'Mỹ', 'Nhàn', 'Quyên', 'Sương', 'Thoa', 'Thúy', 'Tiên',
        'Trinh', 'Tú', 'Ái', 'Bích', 'Đức', 'Khánh', 'Nga', 'Nhật', 'Thủy', 'Vĩnh',
        'Huyền', 'Cường', 'Hòa', 'Khởi', 'Quân', 'Việt', 'Bình', 'Châu', 'Đông', 'Hiếu',
        'Hiệp', 'Huy', 'Khai', 'Nhi', 'Quý', 'Thắng', 'Ánh', 'Bình', 'Cường', 'Dũy',
        'Hà', 'Húng', 'Hương', 'Kháng', 'Làn', 'Lình', 'Mại', 'Mình', 'Nám', 'Ngọc',
        'Phức', 'Phóng', 'Quần', 'Quỷnh', 'Sơn', 'Thảo', 'Tẩm', 'Thảnh', 'Thình', 'Tráng',
        'Trí', 'Tuấn', 'Túng', 'Vẫn', 'Việt', 'Vỹ', 'Xuẫn', 'Yến', 'Bảo', 'Chấu',
        'Đạt', 'Đông', 'Hải', 'Hoà', 'Khoa', 'Hẫn', 'Hiệu', 'Hiệp', 'Hũy', 'Khải',
        'Long', 'Nhĩ', 'Phương', 'Quý', 'Thắng', 'Ánh', 'Ân', 'Băng', 'Cẩm', 'Cúc',
        'Dũng', 'Đan', 'Điệp', 'Giang', 'Hiền', 'Hoài', 'Hòa', 'Hợp', 'Kim', 'Liên',
        'Liễu', 'Loan', 'Mẫn', 'Ngân', 'Nhiên', 'Oanh', 'Phượng', 'Thắm', 'Thiên', 'Thục',
        'Thu', 'Tuyết', 'Uyên', 'Vân', 'Yên', 'Đào', 'Đoan', 'Hậu', 'Lệ', 'Mỹ',
        'Nhàn', 'Quyên', 'Sương', 'Thoa', 'Thúy', 'Tiên', 'Trình', 'Tú', 'An', 'Bình',
        'Cường', 'Duy', 'Hà', 'Hùng', 'Hương', 'Khang', 'Lan', 'Linh', 'Mai', 'Minh',
        'Nam', 'Ngọc', 'Phúc', 'Phong', 'Quân', 'Quỳnh', 'Sơn', 'Thảo', 'Tâm', 'Thanh',
        'Thịnh', 'Trang', 'Trí', 'Tuấn', 'Tùng', 'Vân', 'Việt', 'Vỹ', 'Xuân', 'Yến',
        'Bảo', 'Châu', 'Đạt', 'Đông', 'Hải', 'Hoa', 'Khoa', 'Hân', 'Hiếu', 'Hiệp',
        'Huy', 'Khai', 'Long', 'Nhi', 'Phương', 'Quý', 'Thắng', 'Anh', 'Ân', 'Băng',
        'Cẩm', 'Cúc', 'Dung', 'Đan', 'Điệp', 'Giang', 'Hiền', 'Hoài', 'Hòa', 'Hợp',
        'Kim', 'Liên', 'Liễu', 'Loan', 'Mẫn', 'Ngân', 'Nhiên', 'Oanh', 'Phượng', 'Thắm',
        'Thiên', 'Thục', 'Thu', 'Tuyết', 'Uyên', 'Vân', 'Yên', 'Đào', 'Đoan', 'Hậu',
        'Lệ', 'Mỹ', 'Nhàn', 'Quyên', 'Sương', 'Thoa', 'Thúy', 'Tiên', 'Trinh', 'Tú',
        'Ái', 'Bích', 'Đức', 'Khánh', 'Nga', 'Nhật', 'Thủy', 'Vĩnh', 'Huyền', 'Cường',
        'Hòa', 'Khởi', 'Quân', 'Việt', 'Bình', 'Châu', 'Đông', 'Hiếu', 'Hiệp', 'Huy',
        'Khai', 'Nhi', 'Quý', 'Thắng', 'Ánh', 'Bình', 'Cường', 'Dũy', 'Hà', 'Húng',
        'Hương', 'Kháng', 'Làn', 'Lình', 'Mại', 'Mình', 'Nám', 'Ngọc', 'Phức', 'Phóng',
        'Quần', 'Quỷnh', 'Sơn', 'Thảo', 'Tẩm', 'Thảnh', 'Thình', 'Tráng', 'Trí', 'Tuấn',
        'Túng', 'Vẫn', 'Việt', 'Vỹ', 'Xuẫn', 'Yến', 'Bảo', 'Chấu', 'Đạt', 'Đông',
        'Hải', 'Hoà', 'Khoa', 'Hẫn', 'Hiệu', 'Hiệp', 'Hũy', 'Khải', 'Long', 'Nhĩ',
        'Phương', 'Quý', 'Thắng', 'Ánh', 'Ân', 'Băng', 'Cẩm', 'Cúc', 'Dũng', 'Đan',
        'Điệp', 'Giang', 'Hiền', 'Hoài', 'Hòa', 'Hợp', 'Kim', 'Liên', 'Liễu', 'Loan',
        'Mẫn', 'Ngân', 'Nhiên', 'Oanh', 'Phượng', 'Thắm', 'Thiên', 'Thục', 'Thu', 'Tuyết',
        'Uyên', 'Vân', 'Yên', 'Đào', 'Đoan', 'Hậu', 'Lệ', 'Mỹ', 'Nhàn', 'Quyên', 'Sương',
        'Thoa', 'Thúy', 'Tiên', 'Trình', 'Tú'
    ]
    vietnamese_names = []
    for i in range(5000):
        ho_random = random.choice(ho)
        structure = random.choice([2, 3, 4])
        if structure == 2:
            ten_random = random.choice(ten)
            name = f"{ho_random} {ten_random}"
        elif structure == 3:
            ten_dem_random = random.choice(ten_dem)
            ten_random = random.choice(ten)
            name = f"{ho_random} {ten_dem_random} {ten_random}"
        else:
            ten_dem_random1 = random.choice(ten_dem)
            ten_dem_random2 = random.choice(ten_dem)
            ten_random = random.choice(ten)
            name = f"{ho_random} {ten_dem_random1} {ten_dem_random2} {ten_random}"
        vietnamese_names.append(name)
    return vietnamese_names

class Facebook:
    def __init__(self, cookie: str):
        try:
            self.fb_dtsg = ''
            self.jazoest = ''
            self.cookie = cookie
            self.session = requests.Session()
            self.id = self.cookie.split('c_user=')[1].split(';')[0]
            self.commented_posts = set()
            self.headers = {
                'authority': 'www.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'vi',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                'viewport-width': '1366',
                'Cookie': self.cookie
            }
            url = self.session.get(f'https://www.facebook.com/{self.id}', headers=self.headers).url
            response = self.session.get(url, headers=self.headers).text
            matches = re.findall(r'\["DTSGInitialData",\[\],\{"token":"(.*?)"\}', response)
            if len(matches) > 0:
                self.fb_dtsg += matches[0]
                self.jazoest += re.findall(r'jazoest=(.*?)\"', response)[0]
        except:
            pass

    def info(self):
        try:
            get = self.session.get('https://www.facebook.com/me', headers=self.headers).url
            url = 'https://www.facebook.com/' + get.split('%2F')[-2] + '/' if 'next=' in get else get
            response = self.session.get(url, headers=self.headers, params={"locale": "vi_VN"})
            data_split = response.text.split('"CurrentUserInitialData",[],{')
            json_data = '{' + data_split[1].split('},')[0] + '}'
            parsed_data = json.loads(json_data)
            id = parsed_data.get('USER_ID', '0')
            name = parsed_data.get('NAME', '')
            if id == '0' and name == '':
                return 'cookieout'
            elif '828281030927956' in response.text:
                return '956'
            elif '1501092823525282' in response.text:
                return '282'
            elif '601051028565049' in response.text:
                return 'spam'
            else:
                id, name = parsed_data.get('USER_ID'), parsed_data.get('NAME')
                return {'success': 200, 'id': id, 'name': name}
        except:
            return 'cookieout'

    def tim_ban(self, text):
        try:
            data = {
                'av': self.id,
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'SearchCometResultsInitialResultsQuery',
                'variables': '{"count":5,"allow_streaming":false,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":false,"high_confidence_config":null,"intercept_config":null,"sts_disambiguation":null,"watch_config":null},"context":{"bsid":"23bd9138-cec6-4e71-aaeb-225fc8964e5b","tsid":"0.10477759801522946"},"experience":{"client_defined_experiences":["ADS_PARALLEL_FETCH"],"encoded_server_defined_params":null,"fbid":null,"type":"GLOBAL_SEARCH"},"filters":[],"text":"'+text+'"},"cursor":null,"feedbackSource":23,"fetch_filters":true,"renderLocation":"search_results_page","scale":1,"stream_initial_count":0,"useDefaultActor":false,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":true,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":true,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__FBReels_deprecate_short_form_video_context_gkrelayprovider":true,"__relay_internal__pv__CometFeedStoryDynamicResolutionPhotoAttachmentRenderer_experimentWidthrelayprovider":500,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__WorkCometIsEmployeeGKProviderrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":true,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__CometUFI_dedicated_comment_routable_dialog_gkrelayprovider":false,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":true,"__relay_internal__pv__FBReelsIFUTileContent_reelsIFUPlayOnHoverrelayprovider":false}',
                'server_timestamps': 'true',
                'doc_id': '9545374252239656'
            }
            response = self.session.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).json()
            profile = response["data"]["serpResponse"]["results"]["edges"][0]['rendering_strategy']['result_rendering_strategies'][0]['view_model']['profile']
            name = profile.get('name')
            uid = profile.get('id')
            return {'status': 'success', 'id': uid, 'name': name}
        except:
            return {'status': 'error', 'trangthai': 'thatbai'}

    def ket_ban(self, idkb):
        try:
            data = {
                'av': self.id,
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'FriendingCometFriendRequestSendMutation',
                'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,unexpected,1748257667487,475021,190055527696468,,;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,tap_search_bar,1748257603766,498383,391724414624676,,","click_proof_validation_result":null,"friend_requestee_ids":["'+idkb+'"],"friending_channel":"PROFILE_BUTTON","warn_ack_for_ids":[],"actor_id":"'+self.id+'","client_mutation_id":"6"},"scale":1}',
                'server_timestamps': 'true',
                'doc_id': '8805328442902902'
            }
            response = self.session.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).json()
            trangthai = response["data"]["friend_request_send"]["friend_requestees"]
            if trangthai and trangthai[0].get('friendship_status') == 'OUTGOING_REQUEST':
                return {'status': 'success', 'trangthai': 'thanhcong'}
            else:
                return {'status': 'error', 'trangthai': 'thatbai'}
        except:
            return {'status': 'error', 'trangthai': 'thatbai'}

    def lay_id_bai_viet(self):
        try:
            variables = {
                "RELAY_INCREMENTAL_DELIVERY": True,
                "clientQueryId": "b7876288-8582-4b5a-9420-76f62adfe671",
                "count": 10,
                "cursor": None,
                "feedLocation": "NEWSFEED",
                "feedStyle": "DEFAULT",
                "orderby": ["TOP_STORIES"],
                "renderLocation": "homepage_stream",
                "scale": 1,
                "useDefaultActor": False
            }
            data = {
                'av': self.id,
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'CometNewsFeedPaginationQuery',
                'variables': json.dumps(variables),
                'server_timestamps': 'true',
                'doc_id': '29492828377027602'
            }
            response = self.session.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
            post_ids = re.findall(r'"post_id":"(\d+)"', response)
            if post_ids:
                for post_id in post_ids:
                    if post_id not in self.commented_posts:
                        return {'status': 'success', 'idpost': post_id}
                self.commented_posts.clear()
                return {'status': 'success', 'idpost': post_ids[0]}
            return {'status': 'error', 'trangthai': 'thatbai'}
        except:
            return {'status': 'error', 'trangthai': 'thatbai'}

    def tha_cam_xuc(self, id, type):
        try:
            reac = {
                "LIKE": "1635855486666999",
                "LOVE": "1678524932434102",
                "CARE": "613557422527858",
                "HAHA": "115940658764963",
                "WOW": "478547315650144",
                "SAD": "908563459236466",
                "ANGRY": "444813342392137"
            }
            idreac = reac.get(type)
            data = {
                'av': self.id,
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
                'variables': fr'{{"input":{{"attribution_id_v2":"CometHomeRoot.react,comet.home,tap_tabbar,1719027162723,322693,4748854339,,","feedback_id":"{base64.b64encode(f"feedback:{str(id)}".encode()).decode()}","feedback_reaction_id":"{idreac}","feedback_source":"NEWS_FEED","is_tracking_encrypted":true,"tracking":["AZWUDdylhKB7Q-Esd2HQq9i7j4CmKRfjJP03XBxVNfpztKO0WSnXmh5gtIcplhFxZdk33kQBTHSXLNH-zJaEXFlMxQOu_JG98LVXCvCqk1XLyQqGKuL_dCYK7qSwJmt89TDw1KPpL-BPxB9qLIil1D_4Thuoa4XMgovMVLAXncnXCsoQvAnchMg6ksQOIEX3CqRCqIIKd47O7F7PYR1TkMNbeeSccW83SEUmtuyO5Jc_wiY0ZrrPejfiJeLgtk3snxyTd-JXW1nvjBRjfbLySxmh69u-N_cuDwvqp7A1QwK5pgV49vJlHP63g4do1q6D6kQmTWtBY7iA-beU44knFS7aCLNiq1aGN9Hhg0QTIYJ9rXXEeHbUuAPSK419ieoaj4rb_4lA-Wdaz3oWiWwH0EIzGs0Zj3srHRqfR94oe4PbJ6gz5f64k0kQ2QRWReCO5kpQeiAd1f25oP9yiH_MbpTcfxMr-z83luvUWMF6K0-A-NXEuF5AiCLkWDapNyRwpuGMs8FIdUJmPXF9TGe3wslF5sZRVTKAWRdFMVAsUn-lFT8tVAZVvd4UtScTnmxc1YOArpHD-_Lzt7NDdbuPQWQohqkGVlQVLMoJNZnF_oRLL8je6-ra17lJ8inQPICnw7GP-ne_3A03eT4zA6YsxCC3eIhQK-xyodjfm1j0cMvydXhB89fjTcuz0Uoy0oPyfstl7Sm-AUoGugNch3Mz2jQAXo0E_FX4mbkMYX2WUBW2XSNxssYZYaRXC4FUIrQoVhAJbxU6lomRQIPY8aCS0Ge9iUk8nHq4YZzJgmB7VnFRUd8Oe1sSSiIUWpMNVBONuCIT9Wjipt1lxWEs4KjlHk-SRaEZc_eX4mLwS0RcycI8eXg6kzw2WOlPvGDWalTaMryy6QdJLjoqwidHO21JSbAWPqrBzQAEcoSau_UHC6soSO9UgcBQqdAKBfJbdMhBkmxSwVoxJR_puqsTfuCT6Aa_gFixolGrbgxx5h2-XAARx4SbGplK5kWMw27FpMvgpctU248HpEQ7zGJRTJylE84EWcVHMlVm0pGZb8tlrZSQQme6zxPWbzoQv3xY8CsH4UDu1gBhmWe_wL6KwZJxj3wRrlle54cqhzStoGL5JQwMGaxdwITRusdKgmwwEQJxxH63GvPwqL9oRMvIaHyGfKegOVyG2HMyzmiQmtb5EtaFd6n3JjMCBF74Kcn33TJhQ1yjHoltdO_tKqnj0nPVgRGfN-kdJA7G6HZFvz6j82WfKmzi1lgpUcoZ5T8Fwpx-yyBHV0J4sGF0qR4uBYNcTGkFtbD0tZnUxfy_POfmf8E3phVJrS__XIvnlB5c6yvyGGdYvafQkszlRrTAzDu9pH6TZo1K3Jc1a-wfPWZJ3uBJ_cku-YeTj8piEmR-cMeyWTJR7InVB2IFZx2AoyElAFbMuPVZVp64RgC3ugiyC1nY7HycH2T3POGARB6wP4RFXybScGN4OGwM8e3W2p-Za1BTR09lHRlzeukops0DSBUkhr9GrgMZaw7eAsztGlIXZ_4"],"session_id":"{uuid.uuid4()}","actor_id":"{self.id}","client_mutation_id":"3"}},"useDefaultActor":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false}}',
                'server_timestamps': 'true',
                'doc_id': '7047198228715224'
            }
            response = self.session.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data)
            if '{"data":{"feedback_react":{"feedback":{"id":' in response.text:
                return {'status': 'success', 'trangthai': 'thanhcong'}
            else:
                return {'status': 'error', 'trangthai': 'thatbai'}
        except:
            return {'status': 'error', 'trangthai': 'thatbai'}

    def binh_luan(self, id, msg):
        try:
            feedback_id = base64.b64encode(f"feedback:{id}".encode()).decode()
            data = {
                'av': self.id,
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'useCometUFICreateCommentMutation',
                'variables': fr'{{"feedLocation":"DEDICATED_COMMENTING_SURFACE","feedbackSource":110,"groupID":null,"input":{{"client_mutation_id":"4","actor_id":"{self.id}","attachments":null,"feedback_id":"{feedback_id}","formatting_style":null,"message":{{"ranges":[],"text":"{msg}"}},"attribution_id_v2":"CometHomeRoot.react,comet.home,via_cold_start,1718688700413,194880,4748854339,,","vod_video_timestamp":null,"feedback_referrer":"/","is_tracking_encrypted":true,"tracking":["AZX1ZR3ETYfGknoE2E83CrSh9sg_1G8pbUK70jA-zjEIcfgLxA-C9xuQsGJ1l2Annds9fRCrLlpGUn0MG7aEbkcJS2ci6DaBTSLMtA78T9zR5Ys8RFc5kMcx42G_ikh8Fn-HLo3Qd-HI9oqVmVaqVzSasZBTgBDojRh-0Xs_FulJRLcrI_TQcp1nSSKzSdTqJjMN8GXcT8h0gTnYnUcDs7bsMAGbyuDJdelgAlQw33iNoeyqlsnBq7hDb7Xev6cASboFzU63nUxSs2gPkibXc5a9kXmjqZQuyqDYLfjG9eMcjwPo6U9i9LhNKoZwlyuQA7-8ej9sRmbiXBfLYXtoHp6IqQktunSF92SdR53K-3wQJ7PoBGLThsd_qqTlCYnRWEoVJeYZ9fyznzz4mT6uD2Mbyc8Vp_v_jbbPWk0liI0EIm3dZSk4g3ik_SVzKuOE3dS64yJegVOQXlX7dKMDDJc7P5Be6abulUVqLoSZ-cUCcb7UKGRa5MAvF65gz-XTkwXW5XuhaqwK5ILPhzwKwcj3h-Ndyc0URU_FJMzzxaJ9SDaOa9vL9dKUviP7S0nnig0sPLa5KQgx81BnxbiQsAbmAQMr2cxYoNOXFMmjB_v-amsNBV6KkES74gA7LI0bo56DPEA9smlngWdtnvOgaqlsaSLPcRsS0FKO3qHAYNRBwWvMJpJX8SppIR1KiqmVKgeQavEMM6XMElJc9PDxHNZDfJkKZaYTJT8_qFIuFJVqX6J9DFnqXXVaFH4Wclq8IKZ01mayFbAFbfJarH28k_qLIxS8hOgq9VKNW5LW7XuIaMZ1Z17XlqZ96HT9TtCAcze9kBS9kMJewNCl-WYFvPCTCnwzQZ-HRVOM04vrQOgSPud7vlA3OqD4YY2PSz_ioWSbk98vbJ4c7WVHiFYwQsgQFvMzwES20hKPDrREYks5fAPVrHLuDK1doffY1PTWF2KkSt0uERAcZIibeD5058uKSonW1fPurOnsTpAg8TfALFu1QlkcNt1X4dOoGpYmBR7HGIONwQwv5-peC8F758ujTTWWowBqXzJlA2boriCvdZkvS15rEnUN57lyO8gINQ5heiMCQN8NbHMmrY_ihJD3bdM4s2TGnWH4HBC2hi0jaIOJ8AoCXHQMaMdrGE1st7Y3R_T6Obg6VnabLn8Q-zZfToKdkiyaR9zqsVB8VsMrAtEz0yiGpaOF3KdI2sxvii3Q5XWIYN6gyDXsXVykFS25PsjPmXCF8V1mS7x6e9N9PtNTWwT8IGBZp9frOTQN2O52dOhPdsuCHAf0srrBVHbyYfCMYbOqYEEXQG0pNAmG_wqbTxNew9kTsXDRzYKW-NmEJcvy_xh1dDwg8xJc58Cl71e-rau3iP7o8mWhVSaxi4Bi6LAuj4UKVCt3IYCfm9AR1d5LqBFWU9LrJbRZSMlmUYwZf7PlrKmpnCnZvuismiL7DH3cnUjP0lWAvhy3gxZm1MK8KyRzWmHnTNqaVlL37c2xoE4YSyponeOu5D-lRl_Dp_C2PyR1kG6G0TCWS66UbU89Fu1qmwWjeQwYhzj2Jly9LRyClAbe86VJhIZE18YLPB-n1ng78qz7hHtQ8qT4ejY4csEjSRjjnHdz8U-06qErY-CXNNsVtzpYGuzZ1ZaXqzAQkUcREm98KR8c1vaXaQXumtDklMVgs76gLqZyiG1eCRbOQ6_EcQv7GeFnq5UIqoMH_Xzc78otBTvC5j3aCs5Pvf6k3gQ5ZU7E4uFVhZA7xoyD8sPX6rhdGL8JmLKJSGZQM5ccWpfpDJ5RWJp0bIJdnAJQ8gsYMRAI2OBxx2m2c76lNiUnB750dMe2H3pFzFQVkWQLkmGVY37cgmRNHyXboDMQU2nlbNH017dmklJCk4jVU8aA9Gpo8oHw","{{\"assistant_caller":"comet_above_composer","conversation_guide_session_id":"{uuid.uuid4()}\",\"conversation_guide_shown\":null}}"],"feedback_source":"DEDICATED_COMMENTING_SURFACE","idempotence_token":"client:{uuid.uuid4()}","session_id":"{uuid.uuid4()}"}},"inviteShortLinkKey":null,"renderLocation":null,"scale":1,"useDefaultActor":false,"focusCommentID":null}}',
                'server_timestamps': 'true',
                'doc_id': '24323081780615819'
            }
            cmt_response = self.session.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data)
            if cmt_response.status_code != 200:
                return {'status': 'error', 'trangthai': 'thatbai', 'error': f'HTTP {cmt_response.status_code}'}
            cmt_json = cmt_response.json()
            response_str = str(cmt_json)
            if ('"feedback_submitted":true' in response_str or 
                'create_comment' in response_str or
                'comment_create' in response_str or
                'success' in response_str.lower() or
                'error' not in response_str):
                self.commented_posts.add(id)
                return {'status': 'success', 'trangthai': 'thanhcong'}
            else:
                return {'status': 'error', 'trangthai': 'thatbai', 'response': cmt_json}
        except:
            return {'status': 'error', 'trangthai': 'thatbai'}

    def tim_nhom(self, keyword):
        try:
            data = {
                'av': self.id,
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'SearchCometResultsInitialResultsQuery',
                'variables': '{"allow_streaming":false,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":false,"high_confidence_config":null,"intercept_config":null,"sts_disambiguation":null,"watch_config":null},"context":{"bsid":"435c49d4-a957-431e-834f-d1da37a5f10b","tsid":"0.37005625332226133"},"experience":{"client_defined_experiences":["ADS_PARALLEL_FETCH"],"encoded_server_defined_params":null,"fbid":null,"type":"GROUPS_TAB"},"filters":[],"text":"'+keyword+'"},"count":5,"cursor":"AboQDCkcpXHJTbFDxObZS3n0GamptQsxZrcXlcMFwGKIy8t_OUZV16uazBcCgVOMdao8EgVEpXIG4MarCu1ndTCT45yz6IlSEOoYZsWeqF88dZnyorpLHnwlfVTjfYgLOTH6ehf3WNbEtWS0QH3J4A4edpfakj35aqL9swaRPEe1KSYtaF_h7wjzfta_lLSzyM3JvI6JxKyZmMZJ_DAnhJw3MvQE5zgckZpVwJLHeYmG38bV6CQOTaa2hI8PY1xq5segTD2TAZZ-GJASsyGbZ8iJnjhT1MrtF5v5t_l4X4k1XXHs8woxmR1hmLVRhQGcXcwIms5_kCPaVPGE_ZBqvDGtoSq1vzx5qDIx49eXD-frk0ESlo_Nvj7ix7sXrHDZRpmA2ljWLZjmOXChNzGltKw7KekWeE0BrynOmH7k-L9pu85PJ5MVHm3uR-fFZWx8ytKb5DDwo1vN-pylOwsXs9MYR394Hcv8P4s9k90a4wqcsMHBNQmrcFO4Ab6nXcveCvFVWrF1hAEI0n9F69ye-QIy048hbmveTYV13UOLB5yrVWmAAYDuDlSS64-fHXNziJue641DOHnCxSOdPkKI6tCGm01UQgDJynSG56qtcF9HL8snD_5gZ9sDvqD8VCl-23LbiwRe2WjKrjUPaJmkk1fVLzXPrR8DURyrqHB5WBkE-Tn1idUEZaFMdKn2SSpdGB-9TIGrSWveurlC3483IkPkLveq2s0pr68FPPLMMO7Bk9art2BvG9JwszZjnQ8KjnDCmnUX1a71iCwM_iLnbuENJvWZtEO4Rjqu4XwqRtMWhc9RPZvKOaJY9L2e4DLvZbbARN0o-dS78Epa77LB-Th84FXyTs7KrZ_X57DwMjrYxh9CPyG-dMaxJtC8E-e2tFCYf9jRGgY1QrWky9rSz7oHHVnyDzNGqn-UOyHO8DSGve2mmvuQ6CubtYmcHTIL1SzU-_xhfHVpmzJiZ5lY_fwoncc-VC0uNkdoeVUmdl4OtxbTBr7VY2t5A-arm5Vy3_Dmj2hkGrUTAHFi7Zq4hehYaS04WBuYCKxiuO6Bjq7tWFVa2wnYNrTbEqTUVkc0ie5Bd7O-6Hz_PZa3Z_YWPxuobu2QpGQ_hwMBrFFNpZfPXWYPPO_ggdxV5qnRUbml5wQMyzD7w2p-NQr0jfqHPymCUjFpWj5PZUfwY4CPL-K5Ll7cTFjr6q1epx-0Xcvd5PKnt3hzfiY9yF1AygVKPM7g9KyLk9QNjV5Svjxj0tzsmxis6crBFT1PbeaHaxEkS41OnLHia80Q33yHUpfL7LoZ8QhSAYeObJR8wvmaBYZFQj5qIaYm1agsOl2Z_ukhRcDilQwX_gbPJnuJTcxDEoioLBxt5wdno4j8U7fusivPNVgKIN0Cy3znZwQOPwjDz6ZxnuhYMd9RrmG_un8eV1W6ypT1EVNRRUZlMdb3cMiFyx4CA59xaDhqpPMh_rOLoIV7RTDMjC7IdFHtAP2z4FX6Xv1TYDwipiacO-NGff2nEniPEjYIfhNKFvQQN-MRwaAVXI_VeoIfQ-B8kF2HN3fPGtTkppbuGhFAzx5trYkllKyVZZfGh23fFlAy1UyNStJ4hi61ivshFOOfgHVQpdUNV_nqE1MVPmBPIM2jwB6DpCFamSpX8Wn1LQkgdzlJRMmng-C8sAxwHeIgy5JA_CN-p2KCBCTwV_2D07lGbIVwtgZNqFWnNZa0HlX-bWGJDUGH4r_2Ns_G0VVE-VxBVcIGFC6d1iX98HS_6_ykwSc3Z2KB4nnWNlUa4gyWOlev2yg","feedLocation":"SEARCH","feedbackSource":23,"fetch_filters":true,"focusCommentID":null,"locale":null,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"search_results_page","scale":1,"stream_initial_count":0,"useDefaultActor":false,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":true,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":true,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__FBReels_deprecate_short_form_video_context_gkrelayprovider":true,"__relay_internal__pv__FeedDeepDiveTopicPillThreadViewEnabledrelayprovider":false,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__WorkCometIsEmployeeGKProviderrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":true,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__CometUFI_dedicated_comment_routable_dialog_gkrelayprovider":false,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":true,"__relay_internal__pv__FBReelsIFUTileContent_reelsIFUPlayOnHoverrelayprovider":true}',
                'server_timestamps': 'true',
                'doc_id': '24016506881293628'
            }
            response = self.session.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).json()
            thongtin = response['data']["serpResponse"]["results"]['edges'][0]['rendering_strategy']['view_model']['profile']
            name = thongtin.get('name')
            uid = thongtin.get('id')
            return {'status': 'success', 'id': uid, 'name': name}
        except:
            return {'status': 'error', 'trangthai': 'thatbai'}

    def tham_gia_nhom(self, group_id):
        try:
            data = {
                'av': self.id,
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'GroupCometJoinForumMutation',
                'variables': '{"feedType":"DISCUSSION","groupID":"'+group_id+'","imageMediaType":"image/x-auto","input":{"action_source":"GROUP_MALL","attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1673041528761,114928,2361831622,","group_id":"'+group_id+'","group_share_tracking_params":{"app_id":"2220391788200892","exp_id":"null","is_from_share":false},"actor_id":"'+self.id+'","client_mutation_id":"1"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":true,"scale":2,"source":"GROUP_MALL","renderLocation":"group_mall","__relay_internal__pv__GroupsCometEntityMenuEmbeddedrelayprovider":true,"__relay_internal__pv__GlobalPanelEnabledrelayprovider":false}',
                'server_timestamps': 'true',
                'doc_id': '5853134681430324',
                'fb_api_analytics_tags': '["qpl_active_flow_ids=431626709"]'
            }
            response = self.session.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data)
            if group_id in response.text:
                return {'status': 'success', 'trangthai': 'thanhcong'}
            else:
                return {'status': 'error', 'trangthai': 'thatbai'}
        except:
            return {'status': 'error', 'trangthai': 'thatbai'}

def doc_cookie_tu_file(file_path):
    cookies = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                cookie = line.strip()
                if cookie:
                    cookies.append(cookie)
        return cookies
    except FileNotFoundError:
        print(f"Khong tim thay file {file_path}!")
        return []
    except Exception as e:
        print(f"Loi khi doc file cookie: {str(e)}")
        return []

def main():
    banner()
    
    file_cookie = input('Nhap ten file chua cookie (1 dong 1 cookie): ')
    cookies = doc_cookie_tu_file(file_cookie)
    if not cookies:
        print('Khong co cookie nao hop le, thoat chuong trinh!')
        return
    

    cookies_hop_le = []
    thong_tin_tai_khoan = []
    for cookie in cookies:
        check = kiem_tra_cookie(cookie)
        if check['status'] == 'success':
            print(f"Da dang nhap vao tai khoan Facebook: {check['name']} (ID: {check['user_id']}) - Live")
            cookies_hop_le.append(cookie)
            thong_tin_tai_khoan.append({'name': check['name'], 'id': check['user_id']})
        else:
            print(f"Cookie khong hop le: {check['msg']} - Die")
    
    if not cookies_hop_le:
        print('Khong co cookie nao live, thoat chuong trinh!')
        return
    

    thanh_ngang(65)
    print('=== CAU HINH TOOL ===')
    
    while True:
        try:
            delay = int(input('Nhap delay chung (giay): '))
            if delay > 0:
                break
            else:
                print('Vui long nhap so lon hon 0')
        except:
            print('Vui long nhap so')
    
    while True:
        try:
            so_nhiem_vu = int(input('Nhap so nhiem vu muon thuc hien: '))
            if so_nhiem_vu > 0:
                break
            else:
                print('Vui long nhap so lon hon 0')
        except:
            print('Vui long nhap so')
    

    danh_sach_binh_luan = []
    i = 1
    while True:
        cmt = input(f'Nhap noi dung binh luan so {i} (nhap trong de ket thuc): ').strip()
        if cmt == '':
            break
        danh_sach_binh_luan.append(cmt)
        i += 1
    
    if not danh_sach_binh_luan:
        print('Chua nhap binh luan nao, thoat chuong trinh!')
        return
    

    tu_khoa_nhom = [
        'công nghệ', 'kinh doanh', 'giáo dục', 'y tế', 'thể thao', 'giải trí',
        'du lịch', 'ẩm thực', 'thời trang', 'xe cộ', 'bất động sản', 'tài chính',
        'marketing', 'thiết kế', 'lập trình', 'nhiếp ảnh', 'âm nhạc', 'phim ảnh',
        'sách vở', 'học tập', 'làm đẹp', 'sức khỏe', 'gia đình', 'tình yêu',
        'bạn bè', 'công việc', 'học hành', 'điện tử', 'máy tính', 'điện thoại',
        'công nghệ thông tin', 'trí tuệ nhân tạo', 'blockchain', 'khoa học', 'mạng xã hội',
        'đầu tư', 'khởi nghiệp', 'doanh nghiệp', 'thương mại điện tử', 'quản lý',
        'kế toán', 'ngân hàng', 'bảo hiểm', 'chứng khoán', 'tài sản', 'tiết kiệm',
        'y học', 'sức khỏe tâm lý', 'dinh dưỡng', 'tập gym', 'yoga', 'chạy bộ',
        'bóng đá', 'bóng rổ', 'cầu lông', 'bơi lội', 'võ thuật', 'esports',
        'game online', 'trò chơi', 'phim hoạt hình', 'phim truyền hình', 'ca nhạc',
        'nhạc trẻ', 'nhạc pop', 'nhạc rap', 'nhạc rock', 'nhạc cổ điển', 'nhạc dân ca',
        'văn học', 'thơ ca', 'tiểu thuyết', 'truyện ngắn', 'truyện tranh', 'manga',
        'đọc sách', 'học ngoại ngữ', 'học tiếng Anh', 'học tiếng Nhật', 'học tiếng Hàn',
        'kỹ năng mềm', 'phát triển bản thân', 'motivation', 'lãnh đạo', 'giao tiếp',
        'nấu ăn', 'bánh ngọt', 'đồ uống', 'ẩm thực Việt', 'ẩm thực Á', 'ẩm thực Âu',
        'thời trang nam', 'thời trang nữ', 'phụ kiện', 'giày dép', 'túi xách',
        'xe máy', 'xe hơi', 'xe đạp', 'ô tô', 'mô tô', 'xe điện', 'bất động sản Hà Nội',
        'bất động sản Sài Gòn', 'nhà đất', 'căn hộ', 'chung cư', 'biệt thự',
        'nội thất', 'kiến trúc', 'xây dựng', 'trang trí', 'phong thủy', 'du lịch biển',
        'du lịch núi', 'du lịch nước ngoài', 'phượt', 'cắm trại', 'khám phá',
        'chăm sóc da', 'trang điểm', 'mỹ phẩm', 'làm tóc', 'chăm sóc cơ thể',
        'sức khỏe phụ nữ', 'sức khỏe nam giới', 'yoga thiền', 'giảm cân', 'tăng cân',
        'nuôi dạy con', 'hôn nhân', 'gia đình hạnh phúc', 'tình bạn', 'tình yêu đôi lứa',
        'hẹn hò', 'công nghệ 4.0', 'robotics', 'iot', 'dữ liệu lớn', 'big data',
        'máy học', 'học máy', 'phân tích dữ liệu', 'khoa học máy tính', 'an ninh mạng',
        'lập trình web', 'lập trình app', 'thiết kế đồ họa', 'thiết kế 3D', 'chỉnh sửa ảnh',
        'video editing', 'quay phim', 'dựng phim', 'vẽ tranh', 'hội họa', 'nghệ thuật',
        'thủ công', 'điêu khắc', 'gốm sứ', 'thêu thùa', 'may vá', 'nhạc cụ',
        'guitar', 'piano', 'trống', 'sáo', 'violon', 'kpop', 'jpop', 'âm nhạc truyền thống',
        'phim Việt', 'phim Hollywood', 'phim Hàn Quốc', 'phim Nhật Bản', 'phim kinh dị',
        'phim hài', 'phim tình cảm', 'phim hành động', 'phim khoa học viễn tưởng',
        'truyện cổ tích', 'truyện kinh dị', 'truyện khoa học', 'văn hóa', 'lịch sử',
        'địa lý', 'toán học', 'vật lý', 'hóa học', 'sinh học', 'ngôn ngữ học',
        'tiếng Trung', 'tiếng Pháp', 'tiếng Đức', 'tiếng Tây Ban Nha', 'kỹ năng sống',
        'quản lý thời gian', 'tư duy sáng tạo', 'giải quyết vấn đề', 'tâm lý học',
        'tâm lý tình yêu', 'tâm lý gia đình', 'tâm lý trẻ em', 'nấu ăn chay',
        'ẩm thực đường phố', 'món ngon mỗi ngày', 'công thức nấu ăn', 'bánh mì',
        'phở', 'bún bò', 'bánh xèo', 'thời trang vintage', 'thời trang công sở',
        'thời trang dạo phố', 'thời trang thể thao', 'xe hơi cũ', 'xe hơi mới',
        'sửa xe', 'độ xe', 'đua xe', 'bất động sản Đà Nẵng', 'bất động sản Cần Thơ',
        'nhà phố', 'đất nền', 'cho thuê nhà', 'mua bán nhà đất', 'nội thất gỗ',
        'nội thất hiện đại', 'du lịch Đà Lạt', 'du lịch Phú Quốc', 'du lịch Sapa',
        'du lịch Huế', 'du lịch Hội An', 'chăm sóc tóc', 'làm nail', 'spa',
        'massage', 'chăm sóc sức khỏe', 'tập thể dục', 'thiền', 'chạy marathon',
        'bóng chuyền', 'tennis', 'bóng bàn', 'cờ vua', 'cờ tướng', 'game mobile',
        'game pc', 'phim siêu anh hùng', 'phim cổ trang', 'phim tâm lý', 'nhạc EDM',
        'nhạc ballad', 'nhạc jazz', 'nhạc acoustic', 'sách self-help', 'sách kinh doanh',
        'sách kỹ năng', 'sách lịch sử', 'sách khoa học', 'học online', 'học lập trình',
        'học thiết kế', 'học marketing', 'học tài chính', 'học đầu tư', 'chứng khoán Việt',
        'tiền điện tử', 'bitcoin', 'forex', 'tài chính cá nhân', 'quản lý chi tiêu',
        'sức khỏe tâm thần', 'y học cổ truyền', 'thuốc nam', 'châm cứu', 'bấm huyệt',
        'yoga trị liệu', 'thể dục thẩm mỹ', 'nuôi dạy trẻ', 'giáo dục sớm',
        'tình cảm gia đình', 'kỹ năng nuôi con', 'tình yêu tuổi trẻ', 'hôn nhân hạnh phúc',
        'giao tiếp xã hội', 'kỹ năng thuyết trình', 'công nghệ xanh', 'năng lượng tái tạo',
        'môi trường', 'bảo vệ môi trường', 'nông nghiệp', 'nông nghiệp sạch',
        'trồng cây', 'làm vườn', 'chăm sóc thú cưng', 'chó mèo', 'thú cưng',
        'cá cảnh', 'chim cảnh', 'nghệ thuật đường phố', 'graffiti', 'nhảy hiện đại',
        'vũ đạo', 'khiêu vũ', 'hiphop', 'nhạc cụ dân tộc', 'đàn bầu', 'đàn tranh',
        'sáo trúc', 'phim tài liệu', 'phim chiến tranh', 'phim gia đình', 'sách thiếu nhi',
        'sách giáo khoa', 'học nhóm', 'học bổng', 'du học', 'học tiếng Thái',
        'học tiếng Nga', 'kỹ năng lãnh đạo', 'quản trị doanh nghiệp', 'startup',
        'doanh nhân', 'thương hiệu', 'quảng cáo', 'SEO', 'content marketing',
        'digital marketing', 'bán hàng online', 'mạng lưới kinh doanh', 'thương mại',
        'xuất khẩu', 'nhập khẩu', 'logistics', 'vận chuyển', 'kiến trúc hiện đại',
        'kiến trúc cổ', 'nội thất tối giản', 'phong thủy nhà ở', 'du lịch sinh thái',
        'du lịch văn hóa', 'du lịch tâm linh', 'chăm sóc sắc đẹp', 'mỹ phẩm thiên nhiên',
        'chăm sóc da mặt', 'trị mụn', 'chống lão hóa', 'tập luyện thể thao',
        'dinh dưỡng thể thao', 'chạy bộ đường dài', 'bóng đá futsal', 'game chiến thuật',
        'game nhập vai', 'phim hoạt hình Nhật', 'phim Bollywood', 'nhạc không lời',
        'sách tâm lý', 'sách triết học', 'sách văn học Việt', 'sách văn học nước ngoài',
        'học tiếng Ý', 'học tiếng Bồ Đào Nha', 'kỹ năng viết lách', 'viết blog',
        'viết sách', 'nhà văn', 'nhà thơ', 'ẩm thực chay', 'món ăn truyền thống',
        'bánh chưng', 'bánh tét', 'thời trang trẻ em', 'thời trang cao cấp',
        'xe hơi thể thao', 'xe hơi điện', 'bất động sản nghỉ dưỡng', 'nhà đất nông thôn',
        'nội thất thông minh', 'du lịch bụi', 'du lịch tự túc', 'chăm sóc da dầu',
        'chăm sóc da khô', 'sức khỏe trẻ em', 'sức khỏe người già', 'yoga cho bà bầu',
        'nuôi con bằng sữa mẹ', 'tình yêu đồng giới', 'giao tiếp công sở', 'công nghệ AI',
        'máy bay không người lái', 'drone', 'thực tế ảo', 'AR', 'VR', 'metaverse',
        'lập trình Python', 'lập trình Java', 'lập trình C++', 'thiết kế UI/UX',
        'chỉnh sửa video', 'vẽ kỹ thuật số', 'nghệ thuật thư pháp', 'nhạc indie',
        'phim độc lập', 'sách khoa học viễn tưởng', 'học từ xa', 'học nghề',
        'học nấu ăn', 'học cắt may', 'học làm bánh', 'tài chính vi mô', 'đầu tư vàng',
        'đầu tư cổ phiếu', 'sức khỏe sinh sản', 'tập thể hình', 'bóng rổ đường phố',
        'game sinh tồn', 'phim tâm lý xã hội', 'nhạc rap Việt', 'sách kinh tế',
        'học lập trình game', 'học marketing online', 'học đầu tư bất động sản',
        'chăm sóc sức khỏe tại nhà', 'y học hiện đại', 'thiền định', 'chạy bộ cộng đồng',
        'bóng đá nữ', 'game chiến lược', 'phim tài liệu lịch sử', 'nhạc acoustic Việt',
        'sách phát triển cá nhân', 'học tiếng Việt', 'kỹ năng đàm phán', 'quản lý dự án',
        'công nghệ sinh học', 'năng lượng mặt trời', 'nông nghiệp hữu cơ', 'chăm sóc cây cảnh',
        'nuôi cá cảnh', 'nghệ thuật biểu diễn', 'kịch nghệ', 'múa đương đại', 'phim ngắn',
        'sách trinh thám', 'học làm giàu', 'học kinh doanh online', 'tài chính doanh nghiệp',
        'sức khỏe tinh thần', 'tập yoga tại nhà', 'bóng chuyền bãi biển', 'game mô phỏng',
        'phim viễn tưởng', 'nhạc dân gian', 'sách lịch sử Việt Nam', 'học tiếng Ả Rập',
        'kỹ năng thuyết phục', 'quản lý nhân sự', 'công nghệ tự động hóa', 'năng lượng gió',
        'nông nghiệp thông minh', 'chăm sóc hoa lan', 'nuôi chim cảnh', 'nghệ thuật sân khấu',
        'phim tài liệu khoa học', 'nhạc truyền thống Việt', 'sách văn học cổ điển',
        'học lập trình mobile', 'học quảng cáo online', 'tài chính quốc tế', 'sức khỏe toàn diện',
        'tập luyện tại nhà', 'bóng bàn chuyên nghiệp', 'game phiêu lưu', 'phim kinh điển',
        'nhạc pop Việt', 'sách kỹ năng sống', 'học tiếng Hindi', 'kỹ năng tổ chức',
        'quản lý thời gian hiệu quả', 'công nghệ nano', 'năng lượng sạch', 'nông nghiệp bền vững',
        'chăm sóc bonsai', 'nuôi thú cưng độc lạ', 'nghệ thuật truyền thống', 'phim tài liệu xã hội',
        'nhạc quê hương', 'sách văn học hiện đại', 'học lập trình AI', 'học SEO website',
        'tài chính cá nhân thông minh', 'sức khỏe lâu dài', 'tập luyện sức bền', 'cờ vua online',
        'game thế giới mở', 'phim khoa học giả tưởng', 'nhạc trữ tình', 'sách phát triển kỹ năng',
        'học tiếng Thổ Nhĩ Kỳ', 'kỹ năng làm việc nhóm', 'quản lý rủi ro', 'công nghệ năng lượng',
        'nông nghiệp đô thị', 'chăm sóc cây ăn quả', 'nuôi bò sát', 'nghệ thuật hiện đại',
        'phim tài liệu môi trường', 'nhạc dân ca Việt', 'sách kinh doanh quốc tế',
        'học lập trình blockchain', 'học content marketing', 'tài chính bền vững', 'sức khỏe cộng đồng',
        'tập luyện chức năng', 'cờ tướng online', 'game chiến đấu', 'phim lịch sử', 'nhạc bolero',
        'sách kỹ năng lãnh đạo', 'học tiếng Indonesia', 'kỹ năng giải quyết xung đột',
        'quản lý chuỗi cung ứng', 'công nghệ thông minh', 'nông nghiệp công nghệ cao',
        'chăm sóc cây kiểng', 'nuôi thú cưng nhỏ', 'nghệ thuật cổ điển', 'phim tài liệu văn hóa',
        'nhạc cải lương', 'sách khởi nghiệp', 'học lập trình web full stack', 'học quảng cáo Facebook',
        'tài chính xanh', 'sức khỏe tự nhiên', 'tập luyện ngoài trời', 'cờ vua trẻ em',
        'game nhập vai online', 'phim tâm lý tình cảm', 'nhạc trẻ Việt', 'sách kỹ năng giao tiếp'
    ]
    

    ds_cam_xuc = {
        "1": "LIKE",
        "2": "LOVE",
        "3": "CARE",
        "4": "HAHA",
        "5": "WOW",
        "6": "SAD",
        "7": "ANGRY"
    }
    print('Chon loai cam xuc:')
    print('Nhap [1] de chay Like')
    print('Nhap [2] de chay Love')
    print('Nhap [3] de chay Care')
    print('Nhap [4] de chay Haha')
    print('Nhap [5] de chay Wow')
    print('Nhap [6] de chay Sad')
    print('Nhap [7] de chay Angry')
    print('Co the chon nhieu cam xuc (VD: 1345...)')
    chon = input('Nhap so de chon cam xuc: ').strip()
    cam_xuc_chon = [ds_cam_xuc[c] for c in chon if c in ds_cam_xuc]
    
    if not cam_xuc_chon:
        print('Khong co cam xuc nao duoc chon, su dung mac dinh LIKE')
        cam_xuc_chon = ['LIKE']
    

    vietnamese_names = generate_vietnamese_names()
    
    thanh_ngang(65)
    print(f'Bat dau thuc hien {so_nhiem_vu} nhiem vu voi {len(cookies_hop_le)} tai khoan')
    thanh_ngang(65)
    
    stt = 0
    loi_lien_tuc = 0
    cookie_index = 0
    
    while stt < so_nhiem_vu:
        try:
            cookie = cookies_hop_le[cookie_index]
            tai_khoan = thong_tin_tai_khoan[cookie_index]
            print(f'Dang su dung tai khoan: {tai_khoan["name"]} (ID: {tai_khoan["id"]})')
            
            fb = Facebook(cookie)
            info = fb.info()
            if info == 'cookieout' or info == '956' or info == '282' or info == 'spam':
                print(f'Tai khoan {tai_khoan["name"]} gap loi: {info}')
                cookies_hop_le.pop(cookie_index)
                thong_tin_tai_khoan.pop(cookie_index)
                if not cookies_hop_le:
                    print('Het tai khoan hop le, dung chuong trinh!')
                    break
                cookie_index = cookie_index % len(cookies_hop_le)
                continue
            

            tac_vu = random.choice(['ket_ban', 'tha_cam_xuc', 'tham_gia_nhom', 'binh_luan'])
            
            if tac_vu == 'ket_ban':
                ten = random.choice(vietnamese_names)
                tim_ban = fb.tim_ban(ten)
                if tim_ban.get('trangthai') == 'thatbai':
                    print(f'[LOI] Khong tim thay ban voi ten {ten}')
                    loi_lien_tuc += 1
                else:
                    ket_ban = fb.ket_ban(tim_ban['id'])
                    if ket_ban.get('trangthai') == 'thanhcong':
                        stt += 1
                        thoi_gian = datetime.now().strftime('%H:%M:%S')
                        print(f'| {stt} | {thoi_gian} | Them ban | {tim_ban["id"]} | {tim_ban["name"]}')
                        loi_lien_tuc = 0
                    else:
                        print(f'[LOI] Khong the ket ban voi {tim_ban["name"]}')
                        loi_lien_tuc += 1
            
            elif tac_vu == 'tha_cam_xuc':
                bai_viet = fb.lay_id_bai_viet()
                if bai_viet.get('trangthai') == 'thatbai':
                    print(f'[LOI] Khong tim thay bai viet')
                    loi_lien_tuc += 1
                else:
                    cam_xuc = random.choice(cam_xuc_chon)
                    tha = fb.tha_cam_xuc(bai_viet['idpost'], cam_xuc)
                    if tha.get('trangthai') == 'thanhcong':
                        stt += 1
                        thoi_gian = datetime.now().strftime('%H:%M:%S')
                        print(f'| {stt} | {thoi_gian} | Tha cam xuc {cam_xuc} | {bai_viet["idpost"]}')
                        loi_lien_tuc = 0
                    else:
                        print(f'[LOI] Khong the tha cam xuc cho bai viet {bai_viet["idpost"]}')
                        loi_lien_tuc += 1
            
            elif tac_vu == 'tham_gia_nhom':
                tu_khoa = random.choice(tu_khoa_nhom)
                nhom = fb.tim_nhom(tu_khoa)
                if nhom.get('trangthai') == 'thatbai':
                    print(f'[LOI] Khong tim thay nhom voi tu khoa {tu_khoa}')
                    loi_lien_tuc += 1
                else:
                    tham_gia = fb.tham_gia_nhom(nhom['id'])
                    if tham_gia.get('trangthai') == 'thanhcong':
                        stt += 1
                        thoi_gian = datetime.now().strftime('%H:%M:%S')
                        print(f'| {stt} | {thoi_gian} | Tham gia nhom | {nhom["id"]} | {nhom["name"]}')
                        loi_lien_tuc = 0
                    else:
                        print(f'[LOI] Khong the tham gia nhom {nhom["name"]}')
                        loi_lien_tuc += 1
            
            elif tac_vu == 'binh_luan':
                bai_viet = fb.lay_id_bai_viet()
                if bai_viet.get('trangthai') == 'thatbai':
                    print(f'[LOI] Khong tim thay bai viet')
                    loi_lien_tuc += 1
                else:
                    noi_dung = random.choice(danh_sach_binh_luan)
                    binh_luan = fb.binh_luan(bai_viet['idpost'], noi_dung)
                    if binh_luan.get('trangthai') == 'thanhcong':
                        stt += 1
                        thoi_gian = datetime.now().strftime('%H:%M:%S')
                        print(f'| {stt} | {thoi_gian} | Binh luan | {bai_viet["idpost"]} | {noi_dung}')
                        loi_lien_tuc = 0
                    else:
                        print(f'[LOI] Khong the binh luan cho bai viet {bai_viet["idpost"]}')
                        loi_lien_tuc += 1
            

            if loi_lien_tuc >= 500:
                print('Qua nhieu loi lien tuc, dung chuong trinh!')
                break
           
            cookie_index = (cookie_index + 1) % len(cookies_hop_le)
            

            doi_giay(delay)
            
        except Exception as e:
            print(f'Loi khong xac dinh: {str(e)}')
            loi_lien_tuc += 1
            if loi_lien_tuc >= 10:
                print('Qua nhieu loi lien tuc, dung chuong trinh!')
                break
            doi_giay(delay)
    
    print(f'\nHoan thanh! Da thuc hien {stt}/{so_nhiem_vu} nhiem vu')
    print(f'So lan loi: {loi_lien_tuc}')

if __name__ == "__main__":
    main()


