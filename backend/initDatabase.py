import sqlite3

con = sqlite3.connect('divebase.db')
cur = con.cursor()

cur.execute("""
            CREATE TABLE IF NOT EXISTS divesites (
                id              integer     primary key,
                name            text        unique not null,
                type            text        ,
                latitude        text        not null,
                longitude       text        not null
            );
    """)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES ('Bashful Bommie', 'Reef', '-16.24133', '145.86398');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('The Wedge', 'Drift', '-16.24197', '145.86628');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Wild West', 'Reef', '-16.24591', '145.86179');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('SNO', 'Drift', '-16.19308', '145.89363');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('North SNO', 'Drift', '-16.19127', '145.89784');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Acropolis', 'Reef', '-16.24424', '145.87125');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('North Bay', 'Drift', '-15.97461', '145.82866');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Stonehenge', 'Reef', '-16.00276', '145.83032');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('The Rocks', 'Reef', '-15.99797', '145.83007');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Blue Buoy', 'Reef', '-16.2423', '145.86221');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Totem', 'Drift', '-16.01753', '145.80939');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Phils', 'Drift', '-16.02048', '145.80957');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Nobodys', 'Reef', '-16.01691', '145.79153');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Anybodys', 'Reef', '-16.01637', '145.79448');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Lobos rock', 'Reef', '-35.0263573165302', '117.884378319375');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Swanne Rock', 'Reef', '-35.0263573165302', '117.884378319375');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Salvatierra Wreck', 'Wreck', '-35.0263573165302', '117.884378319375');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Chinese Wreck', 'Wreck', '-35.0263573165302', '117.884378319375');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Los Islotes', 'Reef', '-35.0263573165302', '117.884378319375');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('La Reina', 'Reef', '-35.0263573165302', '117.884378319375');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('La Reinita', 'Reef', '-35.0263573165302', '117.884378319375');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Old Sea Lions', 'Reef', '-35.0263573165302', '117.884378319375');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('La Punta Norte', 'Reef', '-35.0263573165302', '117.884378319375');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('USCGC Bibb', 'Wreck', '-35.0263573165302', '117.884378319375');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Conch Wall', 'Wall', '-35.0263573165302', '117.884378319375');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Crocker Reef', 'Reef', '-42.8832832492579', '147.334564467925');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Davis Reef', 'Reef', '-35.0263573165302', '117.884378319375');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Lodestone Reef', 'Reef', '-18.69487', '147.0929');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Museum of Underwater Art (MOUA) at John Brewer Reef', 'Reef', '-18.62445', '147.05544');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Yongala Wreck', 'Wreck', '-19.37917', '147.67548');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Big Broadhurst Reef', 'Reef', '-18.92967', '147.71873');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Julian Rocks', 'Drift', '-28.61093', '153.62956');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Flat Rock', 'Reef', '-27.39067', '153.55183');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Shag Rock', 'Reef', '-27.41378', '153.52615');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Manta Ray Bommie', 'Reef', '-27.42364', '153.54813');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Flinders Reef', 'Reef', '-26.97865', '153.48531');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Kevins Reef', 'Reef', '-28.77232', '114.58551');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Supermarket', 'Cave', '-28.77827', '114.57402');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Explosives', 'Cave', '-28.77746', '114.57527');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Aquarium Reef 1', 'Cave', '-28.78394', '114.57454');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Aquarium Reef 2', 'Cave', '-28.78528', '114.5741');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Wolf Rock', 'Reef', '-25.91677', '153.20005');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Holts Rock', 'Drift', '-20.2490076635304', '148.94743951256');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Blizzard Ridge Lighthouse Bay Ningaloo Reef', 'Reef', '-21.80079', '114.12374');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Stanley Reef', 'Reef', '-19.23855', '148.09021');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Neptune Islands', 'Channel', '-35.33053', '136.11494');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Clifton Gardens', 'Beach', '-33.8399', '151.25328');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Shelly Beach', 'Beach', '-33.8005', '151.29762');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Blue Fish Point', 'Reef', '-33.80672', '151.30631');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Old Mans Hat', 'Reef', '-33.82161', '151.29379');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Popes Eye Marine National Park', 'Drift', '-38.27634', '144.69859');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Bare Island', 'Ocean', '-33.99195', '151.23126');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Hastings Reef', 'Reef', '-16.51', '146.00781');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Rapid Bay Jetty', 'Reef', '-35.52337', '138.1853');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Rottnest Island', 'Ocean', '-32.00173', '115.5349');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Oak Park', 'Reef', '-34.07', '151.1');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Gold Coast Seaway', 'Drift', '-27.93391', '153.43124');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Wave Break Island', 'Wall', '-27.93262', '153.41871');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Palm Beach Reef', 'Reef', '-28.09546', '153.4839');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('The Scottish Prince Shipwreck', 'Wreck', '-27.96082', '153.43463');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Cook Island', 'Reef', '-28.1943', '153.57634');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Portsea Pier', 'Beach', '-38.31839', '144.71335');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Flinders Pier', 'Wreck', '-38.4757', '145.02642');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Chimanans Hat', 'Channel', '-38.28757', '144.72692');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Blairgowrie Pier', 'Beach', '-38.35699', '144.77363');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Rye Pier', 'Wreck', '-38.36713', '144.82287');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Stingray Bay', 'Reef', '-38.40319', '142.47341');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Warrnambool Breakwater, inside', 'Muck', '-38.40167', '142.47863');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Port Campbell Bay Reef', 'Reef', '-38.62059', '142.98946');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Fly Point', 'Beach', '-32.7144', '152.15188');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Moore Reef', 'Drift', '-16.84578', '146.22734');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Old Aquarium', 'Reef', '-38.40403', '142.47592');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Port Campbell Jetty', 'Beach', '-38.62099', '142.99156');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Lee Breakwater, Portland, Victoria, Australia', 'Beach', '-38.34334', '141.60991');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Lake Purrumbete, Camperdown, Victoria, Australia', 'Lake', '-38.28522', '143.22001');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Lake Bullen Merri, Camperdown', 'Lake', '-38.23805', '143.10521');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Pickering Point', 'Reef', '-38.40083', '142.46753');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Middle Island', 'Ocean', '-38.40307', '142.47041');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Nunns Beach, Portland, Victoria, Australia', 'Beach', '-38.34209', '141.61055');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Peasoup, Port Fairy, Victoria, Australia', 'Beach', '-38.39285', '142.22707');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('HMAS Brisbane', 'Wreck', '-26.62598', '153.14941');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('The Pipeline', 'Muck', '-32.71799', '152.1414');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('North Rock Shark Gutters', 'Ocean', '-32.59982', '152.32326');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Bawley Point 1', 'Ocean', '-35.50477', '150.39545');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Bawley Point 2', 'Sandy bottom', '-35.55754', '150.38423');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Aldens Cave - Flinders Reef', 'Cave', '-26.97898', '153.48702');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Turtle Cleaning Station - Flinders Reef', 'Reef', '-26.97785', '153.48495');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Curtin Artificial Reef - Moreton Bay', 'Wreck', '-27.11029', '153.36485');
        """
cur.execute(query)

query = """
            INSERT INTO divesites(name, type, latitude, longitude)
            VALUES('Eastern Reach - Manta Bommie', 'Reef', '-27.42404', '153.54848');
        """
cur.execute(query)

con.commit()
cur.close()
con.close()
