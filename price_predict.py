import io
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objs as go
from sklearn.preprocessing import LabelEncoder

def load_models():
    rf_model1 = joblib.load('models/randomforest1.sav')
    rf_model2 = joblib.load('models/randomforest2.sav')
    gb_model1 = joblib.load('models/gradientboosting1.sav')
    gb_model2 = joblib.load('models/gradientboosting2.sav')
    xgb_model1 = joblib.load('models/xgboost1.sav')
    xgb_model2 = joblib.load('models/xgboost2.sav')
    cb_model1 = joblib.load('models/catboost1.sav')
    cb_model2 = joblib.load('models/catboost2.sav')
    return rf_model1,rf_model2,gb_model1,gb_model2,xgb_model1,xgb_model2,cb_model1,cb_model2

def feature_encoding(data, features):
    le = LabelEncoder()
    for feature in features:
        le.fit(data[feature])
        data[feature] = le.transform(data[feature])
    return data

building_series = ['','Индивидуальный проект','1-447','1-464','1-510','1-511','1-515','1-515/9М','1-515/9ЮЛ','124-124-1','1605-А','1605-АМ','1МГ-601',
'II-05','II-07','II-08','II-14','II-17','II-18','II-18-01/12','II-18-02/12','II-18-31/12','II-18-31/12А','II-29','II-29-41/37','II-32','II-49','II-49Д','II-57','II-68-01','ii-68',
 'Башня Вулыха','ГМС-1','И-155','И-155МК','И-1782/1','И-209','И-209А','И-522А','И-580','И-700','И-700А','ИП-46С',
 'К-7','КОПЭ','КОПЭ Парус','МЭС-84','П-111М','П-22','П-3','П-30','П-31','П-3М','П-42','П-43','П-44','П-44К','П-44М','П-44Т','П-44ТМ','П-46','П-46М','П-47','П-55','П-55М','ПД-4']

devs = ['','АГРОСТРОЙ', 'Valartis Group', 'КОРТРОС', 'РГ-Девелопмент', 'Бэсткон', 'Доходный дом', '494 УНР', 'KR Properties', 'СЗ ПРОГРЕСС', 'СЗ ВЭЛЛБИ', 'Stenoy', 'Capital Group', 'Неизвестно', 'НИИМосстрой', '3SGroup', 'МонАрх', 'ПИК', 'Колди (Coldy)', 'St Michael', 'Еврофармакол', 'GloraX', 'РКС Девелопмент', 'ГК Новая Жизнь', 'ГК МИЦ', 'Главстрой', 'Apsis Globe', 'Level Group', 'ДОНСТРОЙ', 'Hutton Development', 'СЗ Спартак', 'А101', 'СЗ Минские холмы', 'Glincom', 'ENGEO Development', 'Концерн РУСИЧ', 'Абсолют Недвижимость', 'Touch', 'ДСК-1', 'Концерн КРОСТ', 'Д-Инвест', 'Э.К. Девелопмент', 'Группа Самолет', 'Seven Suns Development', 'Ташир', 'Группа Эталон', 'TEKTA GROUP', 'СЗ ТПУ Рассказовка', 'ГК ФСК', 'ГК Инград', 'MR Group', 'Велесстрой', 'UDS', 'VESPER', 'Группа Аквилон', 'Новые Ватутинки', 'Lexion Development', 'AFI Development', 'Optima Development', 'Sminex-Интеко', 'ГК Основа', 'СПЕЦСТРОЙ-1', 'Центр-Инвест', 'Upside Development', 'Группа Родина', 'ЭЗКС', 'СЗ Звездный', 'СЗ Универсаль', 'Группа ЛСР', 'AB Development', 'Sezar Group']

