import json

eng_bad_words = ['ahole', 'anus', 'ash0le', 'ash0les', 'asholes', 'ass', 'AssMonkey', 'Assface', 'assh0le', 'assh0lez',
                 'asshole', 'asshole', 'assholes', 'assholz', 'asswipe', 'azzhole', 'bassterds', 'bastard', 'bastards',
                 'bastardz', 'basterds', 'basterdz', 'Biatch', 'bitch', 'bitches', 'BlowJob', 'boffing', 'bullshit',
                 'butthole', 'buttwipe', 'c0ck', 'c0cks', 'c0k', 'CarpetMuncher', 'cawk', 'cawks', 'Clit', 'cnts',
                 'cntz', 'cock', 'cockhead', 'cockhead', 'cocks', 'CockSucker', 'cocksucker', 'crap', 'cum', 'cunt',
                 'cunts', 'cuntz', 'dick', 'dild0', 'dild0s', 'dildo', 'dildos', 'dilld0', 'dilld0s', 'dominatricks',
                 'dominatrics', 'dominatrix', 'dyke', 'enema', 'fag', 'fag1t', 'faget', 'fagg1t', 'faggit', 'faggot',
                 'fagit', 'fags', 'fagz', 'faig', 'faigs', 'fart', 'flipping', 'fuck', 'fucker', 'fuckin', 'fucking',
                 'fucks', 'FudgePacker', 'fuk', 'Fukah', 'Fuken', 'fuker', 'Fukin', 'Fukk', 'Fukkah', 'Fukken',
                 'Fukker', 'Fukkin', 'g00k', 'gay', 'gaybor', 'gayboy', 'gaygirl', 'gays', 'gayz', 'Goddamned', 'h00r',
                 'h0ar', 'h0re', 'hells', 'hoar', 'hoor', 'hoore', 'jackoff', 'jap', 'japs', 'jerkoff', 'jisim', 'jiss',
                 'jizm', 'jizz', 'knob', 'knobs', 'knobz', 'kunt', 'kunts', 'kuntz', 'Lesbian', 'Lezzian', 'Lipshits',
                 'Lipshitz', 'masochist', 'masokist', 'massterbait', 'masstrbait', 'masstrbate', 'masterbaiter',
                 'masterbate', 'masterbates', 'mutha', 'fuker', 'motha', 'fucker', 'fuker', 'fukka', 'fukkah', 'fucka',
                 'fuchah', 'fukker', 'fukah', 'MothaFucker', 'MothaFuker', 'MothaFukkah', 'MothaFukker', 'MotherFucker',
                 'MotherFukah', 'MotherFuker', 'MotherFukkah', 'MotherFukker', 'motherfucker', 'MuthaFucker',
                 'MuthaFukah', 'MuthaFuker', 'MuthaFukkah', 'MuthaFukker', 'mutha', 'n1gr', 'nastt', 'nasty', 'nigger',
                 'nigur', 'niiger', 'niigr', 'orafis', 'orgasim', 'orgasm', 'orgasum', 'oriface', 'orifice', 'orifiss',
                 'packi', 'packie', 'packy', 'paki', 'pakie', 'paky', 'pecker', 'peeenus', 'peeenusss', 'peenus',
                 'peinus', 'pen1s', 'penas', 'penis', 'penisbreath', 'penus', 'penuus', 'Phuc', 'Phuck', 'Phuk',
                 'Phuker', 'Phukker', 'polac', 'polack', 'polak', 'Poonani', 'pr1c', 'pr1ck', 'pr1k', 'pusse', 'pussee',
                 'pussy', 'puuke', 'puuker', 'queer', 'queers', 'queerz', 'qweers', 'qweerz', 'qweir', 'recktum',
                 'rectum', 'retard', 'sadist', 'scank', 'schlong', 'screwing', 'semen', 'sex', 'sexx', 'sexxx', 'sx',
                 'sexy', 'Sht', 'sh1t', 'sh1ter', 'sh1ts', 'sh1tter', 'sh1tz', 'shit', 'shits', 'shitter', 'Shitty',
                 'Shity', 'shitz', 'Shyt', 'Shyte', 'Shytty', 'Shyt', 'skanck', 'skank', 'skankee', 'skankey', 'skanks',
                 'Skanky', 'slut', 'sluts', 'Slutty', 'slutz', 'sonofabitch', 'tit', 'turd', 'va1jina', 'vag1na',
                 'vagiina', 'vagina', 'vaj1na', 'vajina', 'vullva', 'vulva', 'w0p', 'wh00r', 'wh0re', 'whore', 'xrated',
                 'xxx', 'bch', 'bitch', 'blowjob', 'clit', 'arschloch', 'fuck', 'shit', 'ass', 'asshole', 'btch',
                 'b17ch', 'b1tch', 'bastard', 'bich', 'boiolas', 'buceta', 'c0ck', 'cawk', 'chink', 'cipa', 'clits',
                 'cock', 'cum', 'cunt', 'dildo', 'dirsa', 'ejakulate', 'fatass', 'fcuk', 'fuk', 'fux0r', 'hoer', 'hore',
                 'jism', 'kawk', 'l3itch', 'l3i+ch', 'lesbian', 'masturbate', 'masterbat', 'masterbat3', 'motherfucker',
                 's.o.b.', 'mofo', 'nazi', 'nigga', 'nigger', 'nutsack', 'phuck', 'pimpis', 'pusse', 'pussy', 'scrotum',
                 'shemale', 'shi+', 'shitt', 'slut', 'smut', 'teets', 'tits', 'boobs', 'b00bs', 'teez', 'testical',
                 'testicle', 'titt', 'w00se', 'jackoff', 'wank', 'whoar', 'whore', 'damn', 'dyke', 'fuck', 'shit',
                 '@$$', 'amcik', 'andskota', 'arse', 'assrammer', 'ayir', 'bi7ch', 'bitch', 'bollock', 'breasts',
                 'buttpirate', 'cabron', 'cazzo', 'chraa', 'chuj', 'Cock', 'cunt', 'd4mn', 'daygo', 'dego', 'dick',
                 'dike', 'dupa', 'dziwka', 'ejackulate', 'Ekrem', 'Ekto', 'enculer', 'faen', 'fag', 'fanculo', 'fanny',
                 'feces', 'feg', 'Felcher', 'ficken', 'fitt', 'Flikker', 'foreskin', 'Fotze', 'Fu', 'fuk', 'futkretzn',
                 'gay', 'gook', 'guiena', 'h0r', 'h4x0r', 'hell', 'helvete', 'hoer', 'honkey', 'Huevon', 'hui', 'injun',
                 'jizz', 'kanker', 'kike', 'klootzak', 'kraut', 'knulle', 'kuk', 'kuksuger', 'Kurac', 'kurwa', 'kusi',
                 'kyrpa', 'lesbo', 'mamhoon', 'masturbat', 'merd', 'mibun', 'monkleigh', 'mouliewop', 'muie', 'mulkku',
                 'muschi', 'nazis', 'nepesaurio', 'nigger', 'orospu', 'paska', 'perse', 'picka', 'pierdol', 'pillu',
                 'pimmel', 'piss', 'pizda', 'poontsee', 'poop', 'porn', 'p0rn', 'pr0n', 'preteen', 'pula', 'pule',
                 'puta', 'puto', 'qahbeh', 'queef', 'rautenberg', 'schaffer', 'scheiss', 'schlampe', 'schmuck', 'screw',
                 'sharmuta', 'sharmute', 'shipal', 'shiz', 'skrib']


def get_keyword_count(file_path):
    fout = open(file_path + '_filter_words', 'a+')
    fout1 = open(file_path + '_unique', 'a+')
    uniq_dict = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            try:
                data = json.loads(line)
                trans = data['transcript']
                filt_json = {}
                filt_dict = {}
                if data['vidid'] in uniq_dict:
                    continue
                uniq_dict[data['vidid']] = 1
                fout1.write(line + '\n')
                for key in eng_bad_words:
                    if ' '+key+' ' in trans:
                        filt_dict[key] = trans.count(' '+key+' ')
                filt_json['vidid'] = data['vidid']
                filt_json['filt_words'] = filt_dict
                fout.write(json.dumps(filt_json) + '\n')
            except Exception as e:
                print(e)
                print(line)
    fout.close()
    fout1.close()


if __name__ == '__main__':
    file_path = '/home/vidooly/Data_Processing/vidooly_s3/transcript/video/2017/08/merged_alltranscript_json_available'
    get_keyword_count(file_path)
