# Personal Finance
#### Video Demo: <URL https://youtu.be/X04jXAEtYTg>

#### Description:
The Personal Finance Management Application is a comprehensive tool designed to help users effectively manage their personal finances. Whether you're tracking income, monitoring expenses, or managing debts, this app provides an intuitive and easy-to-use interface for financial tracking and analysis. The application allows users to input and categorize various types of transactions, analyze spending trends, and track financial goals with ease.

### Key Features:
1. **Income and Expense Tracking**:
   - Users can easily add income and expense transactions using dedicated options for each: `add_income` for income and `add_expense` for expenses.
   - For every transaction, users specify the description, amount, category (for expenses), and the date manually in the format **DD-MM-YYYY**.

2. **Financial Summary**:
   - The app provides a clear overview of the user’s financial situation. By selecting a time period (daily, weekly, monthly, or custom date range), users can view a summary of their total income, total expenses, and overall balance.
   - This summary helps users understand their current financial standing and make informed decisions about saving or spending.

3. **Category Analysis**:
   - Users can analyze their expenses by category over a selected time period. The app generates a table summarizing how much has been spent in each category, helping users identify areas where they might be overspending.
   - Additionally, users can view detailed reports for a specific category, showing a list of all transactions under that category within a defined date range.

4. **Debt Management**:
   - Users can track their debts by adding details such as the total debt amount, the number of installments, and the due day of the month.
   - The application automatically calculates the monthly installment based on the total debt amount and the number of months specified.
   - Users can view a summary of all debts and monitor their progress in repaying them over time.

5. **Date Range and Monthly Reports**:
   - Users can filter and generate reports based on a specific date range or month. This allows them to analyze their spending and income patterns for a given period, helping with financial planning and budgeting.
   - Reports can include income, expenses, and debt payments, providing a holistic view of the user's financial activity over the selected period.

6. **Interactive Tables and Visualizations**:
   - The app uses beautifully formatted tables to display financial data clearly, making it easy for users to understand their financial situation.
   - Users can also view graphical representations of their spending trends through bar charts, helping them identify patterns and trends in their finances visually.

### How It Works:
Upon starting the application, users are presented with a simple text-based menu where they can select the action they want to perform. The options include adding income (`add_income`), adding expenses (`add_expense`), analyzing spending by category, viewing financial summaries, managing debts, and generating detailed reports.

When adding a transaction, users specify:
- **Income**: The description, amount, and date (in **DD-MM-YYYY** format).
- **Expense**: The description, category, amount, and date (in **DD-MM-YYYY** format).

For debts, users specify the total debt amount, the number of installments, and the due day of the month, and the application automatically calculates the monthly payment.

### Technologies Used:
- **Python**: The application is written in Python, making it cross-platform and easy to run on various systems.
- **SQLite**: Financial data is stored in an SQLite database, providing a simple and efficient way to manage the user's data.
- **Matplotlib**: For creating bar charts and visualizations of financial data.
- **Tabulate**: To generate clean, formatted tables that display financial information in an easy-to-read format.

### Future Improvements:
This application is designed to be extensible, with the potential for many more features. Future updates may include:
- **Export functionality**: Allow users to export their data in CSV or PDF formats for easy sharing or printing.
- **Budgeting**: Allow users to set and track monthly budgets for specific categories, helping them stay within their spending limits.
- **Multiple User Support**: Enable multiple users to track their finances separately, making the application more suitable for households or small businesses.

This app is a great starting point for anyone who wants to take control of their finances and improve their financial habits. Whether you're saving for a big purchase or simply trying to keep track of your spending, this app can help you achieve your financial goals.