state_districts = {'': ['']
                ,'ВАО': ['','Богородское','Вешняки','Восточное Измайлово','Восточный','Гольяново','Ивановское','Измайлово','Косино-Ухтомский','Метрогородок','Новогиреево',
                            'Новокосино','Перово','Преображенское','Северное Измайлово','Соколиная гора','Сокольники']
                ,'ЗАО': ['','Внуково','Дорогомилово','Крылатское','Кунцево','Можайский','Ново-Переделкино','Очаково-Матвеевское','Проспект Вернадского','Раменки','Солнцево',
                        'Тропарево-Никулино','Филевский парк','Фили-Давыдково']
                ,'ЗелАО': ['','Крюково','Матушкино','Савёлки','Силино','Старое Крюково']
                ,'НАО(Новомосковский)': ['','Внуковское поселение','Десеновское поселение','Кокошкино дп','Коммунарка поселок','Марушкинское поселение','Московский','Московский поселение',
                        'Мосрентген поселение','Сосенское поселение','Филимонковское поселение','Щербинка']
                ,'САО': ['','Аэропорт','Беговой','Бескудниковский','Войковский','Восточное Дегунино','Головинский','Дмитровский','Западное Дегунино','Коптево','Левобережный','Молжаниновский',
                        'Савеловский','Сокол','Тимирязевский','Ховрино','Хорошевский']
                ,'СВАО': ['','Алексеевский','Алтуфьевский','Бабушкинский','Бибирево','Бутырский','Лианозово','Лосиноостровский','Марфино','Марьина роща','Останкинский','Отрадное','Ростокино',
                        'Свиблово','Северное Медведково','Северный','Южное Медведково','Ярославский']
                ,'СЗАО': ['','Куркино','Митино','Покровское-Стрешнево','Северное Тушино','Строгино','Хорошево-Мневники','Щукино','Южное Тушино']
                ,'ТАО(Троицкий)': ['','Вороновское поселение','Киевский рп','Кленовское поселение','Краснопахорское поселение','Михайлово-Ярцевское поселение','Новофедоровское поселение',
                        'Первомайское поселение','Первомайское поселок','Рогово поселок','Троицк','Щаповское поселение']
                ,'ЦАО': ['','Арбат','Басманный','Замоскворечье','Красносельский','Мещанский','Пресненский','Таганский','Тверской','Хамовники','Якиманка']
                ,'ЮАО': ['','Бирюлево Восточное','Бирюлево Западное','Братеево','Даниловский','Донской','Зябликово','Москворечье-Сабурово','Нагатино-Садовники','Нагатинский затон',
                        'Нагорный','Орехово-Борисово Северное','Орехово-Борисово Южное','Царицыно','Чертаново Северное','Чертаново Центральное','Чертаново Южное']
                ,'ЮВАО': ['','Выхино-Жулебино','Кузьминки','Лефортово','Люблино','Марьино','Некрасовка','Нижегородский','Печатники','Рязанский','Текстильщики','Южнопортовый']
                ,'ЮЗАО': ['','Академический','Гагаринский','Зюзино','Коньково','Котловка','Ломоносовский','Обручевский','Северное Бутово','Теплый Стан','Черемушки','Южное Бутово','Ясенево']}

rf_model1,rf_model2,gb_model1,gb_model2,xgb_model1,xgb_model2,cb_model1,cb_model2 = load_models()
scores1 = [0.8, 0.75, 0.85, 0.8]
scores2 = [0.75, 0.8, 0.9, 0.9]


st.set_page_config(
        page_icon="🏠",
        page_title="Оценка недвижимости онлайн",
)
st.title('Оценка недвижимости онлайн')
realty_type = st.radio("*Рынок",('Первичный', 'Вторичный'))

