from wallet.models.currency import CryptoCurrency


class CoinGeckoCrypto:
    BITCOIN = "bitcoin"
    TON = "the-open-network"
    ETHEREUM = "ethereum"
    USDC = "usd-coin"

    @classmethod
    def map_main_crypto_to_coingecko(cls):
        return {
            CryptoCurrency.TON: cls.TON,
            CryptoCurrency.BITCOIN: cls.BITCOIN,
            CryptoCurrency.ETHEREUM: cls.ETHEREUM,
            CryptoCurrency.USDC: cls.USDC,
        }

    @classmethod
    def map_coingecko_to_main_crypto(cls, key):
        return {
            cls.TON: CryptoCurrency.TON,
            cls.BITCOIN: CryptoCurrency.BITCOIN,
            cls.ETHEREUM: CryptoCurrency.ETHEREUM,
            cls.USDC: CryptoCurrency.USDC,
        }.get(key)
