
import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "ASQAa-Lp2muQAy1hwrsGYgDpqfK_f8s8xnIOxffv47sqzOwLgydl-LWN1-PNI_6Es2c2r4bHfK2riNzP"
        self.client_secret = "EPykuO6BbocFhIV1PGPaZIz_9hOF9rXzPD_cx2kTiufLh81cuuNmM1LPkXSE6hmES2cEOFZnQKXX9FzQ"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
        