if realty_type == 'Вторичный':
    state = st.selectbox('*Округ',(state_districts.keys()))
    district = st.selectbox('*Район',state_districts[state])
    rooms = st.selectbox('*Количество комнат',
         ('','Студия', '1-комнатная', '2-комнатная', '3-комнатная', '4-комнатная', '5-комнатная','Многокомнатная'))
    square = st.slider("*Площадь (м2)", 10, 250,value=50)
    metrotime = st.slider("*Время до метро (пешком, мин)", 0, 90,value=10)
    live_type = st.radio("*Тип помещения",('Жилое', 'Нежилое'))
    buildyear = st.slider("*Год постройки", 1900, 2023,value=2023)
    etage = st.slider("*Этаж", 1, 80,value=1)
    etage_num = st.slider("*Этажей в доме", 1, 80,value=1)

    additional1 = st.checkbox("Указать доп.информацию о квартире")
    if additional1:
        live_sq = st.slider("Жилая площадь (м2)", 0, square,value=0)
        kitchen_sq = st.slider("Площадь кухни (м2)", 0, square//2,value=0)
        plan = st.selectbox('Планировка',
             ('','Изолированная', 'Смежная', 'Смежно-изолированная'))
        height = st.slider("Высота потолка (м)", 2.40, 8.0,value=2.70,step=0.05)
        wc = st.slider("Количество санузлов", 1, 4,value=1)
        balcon = st.slider("Количество балконов/лоджий", 0, 8,value=0)
        view = st.selectbox('Вид из окон',
             ('','Во двор', 'На улицу', 'На улицу и двор'))
        repair = st.selectbox('Ремонт',
             ('','Без ремонта', 'Дизайнерский', 'Евроремонт', 'Косметический'))
        problem = st.selectbox('Обременения',
             ('','Нет', 'Арест', 'Доверительное управление', 'Ипотека', 'Запрет на регистрацию'))
        owner = st.slider("Количество собственников", 1, 10,value=1)
    else:
        live_sq,kitchen_sq,plan,height,wc,balcon,view,repair,problem,owner = 0,0,'Неизвестно',0,1,0,'Неизвестно','Неизвестно','Нет',1

    additional2 = st.checkbox("Указать доп.информацию о доме")
    if additional2:
        buildserie = st.selectbox('Серия строительства',building_series)
        wall_material = st.selectbox('Материал стен',
             ('','Блочный', 'Кирпичный', 'Монолитно кирпичный', 'Монолитный', 'Панельный'))
        floor_material = st.selectbox('Материал перекрытий',
             ('','Деревянные', 'Железобетонные', 'Смешанные'))
        thrash = st.selectbox('Мусоропровод',
             ('','Есть', 'Нет'))
        heating = st.selectbox('Отопление',
             ('','Автономная котельная', 'Индивидуальный тепловой пункт', 'Котел/Квартирное отопление'
             ,'Нет','Центральное'))
    else:
        buildserie,wall_material,floor_material,thrash,heating = 'Неизвестно','Неизвестно','Неизвестно','Неизвестно','Неизвестно'
else:
    state = st.selectbox('*Округ',(state_districts.keys()))
    district = st.selectbox('*Район',state_districts[state])
    rooms = st.selectbox('*Количество комнат',
         ('','Студия', '1-комнатная', '2-комнатная', '3-комнатная', '4-комнатная', '5-комнатная','Многокомнатная'))
    square = st.slider("*Площадь (м2)", 10, 250,value=50)
    metrotime = st.slider("*Время до метро (пешком, мин)", 0, 90,value=10)
    live_type = st.radio("*Тип помещения",('Жилое', 'Нежилое'))
    ready = st.radio("*Сдан/не сдан",('Сдан', 'Не сдан'))
    if ready != "Сдан":
        buildyear = st.slider("*Год сдачи", 2023, 2030,value=2023)
    else:
        buildyear = st.slider("*Год сдачи", 2018, 2023,value=2023)
    etage = st.slider("*Этаж", 1, 80,value=1)
    etage_num = st.slider("*Этажей в доме", 1, 80,value=1)

    additional1 = st.checkbox("Указать доп.информацию о квартире")
    if additional1:
        live_sq = st.slider("Жилая площадь (м2)", 0, square,value=0)
        kitchen_sq = st.slider("Площадь кухни (м2)", 0, square//2,value=0)
        height = st.slider("Высота потолка (м)", 2.40, 8.0,value=3.0,step=0.05)
        wc = st.slider("Количество санузлов", 1, 4,value=1)
        balcon = st.slider("Количество балконов/лоджий", 0, 8,value=0)
        view = st.selectbox('Вид из окон',
             ('','Во двор', 'На улицу', 'На улицу и двор'))
        repair = st.selectbox('Отделка',
             ('','Без отделки', 'Чистовая', 'Предчистовая', 'Черновая', 'Чистовая с мебелью', 'С отделкой'))
    else:
        live_sq,kitchen_sq,height,wc,balcon,view,repair = 0,0,0,1,0,'Неизвестно','Неизвестно'

    additional2 = st.checkbox("Указать доп.информацию о доме")
    if additional2:
        developer = st.selectbox('Застройщик',devs)
        wall_material = st.selectbox('Материал стен',
             ('','Кирпичный', 'Монолитно-кирпичный', 'Монолитный', 'Панельный'))
        buildclass = st.selectbox('Класс ЖК',
             ('','Бизнес', 'Комфорт', 'Премиум', 'Эконом'))
        parking = st.selectbox('Парковка',
             ('','Подземная', 'Открытая','Наземная', 'Многоуровневая'))
    else:
        developer,wall_material,buildclass,parking = 'Неизвестно','Неизвестно','Неизвестно','Неизвестно'

result = st.button('Получить оценку')
if result:
    if realty_type == 'Вторичный':
        if (state != '')&(district != '')&(rooms != ''):
            if additional1:
                if plan == '':
                    plan = 'Неизвестно'
                if view == '':
                    view = 'Неизвестно'
                if repair == '':
                    repair = 'Неизвестно'
                if problem == '':
                    repair = 'Нет'
            if additional2:
                if buildserie == '':
                    buildserie = 'Неизвестно'
                if wall_material == '':
                    wall_material = 'Неизвестно'
                if floor_material == '':
                    floor_material = 'Неизвестно'
                if thrash == '':
                    thrash = 'Неизвестно'
                if heating == '':
                    heating = 'Неизвестно'
            input = {'Округ':[state],'Район':[district],
                     'Кол-во комнат':[rooms],'Площадь':[square],'Время до метро':[metrotime],
                     'Жилое/нежилое':[live_type],'Год постройки':[buildyear],'Этаж':[etage],'Этажность дома':[etage_num],

                     'Жилая площадь':[live_sq],'Площадь кухни':[kitchen_sq],'Планировка':[plan],
                     'Высота потолков':[height],'Санузел':[wc],'Кол-во балконов':[balcon],'Вид из окон':[view],
                     'Ремонт':[repair],'Обременения':[problem],'Собственников':[owner],

                     'Серия строительства':[buildserie],'Материал стен':[wall_material],'Материал пола':[floor_material],
                     'Мусоропровод':[thrash],'Отопление':[heating]}
            X = pd.DataFrame(input)
            data = pd.read_pickle("data2.pkl")
            features = data.select_dtypes(include=['object']).columns.tolist()
            X = feature_encoding(pd.concat([data.loc[:, 'Кол-во комнат':'Этажность дома'],X]), features)[-1:]
            preds = [rf_model2.predict(X)[0],gb_model2.predict(X)[0],
                     xgb_model2.predict(X)[0],cb_model2.predict(X)[0]]
            preds = [min(preds),sum([preds[i]*(scores1[i]/sum(scores1)) for i in range(len(scores1))]),max(preds)]
            round_preds = [round(i / 1000000,1) for i in preds]
        else:
            st.error('Заполните обязательные поля! (*)')
    else:
        if (state != '')&(district != '')&(rooms != ''):
            if additional1:
                if repair == '':
                    repair = 'Неизвестно'
                if view == '':
                    view = 'Неизвестно'
            if additional2:
                if developer == '':
                    developer = 'Неизвестно'
                if wall_material == '':
                    wall_material = 'Неизвестно'
                if buildclass == '':
                    buildclass = 'Неизвестно'
                if parking == '':
                    parking = 'Неизвестно'
            input = {'Округ':[state],'Район':[district],
                     'Кол-во комнат':[rooms],'Площадь':[square],'Время до метро':[metrotime],
                     'Жилое/нежилое':[live_type],'Сдан/не сдан':["Не сдан"],'Год сдачи':[buildyear],
                     'Этаж':[etage],'Этажность дома':[etage_num],

                     'Жилая площадь':[live_sq],'Площадь кухни':[kitchen_sq],
                     'Высота потолков':[height],'Санузел':[wc],'Кол-во балконов':[balcon],'Вид из окон':[view],
                     'Отделка':[repair],'Парковка':[parking],

                     'Материал стен':[wall_material],'Класс':[buildclass],
                     'Застройщик':[developer]}
            X = pd.DataFrame(input)
            data = pd.read_pickle("data1.pkl")
            features = data.select_dtypes(include=['object']).columns.tolist()
            X = feature_encoding(pd.concat([data.loc[:, 'Кол-во комнат':'Этажность дома'],X]), features)[-1:]
            preds = [rf_model1.predict(X)[0],gb_model1.predict(X)[0],
                     xgb_model1.predict(X)[0],cb_model1.predict(X)[0]]
            preds = [min(preds),sum([preds[i]*(scores1[i]/sum(scores1)) for i in range(len(scores1))]),max(preds)]
            round_preds = [round(i / 1000000,1) for i in preds]
        else:
            st.error('Заполните обязательные поля! (*)')

    st.write('**Результат:**')

    fig = go.Figure(go.Bar(y=[''], x=[round_preds[0]], orientation='h',
                marker=dict(color="rgba(0,0,0,0.1)")))
    fig.add_trace(go.Bar(y=[''], x=[round_preds[2]], orientation='h',
                marker=dict(color='rgba(255,75,75,0.6)')))
    fig.add_trace(go.Bar(y=[''], x=[round_preds[0]], orientation='h',
                marker=dict(color="rgba(0,0,0,0.1)")))

    fig.add_vline(x=round_preds[0], line_width=2, line_color="black",
                 annotation_text=str(round_preds[0])+' млн Р', annotation_position="bottom")
    fig.add_vline(x=(round_preds[2]*((round_preds[1]-round_preds[0])/(round_preds[2]-round_preds[0]))+round_preds[0]),
                 line_width=1, line_color="black", opacity=1,
                 annotation=dict(font_size=16, font_family="Arial"),
                 annotation_text='Рекомендуемая цена: \n<b>'+str(round_preds[1])+' млн Р</b>', annotation_position="top")
    fig.add_vline(x=round_preds[2]+round_preds[0], line_width=2, line_color="black",
                 annotation_text=str(round_preds[2])+' млн Р', annotation_position="bottom")

    fig.update_layout(barmode='stack',template='simple_white',showlegend=False,width=750,height=225,
                     yaxis_visible=False,xaxis_visible=False)
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
