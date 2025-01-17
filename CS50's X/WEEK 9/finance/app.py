import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash


from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks."""
    user_id = session["user_id"]

    transactions = db.execute("""
        SELECT symbol,
               SUM(CASE WHEN action = 'BOUGHT' THEN shares ELSE -shares END) as total_shares,
               SUM(CASE WHEN action = 'BOUGHT' THEN paid_price ELSE -paid_price END) as total_investment
        FROM transactions
        WHERE user_id = ?
        GROUP BY symbol
    """, user_id)

    cash_left = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
    cash_left = float(cash_left) if cash_left is not None else 0.0

    total_amount = cash_left
    stock_data = []

    try:
        for stock in transactions:
            if stock["total_shares"] > 0:
                symbol = stock["symbol"]
                stock_info = lookup(symbol)
                current_price = float(stock_info["price"])
                stock_value = current_price * stock["total_shares"]
                avg_paid_price = stock["total_investment"] / \
                    stock["total_shares"] if stock["total_shares"] > 0 else 0
                profit = stock_value - stock["total_investment"]

                stock_data.append({
                    "symbol": symbol,
                    "shares": stock["total_shares"],
                    "avg_paid_price": usd(avg_paid_price),
                    "current_price": usd(current_price),
                    "stock_value": usd(stock_value),
                    "profit": usd(profit)
                })

                total_amount += stock_value
    except (ValueError, LookupError):
        return apology("Failed to update stock prices!")

    return render_template(
        "index.html",
        transactions=stock_data,
        cash_left=usd(cash_left),
        total_amount=usd(total_amount),
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":

        user_id = session["user_id"]
        symbol = request.form.get("symbol").upper()
        stock = lookup(symbol)
        shares = request.form.get("shares")

        if not stock:
            return apology("Symbol is not valid!")

        if not shares.isdigit():
            return apology("Shares must be a positive number!")

        transaction_value = int(shares) * stock["price"]
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        user_cash = user_cash[0]["cash"]

        if user_cash < transaction_value:
            return apology("Not enough money!")

        update_user_cash = user_cash - transaction_value
        db.execute("UPDATE users SET cash = ? WHERE id = ?", update_user_cash, user_id)

        db.execute("INSERT INTO transactions (user_id, symbol, shares, paid_price, stock_price, action) VALUES (?, ?, ?, ?, ?, ?)",
                   user_id,
                   symbol.upper(),
                   shares,
                   transaction_value,
                   stock["price"],
                   "BOUGHT",
                   )

        flash(f"Successfully bought {shares} shares of {symbol}!")
        return redirect("/")

    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions."""

    user_id = session["user_id"]
    portfolio = db.execute("SELECT * FROM transactions WHERE user_id = ?", user_id)

    return render_template("history.html", portfolio=portfolio)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        stock = lookup(str(request.form.get("symbol")))

        if not stock:
            return apology("Invalid symbol!")

        return render_template("quoted.html", stock=stock)

    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if any(not field for field in [username, password, confirmation]):
            return apology("Fields cannot be empty!")

        if password != confirmation:
            return apology("Passwords do not match!")

        try:
            hashed_password = generate_password_hash(password)
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)",
                       username, hashed_password)
            rows = db.execute("SELECT * FROM users WHERE username = ?", username)
            session["user_id"] = rows[0]["id"]
            flash(f"Successfully registred ")
            return redirect("/")
        except ValueError:
            return apology("Username already exists. Please choose a different username.")

    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""

    if request.method == "POST":
        user_id = session["user_id"]
        symbol = request.form.get("symbol").upper()
        stock = lookup(symbol)
        shares = int(request.form.get("shares"))

        if not stock:
            return apology("Stock symbol not found", 400)

        owned_stock1 = db.execute(
            "SELECT SUM(shares) as shares FROM transactions WHERE user_id = ? AND symbol = ? AND action = 'BOUGHT'", user_id, symbol)
        owned_stock2 = db.execute(
            "SELECT SUM(shares) as shares FROM transactions WHERE user_id = ? AND symbol = ? AND action = 'SOLD'", user_id, symbol)
        if owned_stock1[0]["shares"] is None:
            owned_stock1[0]["shares"] = 0
        if owned_stock2[0]["shares"] is None:
            owned_stock2[0]["shares"] = 0

        current_shares = int(owned_stock1[0]["shares"]) - int(owned_stock2[0]["shares"])

        if current_shares < shares:
            return apology("You don't have enough shares to sell!")

        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        cash = cash[0]["cash"]

        sale_value = shares * stock["price"]
        cash += sale_value

        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, user_id)

        db.execute(
            "INSERT INTO transactions (user_id, symbol, shares, paid_price, stock_price, action) VALUES (?, ?, ?, ?, ?, ?)",
            user_id,
            symbol.upper(),
            shares,
            sale_value,
            stock["price"],
            "SOLD",
        )

        flash(f"Successfully sold {shares} shares of {symbol}!")
        return redirect("/")

    return render_template("sell.html")


@app.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():
    """Deposit money to account."""

    if request.method == "POST":
        user_id = session["user_id"]
        amount = request.form.get("amount")

        if not amount or float(amount) <= 0:
            return apology("Invalid deposit amount")

        current_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        new_cash = current_cash + float(amount)
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, user_id)

        flash(f"Successfully deposited ${amount}!")
        return redirect("/")

    return render_template("deposit.html")
