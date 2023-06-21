import tkinter as tk
def calculate_gst():
    try:
        original_cost = float(original_cost_entry.get())
        net_price = float(net_price_entry.get())
       
        gst_amount = ((net_price - original_cost)*100) / original_cost
        gst_result_label.config(text=f"GST Amount: {gst_amount:.2f}")    
    except ValueError:
        gst_result_label.config(text="Please enter valid numbers")

window = tk.Tk()
window.title("GST Tax Finder Calculator")

original_cost_label = tk.Label(window, text="Original Cost:")
original_cost_label.pack()
original_cost_entry = tk.Entry(window)
original_cost_entry.pack()

net_price_label = tk.Label(window, text="Net Price:")
net_price_label.pack()
net_price_entry = tk.Entry(window)
net_price_entry.pack()

calculate_button = tk.Button(window, text="Calculate GST", command=calculate_gst)
calculate_button.pack()
gst_result_label = tk.Label(window, text="GST Amount:")
gst_result_label.pack()

window.mainloop
