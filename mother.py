import subprocess

# 引数として渡すデータのパス
data_input = r"D:\backup\2.ターゲット（完全版）\1201-1300"

i=""

if i== "" or i==1: #webpを変換
    # 実行するPythonス  クリプトのパス
    script_path_0 = r"create_video\0.webp_to_png.py"
    subprocess.run(["python", script_path_0, data_input])

if i== "" or i==2: #音声ファイル作成
    script_path_1 = r"create_video\1.text_to_speech.py"
    subprocess.run(["python", script_path_1, data_input])

if i== "" or i==3: #スライド作成
    script_path_2 = r"create_video\2.do_VBA.py"
    subprocess.run(["python", script_path_2, data_input])

if i== "" or i==4:#ビデオ作成
    script_path_3 = r"create_video\3.audioとimageからmovie作成.py"
    subprocess.run(["python", script_path_3, data_input])
