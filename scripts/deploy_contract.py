from brownie import accounts, SimpleStorage  # type: ignore


def main():
    account = accounts[0]

    deployed_contract = SimpleStorage.deploy({"from": account})
    value = deployed_contract.getValue()
    print(f"Value is: {value}")

    transaction = deployed_contract.setValue(10, {"from": account})
    transaction.wait(1)

    value = deployed_contract.getValue()
    print(f"New value is {value}")
