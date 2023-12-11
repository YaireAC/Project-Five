import tkinter as tk
import random


class SearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Search Visualization")

        self.data = [random.randint(1, 100) for _ in range(100)]
        self.search_index = 0

        self.canvas = tk.Canvas(self.root, width=600, height=200)
        self.canvas.pack()

        self.entry_label = tk.Label(self.root, text="Enter value to search:")
        self.entry_label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.search_button = tk.Button(self.root, text="Start Search", command=self.start_search)
        self.search_button.pack()

    def draw_bars(self, candidate_index=None):
        self.canvas.delete("all")
        bar_width = 6
        spacing = 2
        for i, value in enumerate(self.data):
            x1 = i * (bar_width + spacing)
            x2 = x1 + bar_width
            y1 = 200 - value * 2
            y2 = 200
            color = "lightblue" if i == candidate_index else "gray"
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def start_search(self):
        target_value = int(self.entry.get())
        self.search_index = 0
        self.search(target_value)

    def search(self, target_value):
        if self.search_index < len(self.data):
            candidate_value = self.data[self.search_index]
            self.draw_bars(self.search_index)
            self.root.after(100, self.search, target_value)  # Shorten the delay to 100 milliseconds
            self.search_index += 1

            if candidate_value == target_value:
                print("Value found!")
                return
        else:
            print("Search complete.")


if __name__ == "__main__":
    root = tk.Tk()
    app = SearchApp(root)
    root.mainloop()

# Section 2
"""Some tests that would be usefule this would be lists of numbers. To see if the code is able to run and find more than 1 numbers after the other
That way we can check that the actual generated data set are only numbers. 
Additionally, another test could be to give a cmpletely large number. To see it still is able to search well and conclude its not there. But overall the program completes the requirements.
It searches through 10 integers, highlights the candidate value at each step of the searching process and prints whether found or not"""
