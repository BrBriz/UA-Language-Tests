import customtkinter
import random

words_list_default = ["алфАвІт",
                      "бЕшкет", "близькИй", "болотИстий", "борОдавка", "босОніж", "боЯзнь", "бурштинОвий",
                      "вАги", "вантажІвка", "видАння", "визвОльний", "вИпадок", "вирАзний", "вИсіти", "відвезтИ",
                      "віднестИ", "вІрші", "вітчИм",
                      "глядАч", "горошИна", "граблІ", "гуртОжиток",
                      "данИна", "дАно", "децимЕтр", "джерелО", "діалОг", "добовИй", "добУток", "довезтИ", "довІдник",
                      "дОнька", "дочкА", "дрОва",
                      "експЕрт",
                      "жалюзІ",
                      "завдАння", "завезтИ", "зАгдка", "закінчИти", "залишИти", "занестИ", "заробІток", "зрУчний",
                      "зубОжіння",
                      "індУстрія",
                      "кАмбала", "каталОг", "квартАл", "кИшка", "кіломЕтр", "кінчИти", "кОлія", "корИсний", "котрИй",
                      "кропивА", "кулінАрія", "кУрятина",
                      "лАте", "листопАд", "літОпис", "лЮстро",
                      "мАбУть", "мерЕжа", "металУргія", "мілімЕтр",
                      "навчАння", "нанестИ", "напІй", "нАскрізний", "нАчинка", "ненАвидіти", "ненАвисть", "нестИ", "новИй",
                      "обіцЯнка", "обрУч", "одинАдцять", "одноразОвий", "ознАка", "Олень", "отАман", "Оцет",
                      "партЕр", "перевезтИ", "перевестИ", "перелЯк", "піалА", "пІдлітковий", "пізнАння", "пітнИй",
                      "піцЕрія", "пОдруга", "пОмИлка", "понЯття", "порядкОвий", "посерЕдині", "промІжок", "псевдонІм",
                      "рАзом", "рЕмінь", "рЕшето", "рИнковий", "рівнИна", "рукОпис", "руслО",
                      "сантимЕтр", "серЕдина", "симетрІя", "сімдесЯт", "сільськогосподАрський", "слИна", "соломИнка",
                      "стовідсОтковий", "стрибАти",
                      "текстовИй", "течіЯ", "тУлуб",
                      "украЇнський", "уподОбання", "урочИстий", "усерЕдині",
                      "фартУх", "фаховИй", "фенОмен", "фОльга", "фОрзац",
                      "хАОс",
                      "цАрина", "цЕнтнер", "ціннИк",
                      "чарівнИй", "черговИй", "читАння", "чорнОзем", "чорнОслив",
                      "чотирнАдцять",
                      "шовкОвий",
                      "щЕлепа", "щИпці",
                      "ярмаркОвий"]

words_list = words_list_default

