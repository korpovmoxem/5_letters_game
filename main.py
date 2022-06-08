import os
import sys

from kivy.config import Config
Config.set('graphics', 'resizable', '1')
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '700')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder
from random import choice
from random import random



lst_words = ['Абрис', 'Акула', 'Аминь', 'Арест', 'Афиша', 'Автор', 'Алкаш', 'Анонс', 'Архив', 'Адрес', 'Алтын', 'Апчхи',
             'Астра', 'Абрек', 'Актив', 'Амеба', 'Арена', 'Афера', 'Автол', 'Алиби', 'Ангел', 'Архар', 'Адепт', 'Алмаз',
             'Апорт', 'Астма', 'Аборт', 'Актер', 'Амвон', 'Ареал', 'Атолл', 'Аврал', 'Алеть', 'Ангар', 'Армяк', 'Агнец',
             'Аллюр', 'Аорта', 'Аспид', 'Абзац', 'Акать', 'Амбар', 'Аргон', 'Атлет', 'Авось', 'Акция', 'Ампир', 'Армия',
             'Агент', 'Аллея', 'Анчар', 'Аскет', 'Аббат', 'Аймак', 'Альфа', 'Арбуз', 'Атлас', 'Аванс', 'Акциз', 'Ампер',
             'Аркан', 'Ахать', 'Агава', 'Аллах', 'Анфас', 'Аршин', 'Азарт', 'Алыча', 'Арабы', 'Атака', 'Багет', 'Барак',
             'Батог', 'Белка', 'Бирюк', 'Бобик', 'Босой', 'Брысь', 'Булат', 'Бухта', 'Байка', 'Барин', 'Бачок', 'Берег',
             'Битый', 'Бойня', 'Браво', 'Бугай', 'Буран', 'Бытье', 'Балок', 'Барыш', 'Бегун', 'Бидон', 'Блеск', 'Бомба',
             'Брать', 'Будто', 'Бурый', 'Багаж', 'Банка', 'Баста', 'Белек', 'Бирка', 'Бобер', 'Борть', 'Броня', 'Букса',
             'Буфет', 'Базис', 'Барий', 'Бачки', 'Беляк', 'Битлы', 'Божок', 'Бочка', 'Бубны', 'Бурак', 'Бытие', 'Балка',
             'Барон', 'Бегом', 'Бивни', 'Бланк', 'Болид', 'Брасс', 'Будни', 'Бурун', 'Бабка', 'Бандо', 'Басок', 'Бекон',
             'Биржа', 'Бляха', 'Боров', 'Бровь', 'Букли', 'Буфер', 'Базар', 'Баржа', 'Бахча', 'Белье', 'Битки', 'Божий',
             'Бочар', 'Бубен', 'Бурав', 'Былье', 'Балет', 'Бармы', 'Бдеть', 'Бивак', 'Блажь', 'Более', 'Брань', 'Будка',
             'Бурки', 'Банда', 'Басня', 'Бекас', 'Бином', 'Блюдо', 'Борец', 'Брить', 'Букле', 'Бутуз', 'Бадья', 'Барда',
             'Батут', 'Белый', 'Битва', 'Божба', 'Ботва', 'Брюхо', 'Бульк', 'Былой', 'Балда', 'Барка', 'Башня', 'Бетон',
             'Благо', 'Боком', 'Брада', 'Будет', 'Бурка', 'Бювар', 'Банан', 'Басма', 'Бейка', 'Билет', 'Блуза', 'Бордо',
             'Брешь', 'Букет', 'Бутсы', 'Багор', 'Баран', 'Батон', 'Белок', 'Бисер', 'Богач', 'Босяк', 'Брюки', 'Булка',
             'Быдло', 'Бакен', 'Барич', 'Башка', 'Берет', 'Битюг', 'Бокал', 'Брага', 'Бугор', 'Бурда', 'Бычок', 'Балык',
             'Баски', 'Бедро', 'Бизон', 'Блоха', 'Бонна', 'Бремя', 'Буква', 'Бутон', 'Валуй', 'Вдали', 'Венок', 'Вешка',
             'Вилла', 'Вкруг', 'Вовсю', 'Волхв', 'Время', 'Вчуже', 'Выкуп', 'Ватка', 'Вдоль', 'Весло', 'Взвар', 'Вирши',
             'Влечь', 'Возка', 'Ворот', 'Вслед', 'Выбор', 'Вырез', 'Валек', 'Вброд', 'Везти', 'Ветер', 'Взнос', 'Виток',
             'Вновь', 'Войти', 'Впору', 'Втечь', 'Выгон', 'Вялый', 'Валок', 'Ввысь', 'Веник', 'Вечор', 'Вилка', 'Вкось',
             'Вовсе', 'Волос', 'Врать', 'Вчера', 'Выйти', 'Ватин', 'Вдова', 'Верша', 'Вживе', 'Вирус', 'Влево', 'Вожжи',
             'Ворон', 'Всего', 'Въявь', 'Выпот', 'Вакса', 'Вбить', 'Везде', 'Ветвь', 'Взлет', 'Витой', 'Внове', 'Война',
             'Вояка', 'Всяко', 'Выгиб', 'Вьюга', 'Валки', 'Вволю', 'Венец', 'Вечно', 'Визит', 'Вклад', 'Вовне', 'Волок',
             'Врата', 'Вуаль', 'Вызов', 'Ванна', 'Вдеть', 'Верфь', 'Веять', 'Вираж', 'Власы', 'Вождь', 'Ворог', 'Врыть',
             'Въезд', 'Выпас', 'Вазон', 'Ваять', 'Вежда', 'Весть', 'Вздох', 'Вития', 'Внизу', 'Возок', 'Вотще', 'Всюду',
             'Вывоз', 'Вышка', 'Валка', 'Ввить', 'Велюр', 'Вечер', 'Визир', 'Вишня', 'Вовек', 'Волна', 'Враль', 'Втуне',
             'Выезд', 'Вальс', 'Вдвое', 'Верба', 'Вещун', 'Виола', 'Влага', 'Вожак', 'Вопль', 'Врозь', 'Вшить', 'Выпад',
             'Вагон', 'Вахта', 'Ведро', 'Вести', 'Вздор', 'Висок', 'Вмять', 'Возня', 'Вотум', 'Всход', 'Вывод', 'Вычет',
             'Валик', 'Ввиду', 'Велик', 'Ветла', 'Взять', 'Вихрь', 'Вобла', 'Волан', 'Враки', 'Втрое', 'Выдра', 'Валун',
             'Вдаль', 'Вепрь', 'Вещий', 'Вилок', 'Вкупе', 'Водка', 'Вольт', 'Вроде', 'Вширь', 'Вынос', 'Вафля', 'Вдруг',
             'Весна', 'Взвод', 'Виски', 'Влить', 'Возле', 'Ворох', 'Вслух', 'Вывих', 'Выход', 'Валет', 'Вверх', 'Векша',
             'Ветка', 'Взрыв', 'Вихор', 'Внять', 'Вокал', 'Впрок', 'Втора', 'Выдох', 'Вящий', 'Галлы', 'Гжель', 'Гниль',
             'Гонец', 'Греки', 'Гуано', 'Гараж', 'Гичка', 'Гогот', 'Горка', 'Грипп', 'Гумно', 'Гейша', 'Глист', 'Голос',
             'Гофре', 'Грунт', 'Гусем', 'Галка', 'Гетто', 'Гнида', 'Гомон', 'Греза', 'Грязь', 'Гамма', 'Гирло', 'Говор',
             'Горец', 'Грива', 'Гуляш', 'Гвалт', 'Глина', 'Голод', 'Гость', 'Грудь', 'Гусар', 'Гайка', 'Гетры', 'Гнать',
             'Гольф', 'Графа', 'Грязи', 'Гамак', 'Гипюр', 'Гобой', 'Гопак', 'Греча', 'Гудок', 'Гашиш', 'Гладь', 'Голик',
             'Горох', 'Груда', 'Гусак', 'Газон', 'Герой', 'Глыба', 'Голье', 'Грань', 'Гряда', 'Галун', 'Гиена', 'Гнуть',
             'Гонор', 'Греть', 'Губка', 'Гарус', 'Главк', 'Голец', 'Город', 'Гросс', 'Гурия', 'Газик', 'Гений', 'Глушь',
             'Голыш', 'Гранд', 'Грыжа', 'Гюрза', 'Галоп', 'Гидра', 'Гнить', 'Гонка', 'Греко', 'Гуашь', 'Гарем', 'Глава',
             'Годок', 'Горло', 'Гроза', 'Гунны', 'Гавот', 'Гелий', 'Глубь', 'Голый', 'Грамм', 'Груша', 'Гусли', 'Давка',
             'Давно', 'Далее', 'Дамба', 'Дамка', 'Даром', 'Дверь', 'Дебет', 'Дебил', 'Дебит', 'Дебош', 'Дебри', 'Дебют',
             'Девиз', 'Девка', 'Деизм', 'Деист', 'Декан', 'Дележ', 'Делец', 'Демон', 'Денди', 'Дерби', 'Десна', 'Десть',
             'Детва', 'Детка', 'Дефис', 'Дзюдо', 'Диван', 'Диета', 'Дикий', 'Динар', 'Динго', 'Дичок', 'Длань', 'Длина',
             'Длить', 'Днище', 'Добре', 'Добро', 'Довод', 'Догма', 'Дождь', 'Дозор', 'Доить', 'Дойти', 'Докер', 'Долой',
             'Домна', 'Домой', 'Домра', 'Донец', 'Донка', 'Донор', 'Донос', 'Доска', 'Досуг', 'Досыл', 'Досье', 'Дотла',
             'Доход', 'Дочка', 'Драга', 'Драже', 'Драка', 'Драла', 'Драма', 'Драть', 'Древо', 'Дрейф', 'Дрель', 'Дрема',
             'Дробь', 'Дрова', 'Евнух', 'Евреи', 'Егерь', 'Егоза', 'Едкий', 'Ежели', 'Ежиха', 'Ездка', 'Ездок', 'Езжай',
             'Екать', 'Емкий', 'Ересь', 'Есаул', 'Ехать', 'Жабры', 'Жажда', 'Жакан', 'Жакет', 'Жалко', 'Жарок', 'Жатва',
             'Жатка', 'Жвала', 'Ждать', 'Желоб', 'Желчь', 'Жених', 'Жердь', 'Жерех', 'Жерло', 'Жесть', 'Жетон', 'Живец',
             'Живой', 'Живот', 'Жизнь', 'Жилет', 'Жилец', 'Жилка', 'Жилой', 'Жилье', 'Жираф', 'Житие', 'Житье', 'Жница',
             'Жокей', 'Жрать', 'Жулик', 'Жупан', 'Жупел', 'Жучка', 'Жучок', 'Забег', 'Забой', 'Забор', 'Завал', 'Завет',
             'Завод', 'Завоз', 'Завуч', 'Загар', 'Загиб', 'Загон', 'Задел', 'Задок', 'Задом', 'Задор', 'Заезд', 'Зажим',
             'Зажор', 'Зазор', 'Заика', 'Зайка', 'Зайти', 'Заказ', 'Закал', 'Закат', 'Закон', 'Закут', 'Залеж', 'Залив',
             'Залог', 'Залом', 'Замок', 'Замор', 'Замша', 'Занос', 'Запад', 'Запал', 'Запас', 'Запах', 'Запев', 'Запой',
             'Запор', 'Зараз', 'Зарез', 'Зарок', 'Заряд', 'Засим', 'Засов', 'Засол', 'Затем', 'Затея', 'Затон', 'Затор',
             'Заумь', 'Заход', 'Зачем', 'Зачес', 'Зачет', 'Зачин', 'Звать', 'Звено', 'Зверь', 'Здесь', 'Зебра', 'Зевок',
             'Зелье', 'Земля', 'Зенит', 'Зерно', 'Зефир', 'Зимой', 'Зипун', 'Зиять', 'Злато', 'Злеть', 'Злить', 'Злоба',
             'Злюка', 'Знамя', 'Знать', 'Зразы', 'Зреть', 'Зубец', 'Зубок', 'Зурна', 'Зыбка', 'Зыбун', 'Иваси', 'Ивняк',
             'Игрец', 'Игрок', 'Игрун', 'Идеал', 'Идиот', 'Иерей', 'Ижица', 'Избач', 'Извив', 'Извне', 'Извод', 'Извоз',
             'Изгиб', 'Изгой', 'Излет', 'Излом', 'Изъян', 'Изыск', 'Изюбр', 'Икать', 'Икона', 'Икота', 'Иметь', 'Индус',
             'Индюк', 'Инжир', 'Интер', 'Инъяз', 'Иприт', 'Ирбис', 'Искра', 'Искус', 'Ислам', 'Испуг', 'Истец', 'Исток',
             'Истый', 'Исход', 'Итого', 'Иудеи', 'Ихний', 'Ишиас', 'Кабак', 'Кабан', 'Кагор', 'Кадет', 'Кадка', 'Кадры',
             'Кадык', 'Казак', 'Казан', 'Казна', 'Казнь', 'Казус', 'Кайло', 'Кайма', 'Какао', 'Каков', 'Какой', 'Калан',
             'Калач', 'Калий', 'Калым', 'Камея', 'Камин', 'Камка', 'Камса', 'Камыш', 'Канал', 'Канат', 'Канва', 'Канон',
             'Каноэ', 'Канун', 'Канюк', 'Капля', 'Капор', 'Капот', 'Капут', 'Карат', 'Карга', 'Карий', 'Карст', 'Карта',
             'Каска', 'Касса', 'Каста', 'Катар', 'Катер', 'Катет', 'Катод', 'Каток', 'Катыш', 'Качка', 'Кашка', 'Кашне',
             'Кашпо', 'Каюта', 'Квант', 'Кварц', 'Квота', 'Кегли', 'Келья', 'Кенаф', 'Кепка', 'Кефир', 'Кзади', 'Кивер',
             'Кивок', 'Кизил', 'Кизяк', 'Киоск', 'Кирза', 'Кирка', 'Кисет', 'Кисея', 'Киска', 'Киста', 'Кисть', 'Кичка',
             'Кишка', 'Кладь', 'Клака', 'Класс', 'Клерк', 'Клест', 'Клеть', 'Клещи', 'Клика', 'Клише', 'Клоун', 'Клуша',
             'Клюка', 'Кляча', 'Кнехт', 'Книга', 'Книзу', 'Князь', 'Кобза', 'Кобра', 'Ковер', 'Когда', 'Лабаз', 'Лаваш',
             'Лавка', 'Лавра', 'Ладан', 'Ладья', 'Лазер', 'Лайка', 'Лакей', 'Лампа', 'Лапка', 'Лапта', 'Лапша', 'Ларек',
             'Ларец', 'Ласка', 'Лассо', 'Латка', 'Латук', 'Лафит', 'Лаять', 'Лгать', 'Левак', 'Левша', 'Левый', 'Легат',
             'Лежак', 'Лежка', 'Лежмя', 'Лезть', 'Лейка', 'Лемех', 'Лемма', 'Лемур', 'Лента', 'Ленца', 'Лепет', 'Лепка',
             'Лепта', 'Леска', 'Лесть', 'Летка', 'Леток', 'Летом', 'Летун', 'Леший', 'Лиана', 'Ливер', 'Лидер', 'Ликер',
             'Лилия', 'Лиман', 'Лимит', 'Лимон', 'Лимфа', 'Линек', 'Линза', 'Линия', 'Лирик', 'Литер', 'Литой', 'Литье',
             'Лихач', 'Лихой', 'Лицей', 'Лишай', 'Лишек', 'Лобби', 'Лобок', 'Ловец', 'Ловля', 'Лодка', 'Ложка', 'Ложок',
             'Локон', 'Ломка', 'Лопух', 'Лотос', 'Лохмы', 'Лоция', 'Лошак', 'Лубок', 'Лужок', 'Лузга', 'Лунка', 'Лучок',
             'Лыжня', 'Лысый', 'Лычки', 'Лычко', 'Льяло', 'Любой', 'Люнет', 'Люпин', 'Лютик', 'Лютня', 'Лютый', 'Ляжка',
             'Лямка', 'Ляпис','Мавры', 'Магий', 'Магия', 'Магма', 'Мадам', 'Маета', 'Мажор', 'Мазня', 'Мазок', 'Мазут',
             'Майка', 'Майна', 'Майор', 'Макар', 'Макет', 'Макси', 'Малек', 'Малец', 'Малый', 'Малыш', 'Маляр', 'Мамка',
             'Манго', 'Манеж', 'Манер', 'Мание', 'Мания', 'Манка', 'Манна', 'Манок', 'Манси', 'Манто', 'Манту', 'Марал',
             'Марка', 'Марля', 'Маска', 'Масло', 'Масон', 'Масса', 'Масть', 'Матка', 'Мафия', 'Махра', 'Махры', 'Мачта',
             'Медик', 'Медяк', 'Мезга', 'Мелок', 'Менее', 'Мерин', 'Мерка', 'Месса', 'Мести', 'Место', 'Месть', 'Месяц',
             'Метан', 'Метил', 'Метис', 'Метка', 'Метла', 'Метод', 'Метро', 'Мечта', 'Мешок', 'Мигом', 'Мидия', 'Милый',
             'Минер', 'Минор', 'Минус', 'Миома', 'Мираж', 'Мирра', 'Миска', 'Митра', 'Мишка', 'Млеть', 'Мнить', 'Много',
             'Может', 'Можно', 'Мойва', 'Мойка', 'Молва', 'Молот', 'Молох', 'Молча', 'Монах', 'Мопед', 'Морда', 'Мороз',
             'Моряк', 'Мосол', 'Мотив', 'Мотка', 'Мотня', 'Моток', 'Набат', 'Набег', 'Набок', 'Набор', 'Навар', 'Навек',
             'Навес', 'Навет', 'Навоз', 'Навой', 'Навык', 'Наган', 'Нагар', 'Нагой', 'Нагул', 'Надел', 'Надой', 'Наезд',
             'Нажиг', 'Нажим', 'Нажин', 'Назад', 'Назем', 'Назло', 'Найти', 'Наказ', 'Накат', 'Налет', 'Налив', 'Налим',
             'Налог', 'Намаз', 'Намек', 'Намет', 'Намыв', 'Нанка', 'Нанос', 'Напев', 'Напор', 'Нарез', 'Народ', 'Нарты',
             'Нарыв', 'Наряд', 'Насос', 'Натек', 'Наука', 'Нахал', 'Нация', 'Начес', 'Начет', 'Наяву', 'Наяда', 'Невод',
             'Негде', 'Негры', 'Недра', 'Недуг', 'Нейти', 'Некий', 'Некто', 'Немой', 'Немцы', 'Ненцы', 'Нерпа', 'Нести',
             'Несть', 'Несун', 'Нетто', 'Нефть', 'Нечто', 'Нивхи', 'Нигде', 'Низок', 'Низом', 'Никак', 'Никто', 'Нимфа',
             'Нитка', 'Ничей', 'Ничто', 'Ничья', 'Нищий', 'Новый', 'Ножик', 'Ножка', 'Ножны', 'Номер', 'Норка', 'Норма',
             'Норов', 'Носик', 'Носка', 'Носок', 'Ночью', 'Нужда', 'Нулик', 'Нутро', 'Нынче', 'Нырок', 'Оазис', 'Обвал',
             'Обвод', 'Обгон', 'Обзор', 'Обида', 'Обить', 'Обком', 'Облик', 'Облом', 'Обман', 'Обмен', 'Образ', 'Обрат',
             'Обрез', 'Оброк', 'Обруб', 'Обруч', 'Обрыв', 'Обряд', 'Обувь', 'Обуза', 'Обуть', 'Обход', 'Общий', 'Объем',
             'Обыск', 'Овощи', 'Овощь', 'Овраг', 'Овсюг', 'Овчар', 'Огонь', 'Огрех', 'Одежа', 'Одеть', 'Одурь', 'Ожечь',
             'Ожить', 'Оземь', 'Озеро', 'Озимь', 'Озноб', 'Окать', 'Океан', 'Окись', 'Оклад', 'Оклик', 'Оковы', 'Около',
             'Окрик', 'Окрол', 'Округ', 'Оксид', 'Октет', 'Окунь', 'Олень', 'Олива', 'Олимп', 'Олифа', 'Олово', 'Ольха',
             'Омега', 'Омела', 'Омлет', 'Омуль', 'Омыть', 'Оникс', 'Онуча', 'Опала', 'Опара', 'Опека', 'Опера', 'Опись',
             'Опить', 'Опиум', 'Оплот', 'Опоек', 'Опока', 'Опора', 'Опрос', 'Оптик', 'Оптом', 'Опять', 'Орава', 'Орало',
             'Орать', 'Орган', 'Оргия', 'Орден', 'Ордер', 'Ореол', 'Орлан', 'Орлец', 'Осада', 'Осень', 'Осетр', 'Осина',
             'Оскал', 'Ослик', 'Падеж', 'Падуб', 'Пайка', 'Пакет', 'Пакля', 'Палас', 'Палач', 'Палаш', 'Палех', 'Палец',
             'Палка', 'Панда', 'Панна', 'Панно', 'Панты', 'Папка', 'Парад', 'Парез', 'Парик', 'Пария', 'Паром', 'Парта',
             'Парус', 'Парча', 'Парша', 'Пасмо', 'Паста', 'Пасти', 'Пасть', 'Пасха', 'Патер', 'Пауза', 'Пафос', 'Пахта',
             'Пацан', 'Пачка', 'Пашня', 'Паять', 'Певец', 'Пегий', 'Пекло', 'Пемза', 'Пенал', 'Пение', 'Пенка', 'Пенни',
             'Пепел', 'Перед', 'Перец', 'Перси', 'Перст', 'Персы', 'Песец', 'Песнь', 'Песня', 'Песок', 'Петит', 'Петля',
             'Петух', 'Пехом', 'Печка', 'Пеший', 'Пешка', 'Пешня', 'Пиала', 'Пиано', 'Пижон', 'Пикап', 'Пикет', 'Пикша',
             'Пилка', 'Пилот', 'Пинок', 'Пинта', 'Пират', 'Пирог', 'Писец', 'Питон', 'Питье', 'Пихта', 'Пицца', 'Пищик',
             'Пламя', 'Пласт', 'Плата', 'Плато', 'Плаун', 'Плаха', 'Плева', 'Племя', 'Плеск', 'Плеть', 'Плечо', 'Плешь',
             'Плита', 'Плица', 'Плоть', 'Плыть', 'Пнуть', 'Побег', 'Равно', 'Радар', 'Раджа', 'Радий', 'Радио', 'Радон',
             'Разве', 'Разом', 'Разор', 'Разум', 'Район', 'Ралли', 'Рамка', 'Рампа', 'Ранее', 'Ранет', 'Ранец', 'Ранчо',
             'Расти', 'Ратай', 'Раунд', 'Рафик', 'Рахит', 'Рация', 'Рачий', 'Рачок', 'Рвань', 'Рвать', 'Рвота', 'Рдеть',
             'Ребро', 'Ребус', 'Регби', 'Редис', 'Редут', 'Режим', 'Резак', 'Резец', 'Резка', 'Резня', 'Резон', 'Резус',
             'Рейка', 'Рельс', 'Ремиз', 'Рента', 'Репей', 'Ретро', 'Речка', 'Решка', 'Реять', 'Ржать', 'Рикша', 'Ритор',
             'Рифма', 'Робот', 'Ровно', 'Ровня', 'Рогач', 'Рогоз', 'Родео', 'Родич', 'Родня', 'Рожок', 'Рожон', 'Розан',
             'Розга', 'Розно', 'Рознь', 'Рокот', 'Ролик', 'Роман', 'Рондо', 'Ропак', 'Ропот', 'Ротор', 'Рохля', 'Рояль',
             'Ртуть', 'Рубеж', 'Рубец', 'Рубин', 'Рубка', 'Рубль', 'Ругня', 'Ружье', 'Руина', 'Рукав', 'Рулет', 'Рулон',
             'Рупия', 'Рупор', 'Русак', 'Русло', 'Русый', 'Ручей', 'Ручка', 'Рыбак', 'Рыбец', 'Рыбий', 'Саами', 'Сабля',
             'Саван', 'Садик', 'Садок', 'Сазан', 'Сайда', 'Сайка', 'Сайра', 'Сакля', 'Салат', 'Салки', 'Салон', 'Салоп',
             'Салют', 'Саман', 'Самбо', 'Самец', 'Самка', 'Самум', 'Самый', 'Санки', 'Сапер', 'Сарай', 'Саржа', 'Сарыч',
             'Сатин', 'Сатир', 'Сауна', 'Сахар', 'Сачок', 'Сбить', 'Сбоку', 'Сброд', 'Сбруя', 'Сбыть', 'Свара', 'Сваха',
             'Сверх', 'Свеча', 'Свиль', 'Свист', 'Свита', 'Свить', 'Свора', 'Свояк', 'Свыше', 'Связь', 'Сдать', 'Сдача',
             'Сдвиг', 'Сдоба', 'Сдуру', 'Сдуть', 'Сеанс', 'Север', 'Седло', 'Седой', 'Седок', 'Сезон', 'Секач', 'Секта',
             'Семга', 'Семью', 'Семья', 'Сенаж', 'Сенат', 'Сепия', 'Сербы', 'Серия', 'Серна', 'Серсо', 'Серый', 'Сесть',
             'Сетка', 'Сечка', 'Сеять', 'Сжать', 'Сжечь', 'Сжить', 'Сзади', 'Сивка', 'Сивуч', 'Сивый', 'Сидор', 'Сизый',
             'Силач', 'Силой', 'Силок', 'Силос', 'Синий', 'Синод', 'Синус', 'Синяк', 'Сирин', 'Сироп', 'Сирый', 'Ситец',
             'Ситро', 'Сифон', 'Табак', 'Табло', 'Табор', 'Табун', 'Тавро', 'Таган', 'Таить', 'Тайга', 'Тайна', 'Таков',
             'Такой', 'Такса', 'Такси', 'Талер', 'Талия', 'Талон', 'Талый', 'Тальк', 'Танго', 'Танец', 'Танин', 'Тапер',
             'Тапир', 'Таран', 'Тариф', 'Таска', 'Тафта', 'Тахта', 'Тачка', 'Таять', 'Тварь', 'Твист', 'Театр', 'Тезис',
             'Тезка', 'Теизм', 'Текст', 'Телец', 'Телик', 'Телка', 'Телок', 'Тембр', 'Тенек', 'Тенор', 'Тепло', 'Терем',
             'Терка', 'Тесак', 'Тесто', 'Тесть', 'Тетка', 'Течка', 'Тиара', 'Типаж', 'Типун', 'Тираж', 'Тиран', 'Тиски',
             'Титан', 'Титло', 'Титул', 'Тихий', 'Ткань', 'Ткать', 'Тлеть', 'Товар', 'Тогда', 'Толки', 'Толпа', 'Толща',
             'Томат', 'Тонус', 'Топаз', 'Топка', 'Топор', 'Топот', 'Торба', 'Торги', 'Торец', 'Торос', 'Тоска', 'Тотем',
             'Точка', 'Тощий', 'Трава', 'Тракт', 'Транс', 'Трата', 'Траур', 'Треба', 'Трель', 'Треск', 'Трест', 'Треть',
             'Треух', 'Трефы', 'Триер', 'Трико', 'Тромб', 'Тропа', 'Уазик', 'Убить', 'Убыль', 'Убыть', 'Увить', 'Уголь',
             'Угорь', 'Удаль', 'Удача', 'Удила', 'Удить', 'Уесть', 'Ужели', 'Узина', 'Узить', 'Узкий', 'Узник', 'Уклад',
             'Уклон', 'Укора', 'Укроп', 'Уксус', 'Улика', 'Улита', 'Улица', 'Уметь', 'Умник', 'Умный', 'Умора', 'Умыть',
             'Умять', 'Унция', 'Унять', 'Упечь', 'Упрек', 'Упырь', 'Усечь', 'Усики', 'Успех', 'Устав', 'Устой', 'Уступ',
             'Устье', 'Утеря', 'Утеха', 'Утечь', 'Утиль', 'Утица', 'Утлый', 'Утром', 'Ухарь', 'Ухват', 'Учеба', 'Учить',
             'Учхоз', 'Ушить', 'Ушкуй', 'Ушлый', 'Ушник', 'Ушной', 'Ущерб', 'Фавор', 'Фагот', 'Фазан', 'Фазис', 'Факел',
             'Факир', 'Фалда', 'Фальц', 'Фанза', 'Фасад', 'Фаска', 'Фасон', 'Фауна', 'Фаянс', 'Фенил', 'Фенол', 'Ферзь',
             'Ферма', 'Феска', 'Фетиш', 'Фиакр', 'Фибра', 'Фижмы', 'Физик', 'Фикус', 'Филей', 'Филер', 'Филин', 'Филон',
             'Фильм', 'Финал', 'Финик', 'Финиш', 'Финка', 'Финны', 'Фиорд', 'Фирма', 'Фишка', 'Фланг', 'Флешь', 'Флирт',
             'Флокс', 'Флора', 'Фляга', 'Фокус', 'Фомка', 'Форма', 'Форте', 'Форум', 'Фраза', 'Франк', 'Франт', 'Фрахт',
             'Фреза', 'Френч', 'Фронт', 'Фрукт', 'Фугас', 'Фужер', 'Фуляр', 'Фураж', 'Фурия', 'Фурор', 'Фьорд', 'Фьють',
             'Фюрер', 'Хайло', 'Халат', 'Халва', 'Халда', 'Халиф', 'Хамса', 'Хамье', 'Ханжа', 'Ханты', 'Хвать', 'Хворь',
             'Хвост', 'Херес', 'Хилый', 'Хиляк', 'Химик', 'Химия', 'Хинди', 'Хинин', 'Хиппи', 'Хитон', 'Хлыст',
             'Хлюст', 'Хлябь', 'Хмель', 'Хобби', 'Хобот', 'Ходка', 'Ходок', 'Ходом', 'Холка', 'Холод', 'Холоп', 'Холст',
             'Холуй', 'Хомут', 'Хомяк', 'Хорал', 'Хорда', 'Хорей', 'Хорек', 'Хором', 'Хохма', 'Хохол', 'Хохот', 'Хруст',
             'Худой', 'Хунта', 'Хурал', 'Хурма', 'Хутор', 'Цапка', 'Цапля', 'Цвето', 'Цевка', 'Цевье', 'Цедра', 'Целый',
             'Центр', 'Цепка', 'Цибик', 'Цикля', 'Цинга', 'Циник', 'Цитра', 'Цифра', 'Цокот', 'Цукат', 'Цуцик', 'Цыпка',
             'Цыпки', 'Чабан', 'Чадра', 'Чайка', 'Чалка', 'Чалма', 'Чалый', 'Чарка', 'Часом', 'Часть', 'Чашка', 'Чаять',
             'Чекан', 'Челка', 'Чепец', 'Черви', 'Червь', 'Черед', 'Через', 'Череп', 'Чернь', 'Черта', 'Честь', 'Четки',
             'Чехол', 'Чечет', 'Чешки', 'Чешуя', 'Чибис', 'Чижик', 'Чирей', 'Чирок', 'Число', 'Читка', 'Чохом', 'Чрево',
             'Чреда', 'Чрезо', 'Чтиво', 'Чтить', 'Чубук', 'Чугун', 'Чудак', 'Чудик', 'Чудом', 'Чужак', 'Чужой', 'Чуйка',
             'Чукчи', 'Чулан', 'Чулок', 'Чумак', 'Чурек', 'Чурка', 'Чуток', 'Чутье', 'Чушка', 'Чуять', 'Шабаш', 'Шавка',
             'Шагом', 'Шайба', 'Шайка', 'Шакал', 'Шалаш', 'Шалун', 'Шалый', 'Шаман', 'Шамот', 'Шанец', 'Шапка', 'Шарах',
             'Шарик', 'Шасси', 'Шасть', 'Шатен', 'Шатер', 'Шатия', 'Шатун', 'Шафер', 'Шахта', 'Шашка', 'Шашни', 'Шваль',
             'Шведы', 'Шевро', 'Шейка', 'Шелом', 'Шельф', 'Шемая', 'Шепот', 'Шериф', 'Шерпы', 'Шесть', 'Шизик', 'Шинок',
             'Шипун', 'Ширма', 'Шитый', 'Шитье', 'Шифер', 'Шифон', 'Шихта', 'Шишак', 'Шишка', 'Шкала', 'Шквал', 'Шкода',
             'Школа', 'Шкура', 'Шланг', 'Шлейф', 'Шлюха', 'Шляпа', 'Шмель', 'Шорня', 'Шорох', 'Шорты', 'Шоссе', 'Шофер',
             'Шпага', 'Шпала', 'Шпана', 'Шпаты', 'Шпиль', 'Шпион', 'Шпора', 'Шприц', 'Шпунт', 'Шрифт', 'Штамп', 'Штаны',
             'Штиль', 'Штифт', 'Штора', 'Шторм', 'Штраф', 'Штрек', 'Штрих', 'Штука', 'Штурм', 'Штырь', 'Шулер', 'Шумок',
             'Шурин', 'Шуруп', 'Шутка', 'Шушун', 'Шхеры', 'Шхуна', 'Щегол', 'Щекот', 'Щелка', 'Щелок', 'Щенок', 'Щепка',
             'Щетка', 'Щечка', 'Щипок', 'Щипцы', 'Щиток', 'Щучий', 'Эвены', 'Эклер', 'Экран', 'Элита', 'Эмаль', 'Энный',
             'Эпоха', 'Эрзац', 'Эркер', 'Эскиз', 'Эстет', 'Этика', 'Этнос', 'Ябеда', 'Явить', 'Явный', 'Ягель', 'Ягода',
             'Ягуар', 'Яичко', 'Якобы', 'Якорь', 'Якуты', 'Ямина', 'Ямщик', 'Яркий', 'Ярлык', 'Ярыга', 'Ясень', 'Ясный',
             'Яство', 'Ястык', 'Яхонт', 'Юноша', 'Юниор', 'Юрист']


