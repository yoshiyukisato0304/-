#自己紹介動画の文字起こし

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import ffmpeg

video=ffmpeg.input("/Users/satouyoshiyuki/Desktop/二年次　プログラミング　授業/0422/video/test.mp4") 
stream = ffmpeg.output(video, "/Users/satouyoshiyuki/Desktop/二年次　プログラミング　授業/0422/video/test.mp3") 
# 実行 
ffmpeg.run(stream)

import whisper
model = whisper.load_model("tiny") # モデルを読み込む
result = model.transcribe("/Users/satouyoshiyuki/Desktop/二年次　プログラミング　授業/0422/video/test.mp3") # 音声ファイルを指定する
print(result["text"]) # 認識結果を出力


import pandas as pd
import math
csvfile = open('/content/drive/My Drive/train.csv', encoding='utf-8')
dframe = pd.read_csv(csvfile)
dframe = pd.DataFrame(data=dframe)
dframe["Fare"]=dframe['Fare'].astype(int)
dframe.head(5)
