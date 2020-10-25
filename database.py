import psycopg2

connection = psycopg2.connect(
    dbname = 'xgnrjxwo',
    user = 'xgnrjxwo',
    password = 'GT9jy1pbqBtdLjqHkcJrkCX-iBueay4f',
    host = 'ruby.db.elephantsql.com',
    port = '5432'
)

cursor = connection.cursor()
school_question = 'school_question'

path = "questions/physics/7/1/{}.JPG"


qeury = "insert into school_question(question, variant_id) values({0}, 1)"


# DATABASES = {
#     'default': {
#         # 'ENGINE'    : 'django.db.backends.postgresql',
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'sfpxzsnw',
#         'USER': 'sfpxzsnw',
#         'PASSWORD': 'exdZ_p1Jqy8jDsfoHPyUDdA8_Hby5Xe8',
#         'HOST': 'ruby.db.elephantsql.com',
#         'PORT': '5432'
#     }
# }