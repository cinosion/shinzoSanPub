import json
import ast
import matplotlib.pyplot as plt
import time
from datetime import datetime
from dateutil.parser import parse


'''
'user': {
'id': 1479469147,
'id_str': '1479469147',
'name': '檸檬@社会の端くれ',
'screen_name': 'sutariasu',
'location': 'ほろ苦いレモンの世界',
'description': '大人になりきれないやる気がない大人。都会怖くて震えちゃう系。アニメ大好きマン  島崎信長さんLOVE(°▽°)電車好き お笑い好き  恐ろしいほどRT魔  お米県出身',
'url': None,
'entities': {
  'description': {
    'urls': []
  }
},
'protected': False,
'followers_count': 145,
'friends_count': 276,
'listed_count': 1,
'created_at': 'Mon Jun 03 11:07:49 +0000 2013',
'favourites_count': 527,
'utc_offset': None,
'time_zone': None,
'geo_enabled': True,
'verified': False,
'statuses_count': 29708,
'lang': None,
'contributors_enabled': False,
'is_translator': False,
'is_translation_enabled': False,
'profile_background_color': 'C0DEED',
'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png',
'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png',
'profile_background_tile': False,
'profile_image_url': 'http://pbs.twimg.com/profile_images/420102306747523072/Fk_uOvCf_normal.jpeg',
'profile_image_url_https': 'https://pbs.twimg.com/profile_images/420102306747523072/Fk_uOvCf_normal.jpeg',
'profile_banner_url': 'https://pbs.twimg.com/profile_banners/1479469147/1455972291',
'profile_link_color': '1DA1F2',
'profile_sidebar_border_color': 'C0DEED',
'profile_sidebar_fill_color': 'DDEEF6',
'profile_text_color': '333333',
'profile_use_background_image': True,
'has_extended_profile': True,
'default_profile': True, 'default_profile_image': False,
'following': False,
'follow_request_sent': False,
'notifications': False,
'translator_type': 'none'
}
'''


# 変数
counter=0
listen=[]
start = time.time()

# 抽出
with open('users.csv') as f:
    for line in f:
        if line!="\n":
            # counter +=1
            lineson = ast.literal_eval(line)
            # TwitterJPが200万フォロワーと外れ値なので弾く
            # if lineson['screen_name'] != 'TwitterJP':
            # 数で整理する
            # if lineson['followers_count'] < 10:
            dtt = parse(lineson['created_at']).timestamp()
            listen.append(dtt)
        # if counter == 4: break

# 計測
elapsed_time = time.time() - start
print(f'elapsed_time: {elapsed_time:.0f} [sec]')

# 表示
# print('Recode: ', counter)
plt.hist(listen, bins=200) #, log=True
plt.show()
# plt.boxplot(listen)


















