# Usage

add a py file called `keys.py` in the folder 

```python

keys = {
    '<keyName1>' : '<key1>',
    '<keyName2>' : '<key2>',
    '<keyName3>' : '<key3>',
}

```

run it by call the function `post` in sentBark.py

```python
from barkPython import sendBark

sendBark.post(keyName='iphont11Key', title='iphone11',
              body='iphone11', level='timeSensitive', sound='anticipate')

```