# SSL, TLS, HTTPS
     Before these exists, internet had **big trust problem**

when we send data from client to server
- anybody can see the data
- anyone can change it.
- no proof of talking to real server.

## HTTP (Hyper Text Transfer Protocol)
- is a guideline how to communicate.
- has no security.

## SSL (Secure Sockets Layer)
- makes communication private and safe.
- establishes **Encryption(hide data), Authentication(identify right server) & Integrity(no changes in the middle)**
- Hides data, add security

Due to its weak encryption, security, comes TLS

### TLS (Transport Layer Security)
- it replaces SSL
- any new protocal are being processed by TLs

## HTTPS (HTTP + Security {via TLS}): 
- is HTTP binded under the TLS.
- HTTP to communicate and TLS for security.

## How HTTPS works:
1.  send hello to server (hey i want to esteblish the connection)
2. server send the digital cert, public key, CA, server identification.
3. client check for the cert expiry, CA, and domain match.
4. Client will generate the private key with the public key and share it with the browser which can decrypt the private key.
5. Once both has the private key, they can communicate.

Public key - is slow, and it is used for the initial handshake.
Private key - fast and used in actual communication.

CA - certificate Authority trusted third party,


HTTPS is HTTP running over TLS, where TLS uses certificates for authentication and encryption to protect data in transit.