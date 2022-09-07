tettt = '1.1. Дата разрешения на строительство'

t1 = tettt.split()[0][:-1]
t1 = str(t1).replace('.', '_')

print(t1)

res = []
labels = [
            '1.1. Дата разрешения на строительство',
            '1.2. Номер разрешения на строительство',
            '1.3. Наименование органа (организации)',
            '1.4. Срок действия настоящего разрешения',
            '1.5. Дата внесения изменений или исправлений',
            '2.1. Сведения о физическом лице или индивидуальном предпринимателе',
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
            '3.3. Адрес (местоположение) объекта капитального строительства',
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
            '4.3. Сведения о градостроительном плане земельного участка',
            '4.3.Х.1. Дата:',
            '4.3.Х.2. Номер:',
            '4.3.Х.3. Наименование органа, выдавшего градостроительный план земельного участка:',
            '4.4. Условный номер земельного участка (земельных участков) на утвержденной схеме расположения '
            'земельного участка или земельных участков на кадастровом плане территории (при необходимости)',
            '4.5. Сведения о схеме расположения земельного участка или земельных участков на кадастровом плане '
            'территории',
            '4.5.1. Дата решения:',
            '4.5.2. Номер решения:',
            '4.5.3. Наименовании организации, уполномоченного органа или лица, принявшего решение об утверждении '
            'схемы расположения земельного участка или земельных участков:',
            '4.6. Информация о документации по планировке территории',
            '4.6.1. Сведения о проекте планировки территории',
            '4.6.1.X.1. Дата решения:',
            '4.6.1.Х.2. Номер решения:',
            '4.6.1.Х.3. Наименование организации, уполномоченного органа или лица, принявшего решение об утверждении '
            'проекта планировки территории:',
            '4.6.2. Сведения о проекте межевания территории',
            '4.6.2.Х.1. Дата решения:',
            '4.6.2.Х.2. Номер решения:',
            '4.6.2.Х.3. Наименовании организации, уполномоченного органа или лица, принявшего решение об утверждении '
            'проекта межевания территории:',
            '5.1. Сведения о разработчике - индивидуальном предпринимателе',
            '5.1.1. Фамилия:',
            '5.1.2. Имя:',
            '5.1.3. Отчество',
            '5.1.4. ИНН:',
            '5.1.5. ОГРНИП:',
            '5.2. Сведения о разработчике - юридическом лице',
            '5.2.1. Полное наименование',
            '5.2.2. ИНН:',
            '5.2.3. ОГРН:',
            '5.3. Дата утверждения (при наличии)',
            '5.4. Номер (при наличии)',
            '5.5. Типовое архитектурное решение объекта капитального строительства, утвержденное для исторического '
            'поселения (при наличии)',
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
            '6.2. Сведения о государственной экологической экспертизе',
            '6.2.Х.1. Дата утверждения:',
            '6.2.Х.2. Номер:',
            '6.2.Х.3. Наименование органа, утвердившего положительное заключение государственной экологической '
            'экспертизы:',
            '6.3. Подтверждение соответствия вносимых в проектную документацию изменений требованиям, указанным '
            'в части 3.8 статьи 49 Градостроительного кодекса Российской Федерации',
            '6.3.1. Дата:',
            '6.3.2. Номер:',
            '6.3.3. Сведения о лице, утвердившем указанное подтверждение',
            '6.4. Подтверждение соответствия вносимых в проектную документацию изменений требованиям, указанным '
            'в части 3.9 статьи 49 Градостроительного кодекса Российской Федерации',
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

for x in labels:
    res.append([x, f'INPUT_DATA.get("{x.split()[0][:-1]}")'])


# INPUT_DATA.get('3.3.7')
print(res)

for x in res:
    print(x)

statttt = ('2.1', '3.3', '4.3', '4.5', '4.6', '4.6.1', '5.1', '5.2', '5.5', '6.2', '6.3', '6.4')

if '3.3'.startswith(statttt):
    print('asaa')