## Assignment 2 - Simple Distributed Message-Passing Coding Exercise

Message passing is required because processes in distributed systems run on separate machines and no shared memory. Message passing allows these machines to exchange data and coordinate tasks. Without it, communication would not be able to be held and processes will not be able to continue to work. If a process fails, however, it may stop sending and receiving messages, delaying other blocks and processes that need the data or message it needs to carry to them. In short, the integrity of each process needs to be held in order for the entire system to run properly. 

The difference between this model, message-passing models, compared to the shared-memory programming, is that processes communicate by only sending and receiving messages. Shared-memory programming meanwhile, communicates by reading and writing to the same memory space, which allows for a centralized system in exchange for having to need proper synchronization or sequential orders so that data won't be meshed together into one incomprehensible center.

## Code Revision:
<img width="401" height="412" alt="image" src="https://github.com/user-attachments/assets/500a0f2d-21e3-4306-9435-931f2683cb4c" />

## Test Run:
<img width="755" height="136" alt="image" src="https://github.com/user-attachments/assets/0d97dd1b-3c2c-438c-93fe-7293b7ecbf6b" />
