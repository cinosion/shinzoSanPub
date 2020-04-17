import json
from requests_oauthlib import OAuth1Session
import datetime, time
import re
import oauth_keys


CK = 'CONSUMER_KEY'
CS = 'CONSUMER_SECRET'
AT = 'ACCESS_TOKEN'
ATS = 'ACCESS_TOKEN_SECRET'
twitter = OAuth1Session(CK, CS, AT, ATS)

#https://twitter.com/AbeShinzo/status/1249127951154712576
url = 'https://api.twitter.com/1.1/search/tweets.json'
params ={'q': 'ただ、皆さんのこうした行動によって、多くの命が確実に救われています。そして、今この瞬間も、過酷を極める現場で奮闘して下さっている、医療従事者の皆さんの負担の軽減につながります。お一人お一人のご協力に、心より感謝申し上げます。 filter:retweets @AbeShinzo', 'count': 100, 'max_id': -1}
sec = 0
nextMaxId = -1


def request_twittr():
    twitter = OAuth1Session(CK, CS, AT, ATS)
    res = twitter.get(url, params = params)

    if res.status_code == 200:
        rest = json.loads(res.text)
        with open('users.csv', mode='a') as f:
            for retweet in rest['statuses']:
                f.write('\n')
                f.write(str(retweet['user']))
        #print(rest.keys())
        #print(rest['statuses'][0]['user'])
        #print(rest['search_metadata'].keys())
        #print(rest['search_metadata']['max_id'])
        #nextResultsParam = str(metadata['next_results'])
        global nextMaxId
        nextMaxId = re.match('.*?(\d+)', str(rest['search_metadata']['next_results']))[1]
        print('Succeed: ', nextMaxId)
        return True, res.headers, rest['search_metadata']
    else:
        print('Failed: %d' % res.status_code)
        with open('status.log', mode='a') as f:
            f.write('error: at request phese'+str(res.status_code)+'\n')
        return False, res.headers, None


def ifSuccess(headers, metadata):
    params['max_id'] = nextMaxId
    with open('status.log', mode='a') as f:
        f.write('next_max_id: '+str(nextMaxId)+'\n')
    global sec
    sec = int(headers['X-Rate-Limit-Reset']) -  time.mktime(datetime.datetime.now().timetuple())


def request_management():
    isSuccess, headers, metadata = request_twittr()

    if isSuccess and headers['x-rate-limit-remaining'] != 1:
        ifSuccess(headers, metadata)
        request_management()
    elif isSuccess:
        ifSuccess(headers, metadata)
        print('Sleep: from isSuccess')
        time.sleep(sec)
        request_management()
    else:
        print('Sleep: from else Failed')
        time.sleep(sec)
        request_management()
    '''
    limit = res.headers['x-rate-limit-remaining'] #リクエスト可能残数の取得
    reset = res.headers['x-rate-limit-reset'] #リクエスト可能残数リセットまでの時間(UTC)
    sec = int(res.headers['X-Rate-Limit-Reset']) -  time.mktime(datetime.datetime.now().timetuple()) #UTCを秒数に変換

    print ("limit: " + limit)
    print ("reset: " +  reset)
    print ('reset sec:  %s' % sec)
    '''


request_management()
