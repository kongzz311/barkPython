import requests
from .keys import keys

def post(key=None, keyName = None, category=None, title=None, body=None, automaticallyCopy=None,
         copy=None, group=None, icon=None, level=None, sound = None):
    if key is None and keyName is None:
        return None
    if key is None and keyName is not None:
        if keyName in keys.keys():
            key = keys[keyName]
        else:
            return None
    url = 'https://api.day.app/'+key
    if category is not None:
        url += '/'+category
    if title is not None:
        url += '/'+title
    if body is not None:
        url += '/'+body

    params = {}

    if automaticallyCopy is True:
        params['automaticallyCopy'] = 1
        if copy is not None:
            params['copy'] = copy

    if group is not None:
        params['group'] = group

    if icon is not None:
        params['icon'] = icon

    if sound is not None:
        params['sound'] = sound


    # 可选参数值
    # active：不设置时的默认值，系统会立即亮屏显示通知。
    # timeSensitive：时效性通知，可在专注状态下显示通知。
    # passive：仅将通知添加到通知列表，不会亮屏提醒
    if level is not None:
        params['level'] = level

    resp = requests.get(url, params=params)
    return resp

if __name__ == '__main__':
    resp = post(keyName='iphont11Key', title='iphone11',
         body='iphone11', level='timeSensitive', sound='anticipate')
    print(resp.status_code, resp.text)
