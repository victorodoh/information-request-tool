def clear_window(val):
    # clear window
    if len(val.winfo_children()) > 0:
        for widget in val.winfo_children():
            widget.destroy()