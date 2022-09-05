from fpdf import FPDF

# НАДО ПЕРЕНЕСТИ В КОНФИГ
owner_adrr = '          367000, РД, г.Махачкала, ул. Коркмасова, 18'
tel_number_owner = '(8722) 78-02-72          '


class PDF(FPDF):
    pass  # nothing happens when it is executed.


pdf = PDF(orientation='P', unit='mm', format='A4')  # pdf object
pdf.add_page()

pdf.set_xy(x=80, y=5)
pdf.image('gerb.jpg', link='', type='', w=45, h=35)

# Document title centered, 'B'old, 14 pt
pdf.add_font('PTSerif', '', 'fonts/PTSerif-Regular.ttf', uni=True)
pdf.add_font('PTSerifBold', '', 'fonts/PTSerif-Bold.ttf', uni=True)
pdf.set_font('PTSerif', '', 18)

start_head_text = 30

pdf.set_xy(0.0, start_head_text)
pdf.set_text_color(0, 0, 0)
pdf.cell(w=210.0, h=40.0, align='C', txt="АДМИНИСТРАЦИЯ ГОРОДСКОГО ОКРУГА", border=0)
pdf.set_xy(0.0, start_head_text + 7)
pdf.cell(w=210.0, h=40.0, align='C', txt='С ВНУТРИГОРОДСКИМ ДЕЛЕНИЕМ "ГОРОД МАХАЧКАЛА"', border=0)

pdf.set_xy(0.0, start_head_text + 17)
pdf.set_font('PTSerif', '', 18)
pdf.cell(w=210.0, h=40.0, align='C', txt='УПРАВЛЕНИЕ АРХИТЕКТУРЫ И ГРАДОСТРОИТЕЛЬСТВА', border=0)
# pdf.set_xy(0.0, start_head_text + 25)
# pdf.cell(w=210.0, h=40.0, align='C', txt='КАПИТАЛЬНОГО СТРОИТЕЛЬСТВА')

pdf.set_xy(0.0, start_head_text + 28)
pdf.set_font('PTSerif', '', 10)
pdf.cell(w=105.0, h=40.0, align='L', txt=owner_adrr)
pdf.cell(w=105.0, h=40.0, align='R', txt=tel_number_owner)

pdf.set_line_width(0.5)
pdf.line(10, start_head_text + 51, 200, start_head_text + 51)
pdf.set_line_width(0.0)
pdf.line(10, start_head_text + 52, 200, start_head_text + 52)

pdf.set_xy(0.0, start_head_text + 45)
pdf.set_font('PTSerifBold', '', 16)
pdf.cell(w=210.0, h=40.0, align='C', txt='РАЗРЕШЕНИЕ НА СТРОИТЕЛЬСТВО')

pdf.set_xy(0.0, start_head_text + 50)
pdf.set_font('PTSerif', '', 10)
pdf.cell(w=200.0, h=40.0, align='R', txt=f'стр. {pdf.page_no()}')

pdf.set_xy(0.0, start_head_text + 75)

# INPUT DATA
INPUT_DATA = {
    '1.1': 'Test',
    '1.2': 'Test',
    '2.1.1': 'Unusov gdfgdfgd df gdf gdf gdf gdfgfdgfg gdfgdfgd df gdf gdf gdf gdfgfdgfg gdfgdfgd df gdf gdf gdf gdfgfdgfg gdfgdfgd df gdf gdf gdf gdfgfdgfg  ',
    '2.2.1': 'OOO ALPHA',
    '3.2': 'utfuisdfsdfds',
    '3.3.7': 44363645
}