MAX_WORD_LENGTH = max((len(word) for word in words_list), default=1)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Тести з мови")
        self.geometry("800x300")

        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.used_words = set()

        self.button = customtkinter.CTkButton(self, text="Наголоси", command=self.start_test)
        self.button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.letter_buttons_frame = customtkinter.CTkFrame(self)
        self.letter_buttons_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.letter_buttons_frame.grid_rowconfigure(0, weight=1)


        self.result_label = customtkinter.CTkLabel(self, text="", font=("Arial", 20))
        self.result_label.grid(row=2, column=0, pady=5)


        self.restart_button = customtkinter.CTkButton(self, text="Пройти ще раз", command=self.restart_test)
        self.restart_button.grid(row=3, column=0, pady=10, padx=10, sticky="nsew")
        self.restart_button.grid_remove()

        self.current_word_display = ""
        self.current_word_original = ""
        self.correct_accent_indices = []
        self.letter_buttons = []

        self.bind("<Configure>", self.on_resize)

        self.after(10, self.on_resize, None)

    def _calculate_letter_button_font_size(self):
        base_size = min(self.winfo_width(), self.winfo_height())
        font_size = max(14, base_size // 30)

        num_letter_buttons = len(self.letter_buttons)
        if num_letter_buttons > 0 and self.letter_buttons_frame.winfo_width() > 0:
            frame_width = self.letter_buttons_frame.winfo_width()
            estimated_button_width = frame_width / num_letter_buttons
            calculated_size_by_width = int(estimated_button_width * 0.5)
            font_size = max(font_size, calculated_size_by_width)

        return max(14, font_size)


    def on_resize(self, event):
        if event:
            current_width = event.width
            current_height = event.height
        else:
            if not self.winfo_exists():
                return
            current_width = self.winfo_width()
            current_height = self.winfo_height()
            if current_width == 0 or current_height == 0:
                 return


        base_size = min(current_width, current_height)

        btn_font_size = max(12, base_size // 25)

        label_font_size = max(18, base_size // 25)
        self.result_label.configure(font=("Arial", label_font_size))

        if self.button.winfo_ismapped():
            self.button.configure(font=("Arial", btn_font_size, "bold"))

        if self.restart_button.winfo_ismapped():
            self.restart_button.configure(font=("Arial", btn_font_size, "bold"))

        if self.letter_buttons:
            final_letter_btn_font_size = self._calculate_letter_button_font_size()
            for btn in self.letter_buttons:
                btn.configure(font=("Arial", final_letter_btn_font_size, "bold"))


    def start_test(self):
        self.button.grid_remove()
        self.next_word()

    def restart_test(self):
        self.used_words.clear()
        self.restart_button.grid_remove()
        self.result_label.configure(text="")
        self.on_resize(None)
        self.next_word()

    def next_word(self):
        for btn in self.letter_buttons:
            btn.destroy()
        self.letter_buttons = []

        self.result_label.configure(text="")

        available_words = list(set(words_list) - self.used_words)

        if not available_words:
            self.result_label.configure(text="✅ Ви пройшли всі слова!", text_color="green")
            self.restart_button.grid()
            self.on_resize(None)
            return

        selected_word = random.choice(available_words)
        self.used_words.add(selected_word)

        self.current_word_original = selected_word
        self.current_word_display = selected_word.lower()
        self.correct_accent_indices = [i for i, c in enumerate(selected_word) if c.isupper()]


        word_len = len(self.current_word_display)

        max_possible_cols = MAX_WORD_LENGTH
        for i in range(max_possible_cols):
             self.letter_buttons_frame.grid_columnconfigure(i, weight=0)

        for i in range(word_len):
            self.letter_buttons_frame.grid_columnconfigure(i, weight=1)

        self.update_idletasks()

        final_letter_btn_font_size = self._calculate_letter_button_font_size()

        for i, letter in enumerate(self.current_word_display):
            btn = customtkinter.CTkButton(self.letter_buttons_frame, text=letter,
                                          command=lambda idx=i: self.check_accent(idx),
                                          font=("Arial", final_letter_btn_font_size, "bold"))
            btn.grid(row=0, column=i, padx=3, pady=3, sticky="nsew")
            self.letter_buttons.append(btn)

        self.on_resize(None)

    def _finish_check_and_proceed(self):
        self.on_resize(None)
        self.next_word()

    def check_accent(self, selected_index):
        self.on_resize(None)

        is_correct = selected_index in self.correct_accent_indices

        for i, btn in enumerate(self.letter_buttons):
             if i in self.correct_accent_indices:
                 btn.configure(
                     fg_color="green",
                     hover_color="green",
                     state="disabled"
                 )
             elif i == selected_index:
                 btn.configure(
                     fg_color="red",
                     hover_color="red",
                     state="disabled"
                 )
             else:
                 btn.configure(state="disabled")


        if is_correct:
            self.result_label.configure(text="✅ Правильно!", text_color="green")
        else:
            correct_letters_with_accent = [self.current_word_original[i] for i in self.correct_accent_indices]
            correct_letters_str = "', '".join(correct_letters_with_accent)
            self.result_label.configure(
                text=f"❌ Неправильно. Правильні букви: '{correct_letters_str}'",
                text_color="red"
            )

        self.after(3000, self._finish_check_and_proceed)

app = App()
app.mainloop()