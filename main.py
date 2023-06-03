from googletrans import Translator
import tkinter as tk
import openai
import pathlib
from pathlib import Path

openai.api_key = "OPENAI-API-KEY"

translater = Translator()
dir_path = pathlib.Path.cwd()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.notice_button_image = tk.PhotoImage(file=Path(dir_path, 'Images', '1.png'))
        self.notice_button = tk.Button(self, image=self.notice_button_image, command=self.notice_quote)
        self.notice_button.pack(side="right", anchor="ne")
        self.notice_button.configure(image=self.notice_button_image)

        self.text_field = tk.Text(self, height=3, width=50, wrap="word")
        self.text_field.configure(font=("Arial", 12))
        self.text_field.pack(fill="both", expand=True)

        self.update_button_image = tk.PhotoImage(file=Path(dir_path, 'Images', '2.png'))
        self.update_button = tk.Button(self, image=self.update_button_image, command=self.update_quote)
        self.update_button.pack()
        self.update_button.configure(image=self.update_button_image)

    def notice_quote(self):
        with open("qoutes.txt", "a", encoding="UTF-8") as file:
            file.write(self.trs.text + "\n")

    def update_quote(self):
        prompt = 'Name me a wise quote from ukranian philosophers/writers/thinkers/dramatists/phyologists/critics. WRITE ONLY THIS: "Quote" - Author'
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        self.trs = translater.translate(response.choices[0].text.strip(), dest="uk")
        self.text_field.delete("0.0", tk.END)
        self.text_field.insert(tk.END, self.trs.text)

root = tk.Tk()
root.geometry("500x100+{}+{}".format(int((root.winfo_screenwidth() - 500) / 2), int((root.winfo_screenheight() - 100) / 2)))
root.title("Quotes")
icon_image = tk.PhotoImage(file=Path(dir_path, 'Images', '3.gif'))
root.iconphoto(True, icon_image)
root.icon_image = icon_image
app = Application(master=root)
app.mainloop()