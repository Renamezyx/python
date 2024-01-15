rules = {
    "CPU_electron进程": r"cpu_avg[\s\S]+?tiktok_live_studio: (.*)\n",
    "CPU_MediaSDK进程": r"cpu_avg[\s\S]+?mediasdk_server: (.*)\n",
    "CPU_整体": r"livestudio:[\s\S]+?CPU占用: (.*)%",
    "GPU3D_electron进程-A卡独显数据": r"",
    "GPU3D_MediaSDK进程-A卡独显数据": r"gpu_3d_avg[\s\S]+?mediasdk_server_AMD_Radeon_RX_6700M: (.*)\n",
    "GPU3D_整体": r"livestudio:[\s\S]+?GPU 3D 占用: [\s\S]+?AMD_Radeon_RX_6700M: (.*)%",
    "gpu_encode": r"",
    "内存占用(MB)_electron进程": r"memory_avg[\s\S]+?tiktok_live_studio: (.*)\n",
    "内存占用(MB)_sdk进程": r"memory_avg[\s\S]+?mediasdk_server: (.*)\n",
    "内存占用(MB)_整体": r"livestudio:[\s\S]+?内存占用： (.*)MB",
    "数据留存": "",
    "编码帧率": "主画布编码帧率： (.*)",
    "画布渲染帧率": "渲染帧率： (.*)"
}

data_file_dirpath = r"C:\Users\Admin\Downloads\original-data"
