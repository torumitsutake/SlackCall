# SlackCall
スラックにメッセージを呼び出すためのpythonプログラム


# 前提条件
Slack APIからwebHookURLを取得してください。

# install

```
git clone https://github.com/torumitsutake/SlackCall
cd SlackCall
pip install .
```

# Usage

## import
```python
from pySlackCall import pySlackCall
```


## method


### Slack WebHook URL

```python
setURL(URL)
```


### Slack WebHook URL

```python
callslack(message)
```


# Example
```python
from pySlackCall import pySlackCall

slack = pySlackCall()
slack.setURL("https://[MyURL]")

slack.callslack("にゃーん")
```