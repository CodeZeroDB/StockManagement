import PySimpleGUI as sg

class MainView:
    def __init__(self):
        sg.theme('LightBlue')
        self.header = ["ID", "Product Name", "Quantity", "Price"]
        self.data = [
            [1, "Apple", 50, 0.5],
            [2, "Banana", 30, 0.3],
            [3, "Orange", 20, 0.7],
        ]
        self.layout = [
            [sg.Text("Search:"), sg.Input(key='-SEARCH-', size=(30,1)), sg.Button("Search")],
            [sg.Table(values=self.data, headings=self.header, key='-TABLE-', 
                      auto_size_columns=False, col_widths=[5, 15, 10, 10], 
                      justification='left', enable_events=True, num_rows=10)],
            [sg.Button("Add"), sg.Button("Edit"), sg.Button("Delete"), sg.Button("Refresh"), sg.Button("Exit")]
        ]
        self.window = sg.Window("Stock Management System", self.layout, finalize=True)

    def run(self):
        while True:
            event, values = self.window.read()
            if event in (sg.WINDOW_CLOSED, "Exit"):
                break
            elif event == "Search":
                sg.popup("Search functionality not implemented.")
            elif event == "Add":
                sg.popup("Add functionality not implemented.")
            elif event == "Edit":
                sg.popup("Edit functionality not implemented.")
            elif event == "Delete":
                sg.popup("Delete functionality not implemented.")
            elif event == "Refresh":
                self.window['-TABLE-'].update(values=self.data)
        self.window.close()

if __name__ == "__main__":
    MainView().run()