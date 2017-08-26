import json


def get_vidlist(file_path):
    fout = open(file_path + 'transcript_json_available', 'a+')
    st = False
    st1 = False
    vidid = ''
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            try:

                if len(line) == 11:
                    st = True
                    vidid = line
                    text = ""
                elif (st and len(line) > 16):
                    # print(line[14:17])
                    # st1 = True
                    if (line[14:17] == '-->'):
                        # b =
                        # print(b)
                        if line[-2] == '\'':
                            text = text + line[32:-2] + ' '
                        else:
                            text = text + line[32:-1] + ' '
                        st1 = True
                    # elif (line[:13] == 'Youtube Video'):
                    #     text = line
                elif (st and st1 and len(line) == 0):
                    dat = {}
                    dat['vidid'] = vidid
                    dat['transcript'] = text
                    dat['length'] = len(text)
                    fout.write(json.dumps(dat) + '\n')
                    st = False
                    st1 = False
            except Exception as e:
                print(line)
    fout.close()


def get_channels(channel_path, video_path):
    vid_ch_dict = {}
    with open(channel_path, 'r') as f:
        for line in f:
            line = line.strip()
            json_data = json.loads(line)
            vid_ch_dict[json_data['id']] = json_data['snippet']['channelId']
    fout = open(video_path + 'channels', 'a+')
    with open(video_path, 'r') as f:
        for line in f:
            line = line.strip()
            fout.write(line + ',' + vid_ch_dict[line] + '\n')
    fout.close()


if __name__ == '__main__':
    file_path = '/home/vidooly/Data_Processing/vidooly_s3/transcript/video/2017/08/14/merged_all'
    get_vidlist(file_path)
    # file_path_channels_video = '/home/vidooly/Downloads/videos_data_channelsid_1010000_1020000'
    # file_path_vidid = '/home/vidooly/Data_Processing/vidooly_s3/transcript/video/2017/07/vid_transcript_available'
    # get_channels(file_path_channels_video, file_path_vidid)
