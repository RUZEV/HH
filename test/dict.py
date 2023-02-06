def fetch(list, key):
    id_list = []
    name_list = []
    for i in list:
        for id in i['specializations']:
            id_list.append(id["id"])
    for i in list:
        for id in i['specializations']:
            name_list.append(id["name"])
    diction = dict(zip(id_list, name_list))
    return diction[key]

f = [{"id":"1","name":"Информационные технологии, интернет, телеком","specializations":[{"id":"1.395","name":"Банковское ПО","laboring":False},{"id":"1.400","name":"Оптимизация сайта (SEO)","laboring":False},{"id":"1.420","name":"Администратор баз данных","laboring":False},{"id":"1.474","name":"Стартапы","laboring":False},{"id":"1.475","name":"Игровое ПО","laboring":False},{"id":"1.536","name":"CRM системы","laboring":False},{"id":"1.744","name":"Другое","laboring":False},{"id":"1.3","name":"CTO, CIO, Директор по IT","laboring":False},{"id":"1.9","name":"Web инженер","laboring":False},{"id":"1.10","name":"Web мастер","laboring":False},{"id":"1.25","name":"Аналитик","laboring":False},{"id":"1.30","name":"Арт-директор","laboring":False},{"id":"1.50","name":"Системы управления предприятием (ERP)","laboring":False},{"id":"1.82","name":"Инженер","laboring":False},{"id":"1.89","name":"Интернет","laboring":False},{"id":"1.110","name":"Компьютерная безопасность","laboring":False},{"id":"1.113","name":"Консалтинг, Аутсорсинг","laboring":False},{"id":"1.116","name":"Контент","laboring":False},{"id":"1.117","name":"Тестирование","laboring":False},{"id":"1.137","name":"Маркетинг","laboring":False},{"id":"1.161","name":"Мультимедиа","laboring":False},{"id":"1.172","name":"Начальный уровень, Мало опыта","laboring":False},{"id":"1.203","name":"Передача данных и доступ в интернет","laboring":False},{"id":"1.211","name":"Поддержка, Helpdesk","laboring":False},{"id":"1.221","name":"Программирование, Разработка","laboring":False},{"id":"1.225","name":"Продажи","laboring":False},{"id":"1.232","name":"Продюсер","laboring":False},{"id":"1.246","name":"Развитие бизнеса","laboring":False},{"id":"1.270","name":"Сетевые технологии","laboring":False},{"id":"1.272","name":"Системная интеграция","laboring":False},{"id":"1.273","name":"Системный администратор","laboring":False},{"id":"1.274","name":"Системы автоматизированного проектирования","laboring":False},{"id":"1.277","name":"Сотовые, Беспроводные технологии","laboring":False},{"id":"1.295","name":"Телекоммуникации","laboring":False},{"id":"1.296","name":"Технический писатель","laboring":False},{"id":"1.327","name":"Управление проектами","laboring":False},{"id":"1.359","name":"Электронная коммерция","laboring":False}]},{"id":"20","name":"Строительство, недвижимость","specializations":[{"id":"20.396","name":"Эксплуатация","laboring":False},{"id":"20.445","name":"ЖКХ","laboring":False},{"id":"20.484","name":"Геодезия и картография","laboring":False},{"id":"20.490","name":"Рабочие строительных специальностей","laboring":True},{"id":"20.525","name":"Землеустройство","laboring":False},{"id":"20.526","name":"Оценка","laboring":False},{"id":"20.527","name":"Отопление, вентиляция и кондиционирование","laboring":False},{"id":"20.528","name":"Водоснабжение и канализация","laboring":False},{"id":"20.573","name":"Тендеры","laboring":False},{"id":"20.755","name":"Другое","laboring":False},{"id":"20.20","name":"Агент","laboring":False},{"id":"20.58","name":"Гостиницы, Магазины","laboring":False},{"id":"20.63","name":"Дизайн/Оформление","laboring":False},{"id":"20.70","name":"Жилье","laboring":False},{"id":"20.83","name":"Инженер","laboring":False},{"id":"20.186","name":"Начальный уровень, Мало опыта","laboring":False},{"id":"20.189","name":"Нежилые помещения","laboring":False},{"id":"20.233","name":"Проектирование, Архитектура","laboring":False},{"id":"20.287","name":"Строительство","laboring":False},{"id":"20.325","name":"Управление проектами","laboring":False},{"id":"20.375","name":"Девелопер","laboring":False},{"id":"20.387","name":"Прораб","laboring":False}]},{"id":"17","name":"Продажи","specializations":[{"id":"17.397","name":"Электротехническое оборудование, Светотехника","laboring":False},{"id":"17.401","name":"Химическая продукция","laboring":False},{"id":"17.405","name":"Сертификация","laboring":False},{"id":"17.417","name":"Строительные материалы","laboring":False},{"id":"17.418","name":"Сельское хозяйство","laboring":False},{"id":"17.440","name":"Текстиль, Одежда, Обувь","laboring":False},{"id":"17.441","name":"Франчайзинг","laboring":False},{"id":"17.443","name":"Мебель","laboring":False},{"id":"17.446","name":"Системы безопасности","laboring":False},{"id":"17.486","name":"Сантехника","laboring":False},{"id":"17.487","name":"Бытовая техника","laboring":False},{"id":"17.520","name":"Продавец в магазине","laboring":True},{"id":"17.535","name":"Торговые сети","laboring":False},{"id":"17.538","name":"Продажи по телефону, Телемаркетинг","laboring":True},{"id":"17.572","name":"Тендеры","laboring":False},{"id":"17.580","name":"Клининговые услуги","laboring":False},{"id":"17.623","name":"Финансовые услуги","laboring":False},{"id":"17.625","name":"Решения по автоматизации процессов","laboring":False},{"id":"17.751","name":"Другое","laboring":False},{"id":"17.15","name":"Автомобили, Запчасти","laboring":False},{"id":"17.24","name":"Алкоголь","laboring":False},{"id":"17.59","name":"ГСМ, нефть, бензин","laboring":False},{"id":"17.65","name":"Дилерские сети","laboring":False},{"id":"17.66","name":"Дистрибуция","laboring":False},{"id":"17.111","name":"Компьютерная техника","laboring":False},{"id":"17.112","name":"Компьютерные программы","laboring":False},{"id":"17.144","name":"Медицина, Фармацевтика","laboring":False},{"id":"17.149","name":"Менеджер по работе с клиентами","laboring":False},{"id":"17.152","name":"Металлопрокат","laboring":False},{"id":"17.156","name":"Многоуровневый маркетинг","laboring":False},{"id":"17.183","name":"Начальный уровень, Мало опыта","laboring":False},{"id":"17.196","name":"Оптовая торговля","laboring":False},{"id":"17.231","name":"Продукты питания","laboring":False},{"id":"17.242","name":"Прямые продажи","laboring":False},{"id":"17.256","name":"Розничная торговля","laboring":False},{"id":"17.269","name":"Телекоммуникации, Сетевые решения","laboring":False},{"id":"17.279","name":"Станки, тяжелое оборудование","laboring":False},{"id":"17.301","name":"Товары для бизнеса","laboring":False},{"id":"17.302","name":"FMCG, Товары народного потребления","laboring":False},{"id":"17.303","name":"Торговля биржевыми товарами","laboring":False},{"id":"17.306","name":"Торговый представитель","laboring":False},{"id":"17.324","name":"Управление продажами","laboring":False},{"id":"17.333","name":"Услуги для бизнеса","laboring":False},{"id":"17.334","name":"Услуги для населения","laboring":False},{"id":"17.350","name":"Цветные металлы","laboring":False},{"id":"17.358","name":"Электроника, фото, видео","laboring":False}]},{"id":"13","name":"Медицина, фармацевтика","specializations":[{"id":"13.398","name":"Клинические исследования","laboring":False},{"id":"13.432","name":"Производство","laboring":False},{"id":"13.433","name":"Регистратура","laboring":False},{"id":"13.438","name":"Оптика","laboring":False},{"id":"13.447","name":"Психология","laboring":False},{"id":"13.489","name":"Медицинский представитель","laboring":False},{"id":"13.537","name":"Медицинский советник","laboring":False},{"id":"13.567","name":"Дефектолог, Логопед","laboring":False},{"id":"13.578","name":"Фармацевт","laboring":False},{"id":"13.587","name":"Врач-эксперт","laboring":False},{"id":"13.732","name":"Стоматология","laboring":False},{"id":"13.748","name":"Другое","laboring":False},{"id":"13.49","name":"Ветеринария","laboring":False},{"id":"13.128","name":"Лаборант","laboring":False},{"id":"13.131","name":"Лечащий врач","laboring":False},{"id":"13.138","name":"Маркетинг","laboring":False},{"id":"13.155","name":"Младший и средний медперсонал","laboring":True},{"id":"13.185","name":"Начальный уровень, Мало опыта","laboring":False},{"id":"13.220","name":"Провизор","laboring":False},{"id":"13.227","name":"Продажи","laboring":False},{"id":"13.228","name":"Лекарственные препараты","laboring":False},{"id":"13.229","name":"Медицинское оборудование","laboring":False},{"id":"13.268","name":"Сертификация","laboring":False}]},{"id":"5","name":"Банки, инвестиции, лизинг","specializations":[{"id":"5.399","name":"Ипотека, Ипотечное кредитование","laboring":False},{"id":"5.424","name":"Паевые фонды","laboring":False},{"id":"5.426","name":"Экономист","laboring":False},{"id":"5.444","name":"Финансовый мониторинг","laboring":False},{"id":"5.450","name":"Кредитование малого и среднего бизнеса","laboring":False},{"id":"5.457","name":"Риски: операционные","laboring":False},{"id":"5.458","name":"Риски: финансовые","laboring":False},{"id":"5.459","name":"Риски: рыночные","laboring":False},{"id":"5.460","name":"Автокредитование","laboring":False},{"id":"5.534","name":"Факторинг","laboring":False},{"id":"5.579","name":"Работа с проблемными заемщиками","laboring":False},{"id":"5.691","name":"Private Banking","laboring":False},{"id":"5.735","name":"Другое","laboring":False},{"id":"5.4","name":"Forex","laboring":False},{"id":"5.23","name":"Акции, Ценные бумаги","laboring":False},{"id":"5.27","name":"Аналитик","laboring":False},{"id":"5.34","name":"Аудит, Внутренний контроль","laboring":False},{"id":"5.41","name":"Бумаги с фиксированной доходностью (fixed Income)","laboring":False},{"id":"5.42","name":"Бухгалтер","laboring":False},{"id":"5.45","name":"Валютный контроль","laboring":False},{"id":"5.51","name":"Внутренние операции (Back Office)","laboring":False},{"id":"5.61","name":"Денежный рынок (money market)","laboring":False},{"id":"5.79","name":"Инвестиционная компания","laboring":False},{"id":"5.101","name":"Трейдинг, Дилинг","laboring":False},{"id":"5.103","name":"Кассовое обслуживание, инкассация","laboring":False},{"id":"5.106","name":"Коммерческий банк","laboring":False},{"id":"5.121","name":"Корпоративное финансирование","laboring":False},{"id":"5.123","name":"Корреспондентские, Международные отношения","laboring":False},{"id":"5.124","name":"Риски: кредитные","laboring":False},{"id":"5.126","name":"Кредиты","laboring":False},{"id":"5.132","name":"Лизинг","laboring":False},{"id":"5.133","name":"Риски: лизинговые","laboring":False},{"id":"5.163","name":"Налоги","laboring":False},{"id":"5.177","name":"Начальный уровень, Мало опыта","laboring":False},{"id":"5.192","name":"Обменные пункты, Банкоматы","laboring":False},{"id":"5.195","name":"ОПЕРУ","laboring":False},{"id":"5.210","name":"Пластиковые карты","laboring":False},{"id":"5.215","name":"Портфельные инвестиции","laboring":False},{"id":"5.219","name":"Привлечение клиентов","laboring":False},{"id":"5.224","name":"Продажа финансовых продуктов","laboring":False},{"id":"5.234","name":"Проектное финансирование","laboring":False},{"id":"5.241","name":"Прямые инвестиции","laboring":False},{"id":"5.250","name":"Расчеты","laboring":False},{"id":"5.257","name":"Розничный бизнес","laboring":False},{"id":"5.262","name":"Руководство бухгалтерией","laboring":False},{"id":"5.304","name":"Торговое финансирование","laboring":False},{"id":"5.341","name":"Филиалы","laboring":False},{"id":"5.365","name":"Оценка залога, Стоимости имущества","laboring":False},{"id":"5.366","name":"Риски: прочие","laboring":False},{"id":"5.367","name":"Методология, Банковские технологии","laboring":False},{"id":"5.368","name":"Разработка новых продуктов, Маркетинг","laboring":False},{"id":"5.369","name":"Отчетность","laboring":False},{"id":"5.370","name":"Казначейство, Управление ликвидностью","laboring":False},{"id":"5.371","name":"Кредиты: розничные","laboring":False},{"id":"5.372","name":"Бюджетирование","laboring":False},{"id":"5.394","name":"Эмиссии","laboring":False}]},{"id":"21","name":"Транспорт, логистика","specializations":[{"id":"21.402","name":"Гражданская авиация","laboring":False},{"id":"21.403","name":"Бизнес-авиация","laboring":False},{"id":"21.480","name":"Контейнерные перевозки","laboring":False},{"id":"21.481","name":"Диспетчер","laboring":False},{"id":"21.482","name":"Водитель","laboring":True},{"id":"21.506","name":"Экспедитор","laboring":True},{"id":"21.563","name":"Кладовщик","laboring":True},{"id":"21.564","name":"Рабочий склада","laboring":True},{"id":"21.756","name":"Другое","laboring":False},{"id":"21.763","name":"Общественный транспорт","laboring":False},{"id":"21.12","name":"Авиаперевозки","laboring":False},{"id":"21.17","name":"Автоперевозки","laboring":True},{"id":"21.53","name":"ВЭД","laboring":False},{"id":"21.69","name":"Железнодорожные перевозки","laboring":False},{"id":"21.74","name":"Закупки, Снабжение","laboring":False},{"id":"21.136","name":"Логистика","laboring":False},{"id":"21.158","name":"Морские/Речные перевозки","laboring":False},{"id":"21.176","name":"Начальный уровень, Мало опыта","laboring":False},{"id":"21.275","name":"Складское хозяйство","laboring":False},{"id":"21.292","name":"Таможенное оформление","laboring":False},{"id":"21.310","name":"Трубопроводы","laboring":False}]},{"id":"18","name":"Производство, сельское хозяйство","specializations":[{"id":"18.404","name":"Сертификация","laboring":False},{"id":"18.431","name":"Главный механик","laboring":False},{"id":"18.451","name":"Управление проектами","laboring":False},{"id":"18.453","name":"Ювелирная промышленность","laboring":False},{"id":"18.488","name":"Метролог","laboring":False},{"id":"18.568","name":"Конструктор","laboring":False},{"id":"18.585","name":"Атомная энергетика","laboring":False},{"id":"18.752","name":"Другое","laboring":False},{"id":"18.13","name":"Авиационная промышленность","laboring":False},{"id":"18.16","name":"Автомобильная промышленность","laboring":False},{"id":"18.56","name":"Главный агроном","laboring":False},{"id":"18.57","name":"Главный инженер","laboring":False},{"id":"18.73","name":"Закупки и снабжение","laboring":False},{"id":"18.75","name":"Зоотехник","laboring":False},{"id":"18.81","name":"Инженер","laboring":False},{"id":"18.84","name":"Инженер, Мясо- и птицепереработка","laboring":False},{"id":"18.85","name":"Инженер, Производство и переработка зерновых","laboring":False},{"id":"18.86","name":"Инженер, Производство сахара","laboring":False},{"id":"18.118","name":"Контроль качества","laboring":False},{"id":"18.129","name":"Легкая промышленность","laboring":False},{"id":"18.130","name":"Деревообработка, Лесная промышленность","laboring":False},{"id":"18.142","name":"Машиностроение","laboring":False},{"id":"18.143","name":"Мебельное производство","laboring":False},{"id":"18.153","name":"Металлургия","laboring":False},{"id":"18.174","name":"Начальный уровень, Мало опыта","laboring":False},{"id":"18.190","name":"Нефтепереработка","laboring":False},{"id":"18.201","name":"Охрана труда","laboring":False},{"id":"18.208","name":"Пищевая промышленность","laboring":False},{"id":"18.212","name":"Полиграфия","laboring":False},{"id":"18.245","name":"Радиоэлектронная промышленность","laboring":False},{"id":"18.263","name":"Руководство предприятием","laboring":False},{"id":"18.265","name":"Сельхозпроизводство","laboring":False},{"id":"18.290","name":"Стройматериалы","laboring":False},{"id":"18.291","name":"Табачная промышленность","laboring":False},{"id":"18.297","name":"Технолог","laboring":False},{"id":"18.298","name":"Технолог, Мясо- и птицепереработка","laboring":False},{"id":"18.299","name":"Технолог, Производство и переработка зерновых","laboring":False},{"id":"18.300","name":"Технолог, Производство сахара","laboring":False},{"id":"18.330","name":"Управление цехом","laboring":False},{"id":"18.339","name":"Фармацевтическая промышленность","laboring":False},{"id":"18.348","name":"Химическая промышленность","laboring":False},{"id":"18.354","name":"Эколог","laboring":False},{"id":"18.360","name":"Электроэнергетика","laboring":False},{"id":"18.361","name":"Энергетик производства","laboring":False},{"id":"18.373","name":"Судостроение","laboring":False}]},{"id":"26","name":"Закупки","specializations":[{"id":"26.406","name":"Сертификация","laboring":False},{"id":"26.407","name":"Автомобили, Запчасти","laboring":False},{"id":"26.408","name":"Алкоголь","laboring":False},{"id":"26.409","name":"ГСМ, нефть, бензин","laboring":False},{"id":"26.410","name":"Компьютерная техника","laboring":False},{"id":"26.411","name":"Фармацевтика","laboring":False},{"id":"26.412","name":"Продукты питания","laboring":False},{"id":"26.413","name":"Товары для бизнеса","laboring":False},{"id":"26.414","name":"Электроника, фото, видео","laboring":False},{"id":"26.415","name":"Химическая продукция","laboring":False},{"id":"26.416","name":"FMCG, Товары народного потребления","laboring":False},{"id":"26.419","name":"Начальный уровень, Мало опыта","laboring":False},{"id":"26.427","name":"Металлопрокат","laboring":False},{"id":"26.437","name":"Управление закупками","laboring":False},{"id":"26.439","name":"Строительные материалы","laboring":False},{"id":"26.449","name":"Электротехническое оборудование/светотехника","laboring":False},{"id":"26.473","name":"Станки, Тяжелое оборудование","laboring":False},{"id":"26.574","name":"Тендеры","laboring":False},{"id":"26.742","name":"Другое","laboring":False}]},{"id":"19","name":"Страхование","specializations":[{"id":"19.421","name":"Актуарий","laboring":False},{"id":"19.430","name":"Урегулирование убытков","laboring":False},{"id":"19.483","name":"Перестрахование","laboring":False},{"id":"19.586","name":"Врач-эксперт","laboring":False},{"id":"19.754","name":"Другое","laboring":False},{"id":"19.18","name":"Автострахование","laboring":False},{"id":"19.19","name":"Агент","laboring":False},{"id":"19.28","name":"Андеррайтер","laboring":False},{"id":"19.108","name":"Комплексное страхование физических лиц","laboring":False},{"id":"19.109","name":"Комплексное страхование юридических лиц","laboring":False},{"id":"19.147","name":"Медицинское страхование","laboring":False},{"id":"19.170","name":"Начальный уровень, Мало опыта","laboring":False},{"id":"19.259","name":"Руководитель направления","laboring":False},{"id":"19.282","name":"Страхование бизнеса","laboring":False},{"id":"19.283","name":"Страхование жизни","laboring":False},{"id":"19.284","name":"Страхование недвижимости","laboring":False},{"id":"19.285","name":"Страхование ответственности","laboring":False},{"id":"19.357","name":"Эксперт-оценщик","laboring":False}]},{"id":"23","name":"Юристы","specializations":[{"id":"23.422","name":"Авторское право","laboring":False},{"id":"23.442","name":"Международное право","laboring":False},{"id":"23.476","name":"Земельное право","laboring":False},{"id":"23.477","name":"Договорное право","laboring":False},{"id":"23.478","name":"Регистрация юридических лиц","laboring":False},{"id":"23.479","name":"Взыскание задолженности, Коллекторская деятельность","laboring":False},{"id":"23.539","name":"Антимонопольное право","laboring":False},{"id":"23.759","name":"Другое","laboring":False},{"id":"23.2","name":"Compliance","laboring":False},{"id":"23.21","name":"Адвокат","laboring":False},{"id":"23.29","name":"Арбитраж","laboring":False},{"id":"23.36","name":"Банковское право","laboring":False},{"id":"23.72","name":"Законотворчество","laboring":False},{"id":"23.88","name":"Интеллектуальная собственность","laboring":False},{"id":"23.120","name":"Корпоративное право","laboring":False},{"id":"23.159","name":"Морское право","laboring":False},{"id":"23.165","name":"Налоговое право","laboring":False},{"id":"23.182","name":"Начальный уровень, Мало опыта","laboring":False},{"id":"23.187","name":"Недвижимость","laboring":False},{"id":"23.188","name":"Недропользование","laboring":False},{"id":"23.214","name":"Помощник","laboring":False},{"id":"23.266","name":"Семейное право","laboring":False},{"id":"23.276","name":"Слияния и поглощения","laboring":False},{"id":"23.286","name":"Страховое право","laboring":False},{"id":"23.311","name":"Трудовое право","laboring":False},{"id":"23.314","name":"Уголовное право","laboring":False},{"id":"23.352","name":"Ценные бумаги, Рынки капитала","laboring":False},{"id":"23.362","name":"Юрисконсульт","laboring":False}]},{"id":"3","name":"Маркетинг, реклама, PR","specializations":[{"id":"3.423","name":"Ассистент","laboring":False},{"id":"3.507","name":"Тайный покупатель","laboring":True},{"id":"3.508","name":"Проведение опросов, Интервьюер","laboring":True},{"id":"3.509","name":"Промоутер","laboring":True},{"id":"3.747","name":"Другое","laboring":False},{"id":"3.1","name":"Below The Line (BTL)","laboring":False},{"id":"3.8","name":"PR, Маркетинговые коммуникации","laboring":False},{"id":"3.26","name":"Аналитик","laboring":False},{"id":"3.31","name":"Арт директор","laboring":False},{"id":"3.40","name":"Бренд-менеджмент","laboring":False},{"id":"3.48","name":"Верстальщик","laboring":False},{"id":"3.64","name":"Дизайнер","laboring":False},{"id":"3.90","name":"Интернет-маркетинг","laboring":False},{"id":"3.98","name":"Исследования рынка","laboring":False},{"id":"3.114","name":"Консультант","laboring":False},{"id":"3.119","name":"Копирайтер","laboring":False},{"id":"3.148","name":"Менеджер по работе с клиентами","laboring":False},{"id":"3.150","name":"Менеджмент продукта (Product manager)","laboring":False},{"id":"3.151","name":"Мерчендайзинг","laboring":False},{"id":"3.166","name":"Наружная реклама","laboring":False},{"id":"3.171","name":"Начальный уровень, Мало опыта","laboring":False},{"id":"3.206","name":"Печатная реклама","laboring":False},{"id":"3.209","name":"Планирование, Размещение рекламы","laboring":False},{"id":"3.213","name":"Политический PR","laboring":False},{"id":"3.230","name":"Продвижение, Специальные мероприятия","laboring":False},{"id":"3.236","name":"Производство рекламы","laboring":False},{"id":"3.244","name":"Радио реклама","laboring":False},{"id":"3.253","name":"Рекламный агент","laboring":False},{"id":"3.294","name":"Телевизионная реклама","laboring":False},{"id":"3.305","name":"Торговый маркетинг(Trade marketing)","laboring":False},{"id":"3.318","name":"Управление маркетингом","laboring":False},{"id":"3.328","name":"Управление проектами","laboring":False}]},{"id":"2","name":"Бухгалтерия, управленческий учет, финансы предприятия","specializations":[{"id":"2.425","name":"Экономист","laboring":False},{"id":"2.434","name":"Планово-экономическое управление","laboring":False},{"id":"2.454","name":"МСФО, IFRS","laboring":False},{"id":"2.463","name":"Бухгалтер-калькулятор","laboring":False},{"id":"2.464","name":"Основные средства","laboring":False},{"id":"2.465","name":"GAAP","laboring":False},{"id":"2.467","name":"ACCA","laboring":False},{"id":"2.468","name":"ТМЦ","laboring":False},{"id":"2.469","name":"Первичная документация","laboring":False},{"id":"2.523","name":"CIPA","laboring":False},{"id":"2.737","name":"Другое","laboring":False},{"id":"2.33","name":"Аудит","laboring":False},{"id":"2.43","name":"Бухгалтер","laboring":False},{"id":"2.44","name":"Бюджетирование и планирование","laboring":False},{"id":"2.46","name":"Валютный контроль","laboring":False},{"id":"2.100","name":"Казначейство","laboring":False},{"id":"2.102","name":"Кассир, Инкассатор","laboring":False},{"id":"2.125","name":"Кредитный контроль","laboring":False},{"id":"2.164","name":"Налоги","laboring":False},{"id":"2.179","name":"Начальный уровень, Мало опыта","laboring":False},{"id":"2.200","name":"Оффшоры","laboring":False},{"id":"2.249","name":"Расчет себестоимости","laboring":False},{"id":"2.261","name":"Руководство бухгалтерией","laboring":False},{"id":"2.335","name":"Учет заработной платы","laboring":False},{"id":"2.337","name":"Учет счетов и платежей","laboring":False},{"id":"2.342","name":"Финансовый анализ","laboring":False},{"id":"2.343","name":"Финансовый контроль","laboring":False},{"id":"2.344","name":"Финансовый менеджмент","laboring":False},{"id":"2.351","name":"Ценные бумаги","laboring":False}]},{"id":"4","name":"Административный персонал","specializations":[{"id":"4.428","name":"Последовательный перевод","laboring":False},{"id":"4.429","name":"Делопроизводство","laboring":False},{"id":"4.456","name":"Вечерний секретарь","laboring":False},{"id":"4.494","name":"Уборщица/уборщик","laboring":True},{"id":"4.734","name":"Другое","laboring":False},{"id":"4.32","name":"Архивист","laboring":False},{"id":"4.47","name":"Ввод данных","laboring":False},{"id":"4.52","name":"Водитель","laboring":True},{"id":"4.127","name":"Курьер","laboring":True},{"id":"4.181","name":"Начальный уровень, Мало опыта","laboring":False},{"id":"4.205","name":"Персональный ассистент","laboring":False},{"id":"4.207","name":"Письменный перевод","laboring":False},{"id":"4.255","name":"Ресепшен","laboring":False},{"id":"4.264","name":"Секретарь","laboring":False},{"id":"4.271","name":"Синхронный перевод","laboring":False},{"id":"4.278","name":"Сотрудник call-центра","laboring":True},{"id":"4.332","name":"Управляющий офисом (Оffice manager)","laboring":False},{"id":"4.338","name":"Учет товарооборота","laboring":False},{"id":"4.374","name":"АХО","laboring":False}]},{"id":"16","name":"Государственная служба, некоммерческие организации","specializations":[{"id":"16.435","name":"НИИ","laboring":False},{"id":"16.569","name":"Архивариус","laboring":False},{"id":"16.570","name":"Атташе","laboring":False},{"id":"16.571","name":"Библиотекарь","laboring":False},{"id":"16.658","name":"Муниципалитет","laboring":False},{"id":"16.739","name":"Другое","laboring":False},{"id":"16.760","name":"Военнослужащий","laboring":False},{"id":"16.761","name":"Сотрудник полиции/ГИБДД","laboring":False},{"id":"16.38","name":"Благотворительность","laboring":False},{"id":"16.194","name":"Общественные организации","laboring":False},{"id":"16.216","name":"Правительство","laboring":False}]},{"id":"11","name":"Искусство, развлечения, масс-медиа","specializations":[{"id":"11.436","name":"Кино","laboring":False},{"id":"11.745","name":"Корректор, ретушер","laboring":False},{"id":"11.62","name":"Дизайн, графика, живопись","laboring":False},{"id":"11.71","name":"Журналистика","laboring":False},{"id":"11.76","name":"Издательская деятельность","laboring":False},{"id":"11.99","name":"Казино и игорный бизнес","laboring":False},{"id":"11.134","name":"Литературная, Редакторская деятельность","laboring":False},{"id":"11.157","name":"Мода","laboring":False},{"id":"11.160","name":"Музыка","laboring":False},{"id":"11.173","name":"Начальный уровень, Мало опыта","laboring":False},{"id":"11.218","name":"Пресса","laboring":False},{"id":"11.240","name":"Другое","laboring":False},{"id":"11.243","name":"Радио","laboring":False},{"id":"11.293","name":"Телевидение","laboring":False},{"id":"11.347","name":"Фотография","laboring":False}]},{"id":"9","name":"Высший менеджмент","specializations":[{"id":"9.448","name":"Юриспруденция","laboring":False},{"id":"9.452","name":"Страхование","laboring":False},{"id":"9.521","name":"Спортивные клубы, Фитнес, Салоны красоты","laboring":False},{"id":"9.532","name":"Управление закупками","laboring":False},{"id":"9.562","name":"Антикризисное управление","laboring":False},{"id":"9.738","name":"Другое","laboring":False},{"id":"9.22","name":"Администрирование","laboring":False},{"id":"9.67","name":"Добыча cырья","laboring":False},{"id":"9.78","name":"Инвестиции","laboring":False},{"id":"9.94","name":"Информационные технологии, Интернет, Мультимедиа","laboring":False},{"id":"9.95","name":"Искусство, Развлечения, Масс-медиа","laboring":False},{"id":"9.105","name":"Коммерческий Банк","laboring":False},{"id":"9.115","name":"Консультирование","laboring":False},{"id":"9.139","name":"Маркетинг, Реклама, PR","laboring":False},{"id":"9.145","name":"Медицина, Фармацевтика","laboring":False},{"id":"9.168","name":"Наука, Образование","laboring":False},{"id":"9.226","name":"Продажи","laboring":False},{"id":"9.238","name":"Производство, Технология","laboring":False},{"id":"9.289","name":"Строительство, Недвижимость","laboring":False},{"id":"9.307","name":"Транспорт, Логистика","laboring":False},{"id":"9.312","name":"Туризм, Гостиницы, Рестораны","laboring":False},{"id":"9.317","name":"Управление малым бизнесом","laboring":False},{"id":"9.321","name":"Управление персоналом, Тренинги","laboring":False},{"id":"9.345","name":"Финансы","laboring":False}]},{"id":"7","name":"Автомобильный бизнес","specializations":[{"id":"7.455","name":"Шины, Диски","laboring":False},{"id":"7.502","name":"Тонировщик","laboring":True},{"id":"7.503","name":"Автослесарь","laboring":True},{"id":"7.565","name":"Автожестянщик","laboring":True},{"id":"7.566","name":"Автомойщик","laboring":True},{"id":"7.733","name":"Другое","laboring":False},{"id":"7.14","name":"Автозапчасти","laboring":False},{"id":"7.222","name":"Продажа","laboring":False},{"id":"7.235","name":"Производство","laboring":False},{"id":"7.239","name":"Прокат, лизинг","laboring":False},{"id":"7.267","name":"Сервисное обслуживание","laboring":False},{"id":"7.392","name":"Начальный уровень, Мало опыта","laboring":False}]},{"id":"8","name":"Безопасность","specializations":[{"id":"8.461","name":"Системы видеонаблюдения","laboring":False},{"id":"8.462","name":"Взыскание задолженности, Коллекторская деятельность","laboring":False},{"id":"8.519","name":"Инкассатор","laboring":True},{"id":"8.575","name":"Пожарная безопасность","laboring":False},{"id":"8.736","name":"Другое","laboring":False},{"id":"8.77","name":"Имущественная безопасность","laboring":False},{"id":"8.135","name":"Личная безопасность","laboring":False},{"id":"8.202","name":"Охранник","laboring":True},{"id":"8.260","name":"Руководитель СБ","laboring":False},{"id":"8.356","name":"Экономическая и информационная безопасность","laboring":False}]},{"id":"10","name":"Добыча сырья","specializations":[{"id":"10.470","name":"Бурение","laboring":False},{"id":"10.471","name":"Маркшейдер","laboring":False},{"id":"10.472","name":"Газ","laboring":False},{"id":"10.740","name":"Другое","laboring":False},{"id":"10.54","name":"Геологоразведка","laboring":False},{"id":"10.80","name":"Инженер","laboring":False},{"id":"10.191","name":"Нефть","laboring":False},{"id":"10.258","name":"Руда","laboring":False},{"id":"10.315","name":"Уголь","laboring":False},{"id":"10.323","name":"Управление предприятием","laboring":False},{"id":"10.393","name":"Начальный уровень, Мало опыта","laboring":False}]},{"id":"22","name":"Туризм, гостиницы, рестораны","specializations":[{"id":"22.491","name":"Повар","laboring":True},{"id":"22.504","name":"Хостес","laboring":True},{"id":"22.505","name":"Швейцар","laboring":True},{"id":"22.518","name":"Сомелье","laboring":True},{"id":"22.529","name":"Анимация","laboring":True},{"id":"22.530","name":"Оформление виз","laboring":False},{"id":"22.531","name":"Управление туристическим бизнесом","laboring":False},{"id":"22.757","name":"Другое","laboring":False},{"id":"22.11","name":"Авиабилеты","laboring":False},{"id":"22.35","name":"Банкеты","laboring":False},{"id":"22.39","name":"Бронирование","laboring":False},{"id":"22.55","name":"Гид, Экскурсовод","laboring":False},{"id":"22.104","name":"Кейтеринг","laboring":False},{"id":"22.175","name":"Начальный уровень, Мало опыта","laboring":False},{"id":"22.193","name":"Официант, Бармен","laboring":True},{"id":"22.198","name":"Организация встреч, Конференций","laboring":False},{"id":"22.199","name":"Организация туристических продуктов","laboring":False},{"id":"22.204","name":"Персонал кухни","laboring":True},{"id":"22.223","name":"Продажа туристических услуг","laboring":False},{"id":"22.248","name":"Размещение, Обслуживание гостей","laboring":False},{"id":"22.316","name":"Управление гостиницами","laboring":False},{"id":"22.329","name":"Управление ресторанами, Барами","laboring":False},{"id":"22.353","name":"Шеф-повар","laboring":False}]},{"id":"24","name":"Спортивные клубы, фитнес, салоны красоты","specializations":[{"id":"24.492","name":"Массажист","laboring":True},{"id":"24.493","name":"Парикмахер","laboring":True},{"id":"24.624","name":"Ногтевой сервис","laboring":True},{"id":"24.753","name":"Другое","laboring":False},{"id":"24.377","name":"Косметология","laboring":True},{"id":"24.378","name":"Тренерский состав","laboring":False},{"id":"24.379","name":"Администрация","laboring":False},{"id":"24.380","name":"Продажи","laboring":False}]},{"id":"29","name":"Рабочий персонал","specializations":[{"id":"29.495","name":"Грузчик","laboring":True},{"id":"29.510","name":"Слесарь","laboring":True},{"id":"29.511","name":"Токарь, Фрезеровщик","laboring":True},{"id":"29.512","name":"Фасовщик","laboring":True},{"id":"29.513","name":"Столяр","laboring":True},{"id":"29.514","name":"Сварщик","laboring":True},{"id":"29.515","name":"Электрик","laboring":True},{"id":"29.516","name":"Швея","laboring":True},{"id":"29.517","name":"Сборщик","laboring":True},{"id":"29.540","name":"Гардеробщик","laboring":True},{"id":"29.541","name":"Дворник, Уборщик","laboring":True},{"id":"29.542","name":"Дорожные рабочие","laboring":True},{"id":"29.543","name":"Жестянщик","laboring":True},{"id":"29.544","name":"Заправщик картриджей","laboring":True},{"id":"29.545","name":"Комплектовщик, Укладчик-упаковщик","laboring":True},{"id":"29.546","name":"Краснодеревщик","laboring":True},{"id":"29.547","name":"Кузнец","laboring":True},{"id":"29.548","name":"Лифтер","laboring":True},{"id":"29.549","name":"Машинист производства","laboring":True},{"id":"29.550","name":"Машинист сцены","laboring":True},{"id":"29.551","name":"Машинист экскаватора","laboring":True},{"id":"29.552","name":"Механик","laboring":True},{"id":"29.553","name":"Оператор станков","laboring":True},{"id":"29.554","name":"Пастух, Чабан","laboring":True},{"id":"29.555","name":"Перемотчик","laboring":True},{"id":"29.556","name":"Разнорабочий","laboring":True},{"id":"29.557","name":"Сантехник","laboring":True},{"id":"29.558","name":"Шлифовщик","laboring":True},{"id":"29.559","name":"Штукатур","laboring":True},{"id":"29.560","name":"Электромонтер, Кабельщик","laboring":True},{"id":"29.561","name":"Ювелир","laboring":True},{"id":"29.581","name":"Монтажник","laboring":True},{"id":"29.582","name":"Проводник","laboring":True},{"id":"29.583","name":"Маляр","laboring":True},{"id":"29.588","name":"Другое","laboring":True},{"id":"29.162","name":"Наладчик","laboring":True}]},{"id":"27","name":"Домашний персонал","specializations":[{"id":"27.496","name":"Воспитатель, Гувернантка/гувернёр, Няня","laboring":True},{"id":"27.497","name":"домработница/домработник, Горничная","laboring":True},{"id":"27.498","name":"Персональный водитель","laboring":True},{"id":"27.499","name":"Садовник","laboring":True},{"id":"27.500","name":"Повар","laboring":True},{"id":"27.501","name":"Сиделка","laboring":True},{"id":"27.533","name":"Помощник по хозяйству, Управляющий","laboring":True},{"id":"27.584","name":"Репетитор","laboring":True},{"id":"27.741","name":"Другое","laboring":False}]},{"id":"15","name":"Начало карьеры, студенты","specializations":[{"id":"15.730","name":"Бухгалтерия","laboring":False},{"id":"15.731","name":"Закупки","laboring":False},{"id":"15.750","name":"Другое","laboring":False},{"id":"15.764","name":"Рабочий персонал","laboring":False},{"id":"15.68","name":"Добыча сырья","laboring":False},{"id":"15.93","name":"Информационные технологии, Интернет, Мультимедиа","laboring":False},{"id":"15.96","name":"Искусство, Развлечения, Масс-медиа","laboring":False},{"id":"15.140","name":"Маркетинг, Реклама, PR","laboring":False},{"id":"15.146","name":"Медицина, Фармацевтика","laboring":False},{"id":"15.167","name":"Наука, Образование","laboring":False},{"id":"15.237","name":"Производство, Технологии","laboring":False},{"id":"15.281","name":"Страхование","laboring":False},{"id":"15.288","name":"Строительство, Архитектура","laboring":False},{"id":"15.308","name":"Транспорт, Логистика","laboring":False},{"id":"15.313","name":"Туризм, Гостиницы, Рестораны","laboring":False},{"id":"15.320","name":"Управление персоналом","laboring":False},{"id":"15.346","name":"Финансы, Банки, Инвестиции","laboring":False},{"id":"15.363","name":"Юристы","laboring":False},{"id":"15.388","name":"Административный персонал","laboring":False},{"id":"15.389","name":"Продажи","laboring":False},{"id":"15.390","name":"Автомобильный бизнес","laboring":False},{"id":"15.391","name":"Консультирование","laboring":False}]},{"id":"25","name":"Инсталляция и сервис","specializations":[{"id":"25.743","name":"Другое","laboring":False},{"id":"25.381","name":"Сервисный инженер","laboring":False},{"id":"25.382","name":"Руководитель сервисного центра","laboring":False},{"id":"25.383","name":"Менеджер по сервису - сетевые и телекоммуникационные технологии","laboring":False},{"id":"25.384","name":"Менеджер по сервису - промышленное оборудование","laboring":False},{"id":"25.385","name":"Менеджер по сервису - транспорт","laboring":False},{"id":"25.386","name":"Инсталляция и настройка оборудования","laboring":False}]},{"id":"12","name":"Консультирование","specializations":[{"id":"12.746","name":"Другое","laboring":False},{"id":"12.5","name":"Internet, E-Commerce","laboring":False},{"id":"12.6","name":"Knowledge management","laboring":False},{"id":"12.7","name":"PR Consulting","laboring":False},{"id":"12.92","name":"Информационные технологии","laboring":False},{"id":"12.97","name":"Исследования рынка","laboring":False},{"id":"12.122","name":"Корпоративные финансы","laboring":False},{"id":"12.180","name":"Начальный уровень, Мало опыта","laboring":False},{"id":"12.197","name":"Организационное консультирование","laboring":False},{"id":"12.251","name":"Реинжиниринг бизнес процессов","laboring":False},{"id":"12.252","name":"Реинжиниринг, Аутсорсинг финансовой функции","laboring":False},{"id":"12.280","name":"Стратегия","laboring":False},{"id":"12.322","name":"Управление практикой","laboring":False},{"id":"12.326","name":"Управление проектами","laboring":False},{"id":"12.331","name":"Управленческое консультирование","laboring":False},{"id":"12.376","name":"Недвижимость","laboring":False}]},{"id":"14","name":"Наука, образование","specializations":[{"id":"14.749","name":"Другое","laboring":False},{"id":"14.762","name":"Дошкольное образование","laboring":False},{"id":"14.37","name":"Биотехнологии","laboring":False},{"id":"14.60","name":"Гуманитарные науки","laboring":False},{"id":"14.87","name":"Инженерные науки","laboring":False},{"id":"14.91","name":"Информатика, Информационные системы","laboring":False},{"id":"14.141","name":"Математика","laboring":False},{"id":"14.169","name":"Науки о Земле","laboring":False},{"id":"14.178","name":"Начальный уровень, Мало опыта","laboring":False},{"id":"14.217","name":"Преподавание","laboring":False},{"id":"14.340","name":"Физика","laboring":False},{"id":"14.349","name":"Химия","laboring":False},{"id":"14.355","name":"Экономика, Менеджмент","laboring":False},{"id":"14.364","name":"Языки","laboring":False}]},{"id":"6","name":"Управление персоналом, тренинги","specializations":[{"id":"6.758","name":"Другое","laboring":False},{"id":"6.107","name":"Компенсации и льготы","laboring":False},{"id":"6.184","name":"Начальный уровень, Мало опыта","laboring":False},{"id":"6.247","name":"Развитие персонала","laboring":False},{"id":"6.254","name":"Рекрутмент","laboring":False},{"id":"6.309","name":"Тренинги","laboring":False},{"id":"6.319","name":"Управление персоналом","laboring":False},{"id":"6.336","name":"Учет кадров","laboring":False}]}]
key1 = "1.395"
key2 = "1.400"
print(fetch(f, key2))