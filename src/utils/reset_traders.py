from src.portfolio.accounts import Account
from src.templates.trader_strategies import waren_strategy, george_strategy, ray_strategy, cathie_strategy


def reset_traders():
    Account.get("Warren").reset(waren_strategy)
    Account.get("George").reset(george_strategy)
    Account.get("Ray").reset(ray_strategy)
    Account.get("Cathie").reset(cathie_strategy)


if __name__ == "__main__":
    reset_traders()