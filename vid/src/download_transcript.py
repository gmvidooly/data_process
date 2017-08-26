import youtube_dl
import requests
import os
from pycaption import WebVTTReader
from io import BytesIO, StringIO
import time
import boto3
import urllib
import datetime

local_folder = "/tmp/"
s3r = boto3.resource('s3')


class youtube_video(object):
    def __init__(self, vidid):
        self.vidid = vidid

    def get_subtitle(self, lang='en'):
        ydl = youtube_dl.YoutubeDL({'writesubtitles': True, 'allsubtitles': True, 'writeautomaticsub': True, 'quiet': True})
        url = 'https://www.youtube.com/watch?v=' + self.vidid
        with ydl:
            res = ydl.extract_info(url, download=False)
            if res['requested_subtitles'] and res['requested_subtitles']['en']:
                print('Grabbing vtt file from ' + res['requested_subtitles']['en']['url'])
                response = requests.get(res['requested_subtitles']['en']['url'], stream=True)
                b = BytesIO()
                for block in response.iter_content(1024):
                    b.write(block)
                b.seek(0)
                arr = WebVTTReader().read(b.read().decode('ascii'))
                return arr.get_captions('en-US')
            else:
                return ['Youtube Video does not have any english captions']


if __name__ == '__main__':
    vid = youtube_video('km83Bi9EBwY')
    print(vid.get_subtitle())


def lambda_handler(event, context):
    start_time = time.time()
    print("start_time ", start_time)
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    today = datetime.date.today()
    file_name = key.split('/')[-1]
    s3_path_data = "lambda_logs/data_science/vision/transcript/%s/%s/%s/%s/" % (
    today.year, today.strftime('%m'), today.strftime('%d'), str(file_name[-2:]))
    s3_path_url = "data_science/vision/transcript/ids_file/%s/%s/%s/%s/" % (
        today.year, today.strftime('%m'), today.strftime('%d'), str(file_name[-2:]))

    file_op = local_folder + str(start_time) + file_name
    fout = open(file_op, "w+")
    input_ids = local_folder + "input_ids"
    output_ids = local_folder + "output_ids"
    s3r.Bucket("lambda-outo").download_file(key, input_ids)
    count = 0
    with open(input_ids, 'r') as content, open(output_ids, 'w+') as w:
        for vidid in content:
            if (time.time() - start_time > 240):
                w.write(vidid)
                count += 1
                continue
            try:
                vid = youtube_video(vidid.strip())
                fout.write(vidid + '\n')
                subtitles = vid.get_subtitle()
                for item in subtitles:
                    fout.write(str(item))
                    fout.write('\n')
                # for item in subtitles:
                #     fout.write(item.get_text())
                #     fout.write('\n')
                fout.write('\n\n')
            except Exception as e:
                print(vidid, e)
    fout.close()
    s3r.Bucket('lambda-inin').upload_file(fout.name, s3_path_data + file_name,
                                          ExtraArgs={'ContentType': 'text'})
    print("Uploaded")
    if os.path.exists(fout.name):
        os.remove(fout.name)
    else:
        print("Sorry, I can not remove %s file." % fout.name)
    if count > 0:
        print("Part Compleated ", count)
        s3r.Bucket('lambda-outo').upload_file(output_ids,
                                              s3_path_url + str(count) + "_" + file_name[-2:],
                                              ExtraArgs={'ContentType': 'text'})
    os.remove(output_ids)
    os.remove(input_ids)
