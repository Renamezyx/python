import time

import requests

cookies = {
    'store-idc': 'alisg',
    'store-country-code': 'vn',
    'store-country-code-src': 'uid',
    'tt-target-idc': 'alisg',
    'tt_csrf_token': 'pwk3ZeOK-cSSHNuMJv_1BMdrF9ZZaqD1smuM',
    'ttwid': '1%7CK-jfuT78buPXjt-vjbiO2hxNhyc5uNVAqvd0ESsJWkg%7C1706685771%7Cba55523e261b1b5c4d596223927a9495ed7d34aa8f11b4e43769d6e21deef930',
    's_v_web_id': 'verify_ls1gncg4_k88EyyBH_5kaV_4z3i_AkP8_FrlY91lgJrB4',
    'd_ticket': '773f9fac38e1d8b5cb2f41b1f84d7b3a4a373',
    'multi_sids': '7200687727124251675%3A163fa8baa4cdde7455410a2f856d52b7',
    'cmpl_token': 'AgQQAPOFF-RO0rPTFfHJ810i_9hsCYQWf4A3YNGQrw',
    'passport_auth_status': '57b861b137b29b08fdb5b69c61c1eae8%2C',
    'passport_auth_status_ss': '57b861b137b29b08fdb5b69c61c1eae8%2C',
    'tt_chain_token': 'E9hbdzn15M8TpTyZxfEMdw==',
    'passport_csrf_token': '790debeaf2d6f09f93cbc47af83b71e0',
    'passport_csrf_token_default': '790debeaf2d6f09f93cbc47af83b71e0',
    'sid_guard': 'ebec94da39d198a8de9345e08f70c9e1%7C1706685791%7C5183999%7CSun%2C+31-Mar-2024+07%3A23%3A10+GMT',
    'uid_tt': '3c55461fe2dc28d3c160ccf00a76fd601cb81433f34023ea6cbdb61b0847591c',
    'uid_tt_ss': '3c55461fe2dc28d3c160ccf00a76fd601cb81433f34023ea6cbdb61b0847591c',
    'sid_tt': 'ebec94da39d198a8de9345e08f70c9e1',
    'sessionid': 'ebec94da39d198a8de9345e08f70c9e1',
    'sessionid_ss': 'ebec94da39d198a8de9345e08f70c9e1',
    'sid_ucp_v1': '1.0.0-KGVmOGQxOWIwZDM3N2Y4MGU4YjBmZTcyNGJmOGNlNzMzYWVhZTUwMzQKGAibiIaO5Or-9mMQ3-rnrQYY90A4BkCACBADGgZtYWxpdmEiIGViZWM5NGRhMzlkMTk4YThkZTkzNDVlMDhmNzBjOWUx',
    'ssid_ucp_v1': '1.0.0-KGVmOGQxOWIwZDM3N2Y4MGU4YjBmZTcyNGJmOGNlNzMzYWVhZTUwMzQKGAibiIaO5Or-9mMQ3-rnrQYY90A4BkCACBADGgZtYWxpdmEiIGViZWM5NGRhMzlkMTk4YThkZTkzNDVlMDhmNzBjOWUx',
    'tt-target-idc-sign': 'jKLqoQkWoF_L9rNaQVDekpIFfydtUQrbn2NJLeR0vS8sQ2v6rq7IwC6CTq5JAytPfcSGCU68BMi0pEITOZ07WtLooyr8WTlvvcjb1GAN1hY4fsblB5VBc3-jOGbIOSXFxk6_ulAJF4rdCEsnxrv5dH5NdHnNQ9FKCEvDrfHuyZ4f5CpAErGxuVuhxdS9JMNt82aaqaAeJ_bKInFIq2tL8LM69dTUzlUJJ_9umQMD4Tdkiun07pKPkgAad8KtpHZG4rQhOt3oWjRHlCezWEifxbJMoEBLrOg5oJnL3c1mG9gezOv0FxlwkwE8bMFXbq8MgTZBf7HWUzS0-6xUm95J6hwq85hgcLiJwRUq6ruw50Kguj7t3qIoWzNZ8eP0hIUgjwczXRn9zZ1e9c8sEmCkWfFrRWDvI11h9QSQQ44ezxHyQLMVMnFvQtIO1KpWRolrUuWGUFpSenCR3JiGadKR6oaPTLOa-Mx8fm8NmBlCNCL6fWu4rJW6vYaF2j07xrFk',
    'odin_tt': '9e606e229c0a654fbd979b72d8390c76e733383eadcedb682735537581dd6624950fb392f104972aa3f8a93633898817a6df69aadc3aa39335265e6fac0af2aaf35b15a9efc829632ab88a419dd1597d',
    'msToken': '_YdKZMg43R5o7ABj3Pm8TskBaJ9weAZULurNdblWGP8IjFiQbQ48f66sCeatNLS3f4_i6LtK3BsSU---gyjICoNB44WnHzB_v8tpfI83CF2C',
}

