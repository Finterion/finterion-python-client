from finterion.models.model import Model


class AlgorithmProfile(Model):

    def __init__(
        self,
        trading_symbol,
        target_assets,
        markets,
    ):
        self.trading_symbol = trading_symbol
        self.target_assets = target_assets
        self.markets = markets

    @staticmethod
    def from_dict(data):
        return AlgorithmProfile(
            trading_symbol=data.get("trading_symbol"),
            target_assets=data.get("target_assets"),
            markets=data.get("markets"),
        )

    def to_dict(self):
        return {
            "trading_symbol": self.get_trading_symbol(),
            "target_assets": self.get_target_assets(),
            "markets": self.get_markets(),
        }

    def __repr__(self):
        return self.repr(
            trading_symbol=self.get_trading_symbol(),
            target_assets=self.get_target_assets(),
            markets=self.get_markets()
        )

    def get_trading_symbol(self):
        return self.trading_symbol

    def get_target_assets(self):
        return self.target_assets

    def get_markets(self):
        return self.markets