class GameApp(App):


    word_count = 0  # count of letters in try

    word_to_guess = [i.upper() for i in choice(lst_words)]  # create word to guess

    lst_current_buttons = []    # history of pressed buttons in try

    global_lst_cells = []   # history of used windows at whole game

    try_word = []   # guessed letters. need to check being guessed word in dictionary

    print(word_to_guess)


    def popup_reaction(self, popup_button):

        if popup_button.text == 'Да, хочу новую':
            GameApp.word_to_guess = [i.upper() for i in choice(lst_words)]  # create new word to guess
            GameApp.lst_current_buttons = []    # clear history of pressed button at last game
            GameApp.word_count = 0  # clear count of letters at last game

            # clear all windows
            for cell in GameApp.global_lst_cells:
                cell.text = ''
                cell.background_color = (1, 1, 1, 1)
            self.word_window1_cell1.text = '' # idk after clear cycle first window is not clear
            self.word_window1_cell1.background_color = (1, 1, 1, 1) # same

            # make all letter buttons white
            for but in self.lst_buttons:
                but.background_color = (1, 1, 1, 1)

            # init list of windows
            self.lst_cells = [self.word_window1_cell1, self.word_window1_cell2, self.word_window1_cell3,
                              self.word_window1_cell4,
                              self.word_window1_cell5, self.word_window2_cell1, self.word_window2_cell2,
                              self.word_window2_cell3,
                              self.word_window2_cell4, self.word_window2_cell5, self.word_window3_cell1,
                              self.word_window3_cell2,
                              self.word_window3_cell3, self.word_window3_cell4, self.word_window3_cell5,
                              self.word_window4_cell1,
                              self.word_window4_cell2, self.word_window4_cell3, self.word_window4_cell4,
                              self.word_window4_cell5,
                              self.word_window5_cell1, self.word_window5_cell2, self.word_window5_cell3,
                              self.word_window5_cell4,
                              self.word_window5_cell5]
            self.popup.dismiss()


    def change_window_letter(self, button): # pressed buttons reaction

        if button.text == 'New':    # start new game

            # create popup window
            popup_box = BoxLayout(orientation='vertical', padding=10)
            popup_box.add_widget(Label(text='Хочешь начать новую игру?', font_size=17))
            self.popup = Popup(title='Новая игра', title_size=30, title_align='center', content=popup_box,
                          size_hint=(None, None),
                          size=(300, 300), auto_dismiss=False,
                          background_color=(random(), random(), random(), 0.8))
            button_yes = Button(text='Да, хочу новую', background_color=(1, 0, 0, 1), on_press=self.popup_reaction)
            button_no = Button(text='Нет, продолжаем', background_color=(0, 1, 0, 1), on_press=self.popup.dismiss)
            popup_box.add_widget(button_yes)
            popup_box.add_widget(button_no)
            self.popup.open()

        elif button.text == '<':    # pressed back button (delete last letter)
            if GameApp.word_count > 0:
                GameApp.word_count -= 1
                del GameApp.lst_current_buttons[-1]
                self.lst_cells[GameApp.word_count].text = ''
                del GameApp.global_lst_cells[-1]
                del GameApp.try_word[-1]

        elif button.text == '>':    # push word to check right letters

            if GameApp.word_count == 5:    # check number of letters

