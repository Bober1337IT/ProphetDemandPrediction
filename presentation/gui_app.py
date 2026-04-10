import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from presentation.fake_data_provider import get_mock_data


class PresentationApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("E-commerce Manager - Prophet Analysis")
        self.geometry("1000x750")

        # Sidebar for controls
        self.sidebar = ctk.CTkFrame(self, width=200)
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)

        self.btn_load = ctk.CTkButton(self.sidebar, text="Run Analysis", command=self.update_dashboard)
        self.btn_load.pack(pady=20, padx=10)

        # Tabview Setup
        self.tabs = ctk.CTkTabview(self)
        self.tabs.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Creating individual tabs
        self.tab_forecast = self.tabs.add("Main Forecast")
        self.tab_components = self.tabs.add("Seasonality")
        self.tab_data = self.tabs.add("Raw Data")

    def update_dashboard(self):
        """Updates all tabs with new data and visualizations."""
        df = get_mock_data()

        # 1. Update Forecast Tab
        self.render_chart(df, self.tab_forecast, "Main Sales Forecast")

        # 2. Update Components Tab (Simplified example)
        self.render_chart(df, self.tab_components, "Weekly & Yearly Trends")

        # 3. Update Data Tab (Text representation for now)
        self.render_table(df, self.tab_data)

    def render_chart(self, df, target_tab, title):
        """Helper to draw Matplotlib charts inside a specific tab."""
        # Clear previous content
        for widget in target_tab.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
        ax.plot(df['ds'], df['y'], color="#1f77b4")
        ax.set_title(title)
        plt.xticks(rotation=45)
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=target_tab)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def render_table(self, df, target_tab):
        """Displays the raw numbers in the Data tab."""
        for widget in target_tab.winfo_children():
            widget.destroy()

        # Simple text box to show the last 15 days of data
        text_box = ctk.CTkTextbox(target_tab, font=("Courier New", 12))
        text_box.pack(fill="both", expand=True)
        text_box.insert("0.0", df.tail(15).to_string())


if __name__ == "__main__":
    app = PresentationApp()
    app.mainloop()