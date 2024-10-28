import boto3
import openpyxl
import os
import sys
from dotenv import load_dotenv
def main(root_file_path):
    # Set up
    excel_file_path = r"C:\Users\User\Desktop\english\作成python\スライド作成マクロ_ENG.xlsm"
    sheet_name = "Sheet2"

    # Load Excel file and select sheet
    workbook = openpyxl.load_workbook(excel_file_path, data_only=True)  # data_only パラメータを True に設定
    sheet = workbook[sheet_name]

    text_count = 3  # count of texts
    file_path_female = os.path.join(root_file_path, "audio", "ENG_female")
    for loop in range(1, 4):
        input_folder_i = os.path.join(file_path, str(loop))
        os.makedirs(input_folder_i, exist_ok=True)
        print("フォルダ作成 id=" + str(loop))

    file_path_male = os.path.join(root_file_path, "audio", "ENG_male")
    for loop in range(1, 4):
        input_folder_i = os.path.join(file_path, str(loop))
        os.makedirs(input_folder_i, exist_ok=True)
        print("フォルダ作成 id=" + str(loop))



    # Create a Polly service client
    load_dotenv()

    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    polly = boto3.client('polly', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
                        region_name='us-east-1')

    voice_ids = ['Joanna']


    # Iterate through rows in the Excel sheet
    for row_num, row in enumerate(sheet.iter_rows(min_row=2), start=2):  # Assume header is in the first row
        for i in range(1, 4):
            text_value = row[i].value.strip() if row[i].value else ""  # Assuming text is in columns 1, 2, 3, ...
            print(f"Row: {row_num-1}, Column: {i}, Value: {text_value}")

            # Check if the audio file already exists, if yes, skip
            path_text1 = os.path.join(file_path_female, str(int(i)), f'{row[0].value}.mp3')
            path_text2 = os.path.join(file_path_male, str(int(i)), f'{row[0].value}.mp3')
            if os.path.exists(path_text1) and os.path.exists(path_text2):
                print(f"音声ファイル {row[0].value}.mp3 は既に存在します。スキップします。")
                continue

            # Synthesize [text1 audio]
            result_text_no1 = polly.synthesize_speech(
            Text=text_value,  # row[i].value から text_value に変更
            OutputFormat='mp3',
            VoiceId=voice_ids[0],  # text1 voice
            )

            # Save text1 audio
            with open(path_text1, 'wb') as file_text1:
                file_text1.write(result_text_no1['AudioStream'].read())

            # Synthesize [text2 audio]
            result_text_no2 = polly.synthesize_speech(
            Text=text_value,  # row[i].value から text_value に変更
            OutputFormat='mp3',
            VoiceId=voice_ids[1],  # text2 voice
            )

            # Save text2 audio
            with open(path_text2, 'wb') as file_text2:
                file_text2.write(result_text_no2['AudioStream'].read())

    print("音声ファイルの生成が完了しました。")
    return
       
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # VBAからの呼び出しの場合
        data = sys.argv[1]
        main(data)
    else:
        # コマンドラインからの呼び出しの場合
        data_input = r"C:\Users\User\Desktop\english"
        main(data_input)