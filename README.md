# WEWORK Gpt bot

## Install
1. copy `conf/api-keys.env.sample` to `conf/api-keys.env`
```env
OPENAI_API_KEY="xxxxxxxxxxxxxx"
OPENAI_API_BASE="https://xxx.xxx.xxx/v1"
#自建应用-API接收消息页面-Token
WEWORK_TOKEN=""
# 自建应用-API接收消息页面-TokEncodingAESKey
WEWORK_AES_KEY=""
# 企业微信管理后台-我的企业-企业信息-最下面的企业ID
WEWORK_CORPID=""
#自建应用-应用管理详情页-AgentId
WEWORK_GPT_AGENTID="1000002"
#自建应用-详情页的Secret
WEWOEK_GPT_SECRET=""
```

2. `pip install -r requirements.txt`

3. run `python main.py`

4.Others:

4.1 If you are using Azure OpenAI API
please refer to: [https://github.com/haibbo/cf-openai-azure-proxy](https://github.com/haibbo/cf-openai-azure-proxy)

4.2 If you don't have a host oversea, you can utilize the Cloudflare's freee service, please refer to: [利用Cloudflare搭建ChatGPT API Proxy](doc/利用Cloudflare搭建ChatGPT API Proxy.pdf)