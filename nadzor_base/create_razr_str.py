from tkinter import *
import tkinter.ttk as ttk
import tkinter as tk
from functools import partial
from pdf_creator.pdf_razr_stroit import CreatePdfClass

class YScrolledFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.canvas = canvas = tk.Canvas(self, relief='raised', width=1000, height=640)
        canvas.grid(row=0, column=0, sticky='nsew')

        scroll = tk.Scrollbar(self, command=canvas.yview, orient=tk.VERTICAL)
        canvas.config(yscrollcommand=scroll.set)
        scroll.grid(row=0, column=1, sticky='nsew')

        self.content = tk.Frame(canvas)
        self.canvas.create_window(0, 0, window=self.content, anchor="nw")

        self.bind('<Configure>', self.on_configure)

    def on_configure(self, event):
        bbox = self.content.bbox('ALL')
        self.canvas.config(scrollregion=bbox)

class Notebook(ttk.Notebook):
    def __init__(self, parent, tab_labels):
        super().__init__(parent)

        self._tab = {}
        for text in tab_labels:
            self._tab[text] = YScrolledFrame(self)
            # layout by .add defaults to fill=tk.BOTH, expand=True
            self.add(self._tab[text], text=text, compound=tk.TOP)

    def tab(self, key):
        return self._tab[key].content

