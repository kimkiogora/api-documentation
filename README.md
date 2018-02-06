# Bitpesa API Documentation

## Authentication
Authentication with the BitPesa API relies on correctly setting the headers on each request with the following data:

* **Accept** and **Content-Type** should be 'application/json'
* **Authorization-Key** is your application's API key, which can be received from the developer portal once your application has been approved
* **Authorization-Nonce** is a string, which must be unique per request - a GUID is best
* **Authorization-Signature** is a HMAC-SHA512 digest of the nonce, request method, URL, and a SHA512 hash of the request body - you will need your API Secret, also available on the developer portal, to sign

You will also need

* your API Secret, obtainable from the developer portal
* the request body - this should be a JSON string
* the full request URL, including protocol, host, port and query parameters

### Example data
For the following example, we will assume you are using the following details to create a Personal Sender:

* API Key: `YOUR_API_KEY`
* API Secret: `YOUR_API_SECRET`
* Nonce: `00c6a48a-ccb8-4653-a0c8-de7c1ab67529`
* Response Body:
```
{
  sender: {
    country: 'UG',
    phone_country: 'UG',
    phone_number: '752403639',
    email: 'email@domain.com',
    first_name: 'Example',
    last_name: 'User',
    city: 'Kampala',
    street: 'Somewhere 17-3',
    postal_code: '798983',
    birth_date: '1970-01-01',
    documents: [
      {
        upload: "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAACXBIWXMAAAsT\nAAALEwEAmpwYAAAAB3RJTUUH4gEeCTEzbKJEHgAAAB1pVFh0Q29tbWVudAAA\nAAAAQ3JlYXRlZCB3aXRoIEdJTVBkLmUHAAAADElEQVQI12P4z8AAAAMBAQAY\n3Y2wAAAAAElFTkSuQmCC",
        upload_file_name: 'passport.png',
        metadata: { meta: 'data' }
      }
    ],
    ip: '127.0.0.1',
    metadata: { meta: 'data' }
  }
}
```
* A `POST` request to https://api-sandbox.bitpesa.co/v1/senders

### Building the signature
The string to sign is generated by concatenating request-specific strings together, joined with an ampersand (&):

* the Authorization-Nonce value
* the HTTP verb, in uppercase
* `GET`
* `POST`
* `PUT`
* `PATCH`
* `DELETE`
* the full request URL, including protocol, host, port, query parameters and anchors
* a SHA512 hex digest of the request body JSON
* For the example data above, this will be `947148915d2982f7897ab187fd851e854265883109935e5e8c7ba662232b2de15e92a298067687b5402319f0efebf0561d37fc4e73460c408f91c7e25bb66ae0`
* Please note that, depending on the language, characters in the JSON may be escaped differently and your result might be different from this - see the [code example for your specific language](#complete-code-examples) for individual implementations.

For the [example values](#example-data) above, this results in the following string to sign:

* `00c6a48a-ccb8-4653-a0c8-de7c1ab67529&POST&https://api-sandbox.bitpesa.co/v1/senders&947148915d2982f7897ab187fd851e854265883109935e5e8c7ba662232b2de15e92a298067687b5402319f0efebf0561d37fc4e73460c408f91c7e25bb66ae0`

This string to sign is encrypted with the SHA512 algorithm and your API Secret, with the resulting value:

* `fc44e638c823b660e41f30ba78abe0e04f0dfc6b365e4a7129e44a181530146e4b777940fe8948af6fee5133b7f85d46a3cdcab449b9559617e60e593b73853c`

This is passed as the `Authorization-Signature` header for sending the request.

### Full sample header
```
Accept: application/json
Content-Type: application/json
Authorization-Key: YOUR_API_KEY
Authorization-Nonce: 00c6a48a-ccb8-4653-a0c8-de7c1ab67529
Authorization-Signature: eb36a61a75a7d78d16a774811122b3bbefd9fd3dfba28ffcb94b39e2c2d857cb6b22d77bb520762c813fe1a991e24862c42027c8b15b11553c03d662ed7d11f1
```

### Complete code examples
Full examples of this process are available for the following languages:

* [Ruby](https://github.com/bitpesa/api-documentation/blob/master/authentication/auth_example.rb)
* [PHP](https://github.com/bitpesa/api-documentation/blob/master/authentication/auth_example.php)
* [C#](https://github.com/bitpesa/api-documentation/blob/master/authentication/auth_example.cs)
* [Java](https://github.com/bitpesa/api-documentation/blob/master/authentication/auth_example.java)
* [JavaScript/NodeJS](https://github.com/bitpesa/api-documentation/blob/master/authentication/auth_example.js)

## API Environments
* For testing, use https://api-sandbox.bitpesa.co
* For production, use https://api.bitpesa.co

You will need a valid API Key and API Secret for each environment, obtainable in the Developer Portal once your application has been approved.
