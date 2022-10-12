from email import header
import os


import json


import requests

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send" #나에게 보내기 주소

 
header = {
    
}
 

KAKAO_TOKEN = '억세스토큰'

 

print(sendToMeMessage(text).text)