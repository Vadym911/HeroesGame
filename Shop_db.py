import sqlite3

def create_tables_and_insert_values():
    db = sqlite3.connect("Db_shop.db")
    cursor = db.cursor()

# -------------- item types --------------
    cursor.execute('''CREATE TABLE IF NOT EXISTS item_types(
                    item_type_id  TEXT PRIMARY KEY,
                    item_type_name TEXT)
                    ''')
    cursor.execute("INSERT INTO item_types VALUES('it1', 'unit')")
    cursor.execute("INSERT INTO item_types VALUES('it2', 'armor')")
    cursor.execute("INSERT INTO item_types VALUES('it3', 'weapon')")
    cursor.execute("INSERT INTO item_types VALUES('it4', 'ability')")


# -------------- armor types --------------
    cursor.execute('''CREATE TABLE IF NOT EXISTS armor_types(
                    armor_type_id TEXT PRIMARY KEY,
                    armor_type_name TEXT)
                    ''')

    cursor.execute("INSERT INTO armor_types VALUES('at1', 'helmet')")
    cursor.execute("INSERT INTO armor_types VALUES('at2', 'bodyarmor')")
    cursor.execute("INSERT INTO armor_types VALUES('at3', 'boots')")
    cursor.execute("INSERT INTO armor_types VALUES('at4', 'shield')")


# -------------- weapon types --------------
    cursor.execute('''CREATE TABLE IF NOT EXISTS weapon_types(
                    weapon_type_id TEXT PRIMARY KEY,
                    weapon_type_name TEXT)
                    ''')

    cursor.execute("INSERT INTO weapon_types VALUES('wt1', 'hammers')")
    cursor.execute("INSERT INTO weapon_types VALUES('wt2', 'swords')")
    cursor.execute("INSERT INTO weapon_types VALUES('wt3', 'magic sticks')")
    cursor.execute("INSERT INTO weapon_types VALUES('wt4', 'knifes')")
    cursor.execute("INSERT INTO weapon_types VALUES('wt5', 'bows')")

# -------------- ability types --------------
    cursor.execute('''CREATE TABLE IF NOT EXISTS ability_types(
                    ability_type_id TEXT PRIMARY KEY, 
                    ability_type_name TEXT)
                    ''')

    cursor.execute("INSERT INTO ability_types VALUES('abt1', 'poison book')")
    cursor.execute("INSERT INTO ability_types VALUES('abt2', 'medic book')")
    cursor.execute("INSERT INTO ability_types VALUES('abt3', 'fitness training')")
    cursor.execute("INSERT INTO ability_types VALUES('abt4', 'karate training')")
    cursor.execute("INSERT INTO ability_types VALUES('abt5', 'bow dash')")

# -------------- units --------------
    cursor.execute('''CREATE TABLE IF NOT EXISTS units(
                    unit_id TEXT PRIMARY KEY,
                    item_type_id TEXT,
                    unit_name TEXT,
                    unit_price INTEGER)
                    ''')

    cursor.execute("INSERT INTO units VALUES('u1', 'it1', 'Archer', 200)")
    cursor.execute("INSERT INTO units VALUES('u2', 'it1', 'Barbarian', 200)")
    cursor.execute("INSERT INTO units VALUES('u3', 'it1', 'Healer', 200)")
    cursor.execute("INSERT INTO units VALUES('u4', 'it1', 'Knight', 200)")
    cursor.execute("INSERT INTO units VALUES('u5', 'it1', 'Witch', 200)")
    cursor.execute("INSERT INTO units VALUES('u6', 'it1', 'Wizard', 200)")

# -------------- armor --------------
    cursor.execute('''CREATE TABLE IF NOT EXISTS armor(
                    armor_id TEXT PRIMARY KEY,
                    item_type_id TEXT,
                    armor_type_id TEXT,
                    armor_name TEXT,
                    value INTEGER,
                    price INTEGER)
                    ''')

    cursor.execute("INSERT INTO armor VALUES('h1', 'it2', 'at1', 'wooden helmet', 200, 400)")
    cursor.execute("INSERT INTO armor VALUES('h2', 'it2', 'at1', 'iron helmet', 300, 600)")
    cursor.execute("INSERT INTO armor VALUES('h3', 'it2', 'at1', 'steel helmet', 400, 800)")

    cursor.execute("INSERT INTO armor VALUES('ba1', 'it2', 'at2', 'wooden bodyarmor', 200, 400)")
    cursor.execute("INSERT INTO armor VALUES('ba2', 'it2', 'at2', 'iron bodyarmor', 300, 600)")
    cursor.execute("INSERT INTO armor VALUES('ba3', 'it2', 'at2', 'steel bodyarmor', 400, 800)")

    cursor.execute("INSERT INTO armor VALUES('b1', 'it2', 'at3', 'wooden boots', 200, 400)")
    cursor.execute("INSERT INTO armor VALUES('b2', 'it2', 'at3', 'iron boots', 300, 600)")
    cursor.execute("INSERT INTO armor VALUES('b3', 'it2', 'at3', 'steel boots', 400, 800)")

    cursor.execute("INSERT INTO armor VALUES('s1', 'it2', 'at4', 'wooden shield', 200, 400)")
    cursor.execute("INSERT INTO armor VALUES('s2', 'it2', 'at4', 'iron shield', 300, 600)")
    cursor.execute("INSERT INTO armor VALUES('s3', 'it2', 'at4', 'steel shield', 400, 800)")