headers = {
    'Host': 'webcast22-normal-c-alisg.tiktokv.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json',
    'X-TT-ENV': 'ppe_guess',
    'X-USE-PPE': '1',
    'sdk_aid': '8311',
    'x-ss-stub': '3ef13128eddd429378ca24f2eb624247',
    'x-tt-store-region': 'vn',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'empty',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) TikTokLIVEStudio/0.52.0 Chrome/104.0.5112.102 Electron/20.1.0-tt.8.develop.tmp.40 TTElectron/20.1.0-tt.8.develop.tmp.40 Safari/537.36',
    'Accept-Language': 'zh-CN',
    'X-Argus': 'lAwuLWvG+UX4PJL/TEJumDTSGbWqLU3qggm8628waI1VLr3lQKyhjk7a49sre4x/LjbOky8JhqOLPYi9y1UJkFPFEOPAqHGiKwtM2vbs2G9go5pL6tUuWE1SB4+PWJQ0aQa6ecQzTTvspT3coxHCgfGIMNMdgk1QifZzYWrAGj/tTJRR/QudPRyedMDMxanyU/MXrqyJcXcrXSJEPPt6QWsZtOxyhRzAXTBl2DvcIoiecVqydT4sNOIEA8EaWcWvnYw=',
    'X-Khronos': '1706690528',
    'X-Ladon': '/RUAAGf2Im8xF+t3qEJdR1FwBj8lfBw/P/oXUt+Y2vOoQ1gf',
}

params = {
    'aid': '8311',
    'language': 'en',
    'app_language': 'en',
    'webcast_language': 'en',
    'device_id': '7304628306396431874',
    'priority_region': 'vn',
    'device_platform': 'windows',
    'version_code': '0.52.0',
    'webcast_sdk_version': '520',
    'live_mode': '6',
}


