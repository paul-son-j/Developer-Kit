# SQS  - Simple Queue Service

- sqs is a amazon provided queue service.
- is a queue of message to be processed later by the consumer
- enables async message communication between services.

## Key words:
1. Producer -> one who pushes the message to the sqs.
2. Consumer -> one who pulls the message from sqs to process.
3. Visiblity timeout -> once the consumer pulls the message, the message disappers to other from queue and a timer begins, within the default time if the consumer cannot process the message (consumer died), it reaches timeout, and reapprears in the queue.
4. Deduplicate -> FIFO had inbuilt remove duplicate message feature, which remove duplicate message within 5 min window frame.

**Note**: Visibility timeout < consumer processing time.

    Producer -> SQS -> Consumer

## Types
1. Standard -> high throughput, atleast one message
2. FIFO -> less throughput, only one message

## Standard: 
- process thousands of messages per second.
- In rare cases, do duplicates.
- Not in order.
Eg: Email 

## FIFO
- Garuntees order of process.
- No duplicates
- Less process compared to standard
eg: Bank receipt

## DLQ - Dead letter Queue
 - If the consumer dies, the visibility timeout will reappear the message in the queue.
 - There may be case where the consumer cannot process the message and faillin in to loop. eg. invalid email id
 - At those times, ater retry for a time, the message will be pushed to DLQ, removed from the main stream.
 - From there we can process these message for audit or debug.