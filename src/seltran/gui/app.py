from tkinter import filedialog as tkfd
import customtkinter as ctk

from . import Settings
from .editor import Editor


class App(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.settings = Settings()

        self.title("Japanese Selective Translator!")
        self.geometry("400x600")

        self.editor = Editor(master=self, settings=self.settings)

        self.translate_button = ctk.CTkButton(
            master=self,
            text="Translate",
            command=self.editor.run_nlp,
        )

        self.import_text_file_button = ctk.CTkButton(
            master=self,
            text="Import Text File...",
            command=lambda: [
                f()
                for f in [
                    self.prompt_import_text_file,
                    self.editor.run_nlp,
                ]
            ],
        )
        self.save_as_text_button = ctk.CTkButton(
            master=self,
            text="Save as Text",
            command=self.prompt_save_as_text,
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.editor.grid(sticky="EWNS")
        self.translate_button.grid(sticky="EWNS")
        self.import_text_file_button.grid(sticky="EWNS")
        self.save_as_text_button.grid(sticky="EWNS")

    def prompt_import_text_file(self):
        path = tkfd.askopenfilename()
        if not path:
            return

        with open(path, "r") as f:
            text = f.read()

        self.editor.insert_text(text)

    def prompt_save_as_text(self):
        path = tkfd.asksaveasfilename()
        if not path:
            return

        with open(path, "w") as f:
            f.write(self.editor.get_text())