def create_guess():
    json_data = {
        'bet_duration_in_second': 300,
        'room_id_str': '7330159535892171527',
        'template_id': 2,
    }
    response = requests.post(
        'https://webcast22-normal-c-alisg.tiktokv.com/webcast/game_revenue/guess/create_guess/',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    if response.status_code == 200:
        return response.json()["data"]["round_id_str"]
    return None


def get_guess_info(room_id_str, round_id_str):
    headers = {
        'Host': 'webcast22-normal-c-alisg.tiktokv.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-TT-ENV': 'ppe_guess',
        'X-USE-PPE': '1',
        'sdk_aid': '8311',
        'x-tt-store-region': 'vn',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Dest': 'empty',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) TikTokLIVEStudio/0.52.0 Chrome/104.0.5112.102 Electron/20.1.0-tt.8.develop.tmp.40 TTElectron/20.1.0-tt.8.develop.tmp.40 Safari/537.36',
        'Accept-Language': 'zh-CN',
        # 'Cookie': 'store-idc=alisg; store-country-code=vn; store-country-code-src=uid; tt-target-idc=alisg; tt_csrf_token=pwk3ZeOK-cSSHNuMJv_1BMdrF9ZZaqD1smuM; ttwid=1%7CK-jfuT78buPXjt-vjbiO2hxNhyc5uNVAqvd0ESsJWkg%7C1706685771%7Cba55523e261b1b5c4d596223927a9495ed7d34aa8f11b4e43769d6e21deef930; s_v_web_id=verify_ls1gncg4_k88EyyBH_5kaV_4z3i_AkP8_FrlY91lgJrB4; d_ticket=773f9fac38e1d8b5cb2f41b1f84d7b3a4a373; multi_sids=7200687727124251675%3A163fa8baa4cdde7455410a2f856d52b7; cmpl_token=AgQQAPOFF-RO0rPTFfHJ810i_9hsCYQWf4A3YNGQrw; passport_auth_status=57b861b137b29b08fdb5b69c61c1eae8%2C; passport_auth_status_ss=57b861b137b29b08fdb5b69c61c1eae8%2C; tt_chain_token=E9hbdzn15M8TpTyZxfEMdw==; passport_csrf_token=790debeaf2d6f09f93cbc47af83b71e0; passport_csrf_token_default=790debeaf2d6f09f93cbc47af83b71e0; sid_guard=ebec94da39d198a8de9345e08f70c9e1%7C1706685791%7C5183999%7CSun%2C+31-Mar-2024+07%3A23%3A10+GMT; uid_tt=3c55461fe2dc28d3c160ccf00a76fd601cb81433f34023ea6cbdb61b0847591c; uid_tt_ss=3c55461fe2dc28d3c160ccf00a76fd601cb81433f34023ea6cbdb61b0847591c; sid_tt=ebec94da39d198a8de9345e08f70c9e1; sessionid=ebec94da39d198a8de9345e08f70c9e1; sessionid_ss=ebec94da39d198a8de9345e08f70c9e1; sid_ucp_v1=1.0.0-KGVmOGQxOWIwZDM3N2Y4MGU4YjBmZTcyNGJmOGNlNzMzYWVhZTUwMzQKGAibiIaO5Or-9mMQ3-rnrQYY90A4BkCACBADGgZtYWxpdmEiIGViZWM5NGRhMzlkMTk4YThkZTkzNDVlMDhmNzBjOWUx; ssid_ucp_v1=1.0.0-KGVmOGQxOWIwZDM3N2Y4MGU4YjBmZTcyNGJmOGNlNzMzYWVhZTUwMzQKGAibiIaO5Or-9mMQ3-rnrQYY90A4BkCACBADGgZtYWxpdmEiIGViZWM5NGRhMzlkMTk4YThkZTkzNDVlMDhmNzBjOWUx; tt-target-idc-sign=jKLqoQkWoF_L9rNaQVDekpIFfydtUQrbn2NJLeR0vS8sQ2v6rq7IwC6CTq5JAytPfcSGCU68BMi0pEITOZ07WtLooyr8WTlvvcjb1GAN1hY4fsblB5VBc3-jOGbIOSXFxk6_ulAJF4rdCEsnxrv5dH5NdHnNQ9FKCEvDrfHuyZ4f5CpAErGxuVuhxdS9JMNt82aaqaAeJ_bKInFIq2tL8LM69dTUzlUJJ_9umQMD4Tdkiun07pKPkgAad8KtpHZG4rQhOt3oWjRHlCezWEifxbJMoEBLrOg5oJnL3c1mG9gezOv0FxlwkwE8bMFXbq8MgTZBf7HWUzS0-6xUm95J6hwq85hgcLiJwRUq6ruw50Kguj7t3qIoWzNZ8eP0hIUgjwczXRn9zZ1e9c8sEmCkWfFrRWDvI11h9QSQQ44ezxHyQLMVMnFvQtIO1KpWRolrUuWGUFpSenCR3JiGadKR6oaPTLOa-Mx8fm8NmBlCNCL6fWu4rJW6vYaF2j07xrFk; odin_tt=9e606e229c0a654fbd979b72d8390c76e733383eadcedb682735537581dd6624950fb392f104972aa3f8a93633898817a6df69aadc3aa39335265e6fac0af2aaf35b15a9efc829632ab88a419dd1597d; msToken=__rUhAOJUi195c2dbb6sDu2Yp8Lq1Xqajk4h0wZ2qq5MrfFsfEhwYxQNFd998moRnWeVMvpYv0xsenzc3CVZ5ngGOAlQBDoVpttYN2gNZp1-',
        'X-Argus': '6mvRUmhUhrU8WLMF5uShVIGe09xoW3EmybQ50/xEQImSe8aJ9ueAtnD66jXI/YLJcIrn2Bp4odPqjmp3ofzYxcMZiACY0fOhmBs8c3psl8k1HE6aIhgR+wFkIO126JeYNsd4ytYVlK4mHOT44QJ7K9Mzxfr44rcmF1dNVnciy6rcz1I+b3G3YE+WqDrKqskDOMLL7G5wng6AMiGCpC2dBFclr+9EAHiDjl6jIL2xUS2doduSoERMzblT3VDuBzupFCs=',
        'X-Khronos': '1706691520',
        'X-Ladon': 'CFIAAC66kGwjhy874pEcac/1Njtq7wtuxxk4m1Ua8eiRjezl',
    }
    params = {
        'aid': '8311',
        'language': 'en',
        'app_language': 'en',
        'webcast_language': 'en',
        'device_id': '7304628306396431874',
        'priority_region': 'vn',
        'device_platform': 'windows',
        'version_code': '0.52.0',
        'webcast_sdk_version': '520',
        'live_mode': '6',
        'room_id_str': room_id_str,
        'round_id_str': round_id_str,
    }
    response = requests.get(
        'https://webcast22-normal-c-alisg.tiktokv.com/webcast/game_revenue/guess/get_guess_info/',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    if response.status_code == 200:
        print(response.json())
        return response.json()["data"]["guess_round"]["guess_options"][0]["option_id_str"]
    return None


def input_answer(option_idx, room_id_str, round_id_str):
    json_data = {
        'option_idx': str(option_idx),
        'room_id_str': str(room_id_str),
        'round_id_str': str(round_id_str),
    }
    response = requests.post(
        'https://webcast22-normal-c-alisg.tiktokv.com/webcast/game_revenue/guess/input_answer/',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    if response.status_code == 200:
        return response.json()
    return None


if __name__ == '__main__':
    i = 50
    while i > 0:
        i = i - 1
        round_id_str = create_guess()
        time.sleep(2)
        option_idx = get_guess_info('7330159535892171527', round_id_str)
        time.sleep(2)
        res = input_answer(option_idx, '7330159535892171527', round_id_str)
        print(res)
