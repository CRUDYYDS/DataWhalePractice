import erniebot
import os

erniebot.api_type = "aistudio"
erniebot.access_token = os.environ.get("EB_ACCESS_TOKEN")

def gen_wenxin_messages(prompt):
    '''
    构造文心模型请求参数 messages

    请求参数：
        prompt: 对应的用户提示词
    '''
    messages = [{"role": "user", "content": prompt}]
    return messages


def get_completion(prompt, model="ernie-speed-128k", temperature=0.01):
    '''
    获取文心模型调用结果

    请求参数：
        prompt: 对应的提示词
        model: 调用的模型
        temperature: 模型输出的温度系数，控制输出的随机程度，取值范围是 0~1.0，且不能设置为 0。温度系数越低，输出内容越一致。
    '''

    chat_comp = erniebot.ChatCompletion()
    message = gen_wenxin_messages(prompt)

    resp = chat_comp.create(messages=message, 
                        model=model,
                        temperature = temperature,
                        system="你是一名个人助理")

    return resp["result"]
