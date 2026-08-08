# CodeAlpha Internship – Task 2

## Stock Portfolio Tracker 📈

This project is developed as part of the **CodeAlpha Python Programming Internship – Task 2: Stock Portfolio Tracker**.

The Stock Portfolio Tracker is a simple Python program that allows users to select stocks, enter the quantity they own, calculate their total investment, and save their portfolio details to a text file.

## 📌 Project Description

This program uses predefined stock prices and allows the user to build a simple stock portfolio.

The program:

* Displays available stocks and their prices
* Accepts a stock symbol from the user
* Accepts the quantity of shares
* Calculates the investment for each stock
* Calculates the total portfolio investment
* Displays the complete portfolio
* Saves the portfolio report in a text file

## ✨ Features

* Predefined stock prices for:

  * AAPL
  * TSLA
  * GOOGL
  * MSFT
  * AMZN
* User-friendly command-line interface
* Input validation for stock symbols
* Input validation for share quantity
* Investment calculation
* Total investment calculation
* Portfolio summary
* Automatic creation of `portfolio.txt`

## 🛠️ Technologies Used

* **Python 3**
* Dictionaries
* Lists
* Loops
* Functions and variables
* Conditional statements
* Exception handling
* File handling
* String formatting

## 📂 Project Structure

```text
CodeAlpha-Task-2-Stock-Portfolio/
│
├── stock_portfolio.py
├── portfolio.txt
└── README.md
```

## 💰 Available Stocks

| Stock | Price |
| ----- | ----: |
| AAPL  |  $180 |
| TSLA  |  $250 |
| GOOGL |  $140 |
| MSFT  |  $420 |
| AMZN  |  $185 |

> Note: These stock prices are hardcoded for educational purposes and are not live market prices.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd CodeAlpha-Task-2-Stock-Portfolio
```

### 3. Run the Python program

```bash
python stock_portfolio.py
```

## 💬 Example

```text
=============================================
       STOCK PORTFOLIO TRACKER
=============================================

Available Stocks:
AAPL: $180
TSLA: $250
GOOGL: $140
MSFT: $420
AMZN: $185

Enter 'done' when you have finished adding stocks.

Enter stock symbol: AAPL
Enter quantity: 2
AAPL added successfully!
Investment for AAPL: $360

Enter stock symbol: TSLA
Enter quantity: 3
TSLA added successfully!
Investment for TSLA: $750

Enter stock symbol: done

=======================================================
              YOUR PORTFOLIO
=======================================================
Stock     Quantity  Price       Investment
-------------------------------------------------------
AAPL      2         $180        $360
TSLA      3         $250        $750
-------------------------------------------------------
Total Investment: $1110

Portfolio saved successfully to portfolio.txt
Thank you for using Stock Portfolio Tracker!
```

## 📄 Portfolio Report

After running the program, a file named `portfolio.txt` is automatically created.

Example:

```text
STOCK PORTFOLIO REPORT
========================================

Stock: AAPL
Quantity: 2
Price: $180
Investment: $360
------------------------------

Stock: TSLA
Quantity: 3
Price: $250
Investment: $750
------------------------------

Total Investment: $1110
```

## 🎯 Learning Objectives

Through this project, I practiced:

* Working with Python dictionaries
* Working with lists
* Using `while` and `for` loops
* Taking and validating user input
* Performing mathematical calculations
* Handling invalid input using `try-except`
* Formatting output
* Writing data to a text file
* Building a simple command-line application

## 🚀 Future Improvements

The project can be improved by adding:

* Live stock market prices using an API
* More stocks and companies
* Buy and sell functionality
* Profit and loss calculation
* Portfolio percentage allocation
* Graphical user interface (GUI)
* Database support
* Historical stock price tracking

## 👩‍💻 Internship

**Program:** CodeAlpha Python Programming Internship
**Task:** Task 2 – Stock Portfolio Tracker

## 📜 License

This project was created for educational and internship purposes.
