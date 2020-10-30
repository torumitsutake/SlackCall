#coding: UTF-8

import slackweb

class pySlackCall():
    #field 
    WebhookURL = ""
    slack = slackweb.Slack(url=WebhookURL)

    def setURL(self,url):
        self.WebhookURL = url
        self.slack  = slackweb.Slack(url=self.WebhookURL)

    def callslack(self,mes="計算が終了しました"):
        self.slack.notify(text=mes)
        
