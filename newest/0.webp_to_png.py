import os
from PIL import Image
import sys
import shutil

def main(input_root_folder):
    input_folder = os.path.join(input_root_folder, "webp")
    output_folder = os.path.abspath(os.path.join(input_folder, "..", "png"))
    output_folder_slide = os.path.abspath(os.path.join(input_folder, "..", "スライド"))
    # 一つ上の階層に戻り、pngというフォルダを作成
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(output_folder_slide, exist_ok=True)

    def convert_webp_to_png(input_folder, output_folder):
        if not os.path.exists(input_folder):
            print("入力フォルダが見つかりません。")
            return
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        processed_files = set(os.listdir(output_folder))

        for filename in os.listdir(input_folder):

            if filename.endswith(".webp"):
                input_path = os.path.join(input_folder, filename)
                output_filename = os.path.splitext(filename)[0] + ".png"
                output_path = os.path.join(output_folder, output_filename)
                print(output_path)

                if output_filename in processed_files:
                    print(f"{filename} はすでに処理されています。スキップします。")
                    continue

                try:
                    im = Image.open(input_path).convert("RGBA")
                    im.save(output_path, "PNG")
                    print(f"{filename} を {output_path} に変換しました。")
                except Exception as e:
                    print(f"{filename} の変換中にエラーが発生しました: {str(e)}")
        
    if not os.path.exists(output_folder):
        os.makedirs(output_folder, exist_ok=True)
    convert_webp_to_png(input_folder, output_folder)

    def rename_files(folder_path):
        # 新しいフォルダのパスを作成
        renamed_folder_path = os.path.join(os.path.dirname(folder_path), "renamed")
        # 新しいフォルダを作成
        os.makedirs(renamed_folder_path, exist_ok=True)
        
        # フォルダ内のファイルを取得して昇順にソート
        files = sorted(os.listdir(folder_path))
        # カウンターを初期化
        counter = 1
        # 各ファイルについて処理
        for file_name in files:
            # ファイルの拡張子を取得
            file_ext = os.path.splitext(file_name)[1]
            # 新しいファイル名を生成
            new_file_name = f"{counter}{file_ext}"
            # ファイルのフルパスを取得
            old_file_path = os.path.join(folder_path, file_name)
            new_file_path = os.path.join(renamed_folder_path, new_file_name)
            # ファイルをリネーム
            os.rename(old_file_path, new_file_path)
            # カウンターをインクリメント
            counter += 1

    # テスト用フォルダパス
    folder_path = output_folder
    # フォルダ内のファイルをリネームして"renamed"フォルダに出力
    rename_files(folder_path)
    
    # 最後に作成した PNG フォルダを削除
   # shutil.rmtree(output_folder)
    return

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # VBAからの呼び出しの場合
        data = sys.argv[1]
        main(data)
    else:
        # コマンドラインからの呼び出しの場合
        data_input = r"C:\Users\User\Downloads\新しいフォルダー"
        main(data_input)