data_table = [['Раздел 1. Реквизиты разрешения на строительство'],
              ['1.1. Дата разрешения на строительство :', INPUT_DATA.get('1.1')],
              ['1.2. Номер разрешения на строительство :', INPUT_DATA.get('1.2')],
              ['1.3. Наименование органа (организации) :', INPUT_DATA.get('1.3')],
              ['1.4. Срок действия настоящего разрешения :', INPUT_DATA.get('1.4')],
              ['1.5. Дата внесения изменений или исправлений :', INPUT_DATA.get('1.5')],
              ['Раздел 2. Информация о застройщике'],
              ['2.1. Сведения о физическом лице или индивидуальном предпринимателе'],
              ['2.1.1. Фамилия:', INPUT_DATA.get('2.1.1')],
              ['2.1.2. Имя:', INPUT_DATA.get('2.1.2')],
              ['2.1.3. Отчество :', INPUT_DATA.get('2.1.3')],
              ['2.1.4. ИНН:', INPUT_DATA.get('2.1.4')],
              ['2.1.5. ОГРНИП :', INPUT_DATA.get('2.1.5')],
              ['2.2. Сведения о юридическом лице'],
              ['2.2.1. Полное наименование :', INPUT_DATA.get('2.2.1')],
              ['2.2.2. ИНН:', INPUT_DATA.get('2.2.2')],
              ['2.2.3. ОГРН:', INPUT_DATA.get('2.2.3')],
              ['Раздел 3. Информация об объекте капитального строительства'],
              ['3.1. Наименование объекта капитального строительства (этапа) в соответствии с проектной документацией:'
                  , INPUT_DATA.get('3.1')],
              ['3.2. Вид выполняемых работ в отношении объекта капитального строительства в соответствии с проектной '
               'документацией :',
               INPUT_DATA.get('3.2')],
              ['3.3. Адрес (местоположение) объекта капитального строительства', INPUT_DATA.get('3.3')],
              ['3.3.1. Субъект Российской Федерации:', INPUT_DATA.get('3.3.1')],
              ['3.3.2. Муниципальный район, муниципальный округ, городской округ или внутригородская территория (для '
               'городов федерального значения) в составе субъекта Российской Федерации, федеральная территория:',
               INPUT_DATA.get('3.3.2')],
              ['3.3.3. Городское или сельское поселение в составе муниципального района (для муниципального района) '
               'или внутригородского района городского округа (за исключением зданий, строений, сооружений, '
               'расположенных на федеральных территориях):', INPUT_DATA.get('3.3.3')],
              ['3.3.4. Тип и наименование населенного пункта:', INPUT_DATA.get('3.3.4')],
              ['3.3.5. Наименование элемента планировочной структуры:', INPUT_DATA.get('3.3.5')],
              ['3.3.6. Наименование элемента улично-дорожной сети:', INPUT_DATA.get('3.3.6')],
              ['3.3.7. Тип и номер здания (сооружения):', INPUT_DATA.get('3.3.7')]

              ]


def check_cell_h(text_cell):
    pdf_test = PDF(orientation='P', unit='mm', format='A4')  # pdf object
    pdf_test.add_page()
    pdf_test.add_font('PTSerif', '', 'fonts/PTSerif-Regular.ttf', uni=True)
    pdf_test.set_font('PTSerif', '', 10)
    th_test = pdf_test.font_size
    cell_h_test = 1.5 * th_test
    top_test = pdf_test.y
    epw_test = pdf_test.w - 2 * pdf_test.l_margin
    test_cell_w = epw_test / 2
    pdf_test.multi_cell(test_cell_w, cell_h_test, str(text_cell), border=1)
    multicell_test_h = pdf_test.get_y() - top_test
    # pdf_test.output('test2.pdf', 'F')
    return multicell_test_h


# Effective page width, or just epw
epw = pdf.w - 2 * pdf.l_margin
th = pdf.font_size
cell_h = 1.5 * th
multicell_h = cell_h

pdf.ln(0.5)
for idx_row, row in enumerate(data_table):
    pdf.set_font('PTSerif', '', 10)
    align_one_colun = 'L'
    if len(row) < 2:
        if str(row[0]).startswith('Раздел'):
            pdf.set_font('PTSerifBold', '', 12)
            align_one_colun = 'C'
        elif str(row[0]).startswith('2.'):
            if not data_table[idx_row + 1][1]:
                continue
        col_width = epw
        pdf.cell(col_width, cell_h, str(row[0]), border=1, align=align_one_colun)
        pdf.ln(cell_h)
    else:
        pdf.set_font('PTSerif', '', 10)
        for idx, datum in enumerate(row):
            col_width = epw / 2
            if idx == 0:
                if row[(idx + 1)]:
                    multicell_h_1 = check_cell_h(row[(idx + 1)])
                    # Save top coordinate
                    top = pdf.y
                    # Calculate x position of next cell
                    offset = pdf.x + col_width
                    pdf.multi_cell(col_width, multicell_h_1, str(datum), border=1)
                    multicell_h = pdf.get_y() - top
                    # print(multicell_h)
                    pdf.y = top
                    # Move to computed offset
                    pdf.x = offset
            else:
                if datum:
                    multicell_h_1 = check_cell_h(row[(idx - 1)])
                    pdf.multi_cell(col_width, multicell_h_1, str(datum), border=1)
                    multicell_h = cell_h
                    # pdf.ln(cell_h)

pdf.output('test.pdf', 'F')