# -------------- weapons --------------
    cursor.execute('''CREATE TABLE IF NOT EXISTS weapons(
                    weapon_id TEXT PRIMARY KEY,
                    item_type_id TEXT,
                    weapon_type_id TEXT,
                    weapon_name TEXT,
                    usable_for_unit TEXT,
                    value INTEGER,
                    price INTEGER)
                    ''')

    cursor.execute("INSERT INTO weapons VALUES('hm1', 'it3', 'wt1', 'wooden hammer', 'u2', 400, 800)")
    cursor.execute("INSERT INTO weapons VALUES('hm2', 'it3', 'wt1', 'iron hammer', 'u2', 500, 1000)")
    cursor.execute("INSERT INTO weapons VALUES('hm3', 'it3', 'wt1', 'steel hammer', 'u2', 800, 1600)")

    cursor.execute("INSERT INTO weapons VALUES('sw1', 'it3', 'wt2', 'wooden sword', 'u4', 400, 800)")
    cursor.execute("INSERT INTO weapons VALUES('sw2', 'it3', 'wt2', 'iron sword', 'u4', 500, 1000)")
    cursor.execute("INSERT INTO weapons VALUES('sw3', 'it3', 'wt2', 'steel sword', 'u4', 800, 1600)")

    cursor.execute("INSERT INTO weapons VALUES('ms2', 'it3', 'wt3', 'magic stick 1 lvl', 'u6', 400, 800)")
    cursor.execute("INSERT INTO weapons VALUES('ms3', 'it3', 'wt3', 'magic stick 2 lvl', 'u6', 500, 1000)")
    cursor.execute("INSERT INTO weapons VALUES('ms1', 'it3', 'wt3', 'magic stick 3 lvl', 'u6', 800, 1600)")

    cursor.execute("INSERT INTO weapons VALUES('kn1', 'it3', 'wt4', 'knife 1 lvl', 'u3', 400, 800)")
    cursor.execute("INSERT INTO weapons VALUES('kn2', 'it3', 'wt4', 'knife 2 lvl', 'u3', 500, 1000)")
    cursor.execute("INSERT INTO weapons VALUES('kn3', 'it3', 'wt4', 'knife 3 lvl', 'u3', 800, 1600)")

    cursor.execute("INSERT INTO weapons VALUES('bw1', 'it3', 'wt5', 'bow 1 lvl', 'u1', 400, 800)")
    cursor.execute("INSERT INTO weapons VALUES('bw2', 'it3', 'wt5', 'bow 2 lvl', 'u1', 500, 1000)")
    cursor.execute("INSERT INTO weapons VALUES('bw3', 'it3', 'wt5', 'bow 3 lvl', 'u1', 800, 1600)")

    cursor.execute("INSERT INTO weapons VALUES('ws1', 'it3', 'wt6', 'witch stick 1 lvl', 'u5', 400, 800)")
    cursor.execute("INSERT INTO weapons VALUES('ws2', 'it3', 'wt6', 'witch stick 2 lvl', 'u5', 500, 1000)")
    cursor.execute("INSERT INTO weapons VALUES('ws3', 'it3', 'wt6', 'witch stick 3 lvl', 'u5', 800, 1600)")


# -------------- abilities --------------
    cursor.execute('''CREATE TABLE IF NOT EXISTS abilities(
                    ability_id TEXT PRIMARY KEY,
                    item_type_id TEXT,
                    ability_type_id TEXT,
                    ability_name TEXT,
                    usable_for_unit TEXT,
                    value INTEGER,
                    price INTEGER)
                    ''')

    cursor.execute("INSERT INTO abilities VALUES('pb1', 'it4', 'at1', 'poison book 1 lvl', 'u5', 0.2, 1000)")
    cursor.execute("INSERT INTO abilities VALUES('pb2', 'it4', 'at1', 'poison book 2 lvl', 'u5', 0.3, 2000)")
    cursor.execute("INSERT INTO abilities VALUES('pb3', 'it4', 'at1', 'poison book 3 lvl', 'u5', 0.4, 3000)")

    cursor.execute("INSERT INTO abilities VALUES('mb1', 'it4', 'at2', 'medic book 1 lvl', 'u3', 0.2, 1000)")
    cursor.execute("INSERT INTO abilities VALUES('mb2', 'it4', 'at2', 'medic book 2 lvl', 'u3', 0.4, 2000)")
    cursor.execute("INSERT INTO abilities VALUES('mb3', 'it4', 'at2', 'medic book 3 lvl', 'u3', 0.6, 3000)")

    cursor.execute("INSERT INTO abilities VALUES('ft1', 'it4', 'at3', 'fitness training 1 lvl', 'u2', 0.2, 1000)")
    cursor.execute("INSERT INTO abilities VALUES('ft2', 'it4', 'at3', 'fitness training 2 lvl', 'u2', 0.3, 2000)")
    cursor.execute("INSERT INTO abilities VALUES('ft3', 'it4', 'at3', 'fitness training 3 lvl', 'u2', 0.4, 3000)")

    cursor.execute("INSERT INTO abilities VALUES('kt1', 'it4', 'at4', 'karate training 1 lvl', 'u4', 2, 1000)")
    cursor.execute("INSERT INTO abilities VALUES('kt2', 'it4', 'at4', 'karate training 2 lvl', 'u4', 2, 2000)")
    cursor.execute("INSERT INTO abilities VALUES('kt3', 'it4', 'at4', 'karate training 3 lvl', 'u4', 3, 3000)")

    cursor.execute("INSERT INTO abilities VALUES('bd1', 'it4', 'at5', 'bow dash 1 lvl', 'u1', 0.4, 1000)")
    cursor.execute("INSERT INTO abilities VALUES('bd2', 'it4', 'at5', 'bow dash 2 lvl', 'u1', 0.6, 2000)")
    cursor.execute("INSERT INTO abilities VALUES('bd3', 'it4', 'at5', 'bow dash 3 lvl', 'u1', 0.8, 3000)")

    db.commit()
    db.close()

create_tables_and_insert_values()