import tkinter as tk
from tkinter import messagebox, simpledialog


#Create the "container"
root = tk.Tk()
root.title("Vending Machine")
root.geometry("460x700")
root.configure(bg="#132A54")


#Give user budget
budget = 5.00


#Let's keep track of the stock and purchases
stock = {
    "01": 5,
    "02": 5,
    "03": 5,
    "04": 5
}

purchase_history = []


#Create title
title = tk.Label(
    root,
    text="Vending Machine",
    fg="#FFFFFF",
    bg="#132A54",
    font=("Arial", 16, "bold")
)
title.pack(pady=20)


#Show budget
budget_frame = tk.Frame(root, bg="#243F6D")
budget_frame.pack(fill="x", padx=25, pady=10)

tk.Label(
    budget_frame,
    text="Current Budget",
    font=("Arial", 11),
    fg="#FFFFFF",
    bg="#243F6D"
).pack(pady=(10, 0))

budget_label = tk.Label(
    budget_frame,
    text=f"${budget:.2f}",
    font=("Arial", 16, "bold"),
    fg="#FFFFFF",
    bg="#243F6D"
)
budget_label.pack(pady=5)


#Create a place for the products
product_frame = tk.Frame(root, bg="#132A54")
product_frame.pack(pady=10)


#Product 1: Nipis Madu
nipismadu_label = tk.Label(
    product_frame,
    text="(01)\nNipis Madu\n$0.33\nStock: 5",
    fg="#172B4D",
    bg="#F1F3F9",
    width=17,
    height=5
)
nipismadu_label.grid(row=0, column=0, padx=5, pady=5)


#Product 2: Cheetos Puff
cheetos_label = tk.Label(
    product_frame,
    text="(02)\nCheetos Puff\n$1.12\nStock: 5",
    fg="#172B4D",
    bg="#F1F3F9",
    width=17,
    height=5
)
cheetos_label.grid(row=0, column=1, padx=5, pady=5)


#Product 3: Onigiri
onigiri_label = tk.Label(
    product_frame,
    text="(03)\nOnigiri\n$0.55\nStock: 5",
    fg="#172B4D",
    bg="#F1F3F9",
    width=17,
    height=5
)
onigiri_label.grid(row=1, column=0, padx=5, pady=5)


#Product 4: Milku
milku_label = tk.Label(
    product_frame,
    text="(04)\nMilku\n$0.22\nStock: 5",
    fg="#172B4D",
    bg="#F1F3F9",
    width=17,
    height=5
)
milku_label.grid(row=1, column=1, padx=5, pady=5)


#Create a box for purchasing items
input_frame = tk.Frame(
    root,
    bg="#F1F3F9",
    padx=15,
    pady=15
)
input_frame.pack(fill="x", padx=25, pady=10)


tk.Label(
    input_frame,
    text="Enter Product Code:",
    font=("Arial", 12, "bold"),
    fg="#172B4D",
    bg="#F1F3F9"
).pack(pady=5)


product_entry = tk.Entry(
    input_frame,
    font=("Arial", 14),
    justify="center"
)
product_entry.pack(pady=5)


#Create a label for purchase results
result_label = tk.Label(
    input_frame,
    text="Please select a product!",
    font=("Arial", 11),
    fg="#172B4D",
    bg="#F1F3F9"
)
result_label.pack(pady=5)


#Let the user add more money
def add_balance():

    global budget

    amount = simpledialog.askfloat(
        "Add Balance",
        "Enter amount to add ($):",
        parent=root,
        minvalue=0.01
    )

    if amount is None:
        return

    #Add the money to the current budget
    budget = round(budget + amount, 2)

    #Update the budget shown on screen
    budget_label.config(
        text=f"${budget:.2f}"
    )

    result_label.config(
        text=f"${amount:.2f} added to your balance!",
        fg="green"
    )


#Update the stock shown on each product
def update_stock_display():

    nipismadu_label.config(
        text=f"(01)\nNipis Madu\n$0.33\nStock: {stock['01']}"
    )

    cheetos_label.config(
        text=f"(02)\nCheetos Puff\n$1.12\nStock: {stock['02']}"
    )

    onigiri_label.config(
        text=f"(03)\nOnigiri\n$0.55\nStock: {stock['03']}"
    )

    milku_label.config(
        text=f"(04)\nMilku\n$0.22\nStock: {stock['04']}"
    )


#Show the user's purchase history
def show_history():

    if len(purchase_history) == 0:

        messagebox.showinfo(
            "Purchase History",
            "You haven't purchased anything yet!"
        )

    else:

        history_text = ""

        for purchase in purchase_history:
            history_text = history_text + purchase + "\n"

        messagebox.showinfo(
            "Purchase History",
            history_text
        )


#Create the purchase function
def buy_product():

    global budget

    #Get the product code entered by user
    code = product_entry.get().strip()

    #Check which product the user selected
    if code == "01":
        product = "Nipis Madu"
        price = 0.33

    elif code == "02":
        product = "Cheetos Puff"
        price = 1.12

    elif code == "03":
        product = "Onigiri"
        price = 0.55

    elif code == "04":
        product = "Milku"
        price = 0.22

    else:
        result_label.config(
            text="Invalid product code!",
            fg="red"
        )
        return

    #Check if the product is still available
    if stock[code] == 0:

        result_label.config(
            text="Sorry, this product is out of stock!",
            fg="red"
        )
        return

    #Check if the user has enough budget
    if budget < price:

        result_label.config(
            text="Insufficient balance!",
            fg="red"
        )
        return

    #Deduct the price from the current budget
    budget = round(budget - price, 2)

    #Reduce the product stock
    stock[code] = stock[code] - 1

    #Save the purchased product
    purchase_history.append(
        f"{product} - ${price:.2f}"
    )

    #Update the budget and product stock
    budget_label.config(
        text=f"${budget:.2f}"
    )

    update_stock_display()

    #Show purchase confirmation
    result_label.config(
        text=f"You purchased {product}!\nBalance left: ${budget:.2f}",
        fg="green"
    )

    #Clear the product code box
    product_entry.delete(0, tk.END)


#Create the add balance button
add_balance_button = tk.Button(
    budget_frame,
    text="Add Balance",
    command=add_balance,
    font=("Arial", 10, "bold"),
    bg="#3455A0",
    fg="#FFFFFF",
    relief="flat",
    padx=15,
    pady=5
)
add_balance_button.pack(pady=5)


#Create the buy button
buy_button = tk.Button(
    input_frame,
    text="Buy",
    command=buy_product,
    font=("Arial", 12, "bold"),
    bg="#3455A0",
    fg="#FFFFFF",
    activebackground="#243F6D",
    activeforeground="#FFFFFF",
    relief="flat",
    padx=40,
    pady=10
)
buy_button.pack(pady=10)


#Create the Purchase History button
history_button = tk.Button(
    input_frame,
    text="Purchase History",
    command=show_history,
    font=("Arial", 10, "bold"),
    bg="#3455A0",
    fg="#FFFFFF",
    relief="flat",
    padx=15,
    pady=5
)
history_button.pack(pady=5)


#Start the system (YAY SLEESAI :D)
root.mainloop()