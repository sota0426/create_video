import os

def rename_files(input_folder):
    # 入力フォルダが存在するか確認
    if not os.path.exists(input_folder):
        print(f"入力フォルダが見つかりません: {input_folder}")
        return

    # 入力フォルダ内のファイルを処理
    for filename in os.listdir(input_folder):
        if filename.endswith(".webp"):
            try:
                # ファイル名の数字部分を抽出して100を引く
                num = int(filename.split('.')[0])
                new_num = num - 10

                # 新しいファイル名を作成
                new_filename = f"{new_num}.webp"

                # ファイルのフルパスを作成
                old_file = os.path.join(input_folder, filename)
                new_file = os.path.join(input_folder, new_filename)

                # ファイル名を変更（移動）
                os.rename(old_file, new_file)
                print(f"ファイル名を変更しました: {filename} -> {new_filename}")
            except ValueError:
                print(f"無効なファイル名: {filename} (数値部分を認識できません)")
            except Exception as e:
                print(f"エラーが発生しました: {e}")

# 使用例
input_folder = r"C:\Users\User\Desktop\新しいフォルダー"  # ここに入力フォルダのパスを指定
rename_files(input_folder)
