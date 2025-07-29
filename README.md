# Detecting illicit activity in Ethereum account transaction data using machine learning methods

## Data overview
* Scmed data is collected from Crypto-Scam-DB
* Benign data is randomly collected from etherscan.io
* Collected roughly 18k Ethereum account's transaction-related data
* Almost 2.8K accounts are labeled to connect with illicit activities

## Feature Generation
* We developed a Feature Extractor that uses the APIs of etherscan.io
* We collected transaction-related data of the selected accounts
* We collected 51 transection-related attributes from the api data
