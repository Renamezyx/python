import os

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


studio = StudioControl()


def open_logs_dir():
    studio.open_dir("{0}\\logs".format(studio.studio_data_path))


def open_language_dir():
    if studio.version:
        studio.open_dir(
            '{0}\\{1}\\resources\\app\\locales\\Live_Studio'.format(studio.studio_file_path, studio.version))


def switch_branch():
    if studio.branch == "studio/release/stable-0.53":
        value = ""
    else:
        value = "studio/release/stable-0.53"
    JSONFileHandler.update_json(
        file_path=os.path.join(studio.studio_file_path, studio.version, 'resources\\app\\package.json'),
        key="branch", value=value)
    return value


def update_effects():
    local_store_path = os.path.join(studio.studio_data_path, "TTStore", "localStore.json")
    os.remove(local_store_path)
    if os.path.exists(local_store_path):
        os.remove(local_store_path)


def clear_screen():
    store_path = os.path.join(studio.studio_data_path, "TTStore", "store.json")
    JSONFileHandler.delete_json_key(store_path, "source")


if __name__ == '__main__':
    update_effects()
