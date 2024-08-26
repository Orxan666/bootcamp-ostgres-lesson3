# import psycopg2

# conn=psycopg2.connect('dbname=elmoviesad_db user=postgres port=5432 password=Orxan_666')
# cur=conn.cursor()

# primary key - unique ve not null -in birlesmesidir
# query='''
# CREATE TABLE movie(
# id SERIAL PRIMARY KEY,
# title  VARCHAR(40) NOT NULL,
# description TEXT,
# view_count INT DEFAULT 0,
# release DATE,
# has_fragman BOOLEAN
# );


# '''3
# cur.execute(query)
# conn.commit()
# =========================================================


# 1ci sual :)
# query=''' 
# CREATE TABLE product(




# id SERIAL PRIMARY KEY,
# productn VARCHAR(50) NOT NULL,
# product_count INT DEFAULT 0,
# new BOOLEAN NOT NULL,
# seller Identify Column ID SERIAL,
# release DATE,
# productcamein NOW(),
# lastime DATE NOW(),
# price FLOAT NOT NULL,
# sold INT DEFAULT 0,
# barcode UNIQUE NOT NULL,
# );
# '''
# import psycopg2

# conn=psycopg2.connect('dbname=store, user=postgres, port=5432, password=elsad123')
# cur=conn.cursor()
# query='''
# CREATE TABLE product(
# id PRIMARY KEY SERIAL,
# name VARCHAR(50) NOT NULL,
# product_count INT DEFAULT 0,
# new_product BOOLEAN,NOT  NULL,
# product_sell_count INT DEFAULT 0,
# release DATE,
# lasttime  TIME.NOW,
# product_code  UNIQUE,NOT NULL


# '''
# cur.execute(query)
# conn.commit()
#------------------------------------------------_-)))))))))))))))))))))))))))))))

#______________________________________---------------------------------------
# 3cu sual :)
# universit=psycopg2.connect('dbname=university user=postgres port=5432 password=9002Malim')
# cur=universit.cursor()
# query='''
# CREATE TABLE student(
# id SERIAL PRIMARY KEY,
# name VARCHAR(50) NOY NULL,
# surname VARCHAR(50) NOT NULL,
# email VARCHAR(50) UNIQUE NOT ULL,
# phone_number VARCHAR(20) UNIQUE NOT NULL,
# profession VARCHAR(100) NOT NULL,
# job VARCHAR(100) NOT NULL,
# admision DATE,
# gpa FLOAT DEFUALT 0,
# )
# '''
# =================================

# Tələbələri saxlamaq üçün university adlı bir verilənlər bazası və həmin bazada student adlı bir cədvəl yaradın. Cədvəl aşağıdakı kimi olacaq:
# tələbə id - məcburi, öz-özünə artan, bənzərsiz
# tələbənin adı - maksimum 50 hərf, məcburi
# tələbənin soyadı - maksimum 50 hərf, məcburi
# tələbənin emaili - bənzərsiz və məcburi olmalıdır
# tələbənin telefon nömrəsi - bənzərsiz və məcburi olmalıdır
# tələbənin fakültəsi - maksimum 100 hərf, məcburi
# tələbənin ixtisası - maksimum 100 hərf, məcburi
# tələbənin qeydiyyat tarixi
# tələbənin GPA (Orta balı) - default

import psycopg2

con=psycopg2.connect('dbname=elsadholding_db user=postgres port=5432 password=Orxan_666')
cur=con.cursor()

def show(cursor):
    # cur.execute(query)
    length = 20
    print(*[desc[0].ljust(20) for desc in cursor.description], sep='')
    print('-'*140)
    result = cur.fetchall()
    for row in result:
        for col in row:
            print(str(col).ljust(length)[:17], end='')
        print()
# title, company, salary, expiration_date, lang
# query="""
# CREATE TABLE jobs2(
# id SERIAL PRIMARY KEY,
# title VARCHAR(100),
# company VARCHAR(100),
# salary INT,
# expiration_date DATE,
# lang BOOLEAN

# )   
# """

# cur.execute(query);
# con.commit()




info_list = [
    # title, company, salary, expiration date, foreign language requirement
    ('iOS developer', 'A2Z Technologies', 3500, '2022-07-18', True),
    ('Tender Specialist', 'A2Z Technologies', 1500, '2022-06-11', False),
    ('Database Administrator', 'ABB ASC', 1500, '2022-07-12', True),
    ('Database Administrator', 'A2Z Technologies', 2500, '2022-07-14', True),
    ('Front-End Developer', 'AzeriMed QSC', 1500, '2022-07-23', False),
    ('Software Testing Engineer', 'ABB ASC', 1500, '2022-08-10', False),
    ('Back-end Developer', 'ABB ASC', 4100, '2022-07-11', True),
    ('Chief Business Analyst', 'ABB ASC', 2200, '2022-07-03', True),
    ('Android Developer', 'ABB ASC', 1300, '2022-07-22', True),
    ('Front-end Developer', 'ABB ASC', 3200, '2022-07-06', True),
    ('Full stack PHP Developer', 'AzeriMed QSC', 2400, '2022-07-17', False),
    ('Automated Operations System Programmer', 'ABB ASC', 2700, '2022-07-15', True),
    ('Software Engineer', 'Kontakt Home', 2700, '2022-07-13', False),
    ('Legal Specialist', 'Kontakt Home', 1500, '2022-07-03', False),
    ('Delivery Services Specialist', 'Kontakt Home', 500, '2022-07-15', True),
    ('PHP Developer', 'ARIS', 1500, '2022-07-11', True),
    ('Product Manager', 'Kontakt Home', 2800, '2022-07-05', True),
    ('Lead Software Engineer', 'Kontakt Home', 2500, '2022-07-02', False),
    ('IT Documentation Specialist', 'Azericard', 1500, '2022-07-25', True),
    ('Information Security Specialist', 'DEFSCOPE LLC', 2500, '2022-07-03', False),
    ('IT Helpdesk', 'Azericard', 1500, '2022-07-30', True),
    ('Cybersecurity Business Development Internship', 'DEFSCOPE LLC', 2900, '2022-07-19', False),
    ('Vue.js Developer', 'ARIS', 1500, '2022-07-29', True),
]
query="""

INSERT INTO jobs2(title, company, salary, expiration_date, lang) VALUES (%s,%s,%s,%s,%s)

"""

for item in info_list:
    cur.execute(query,item)
con.commit()


