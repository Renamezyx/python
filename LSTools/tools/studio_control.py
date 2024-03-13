import ast
import json
import os
import re

from enums.studio_battle_enum import BattleStatusEnum
from utils.json_file_handler import JSONFileHandler


class StudioControl:
    def __init__(self):
        self.studio_file_path = "C:\\Program Files\\TikTok LIVE Studio"
        self.studio_data_path = os.path.join(os.path.expandvars('%appdata%'), "TikTok LIVE Studio")

    @property
    def version(self):
        folders = [os.path.join(self.studio_file_path, name) for name in
                   os.listdir(self.studio_file_path) if
                   os.path.isdir(os.path.join(self.studio_file_path, name))]
        curr_version_path = max(folders, key=self.get_folder_size)
        return curr_version_path.split('\\')[-1]

    @property
    def branch(self):
        package = JSONFileHandler.read_json_file(
            file_path=os.path.join(studio.studio_file_path, studio.version, 'resources\\app\\package.json'))
        branch = package['branch']
        return branch

    def open_dir(self, path):
        os.system('start "" "{0}"'.format(path))

    def get_folder_size(self, folder_path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                total_size += os.path.getsize(file_path)
        return total_size

    @property
    def link_mic_battle_pb_by_log(self):
        with open(os.path.join(self.studio_data_path, "logs", "renderer.log"), "r", encoding="utf-8") as log_file:
            pb_list = []
            result = []
            pb_re_str = r'LinkMicBattlePB (.*)'
            for line in log_file.readlines():
                res = re.search(pb_re_str, line)
                if res:
                    pb_list.append(res.group(1))
            for i in pb_list:
                i = re.sub(r'(\w+): ', r'"\1":', i)
                i = i.replace("'", '"')
                # i = json.dumps(i)
                result.append(i)
        return result


studio = StudioControl()


def open_logs_dir():
    studio.open_dir("{0}\\logs".format(studio.studio_data_path))


def open_language_dir():
    if studio.version:
        studio.open_dir(
            '{0}\\{1}\\resources\\app\\locales\\Live_Studio'.format(studio.studio_file_path, studio.version))


def switch_branch():
    if studio.branch == "studio/release/stable-0.53":
        value = "1"
    else:
        value = "studio/release/stable-0.53"
    JSONFileHandler.update_json(
        file_path=os.path.join(studio.studio_file_path, studio.version, 'resources\\app\\package.json'),
        key="branch", value=value)
    return value


def update_effects():
    local_store_path = os.path.join(studio.studio_data_path, "TTStore", "localStore.json")
    if os.path.exists(local_store_path):
        os.remove(local_store_path)


def clear_screen():
    store_path = os.path.join(studio.studio_data_path, "TTStore", "store.json")
    JSONFileHandler.delete_json_key(store_path, "source")


def generate_finsh_pk():
    battle_status_dict = {member.value: member.name for member in BattleStatusEnum}
    print(battle_status_dict)
    end_pb_str = studio.link_mic_battle_pb_by_log[-1]
    print(end_pb_str)
    end_pb = json.loads(end_pb_str)

    if end_pb["battle_settings"]["status"] == 2:
        channel_id = end_pb["battle_settings"]["channel_id"]
        battle_id = end_pb["battle_settings"]["battle_id"]
        other_party_left = "false" if len(end_pb["anchors_info"]) == 2 else "true"
        other_party_user_id = ",".join([anchor_info["key"] for anchor_info in end_pb["anchors_info"][1:]])
        params = f"""
        aid: 8311
        app_name: tiktok_live_studio
        device_id: 7304628306396431874
        install_id: 7324947231760729857
        channel: studio
        version_code: 0.51
        language: en
        app_language: en
        webcast_language: en
        priority_region: mk
        webcast_sdk_version: 510
        live_mode: 6
        channel_id: {channel_id}
        battle_id: {battle_id}
        cut_short: false
        other_party_left: {other_party_left}
        other_party_user_id: {other_party_user_id}
        finish_source: normal_finish
        finish_is_background: 0
        finish_network_quality: 1
        finish_cur_bitrate: 5400
        finish_is_sdk: 1
        """.replace(" ", '')
        return params
    else:
        return battle_status_dict[end_pb["battle_settings"]["status"]]


if __name__ == '__main__':
    print(generate_finsh_pk())
