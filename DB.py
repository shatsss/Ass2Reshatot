# coding=utf-8
from Resource import Resource


# class that holds out articles(our DB)
class DB:
    def __init__(self):
        self.list = []
        self.CreateDBOfArticles()

    # create the DB of our application
    def CreateDBOfArticles(self):
        resources_list = [Resource('http://www.ynet.co.il/articles/0,7340,L-4713571,00.html',
                                   'https://images1.ynet.co.il/PicServer4/2014/08/05/5506384/52203970100690640360no.jpg',
                                   'החוש הדומיננטי שיעזור לכם בלימודים',
                                   'החוש הדומיננטי שיעזור לכם בלימודים. אילו טיפים של שימושבחושים יעזרו לכם?'),
                          Resource('http://www.ynet.co.il/articles/0,7340,L-5045541,00.html',
                                   'https://images1.ynet.co.il/PicServer5/2017/11/23/8172884/817287001000100980704no.jpg',
                                   '"כ"ט בנובמבר: "שמחה שנמשכה ימים ולילות, הייתה אופוריה"',
                                   'ב1947- הם היו ילדים או צעירים בתחילת דרכם,' +
                                   ' אבל את היום הגורלי ב29- בנובמבר הם לא שוכחים עד היום.' +
                                   ' "כולם היו צמודים לרדיו. אני זוכרת את התפרצות השמחה, ריקודים והתחבקויות."'),
                          Resource('https://www.calcalist.co.il/world/articles/0,7340,L-3726321,00.html',
                                   'https://images1.calcalist.co.il/PicServer3/2017/11/30/775736/2_l.jpg',
                                   'רוצים נייר טואלט? הזדהו: כך משפרים הסינים את מצב השירותים הציבוריים',
                                   'שבוע קרא נשיא סין שי ג‘ינפינג להמשיך את מהפכת השירותים' +
                                   ' הציבוריים עליה הכריז ב-2015. עד כה שופצו ונבנו 68 אלף מתקנים'),
                          Resource('http://www.nrg.co.il/online/13/ART2/902/962.html',
                                   'http://www.nrg.co.il/images/archive/465x349/1/646/416.jpg',
                                   'מחקו לכם הודעה בווטסאפ? עדיין תוכלו לקרוא אותה',
                                   'אפליקציה בשם Notification History מאפשרת למשתמשי אנדרואיד' +
                                   ' לקורא את הנתונים הזמניים הנשמרים ביומן הפעילות של הסמארטפון. כולל הודעות מחוקות.'),
                          Resource('http://www.nrg.co.il/online/55/ART2/904/542.html',
                                   'http://www.nrg.co.il/images/archive/465x349/1/795/429.jpg',
                                   'גם בחורף: זה בדיוק הזמן לקפוץ לאילת',
                                   'העיר הדרומית נעימה לנופש גם בחודשי החורף.' +
                                   ' כעת מוצעים מחירים אטרקטיביים במיוחד בחבילות שכוללות מגוון אטרקציות, לינה וטיסות'),
                          Resource('https://food.walla.co.il/item/3113079',
                                   'https://img.wcdn.co.il/f_auto,w_700/2/5/1/3/2513314-46.jpg',
                                   '12 בתי קפה שמתאימים לעבודה עם לפטופ',
                                   'בין אם אתם סטודנטים או עצמאיים, זה תמיד סיפור למצוא בית קפה נעים וטעים לרבוץ בו.' +
                                   ' קיבצנו עבורכם 12 מקומות אהובים בדיוק למטרה זו, בארבע הערים הגדולות'),
                          Resource('https://news.walla.co.il/item/3114145',
                                   'https://img.wcdn.co.il/f_auto,w_700/2/4/9/5/2495334-46.jpg',
                                   'שותק על אזריה, נלחם באהוד ברק: בנט מנסה להיבנות כימין ממלכתי',
                                   'כשרגב נלחמת ברעש בתאטרון יפו, בנט משנה בשקט את נהלי סל התרבות כך ' +
                                   'שהחומרים "השמאלנים" ייפלטו. כשהקשת הפוליטית מתרעמת על דיווחי' +
                                   ' ה"דיל" של טראמפ עם הפלסטינים, בנט שותק עד שהרשות תסרב.'),
                          Resource('https://news.walla.co.il/item/3114283',
                                   'https://img.wcdn.co.il/f_auto,w_700/2/5/1/4/2514588-46.jpg',
                                   'רצח בכל שלושה ימים: צרפת יוצאת למאבק באלימות נגד נשים',
                                   'אחרי ש126- נשים נרצחו בידי בני זוגן בשנה שעברה, ' +
                                   'הציג מקרון צעדים חדשים למלחמה בתופעה. "זאת בושה לצרפת,"' +
                                   ' אמר הנשיא שאחת מהבטחות הבחירות שלו הייתה להשיג שוויון מגדרי.')]
        self.list = resources_list

    # get the length of our dictionary
    def GetLength(self):
        return len(self.list)

    # get the list that holds out DB
    def GetList(self, i):
        return self.list[i]
