# Quick integration guide

Before you start with the implementation please [contact our team](mailto:info@bitpesa.co) as they will assess whether we can waive some of the requirements around our API, including the need for KYC'ing the senders and whether you can collect money on our behalf.

Once you finish with the integration we will have a call to check that your implementation works as expected, and as a minimum supports the following functionalities:

* Authenticate to our site
* Create and re-use senders
* Create and fund transactions
* Check the status of transactions both via webhooks and manually
* Handling and cancelling failed transactions

Please read our [README](README.md) and the [Transaction Flow Guide](transaction-flow.md) before going through the implementation, but to make the process of creating a minimum approved integration easier, we propose you follow the following steps in this order:

## Authentication

Please read our [Authentication guide](authentication.md) on how to register for an API key and how to use it on our site. You can also find example implementations around authentication for some of the major programming languages.

## Creating transactions

Please read [our guide on creating transactions](transaction-flow.md#creating-transactions)
 on how you can create transactions, and the various options you have. Please make sure you already have discussed with us how your transactions will be funded before you start with this task.

## Funding transactions

If you are going to have a balance with us, then please read [our guide on funding transactions](transaction-flow.md#funding-transactions) on how you can fund the transaction. Funding the transaction means you approve the amounts that were returned in the transaction and you are happy for us to initate the payout.

## Checking transaction status

Once a transaction is funded you can use our webhook facilities to listen in changes in the transaction state. You should listen to both the transaction and the recipient events. On more info about webhooks please see our [webhook guide](README.md#webhooks). You should also be able to query transactions manually, but this facility should only be used rarely.

## Handling errors

You need to be sure that you can handle transactions where the payout has failed. For a generic guide please see [how you receiving error messages](transaction-flow.md#receiving-error-messages) and how you can [cancel recipients and transactions](transaction-flow.md#cancelling-recipients-and-transactions). Note that we will never cancel funded transactions without your request.

Since there can be a wide range of different errors, as a starting implementation we usually propose the following logic:

* Wait for at least 24 hours after the transaction is funded to see if it has been paid out successfully or not
* If hasn't been paid out, then please cancel the transaction using the API, and wait for the cancellation to finish
* If it cannot be cancelled please contact our Customer Service team to investigate

Once you have been successfully integrated with us you can add additional logic for a few specific error messages (for example the ability to change the bank account number if the error states it is invalid). However these are not required for a successful integration, and the logic mentioned above works for most of the cases where there was an error.

## Re-using senders

Finally you need to be able to re-use senders. This means any time you wish to create a transaction for the same sender you already used, you should use the same sender ID instead of creating a completely new sender object. For more details please see [senders on transactions](transaction-flow.md#sender).
