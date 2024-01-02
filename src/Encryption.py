import hmac
import time


class Encryption:
    def __init__(self):
        # 公钥
        self.k = "123456789"

    def getSecretKey(self):
        # 根据当前时间创造密钥
        time_str = str(time.time())

        # string -> bytes
        b_k = bytes(self.k, encoding='utf-8')
        b_t = bytes(time_str, encoding='utf-8')

        # 加密算法
        mod = 'MD5'
        h = hmac.new(b_k, b_t, mod)

        # 返回的16进制
        secret_key = str(h.hexdigest())

        return secret_key

    def createPwd(self, secret_key):
        # 根据密钥生成公钥

        # 转为16进制，截取前6位
        pwd = str(int(secret_key.upper(), 16))[0:6]
        return pwd


if __name__ == '__main__':
    encryption = Encryption()
    secret_key = "3343ff459c078adae87042f4b44a7984"
    print(encryption.createPwd(secret_key))
