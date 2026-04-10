import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
# Import the data provider function from your separate file
from fake_data_provider import get_mock_data


class PresentationApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window configuration
        self.title("E-commerce Manager - Mock Data")
        self.geometry("900x600")

        # Sidebar Setup: Used for navigation and control buttons
        self.sidebar = ctk.CTkFrame(self, width=200)
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)

        # Dashboard Title
        self.label = ctk.CTkLabel(self.sidebar, text="Control Panel", font=("Arial", 16, "bold"))
        self.label.pack(pady=20)

        # Action Button: Triggers data fetching and chart rendering
        self.btn_load = ctk.CTkButton(self.sidebar, text="Fetch Data", command=self.update_chart)
        self.btn_load.pack(pady=10, padx=10)

        # Main Display Area: This is where the charts will be rendered
        self.display_frame = ctk.CTkFrame(self)
        self.display_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    def update_chart(self):
        """
        Fetches mock data, creates a Matplotlib figure,
        and embeds it into the CustomTkinter frame.
        """
        # Retrieve data from our external data provider
        df = get_mock_data()

        # Matplotlib Figure Creation
        # figsize determines the dimensions, dpi sets the resolution
        fig, ax = plt.subplots(figsize=(5, 4), dpi=100)

        # Plotting the sales data (ds = dates, y = values)
        ax.plot(df['ds'], df['y'], label="Mock Sales", color="#1f77b4")

        # Visual styling for the chart
        ax.set_title("Data Preview from fake_data_provider.py")
        plt.xticks(rotation=45)  # Rotate date labels for better readability
        plt.tight_layout()  # Ensures labels don't get cut off

        # Component Cleanup: Remove old charts before drawing a new one
        # This prevents multiple charts from stacking inside the frame
        for widget in self.display_frame.winfo_children():
            widget.destroy()

        # Canvas Integration: Bridges Matplotlib and Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.display_frame)
        canvas.draw()

        # Place the canvas widget into the frame using pack
        canvas.get_tk_widget().pack(fill="both", expand=True)


if __name__ == "__main__":
    app = PresentationApp()
    app.mainloop()