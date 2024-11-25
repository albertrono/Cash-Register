# Shukran Supermarkets Cash Register

A Python program that simulates a cash register system for Shukran Supermarkets. The system handles cash and mobile money payments, provides exact change when possible, and tracks the available denominations in the cash register.

## Features

- **Payment Options**: Allows customers to pay using cash or mobile money.
- **Change Calculation**: Calculates the change to be returned to the customer in the smallest number of notes/coins.
- **Cash Register Tracking**: Maintains an inventory of available denominations in the cash register, updating it as transactions occur.
- **Error Handling**:
  - Insufficient payment prompts the customer to add more money.
  - Handles scenarios where exact change cannot be given due to insufficient denominations.

## How It Works

1. The program starts by initializing the cash register with a predefined set of denominations and counts.
2. The customer chooses a payment method:
   - **Cash Payment**:
     - If the cash provided is insufficient, the program prompts for additional payment.
     - If the cash exceeds the total, the program calculates the change and distributes it using the available denominations.
   - **Mobile Money Payment**:
     - Verifies the payment and handles overpayment or insufficient payment.
3. After each transaction, the cash register inventory is updated and displayed.
4. The program concludes with a thank-you message and the current state of the cash register.

## Denominations in the Cash Register

The cash register is initialized with the following denominations and counts:

| Denomination (KES) | Initial Count |
|---------------------|---------------|
| 1000               | 10            |
| 500                | 20            |
| 200                | 30            |
| 100                | 50            |
| 50                 | 100           |
| 20                 | 200           |
| 10                 | 300           |
| 5                  | 500           |
| 1                  | 1000          |

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/albertrono/Cash-Register.git