<<<<<<< Updated upstream
                    # guessed only letter
                    elif GameApp.lst_current_buttons[i].text in GameApp.word_to_guess:
                        self.lst_cells[i].background_color = [1, 1, 0, 1]
=======
                if ''.join(GameApp.try_word).capitalize() in lst_words:  # check word in dictionary

                    self.count_guessed_letters = 0
>>>>>>> Stashed changes

                    for i in range(5):  # check every letter

                        # guessed letter and position
                        if GameApp.lst_current_buttons[i].text == GameApp.word_to_guess[i]:
                            self.lst_cells[i].background_color = [0,1,0,1]
                            self.lst_current_buttons[i].background_color = [0,1,0,1]
                            self.count_guessed_letters += 1

                        # guessed only letter
                        elif GameApp.lst_current_buttons[i].text in GameApp.word_to_guess:
                            self.lst_cells[i].background_color = [1, 1, 0, 1]
                            self.lst_current_buttons[i].background_color = [1, 1, 0, 1]

                        # guessed no letter
                        else:
                            self.lst_current_buttons[i].background_color = [0,0,0,1]

                        GameApp.try_word = []

                    # guessed word
                    if self.count_guessed_letters == 5:

                        # create popup
                        popup_box = BoxLayout(orientation='vertical', padding=10)
                        popup_box.add_widget(Label(text=f'Тебе удалось угадать слово \n{"".join(GameApp.word_to_guess).capitalize()}\n'
                                                        f''
                                                        f'Начать новую игру?', font_size=17))
                        self.popup = Popup(title='Ура!', title_size=15,
                                           title_align='center', content=popup_box,
                                           size_hint=(None, None),
                                           size=(300, 300), auto_dismiss=False,
                                           background_color=(random(), random(), random(), 0.8))
                        button_yes = Button(text='Да, хочу новую', background_color=(0, 1, 0, 1),
                                            on_press=self.popup.dismiss)
                        button_no = Button(text='Нет, надоело', background_color=(1, 0, 0, 1),
                                           on_press=self.popup.dismiss)
                        popup_box.add_widget(button_yes)
                        popup_box.add_widget(button_no)
                        self.popup.open()

                    # clear counter and lists
                    del self.lst_cells[:5]
                    GameApp.word_count = 0
                    GameApp.lst_current_buttons = []

                    # was last try
                    if len(GameApp.global_lst_cells) == 25:
                        
                        # create popup
                        pass


        # write letter to window
        elif GameApp.word_count != 5:
            self.lst_cells[GameApp.word_count].text = button.text
            GameApp.word_count += 1
            GameApp.lst_current_buttons.append(button)
            GameApp.global_lst_cells.append(self.lst_cells[GameApp.word_count])
            GameApp.try_word.append(button.text)


    def build(self):

        # create game field
        root = BoxLayout(orientation='vertical', padding=5)

        # 1 answer window
        self.word_window1 = BoxLayout(orientation='horizontal', padding=3)

        self.word_window1_cell1 = TextInput(text='', font_size=70)
        self.word_window1_cell2 = TextInput(text='', font_size=70)
        self.word_window1_cell3 = TextInput(text='', font_size=70)
        self.word_window1_cell4 = TextInput(text='', font_size=70)
        self.word_window1_cell5 = TextInput(text='', font_size=70)

        self.word_window1.add_widget(self.word_window1_cell1)
        self.word_window1.add_widget(self.word_window1_cell2)
        self.word_window1.add_widget(self.word_window1_cell3)
        self.word_window1.add_widget(self.word_window1_cell4)
        self.word_window1.add_widget(self.word_window1_cell5)


        # 2 answer window
        self.word_window2 = BoxLayout(orientation='horizontal', padding=3)

        self.word_window2_cell1 = TextInput(text='', font_size=70)
        self.word_window2_cell2 = TextInput(text='', font_size=70)
        self.word_window2_cell3 = TextInput(text='', font_size=70)
        self.word_window2_cell4 = TextInput(text='', font_size=70)
        self.word_window2_cell5 = TextInput(text='', font_size=70)

        self.word_window2.add_widget(self.word_window2_cell1)
        self.word_window2.add_widget(self.word_window2_cell2)
        self.word_window2.add_widget(self.word_window2_cell3)
        self.word_window2.add_widget(self.word_window2_cell4)
        self.word_window2.add_widget(self.word_window2_cell5)

        # 3 answer window
        self.word_window3 = BoxLayout(orientation='horizontal', padding=3)

        self.word_window3_cell1 = TextInput(text='', font_size=70)
        self.word_window3_cell2 = TextInput(text='', font_size=70)
        self.word_window3_cell3 = TextInput(text='', font_size=70)
        self.word_window3_cell4 = TextInput(text='', font_size=70)
        self.word_window3_cell5 = TextInput(text='', font_size=70)

        self.word_window3.add_widget(self.word_window3_cell1)
        self.word_window3.add_widget(self.word_window3_cell2)
        self.word_window3.add_widget(self.word_window3_cell3)
        self.word_window3.add_widget(self.word_window3_cell4)
        self.word_window3.add_widget(self.word_window3_cell5)

        # 4 answer window
        self.word_window4 = BoxLayout(orientation='horizontal', padding=3)

        self.word_window4_cell1 = TextInput(text='', font_size=70)
        self.word_window4_cell2 = TextInput(text='', font_size=70)
        self.word_window4_cell3 = TextInput(text='', font_size=70)
        self.word_window4_cell4 = TextInput(text='', font_size=70)
        self.word_window4_cell5 = TextInput(text='', font_size=70)

        self.word_window4.add_widget(self.word_window4_cell1)
        self.word_window4.add_widget(self.word_window4_cell2)
        self.word_window4.add_widget(self.word_window4_cell3)
        self.word_window4.add_widget(self.word_window4_cell4)
        self.word_window4.add_widget(self.word_window4_cell5)

        # 4 answer window
        self.word_window5 = BoxLayout(orientation='horizontal', padding=3)

        self.word_window5_cell1 = TextInput(text='', font_size=70)
        self.word_window5_cell2 = TextInput(text='', font_size=70)
        self.word_window5_cell3 = TextInput(text='', font_size=70)
        self.word_window5_cell4 = TextInput(text='', font_size=70)
        self.word_window5_cell5 = TextInput(text='', font_size=70)

        self.word_window5.add_widget(self.word_window5_cell1)
        self.word_window5.add_widget(self.word_window5_cell2)
        self.word_window5.add_widget(self.word_window5_cell3)
        self.word_window5.add_widget(self.word_window5_cell4)
        self.word_window5.add_widget(self.word_window5_cell5)

        root.add_widget(self.word_window1)
        root.add_widget(self.word_window2)
        root.add_widget(self.word_window3)
        root.add_widget(self.word_window4)
        root.add_widget(self.word_window5)

        self.lst_cells = [self.word_window1_cell1, self.word_window1_cell2, self.word_window1_cell3, self.word_window1_cell4,
                     self.word_window1_cell5, self.word_window2_cell1, self.word_window2_cell2, self.word_window2_cell3,
                     self.word_window2_cell4, self.word_window2_cell5, self.word_window3_cell1, self.word_window3_cell2,
                     self.word_window3_cell3, self.word_window3_cell4, self.word_window3_cell5, self.word_window4_cell1,
                     self.word_window4_cell2, self.word_window4_cell3, self.word_window4_cell4, self.word_window4_cell5,
                     self.word_window5_cell1, self.word_window5_cell2, self.word_window5_cell3, self.word_window5_cell4,
                     self.word_window5_cell5]


        # create buttons
        self.allButtons = GridLayout(cols=12)

        self.button_1 = Button(text='Й', background_color=[1,1,1,1], on_press=self.change_window_letter)
        self.button_2 = Button(text='Ц', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_3 = Button(text='У', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_4 = Button(text='К', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_5 = Button(text='Е', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_6 = Button(text='Н', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_7 = Button(text='Г', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_8 = Button(text='Ш', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_9 = Button(text='Щ', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_10 = Button(text='З', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_11 = Button(text='Х', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_12 = Button(text='Ъ', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_13 = Button(text='Ф', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_14 = Button(text='Ы', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_15 = Button(text='В', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_16 = Button(text='А', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_17 = Button(text='П', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_18 = Button(text='Р', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_19 = Button(text='О', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_20 = Button(text='Л', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_21 = Button(text='Д', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_22 = Button(text='Ж', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_23 = Button(text='Э', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_24 = Button(text='Я', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_25 = Button(text='Ч', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_26 = Button(text='С', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_27 = Button(text='М', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_28 = Button(text='И', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_29 = Button(text='Т', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_30 = Button(text='Ь', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_31 = Button(text='Б', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_32 = Button(text='Ю', background_color=[1, 1, 1, 1], on_press=self.change_window_letter)
        self.button_back = Button(text='<', background_color=[1, 0, 0, 1], on_press=self.change_window_letter)
        self.button_enter = Button(text='>', background_color=[0, 0, 1, 1], on_press=self.change_window_letter)
        self.button_newgame = Button(text='New', background_color=[0, 1, 1, 1], on_press=self.change_window_letter)

        self.lst_buttons = [self.button_1, self.button_2, self.button_3, self.button_4, self.button_5, self.button_6,
                            self.button_7, self.button_8, self.button_9, self.button_10, self.button_11, self.button_12,
                            self.button_13, self.button_14, self.button_15, self.button_16, self.button_17,
                            self.button_18, self.button_19, self.button_20, self.button_21, self.button_22,
                            self.button_23, self.button_24, self.button_25, self.button_26, self.button_27,
                            self.button_28, self.button_29, self.button_30, self.button_31, self.button_32]


        self.allButtons.add_widget(self.button_1)
        self.allButtons.add_widget(self.button_2)
        self.allButtons.add_widget(self.button_3)
        self.allButtons.add_widget(self.button_4)
        self.allButtons.add_widget(self.button_5)
        self.allButtons.add_widget(self.button_6)
        self.allButtons.add_widget(self.button_7)
        self.allButtons.add_widget(self.button_8)
        self.allButtons.add_widget(self.button_9)
        self.allButtons.add_widget(self.button_10)
        self.allButtons.add_widget(self.button_11)
        self.allButtons.add_widget(self.button_12)
        self.allButtons.add_widget(self.button_13)
        self.allButtons.add_widget(self.button_14)
        self.allButtons.add_widget(self.button_15)
        self.allButtons.add_widget(self.button_16)
        self.allButtons.add_widget(self.button_17)
        self.allButtons.add_widget(self.button_18)
        self.allButtons.add_widget(self.button_19)
        self.allButtons.add_widget(self.button_20)
        self.allButtons.add_widget(self.button_21)
        self.allButtons.add_widget(self.button_22)
        self.allButtons.add_widget(self.button_23)
        self.allButtons.add_widget(self.button_24)
        self.allButtons.add_widget(self.button_25)
        self.allButtons.add_widget(self.button_26)
        self.allButtons.add_widget(self.button_27)
        self.allButtons.add_widget(self.button_28)
        self.allButtons.add_widget(self.button_29)
        self.allButtons.add_widget(self.button_30)
        self.allButtons.add_widget(self.button_31)
        self.allButtons.add_widget(self.button_32)
        self.allButtons.add_widget(self.button_back)
        self.allButtons.add_widget(self.button_enter)
        self.allButtons.add_widget(self.button_newgame)

        root.add_widget(self.allButtons)

        return root


if __name__ == '__main__':
    GameApp().run()