class AddRazrStr:
    def __init__(self, tk_main):
        self.result = None
        # self.create_window = Tk()
        self.create_window = Toplevel(tk_main)
        self.create_window.title('Добавить разрешение на строительство')
        self.create_window.geometry('600x450')
        self.razdels_tabs = ['Раздел 1', 'Раздел 2', 'Раздел 3', 'Раздел 4', 'Раздел 5', 'Раздел 6',
                             'Раздел 7', 'Раздел 8']

        self.labels = [
            '1.1. Дата разрешения на строительство',
            '1.2. Номер разрешения на строительство',
            '1.3. Наименование органа (организации)',
            '1.4. Срок действия настоящего разрешения',
            '1.5. Дата внесения изменений или исправлений',
            # '2.1. Сведения о физическом лице или индивидуальном предпринимателе',
            '2.1.1. Фамилия:',
            '2.1.2. Имя:',
            '2.1.3. Отчество',
            '2.1.4. ИНН:',
            '2.1.5. ОГРНИП',
            '2.2. Сведения о юридическом лице',
            '2.2.1. Полное наименование',
            '2.2.2. ИНН:',
            '2.2.3. ОГРН:',
            '3.1. Наименование объекта капитального строительства (этапа) в соответствии с проектной документацией:',
            '3.2. Вид выполняемых работ в отношении объекта капитального строительства в соответствии с проектной '
            'документацией',
            # '3.3. Адрес (местоположение) объекта капитального строительства',
            '3.3.1. Субъект Российской Федерации:',
            '3.3.2. Муниципальный район, муниципальный округ, городской округ или внутригородская территория (для '
            'городов федерального значения) в составе субъекта Российской Федерации, федеральная территория:',
            '3.3.3. Городское или сельское поселение в составе муниципального района (для муниципального района) или '
            'внутригородского района городского округа (за исключением зданий, строений, сооружений, расположенных на '
            'федеральных территориях):',
            '3.3.4. Тип и наименование населенного пункта:',
            '3.3.5. Наименование элемента планировочной структуры:',
            '3.3.6. Наименование элемента улично-дорожной сети:',
            '3.3.7. Тип и номер здания (сооружения):',
            '4.1. Кадастровый номер земельного участка (земельных участков), в границах которого (которых) расположен '
            'или планируется расположение объекта капитального строительства',
            '4.2. Площадь земельного участка (земельных участков), в границах которого (которых) расположен или '
            'планируется расположение объекта капитального строительства',
            # '4.3. Сведения о градостроительном плане земельного участка',
            '4.3.Х.1. Дата:',
            '4.3.Х.2. Номер:',
            '4.3.Х.3. Наименование органа, выдавшего градостроительный план земельного участка:',
            '4.4. Условный номер земельного участка (земельных участков) на утвержденной схеме расположения '
            'земельного участка или земельных участков на кадастровом плане территории (при необходимости)',
            # '4.5. Сведения о схеме расположения земельного участка или земельных участков на кадастровом плане '
            # 'территории',
            '4.5.1. Дата решения:',
            '4.5.2. Номер решения:',
            '4.5.3. Наименовании организации, уполномоченного органа или лица, принявшего решение об утверждении '
            'схемы расположения земельного участка или земельных участков:',
            # '4.6. Информация о документации по планировке территории',
            # '4.6.1. Сведения о проекте планировки территории',
            '4.6.1.X.1. Дата решения:',
            '4.6.1.Х.2. Номер решения:',
            '4.6.1.Х.3. Наименование организации, уполномоченного органа или лица, принявшего решение об утверждении '
            'проекта планировки территории:',
            # '4.6.2. Сведения о проекте межевания территории',
            '4.6.2.Х.1. Дата решения:',
            '4.6.2.Х.2. Номер решения:',
            '4.6.2.Х.3. Наименовании организации, уполномоченного органа или лица, принявшего решение об утверждении '
            'проекта межевания территории:',
            # '5.1. Сведения о разработчике - индивидуальном предпринимателе',
            '5.1.1. Фамилия:',
            '5.1.2. Имя:',
            '5.1.3. Отчество',
            '5.1.4. ИНН:',
            '5.1.5. ОГРНИП:',
            # '5.2. Сведения о разработчике - юридическом лице',
            '5.2.1. Полное наименование',
            '5.2.2. ИНН:',
            '5.2.3. ОГРН:',
            '5.3. Дата утверждения (при наличии)',
            '5.4. Номер (при наличии)',
            # '5.5. Типовое архитектурное решение объекта капитального строительства, утвержденное для исторического '
            # 'поселения (при наличии)',
            '5.5.1. Дата:',
            '5.5.2. Номер:',
            '5.5.3. Наименование документа:',
            '5.5.4. Наименование уполномоченного органа, принявшего решение об утверждении типового архитектурного '
            'решения:',
            '6.1. Сведения об экспертизе проектной документации',
            '6.1.X.1. Дата утверждения:',
            '6.1.Х.2. Номер:',
            '6.1.Х.3. Наименование органа или организации, 3выдавшей положительное заключение экспертизы проектной '
            'документации:',
            # '6.2. Сведения о государственной экологической экспертизе',
            '6.2.Х.1. Дата утверждения:',
            '6.2.Х.2. Номер:',
            '6.2.Х.3. Наименование органа, утвердившего положительное заключение государственной экологической '
            'экспертизы:',
            # '6.3. Подтверждение соответствия вносимых в проектную документацию изменений требованиям, указанным '
            # 'в части 3.8 статьи 49 Градостроительного кодекса Российской Федерации',
            '6.3.1. Дата:',
            '6.3.2. Номер:',
            '6.3.3. Сведения о лице, утвердившем указанное подтверждение',
            # '6.4. Подтверждение соответствия вносимых в проектную документацию изменений требованиям, указанным '
            # 'в части 3.9 статьи 49 Градостроительного кодекса Российской Федерации',
            '6.4.1. Дата:',
            '6.4.2. Номер:',
            '6.4.3. Наименование органа исполнительной власти или организации, проводившей оценку соответствия:',
            '7.Х. Наименование объекта капитального строительства, предусмотренного проектной документацией',
            '7.Х.1. Вид объекта капитального строительства',
            '7.Х.2. Назначение объекта',
            '7.Х.3. Кадастровый номер реконструируемого объекта капитального строительства',
            '7.Х.4. Площадь застройки (кв.м)',
            '7.Х.4.1. Площадь застройки части объекта капитального строительства (кв.м)',
            '7.Х.5. Площадь (кв.м)',
            '7.Х.5.1. Площадь части объекта капитального строительства (кв.м)',
            '7.Х.6. Площадь нежилых помещений (кв.м):',
            '7.Х.7. Площадь жилых помещений (кв.м):',
            '7.Х.8. Количество помещений (штук):',
            '7.Х.9. Количество нежилых помещений (штук):',
            '7.Х.10. Количество жилых помещений (штук):',
            '7.Х.11. в том числе квартир (штук):',
            '7.Х.12. Количество машино-мест (штук):',
            '7.Х.13. Количество этажей:',
            '7.Х.14. в том числе, количество подземных этажей:',
            '7.Х.15. Вместимость (человек):',
            '7.Х.16. Высота (м):',
            '7.Х.17. Иные показатели',
            '8.Х. Наименование линейного объекта, предусмотренного проектной документацией',
            '8.Х.1. Кадастровый номер реконструируемого линейного объекта:',
            '8.Х.2. Протяженность (м)',
            '8.Х.2.1. Протяженность участка или части линейного объекта (м)',
            '8.Х.3. Категория (класс):',
            '8.Х.4. Мощность (пропускная способность, грузооборот, интенсивность движения):',
            '8.Х.5. Тип (кабельная линия электропередачи, воздушная линия электропередачи, кабельно-воздушная линия '
            'электропередачи), уровень напряжения линий электропередачи:',
            '8.Х.6. Иные показатели',
        ]

        self.dict_enter_values = {}

        # self.create_notebooks()
        self.new_not()



    def new_not(self):
        tab_parent = Notebook(self.create_window, self.razdels_tabs)
        tab_parent.grid(row=0, column=0, sticky='nsew')

        vars_string = []
        vars_string_keys = []
        for x in self.labels:
            vars_string.append(x.split()[0][:-1])
            vars_string_keys.append(x.split()[0][:-1])

        def make_pdf_class():
            pdfclass = CreatePdfClass()
            pdfclass.input_data = self.dict_enter_values
            pdfclass.make_razr_pdf()

        def make_input_dict():
            for index_, _x in enumerate(vars_string):
                try:
                    val = _x.get()
                    if val:
                        self.dict_enter_values[vars_string_keys[index_]] = val
                except:
                    pass
            make_pdf_class()
            print(self.dict_enter_values)

        # tab_parent = ttk.Notebook(self.create_window)
        tab1 = tab2 = tab3 = tab4 = tab5 = tab6 = tab7 = tab8 = ttk.Frame(tab_parent)
        list_tabs = [tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8]
        for idx, tab in enumerate(list_tabs):
            tab = tab_parent.tab(self.razdels_tabs[idx])
            # tab = ttk.Frame(tab_parent)
            # tab_parent.add(tab, text=self.razdels_tabs[idx])

            # canvas1.config(yscrollcommand=scroll.set, scrollregion=(0, 0, 100, 1000))

            row_tab = 0
            for id_labels, label_idx in enumerate(self.labels):
                if str(label_idx).startswith(str(idx + 1)):
                    tk.Label(tab, text=label_idx, justify=LEFT, wraplength=400).grid(row=row_tab, column=0, padx=0,
                                                                                     pady=5, sticky=W)

                    temp_key = str(label_idx.split()[0][:-1])

                    vars_string[id_labels] = StringVar()

                    tk.Entry(tab, justify=LEFT, textvariable=vars_string[id_labels], width=200).grid(row=row_tab, column=1, padx=0,
                                                                                          pady=5, sticky=W)

                    row_tab += 1

            loginButton = Button(tab, text="Вход", command=make_input_dict, width=30).grid(row=row_tab, column=0)
        tab_parent.pack(expand=1, anchor="nw")
        # self.create_window.mainloop()



    # def create_notebooks_old(self):
    #     vars_string = []
    #     vars_string_keys = []
    #     for x in self.labels:
    #         vars_string.append(x.split()[0][:-1])
    #         vars_string_keys.append(x.split()[0][:-1])
    #
    #     def make_input_dict():
    #         for index_, _x in enumerate(vars_string):
    #             try:
    #                 val = _x.get()
    #                 if val:
    #                     self.dict_enter_values[vars_string_keys[index_]] = val
    #             except:
    #                 pass
    #
    #         print(self.dict_enter_values)
    #
    #     tab_parent = ttk.Notebook(self.create_window)
    #     tab1 = tab2 = tab3 = tab4 = tab5 = tab6 = tab7 = tab8 = ttk.Frame(tab_parent)
    #     list_tabs = [tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8]
    #     for idx, tab in enumerate(list_tabs):
    #         tab = ttk.Frame(tab_parent)
    #         tab_parent.add(tab, text=self.razdels_tabs[idx])
    #
    #         # canvas1.config(yscrollcommand=scroll.set, scrollregion=(0, 0, 100, 1000))
    #
    #         row_tab = 0
    #         for id_labels, label_idx in enumerate(self.labels):
    #             if str(label_idx).startswith(str(idx+1)):
    #                 tk.Label(tab, text=label_idx, justify=LEFT, wraplength=400).grid(row=row_tab, column=0, padx=0, pady=5, sticky=W)
    #
    #                 temp_key = str(label_idx.split()[0][:-1])
    #
    #                 vars_string[id_labels] = StringVar()
    #
    #                 tk.Entry(tab, justify=LEFT, textvariable=vars_string[id_labels]).grid(row=row_tab, column=1, padx=0, pady=5, sticky=W)
    #
    #                 row_tab += 1
    #
    #         loginButton = Button(tab, text="Вход", command=make_input_dict, width=30).grid(row=row_tab, column=0)
    #     tab_parent.pack(expand=1, anchor="nw")
    #     self.create_window.mainloop()


if __name__ == '__main__':
    test_cls = AddRazrStr()
