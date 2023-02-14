from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from main import bot, ConversationHandler
from database_modules import *

admin_reply_keyboard = [['حذف موضوع', 'افزودن موضوع'],
                        ['حذف همه ی موضوعات', 'نمایش موضوعات'],
                        ['بازگردانی کارتها', 'پخش کارتها', 'ایجاد کارتها'],
                        ['مشاهده ی اطلاعات کاربران']]
confirm_keyboard = [['خیر', 'بله']]
reply_keyboard_broadcast = [['زیرگروه ها', 'سرگروه ها']]
admin_markup = ReplyKeyboardMarkup(admin_reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
confirm_markup = ReplyKeyboardMarkup(confirm_keyboard, resize_keyboard=True, one_time_keyboard=True)
broadcast_markup = ReplyKeyboardMarkup(reply_keyboard_broadcast, resize_keyboard=True, one_time_keyboard=True)

CHECKADMINPASS, CHOOSEACTION, ADDSUB, DELETESUB, SHOWSUBJECTS, DELETEALLSUBJECTS, CREATECARDS, BROADCASTCARDS, RETURNCARDS, SHOWUSERINFORMATION = range(
    10)


async def admin(update, context):
    user = update.message.from_user
    user_data = context.user_data
    text = update.message.text
    print(text)

    await update.message.reply_text("رمز ورود به عنوان ادمین را وارد کنید:")
    return CHECKADMINPASS


admin_pass = os.getenv('ADMIN_PASS')


async def check_admin_pass(update, context):
    user = update.message.from_user
    user_data = context.user_data

    text = update.message.text
    check = text == admin_pass
    global student_num
    global hack
    hack = False
    student_num = -1
    if check:
        await update.message.reply_text("با موفقیت وارد شدید.", reply_markup=admin_markup)
        return CHOOSEACTION
    else:
        await update.message.reply_text("رمز ورود صحیح نیست لطفا دوباره سعی کنید:")
        return CHECKADMINPASS
        # try:
        #     user_data['enter_wrong_pass'] += 1
        # except:
        #     user_data['enter_wrong_pass'] = 1
        # wrong_pass = user_data['enter_wrong_pass']
        # hack = False
        # student_num = -1
        # if wrong_pass == 1:
        #     await update.message.reply_text("رمز ورود صحیح نیست لطفا دوباره سعی کنید:")
        # elif wrong_pass == 2:
        #     await update.message.reply_text("اگه ادمین نیستی الکی رمز نزن😐")
        #     await update.message.reply_text("اگه ادمینی رمز درستو بزن:")
        # elif wrong_pass == 3:
        #     await update.message.reply_text("مگه نمیگم اگه ادمین نیستی الکی رمز نزن🤨")
        # elif wrong_pass == 4:
        #     await update.message.reply_text("ببین تا صبم اینجا وایسی من رات نمیدم تو🤷‍♂️")
        # elif wrong_pass == 5:
        #     await update.message.reply_text("خب حالا مثلا ک چی؟😐")
        # elif wrong_pass == 6:
        #     await update.message.reply_text("بسه دیگه الان هنگ میکنم🤦‍♂️")
        # elif wrong_pass == 7:
        #     await update.message.reply_text("بچه برو درستو بخون دست از سر کچل من بردار")
        # elif wrong_pass == 8:
        #     await update.message.reply_text("نمیری؟😬")
        # elif wrong_pass == 9:
        #     await update.message.reply_text("تا کی میخوای اینجا بمونی؟😑")
        # elif wrong_pass == 10:
        #     await update.message.reply_text("بمون تا زیر پات علف سبز شه😒")
        # elif wrong_pass == 11:
        #     await update.message.reply_text("من ک دیگه جوابتو نمیدم👨‍🦯👨‍🦯")
        # elif wrong_pass == 12:
        #     await update.message.reply_text("😐")
        # elif wrong_pass == 13:
        #     await update.message.reply_text("😐😐")
        # elif wrong_pass == 14:
        #     await update.message.reply_text("😐😐😐")
        # elif wrong_pass == 15:
        #     await update.message.reply_text("😐😐😐😐")
        # elif wrong_pass == 16:
        #     await update.message.reply_text("😐😐😐😐😐")
        # elif wrong_pass == 17:
        #     await update.message.reply_text("خیلی بیکاری")
        # elif wrong_pass == 18:
        #     await update.message.reply_text("حالا ک فک میکنم من بیکارم ک نشستم کد اینارو زدم🫠")
        # elif wrong_pass == 19:
        #     await update.message.reply_text("عجب😐")
        # elif wrong_pass == 20:
        #     await update.message.reply_text("نری زنگ میزنم ب پلیس")
        # elif wrong_pass == 21:
        #     await update.message.reply_text("بابا دست از سرم بردار بذار برم ب کارای بقیه برسم🤦‍♂️")
        # elif wrong_pass == 22:
        #     await update.message.reply_text("کککککممممکککککککک")
        #     await update.message.reply_text("یکی منو از دست این نجات بدهههه😭")
        # elif wrong_pass == 23:
        #     await update.message.reply_text("😭😭😭😭")
        # elif wrong_pass == 24:
        #     await update.message.reply_text("😭😭😭😭")
        # elif wrong_pass == 25:
        #     await update.message.reply_text("باشه.باشه رمز ورودو بت میدم.فقط ولم کن😭")
        # elif wrong_pass == 26:
        #     await update.message.reply_text("رمز اینه: ********")
        # elif wrong_pass == 27:
        #     await update.message.reply_text("مثل اینکه با زبون خوش نمیری")
        # elif wrong_pass == 28:
        #     await update.message.reply_text("ی پیام دیگه بدی گوشیتو هک میکنم")
        # elif wrong_pass == 29:
        #     await update.message.reply_text("خودت خواستیا!")
        # elif wrong_pass == 30:
        #     await update.message.reply_text("درحال هک ...")
        # elif wrong_pass == 31:
        #     await update.message.reply_text("دارم هکت میکنم مزاحمم نشو")
        #     try:
        #         student_num = get_student_number(user.id)
        #         hack = True
        #     except:
        #         print('شماره دانشجویی ثبت نیست')
        #
        # elif wrong_pass == 32 and hack==True:
        #     await update.message.reply_text("هک کامل شد!")
        #     fname = get_student_fname(student_num)
        #     lname = get_student_lname(student_num)
        #
        #     await update.message.reply_text("نام: %s" % fname)
        #     await update.message.reply_text("نام خانوادگی: %s" % lname)
        #
        # elif wrong_pass == 32 and hack==False:
        #     await update.message.reply_text("هک نشدی😕")
        #
        # elif wrong_pass == 33:
        #     await update.message.reply_text("من دیگه واقعا رفتم!خداحافظ")
        # else:
        #     await update.message.reply_text("😴")
        #     return ConversationHandler.END
        # return CHECKADMINPASS


async def choose_action(update, context):
    user = update.message.from_user
    user_data = context.user_data

    text = update.message.text
    if text == 'افزودن موضوع':
        return ADDSUB
    elif text == 'حذف موضوع':
        return DELETESUB
    elif text == 'نمایش موضوعات':
        return SHOWSUBJECTS
    elif text == 'حذف همه ی موضوعات':
        return DELETEALLSUBJECTS
    elif text == 'ایجاد کارتها':
        await update.message.reply_text("آیا از انجام این فرایند مطمئن هستید؟", reply_markup=confirm_markup)
        return CREATECARDS
    elif text == 'پخش کارتها':
        await update.message.reply_text("قصد پخش کدام دسته از کارتها را دارید؟", reply_markup=broadcast_markup)
        return BROADCASTCARDS
    elif text == 'بازگردانی کارتهای پخش شده':
        return RETURNCARDS
    elif text == 'مشاهده ی اطلاعات کاربران':
        return SHOWUSERINFORMATION
    else:
        await update.message.reply_text("لطفا دستور صحیح را وارد کنید.")
        return CHOOSEACTION


async def create_card_cancel(update, context):
    await update.message.reply_text("ایجاد کارتها لغو شد!", reply_markup=admin_markup)
    return CHOOSEACTION


async def add_cards_db(update, context):
    cnx = database_connector()
    cursor = cnx.cursor()
    delete_leader_cards = "DELETE FROM leader_cards WHERE id != 0;"
    cursor.execute(delete_leader_cards)

    cursor = cnx.cursor()
    delete_cards = "DELETE FROM cards WHERE id != 0;"
    cursor.execute(delete_cards)
    cnx.commit()
    cursor.close()
    cards = create_cards()
    cursor = cnx.cursor()
    for data in cards:
        for i in range(len(data) - 1):
            add_card = "INSERT INTO `cards`(`student_id`,`subject_id`) VALUES " \
                       "({student_id},{subject_id})".format(student_id=data[i + 1], subject_id=data[0])
            print(add_card)
            cursor.execute(add_card)
            cursor = cnx.cursor()
    cnx.commit()
    cursor.close()
    database_disconect(cnx)
    await update.message.reply_text("کارتها با موفقیت در دیتابیس ایجاد شدند.", reply_markup=admin_markup)
    return CHOOSEACTION


async def broadcast_leader_cards(update, context):
    leader_nums = get_leader_nums()
    for student_number in leader_nums:
        first_name = get_student_fname(student_number)
        last_name = get_student_lname(student_number)
        chat_id = get_student_chat_id(student_number)
        topic = get_leader_topic(student_number)
        description = get_leader_description(student_number)

        text = " \n سلام {fname} {lname} عزیز با شماره دانشجویی {student_num}" \
               "\n شما در جلسه ی آینده به عنوان سرگروه انتخاب شده اید" \
               " \n.میباشد {top} موضوع گروه شما در جلسه ی آینده " \
               "\n{descrip} :توضیحات".format(fname=first_name, lname=last_name, student_num=student_number, top=topic,
                                             descrip=description)
        print(text)
        try:
            await bot.send_message(chat_id=chat_id, text=text)
        except:
            print("chat with id %d not fount" % chat_id)
    await update.message.reply_text("کارتهای سرگروه ها با موفقیت پخش شدند.", reply_markup=admin_markup)
    return CHOOSEACTION


async def broadcast_cards(update, context):

    student_nums = get_student_nums()
    for student_number in student_nums:
        subject_id = get_subject_id(student_number)
        first_name = get_student_fname(student_number)
        last_name = get_student_lname(student_number)
        chat_id = get_student_chat_id(student_number)
        topic = get_subject_topic(subject_id)
        description = get_subject_description(subject_id)
        title = get_subject_title(subject_id)

        text = " \n سلام {fname} {lname} عزیز با شماره دانشجویی {student_num}" \
               " \n.میباشد {title} موضوع شما در جلسه ی آینده " \
               "\n{descrip} :توضیحات".format(fname=first_name, lname=last_name, student_num=student_number, title=title,
                                             descrip=description)
        print(text)
        try:
            await bot.send_message(chat_id=chat_id, text=text)
        except:
            print("chat with id %d not fount" % chat_id)
    await update.message.reply_text("کارتها ها با موفقیت پخش شدند.", reply_markup=admin_markup)
    return CHOOSEACTION


if __name__ == '__main__':
    get_subject_topic(6)
