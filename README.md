# Check Splitter App

## Overview
Check Splitter is a mobile application designed to simplify the process of splitting a bill among a group of people. By taking a picture of the receipt, the app itemizes the bill, allows group members to select their items, and calculates the total amount each person owes. The app also integrates with Venmo for easy payment to the person who paid the bill.

## Features
**Receipt Scanning**: Take a picture of the receipt to automatically itemize the bill.  
**Split Adjustment**: Allow manual input and adjustments in case the automatic image processing doesn't accurately itemize the bill.  
**Item Selection**: Group members can select the items they ordered.  
**Total Calculation**: Automatically calculates the total amount each person owes, including tax and tip.  
**Venmo Integration**: Seamlessly pay the person who paid the bill through Venmo.

## Tech Stack
**Frontend**: React Native  
**Backend**: Node.js with Express.js  
**Database**: PostgreSQL  
**Image Processing**: Tesseract OCR (Python)  
**Payment Integration**: Venmo API  
**Cloud** Services: AWS or Google Cloud

## Development Roadmap
1. Gather itemized receipts using Tesseract OCR in Python
2. Display itemized receipts as components on front-end using React Native
3. Allow for creation of group 
4. Allow for assignment of charges to different members
5. Algorithm for calculating portion of tax and tip
6. Integration with Venmo to allow for seamless payment/requests

## Extra features
Rather than the person paying for the bill having to manually enter everyones purchases, allow everyone to join a "lobby" and select their own items  

## Notes
Already been done, how can I make it better?  
Need to do market research, see what certain apps do well, also what they lack / do poorly.  

