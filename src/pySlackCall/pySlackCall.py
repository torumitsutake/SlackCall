#coding: UTF-8

import slackweb

class pySlackCall():
    #field 
    WebhookURL = "https://hooks.slack.com/services/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"
    slack = slackweb.Slack(url=WebhookURL)

    def setURL(self,url):
        self.WebhookURL = url
        self.slack  = slackweb.Slack(url=self.WebhookURL)

    def callslack(self,mes="計算が終了しました"):
        self.slack.notify(text=mes)
        
