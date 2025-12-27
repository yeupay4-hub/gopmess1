import requests
import os
import re
import json
import random
import base64
import uuid
import time
from datetime import datetime
import platform

try:
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
except:
    os.system('pip install pystyle requests platform colorama beautifulsoup4 selenium mechanize webdriver_manager aiohttp flask')
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

try:
    import pyfiglet
    from termcolor import colored
except:
    os.system('pip install pyfiglet termcolor')
    import pyfiglet
    from termcolor import colored

def clear():
    if platform.system().lower() == 'linux':
        os.system('clear')
    else:
        os.system('cls')

def banner():
    clear()
    ascii_banner = pyfiglet.figlet_format("   Mdung", font="slant")
    print(colored(ascii_banner, 'cyan', attrs=['bold']))
    print("=" * 60)
    print(colored("       Tool Nuôi Facebook Treo Card Đa Cookie By Mdung 🧸", 'white', attrs=['bold']))
    print("=" * 60)
    print(colored("➩ Telegram: https://t.me/ctevclwar", 'green'))
    print(colored("➩ FaceBook 1: https://www.facebook.com/daikafi5", 'green'))
    print(colored("➩ FaceBook 2: https://www.facebook.com/profile.php?id=61570431072611", 'green'))
    print("=" * 60)

def doi_giay(value):
    print(f'Đợi {value} giây...')
    time.sleep(value)

def kiem_tra_cookie(cookie):
    try:
        if 'c_user=' not in cookie:
            return {"status": "failed", "msg": "Cookie không chứa user_id"}
        
        user_id = cookie.split('c_user=')[1].split(';')[0]
        url = f"https://graph2.facebook.com/v3.3/{user_id}/picture?redirect=0"
        response = requests.get(url, timeout=30)
        check_data = response.json()

        if not check_data.get('data', {}).get('height') or not check_data.get('data', {}).get('width'):
            return {"status": "failed", "msg": "Cookie không hợp lệ"}

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
        return {"status": "failed", "msg": f"Lỗi xảy ra: {str(e)}"}

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
        'Phương', 'Bì', 'Hầu', 'Sầm'
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
        'Tiên', 'Trang', 'Trinh', 'Tú'
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
        'Hiệp', 'Huy', 'Khai', 'Nhi', 'Quý', 'Thắng'
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

def nhap_danh_sach_cookie():
    banner()
    cookie_list = []
    stt = 1
    while True:
        ck = input(colored(f"Nhập cookie thứ {stt} (Ấn 'enter' để dừng nhập): ", 'yellow', attrs=['bold'])).strip()
        if ck.lower() in ['', 'enter']:
            print('Đã lưu cookie')
            if not cookie_list:
                print('Không có cookie nào được lưu')
            else:
                for i, c in enumerate(cookie_list, 1):
                    print(f'  {i}. {c[:50]}...')
            break
        if 'c_user=' in ck:
            cookie_list.append(ck)
            stt += 1
    return cookie_list

