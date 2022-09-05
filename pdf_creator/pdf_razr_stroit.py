from fpdf import FPDF

# НАДО ПЕРЕНЕСТИ В КОНФИГ
owner_adrr = '          367000, РД, г.Махачкала, ул. Дахадаева, 11'
tel_number_owner = '8(999)123-45-67          '


class PDF(FPDF):
    pass  # nothing happens when it is executed.


pdf = PDF(orientation='P', unit='mm', format='A4')  # pdf object
pdf.add_page()

pdf.set_xy(x=80, y=5)
pdf.image('gerb.jpg', link='', type='', w=45, h=35)

# Document title centered, 'B'old, 14 pt
pdf.add_font('PTSerif', '', 'fonts/PTSerif-Regular.ttf', uni=True)
pdf.add_font('PTSerifBold', '', 'fonts/PTSerif-Bold.ttf', uni=True)
pdf.set_font('PTSerif', '', 22)

start_head_text = 30

pdf.set_xy(0.0, start_head_text)
pdf.set_text_color(0, 0, 0)
pdf.cell(w=210.0, h=40.0, align='C', txt="АДМИНИСТРАЦИЯ ГОРОДА МАХАЧКАЛЫ", border=0)

pdf.set_xy(0.0, start_head_text + 10)
pdf.set_font('PTSerif', '', 18)
pdf.cell(w=210.0, h=40.0, align='C', txt='УПРАВЛЕНИЕ ПО ВОПРОСАМ КООРДИНАЦИИ', border=0)
pdf.set_xy(0.0, start_head_text + 18)
pdf.cell(w=210.0, h=40.0, align='C', txt='КАПИТАЛЬНОГО СТРОИТЕЛЬСТВА')

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
INPUT_DATA = {'1.1': 'Test', '1.2': 'Test'}

data_table = [['Раздел 1. Реквизиты разрешения на строительство'],
              ['1.1. Дата разрешения на строительство :', INPUT_DATA.get('1.1')],
              ['1.2. Номер разрешения на строительство :', INPUT_DATA.get('1.2')]]

# 1.3. Наименование органа (организации) :
# 1.4. Срок действия настоящего разрешения :
# 1.5. Дата внесения изменений или исправлений :


# Effective page width, or just epw
epw = pdf.w - 2 * pdf.l_margin
th = pdf.font_size

pdf.ln(0.5)
for row in data_table:
    if len(row) < 2:
        pdf.set_font('PTSerifBold', '', 12)
        col_width = epw
        pdf.cell(col_width, 2 * th, str(row[0]), border=1, align='C')
    else:
        pdf.set_font('PTSerif', '', 10)
        for datum in row:
            col_width = epw / 2
            pdf.cell(col_width, 2 * th, str(datum), border=1)
    pdf.ln(2 * th)

#
#
# # Set column width to 1/4 of effective page width to distribute content
# # evenly across table and page
# col_width = epw / 4
#
# # Since we do not need to draw lines anymore, there is no need to separate
# # headers from data matrix.
# #
# data = [['First name', 'Last name', 'Age', 'City'],
#         ['Jules', 'Smith', 34, 'San Juan'],
#         ['Mary', 'Ramos', 45, 'Orlando'], [
#             'Carlson', 'Banks', 19, 'Los Angeles'],
# ['Jules', 'Smith', 34, 'San Juan'],
#         ['Mary', 'Ramos', 45, 'Orlando'], [
#             'Carlson', 'Banks', 19, 'Los Angeles'],
# ['Jules', 'Smith', 34, 'San Juan'],
#         ['Mary', 'Ramos', 45, 'Orlando'], [
#             'Carlson', 'Banks', 19, 'Los Angeles'],
# ['Jules', 'Smith', 34, 'San Juan'],
#         ['Mary', 'Ramos', 45, 'Orlando'], [
#             'Carlson', 'Banks', 19, 'Los Angeles'],
# ['Jules', 'Smith', 34, 'San Juan'],
#         ['Mary', 'Ramos', 45, 'Orlando'], [
#             'Carlson', 'Banks', 19, 'Los Angeles'],
# ['Jules', 'Smith', 34, 'San Juan'],
#         ['Mary', 'Ramos', 45, 'Orlando'], [
#             'Carlson', 'Banks', 19, 'Los Angeles'],
# ['Jules', 'Smith', 34, 'San Juan'],
#         ['Mary', 'Ramos', 45, 'Orlando'], [
#             'Carlson', 'Banks', 19, 'Los Angeles'],
# ['Jules', 'Smith', 34, 'San Juan'],
#         ['Mary', 'Ramos', 45, 'Orlando'], [
#             'Carlson', 'Banks', 19, 'Los Angeles'],
# ['Jules', 'Smith', 34, 'San Juan'],
#         ['Mary', 'Ramos', 45, 'Orlando'], [
#             'Carlson', 'Banks', 19, 'Los Angeles'],
# ['Jules', 'Smith', 34, 'San Juan'],
#         ['Mary', 'Ramos', 45, 'Orlando'], [
#             'Carlson', 'Banks', 19, 'Los Angeles']
#         ]
#
# # Document title centered, 'B'old, 14 pt
#
#
# # pdf.set_font('Times', 'B', 14.0)
# pdf.cell(epw, 0.0, 'helljjjjjjj', align='C')
# # pdf.set_font('Times', '', 10.0)
# pdf.ln(0.5)
#
# # Text height is the same as current font size
# th = pdf.font_size
#
# for row in data:
#     for datum in row:
#         # Enter data in colums
#         # Notice the use of the function str to coerce any input to the
#         # string type. This is needed
#         # since pyFPDF expects a string, not a number.
#         pdf.cell(col_width, th, str(datum), border=1)
#
#     pdf.ln(th)
#
# # Line break equivalent to 4 lines
# pdf.ln(4 * th)
#
# pdf.set_font('Times', 'B', 14.0)
# pdf.cell(epw, 0.0, 'With more padding', align='C')
# pdf.set_font('Times', '', 10.0)
# pdf.ln(0.5)
#
# # Here we add more padding by passing 2*th as height
# for row in data:
#     for datum in row:
#         # Enter data in colums
#         pdf.cell(col_width, 2 * th, str(datum), border=1)
#
#     pdf.ln(2 * th)

pdf.output('test.pdf', 'F')
