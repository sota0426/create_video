import subprocess

# 引数として渡すデータのパス
data_input = r"C:\Users\User\Desktop\english"

i="2"

if i== "" or i==1: #webpを変換
    # 実行するPythonス  クリプトのパス
    script_path_0 = r"1.text_to_speech_ENG.py"
    subprocess.run(["python", script_path_0, data_input])

if i== "" or i==2: #音声ファイル作成
    script_path_1 = r"1.text_to_speech_JPN.py"
    subprocess.run(["python", script_path_1, data_input])