def main():
    banner()
    
    # Nhập cookie thủ công
    print(colored("=== NHẬP COOKIE ===", 'cyan', attrs=['bold']))
    print()
    
    cookies = nhap_danh_sach_cookie()
    if not cookies:
        print(colored('Không có cookie nào được nhập!', 'red'))
        return
    
    # Kiểm tra cookie
    cookies_hop_le = []
    thong_tin_tai_khoan = []
    print(colored("\nKIỂM TRA COOKIE", 'yellow', attrs=['bold']))
    for i, cookie in enumerate(cookies, 1):
        check = kiem_tra_cookie(cookie)
        if check['status'] == 'success':
            print(colored(f"   [{i}] ✅ Live - {check['name']} (ID: {check['user_id']})", 'green'))
            cookies_hop_le.append(cookie)
            thong_tin_tai_khoan.append({'name': check['name'], 'id': check['user_id']})
        else:
            print(colored(f"   [{i}] ❌ Die - {check['msg']}", 'red'))
    
    if not cookies_hop_le:
        print(colored('Không có cookie nào live, thoát chương trình!', 'red'))
        return

    cookies_hop_le = []
    thong_tin_tai_khoan = []
    print(colored("\n2. KIỂM TRA COOKIE", 'yellow', attrs=['bold']))
    for i, cookie in enumerate(cookies, 1):
        check = kiem_tra_cookie(cookie)
        if check['status'] == 'success':
            print(colored(f"   [{i}] ✅ Live - {check['name']} (ID: {check['user_id']})", 'green'))
            cookies_hop_le.append(cookie)
            thong_tin_tai_khoan.append({'name': check['name'], 'id': check['user_id']})
        else:
            print(colored(f"   [{i}] ❌ Die - {check['msg']}", 'red'))
    
    if not cookies_hop_le:
        print(colored('Không có cookie nào live, thoát chương trình!', 'red'))
        return
    
    # Nhập cấu hình
    print(colored("\n3. THỰC HÀNH", 'yellow', attrs=['bold']))
    
    while True:
        try:
            delay = int(input(colored('   Nhập delay chung (giây): ', 'white')))
            if delay > 0:
                break
            else:
                print(colored('   Vui lòng nhập số lớn hơn 0', 'red'))
        except:
            print(colored('   Vui lòng nhập số', 'red'))
    
    while True:
        try:
            so_nhiem_vu = int(input(colored('   Nhập số nhiệm vụ muốn thực hiện: ', 'white')))
            if so_nhiem_vu > 0:
                break
            else:
                print(colored('   Vui lòng nhập số lớn hơn 0', 'red'))
        except:
            print(colored('   Vui lòng nhập số', 'red'))
    
    # Nhập danh sách bình luận
    danh_sach_binh_luan = []
    print(colored("\n4. NHẬP NỘI DUNG BÌNH LUẬN", 'yellow', attrs=['bold']))
    i = 1
    while True:
        cmt = input(colored(f'   Nhập nội dung bình luận số {i} (nhập trống để kết thúc): ', 'white')).strip()
        if cmt == '':
            break
        danh_sach_binh_luan.append(cmt)
        i += 1
    
    if not danh_sach_binh_luan:
        danh_sach_binh_luan = ['👍', '🤗', '❤️', '😊', '🥰']
        print(colored('   Sử dụng bình luận mặc định!', 'yellow'))
    
    # Từ khóa nhóm (rút gọn)
    tu_khoa_nhom = [
        'công nghệ', 'kinh doanh', 'giáo dục', 'y tế', 'thể thao', 'giải trí',
        'du lịch', 'ẩm thực', 'thời trang', 'xe cộ', 'bất động sản', 'tài chính',
        'marketing', 'thiết kế', 'lập trình', 'nhiếp ảnh', 'âm nhạc', 'phim ảnh',
        'sách vở', 'học tập', 'làm đẹp', 'sức khỏe', 'gia đình', 'tình yêu'
    ]
    
    # Chọn cảm xúc
    ds_cam_xuc = {
        "1": "LIKE",
        "2": "LOVE",
        "3": "CARE",
        "4": "HAHA",
        "5": "WOW",
        "6": "SAD",
        "7": "ANGRY"
    }
    print(colored("\n5. CHỌN CẢM XÚC", 'yellow', attrs=['bold']))
    print(colored('   [1] Like 👍', 'white'))
    print(colored('   [2] Love ❤️', 'white'))
    print(colored('   [3] Care 💤', 'white'))
    print(colored('   [4] Haha 🎃', 'white'))
    print(colored('   [5] WOW 😧', 'white'))
    print(colored('   [6] Sad 🥹', 'white'))
    print(colored('   [7] Angry 😡', 'white'))
    print(colored('   Có thể chọn nhiều cảm xúc (VD: 1345...)', 'green'))
    chon = input(colored('   Nhập số để chọn cảm xúc: ', 'white')).strip()
    cam_xuc_chon = [ds_cam_xuc[c] for c in chon if c in ds_cam_xuc]
    
    if not cam_xuc_chon:
        print(colored('   Không có cảm xúc nào được chọn, sử dụng mặc định LIKE', 'yellow'))
        cam_xuc_chon = ['LIKE']
    
    # Tạo tên Việt
    vietnamese_names = generate_vietnamese_names()
    
    print(colored(f"\n6. BẮT ĐẦU THỰC HIỆN", 'cyan', attrs=['bold']))
    print(colored(f"   Số nhiệm vụ: {so_nhiem_vu}", 'white'))
    print(colored(f"   Số tài khoản: {len(cookies_hop_le)}", 'white'))
    print(colored(f"   Delay: {delay} giây", 'white'))
    print("=" * 60)
    
    stt = 0
    loi_lien_tuc = 0
    cookie_index = 0
    
    while stt < so_nhiem_vu:
        try:
            cookie = cookies_hop_le[cookie_index]
            tai_khoan = thong_tin_tai_khoan[cookie_index]
            print(colored(f'Đang sử dụng tài khoản: {tai_khoan["name"]} (ID: {tai_khoan["id"]})', 'cyan'))
            
            fb = Facebook(cookie)
            info = fb.info()
            if info == 'cookieout' or info == '956' or info == '282' or info == 'spam':
                print(colored(f'Tài khoản {tai_khoan["name"]} gặp lỗi: {info}', 'red'))
                cookies_hop_le.pop(cookie_index)
                thong_tin_tai_khoan.pop(cookie_index)
                if not cookies_hop_le:
                    print(colored('Hết tài khoản hợp lệ, dừng chương trình!', 'red'))
                    break
                cookie_index = cookie_index % len(cookies_hop_le)
                continue
            
            # Chọn tác vụ ngẫu nhiên
            tac_vu = random.choice(['ket_ban', 'tha_cam_xuc', 'tham_gia_nhom', 'binh_luan'])
            
            if tac_vu == 'ket_ban':
                ten = random.choice(vietnamese_names)
                tim_ban = fb.tim_ban(ten)
                if tim_ban.get('trangthai') == 'thatbai':
                    print(colored(f'[LOI] Không tìm thấy bạn với tên {ten}', 'red'))
                    loi_lien_tuc += 1
                else:
                    ket_ban = fb.ket_ban(tim_ban['id'])
                    if ket_ban.get('trangthai') == 'thanhcong':
                        stt += 1
                        thoi_gian = datetime.now().strftime('%H:%M:%S')
                        print(colored(f'| {stt} | {thoi_gian} | Thêm bạn | {tim_ban["id"]} | {tim_ban["name"]}', 'green'))
                        loi_lien_tuc = 0
                    else:
                        print(colored(f'[LOI] Không thể kết bạn với {tim_ban["name"]}', 'red'))
                        loi_lien_tuc += 1
            
            elif tac_vu == 'tha_cam_xuc':
                bai_viet = fb.lay_id_bai_viet()
                if bai_viet.get('trangthai') == 'thatbai':
                    print(colored(f'[LOI] Không tìm thấy bài viết', 'red'))
                    loi_lien_tuc += 1
                else:
                    cam_xuc = random.choice(cam_xuc_chon)
                    tha = fb.tha_cam_xuc(bai_viet['idpost'], cam_xuc)
                    if tha.get('trangthai') == 'thanhcong':
                        stt += 1
                        thoi_gian = datetime.now().strftime('%H:%M:%S')
                        print(colored(f'| {stt} | {thoi_gian} | Thả cảm xúc {cam_xuc} | {bai_viet["idpost"]}', 'green'))
                        loi_lien_tuc = 0
                    else:
                        print(colored(f'[LOI] Không thể thả cảm xúc cho bài viết {bai_viet["idpost"]}', 'red'))
                        loi_lien_tuc += 1
            
            elif tac_vu == 'tham_gia_nhom':
                tu_khoa = random.choice(tu_khoa_nhom)
                nhom = fb.tim_nhom(tu_khoa)
                if nhom.get('trangthai') == 'thatbai':
                    print(colored(f'[LOI] Không tìm thấy nhóm với từ khóa {tu_khoa}', 'red'))
                    loi_lien_tuc += 1
                else:
                    tham_gia = fb.tham_gia_nhom(nhom['id'])
                    if tham_gia.get('trangthai') == 'thanhcong':
                        stt += 1
                        thoi_gian = datetime.now().strftime('%H:%M:%S')
                        print(colored(f'| {stt} | {thoi_gian} | Tham gia nhóm | {nhom["id"]} | {nhom["name"]}', 'green'))
                        loi_lien_tuc = 0
                    else:
                        print(colored(f'[LOI] Không thể tham gia nhóm {nhom["name"]}', 'red'))
                        loi_lien_tuc += 1
            
            elif tac_vu == 'binh_luan':
                bai_viet = fb.lay_id_bai_viet()
                if bai_viet.get('trangthai') == 'thatbai':
                    print(colored(f'[LOI] Không tìm thấy bài viết', 'red'))
                    loi_lien_tuc += 1
                else:
                    noi_dung = random.choice(danh_sach_binh_luan)
                    binh_luan = fb.binh_luan(bai_viet['idpost'], noi_dung)
                    if binh_luan.get('trangthai') == 'thanhcong':
                        stt += 1
                        thoi_gian = datetime.now().strftime('%H:%M:%S')
                        print(colored(f'| {stt} | {thoi_gian} | Bình luận | {bai_viet["idpost"]} | {noi_dung}', 'green'))
                        loi_lien_tuc = 0
                    else:
                        print(colored(f'[LOI] Không thể bình luận cho bài viết {bai_viet["idpost"]}', 'red'))
                        loi_lien_tuc += 1
            
            # Kiểm tra lỗi liên tục
            if loi_lien_tuc >= 50:
                print(colored('Quá nhiều lỗi liên tục, dừng chương trình!', 'red'))
                break
            
            # Chuyển sang cookie tiếp theo
            cookie_index = (cookie_index + 1) % len(cookies_hop_le)
            
            # Delay
            if stt < so_nhiem_vu:
                doi_giay(delay)
            
        except Exception as e:
            print(colored(f'Lỗi không xác định: {str(e)}', 'red'))
            loi_lien_tuc += 1
            if loi_lien_tuc >= 10:
                print(colored('Quá nhiều lỗi liên tục, dừng chương trình!', 'red'))
                break
            doi_giay(delay)
    
    print(colored(f"\nHOÀN THÀNH!", 'cyan', attrs=['bold']))
    print(colored(f"Đã thực hiện: {stt}/{so_nhiem_vu} nhiệm vụ", 'white'))
    print(colored(f"Số lần lỗi: {loi_lien_tuc}", 'white'))
    print("=" * 60)
    input(colored("Nhấn Enter để thoát...", 'yellow'))

if __name__ == "__main__":
    main()
