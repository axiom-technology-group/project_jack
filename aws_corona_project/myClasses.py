import datetime
from enum import Enum

class MyLogging:
    
    def __init__(self):
        self._filename = str()
        self._filemode = str()
        self._name = str()
        self._loglevel = 0
        self._levels = {'critical':50, 'error':40, 'warning':30,
               'info':20, 'debug':10, 'notset':0}

    def basicConfig(self, filename, filemode, level=30, name='root'):
        self._filename = filename
        self._filemode = filemode
        self._name = name
        self._loglevel = level

    def log(self, level, script):
        if level not in self._levels:
            raise TypeError('Invalid level')
        try:
            f = open(self._filename, self._filemode)
        except:
            raise IOError('Fails to read the file.')
        
        if self._levels.get(level) >= self._loglevel:
            text_in = str(
                datetime.datetime.now()) + ' - ' + self._name + ' - ' + level.upper() + ' - ' + script
            f.write(text_in + '\n')
            f.close()


class Country(Enum):
    AFGHANISTAN = {'Name': 'Afghanistan', 'Code': 'AFG', 'Flag': 'af.png'}
    ALBANIA = {'Name': 'Albania', 'Code': 'ALB', 'Flag': 'al.png'}
    ALGERIA = {'Name': 'Algeria', 'Code': 'DZA', 'Flag': 'dz.png'}
    AMERICAN_SAMOA = {'Name': 'American Samoa',
                      'Code': 'ASM', 'Flag': 'as.png'}
    ANDORRA = {'Name': 'Andorra', 'Code': 'AND', 'Flag': 'ad.png'}
    ANGOLA = {'Name': 'Angola', 'Code': 'AGO', 'Flag': 'ao.png'}
    ANGUILLA = {'Name': 'Anguilla', 'Code': 'AIA', 'Flag': 'ai.png'}
    ANTARCTICA = {'Name': 'Antarctica', 'Code': 'ATA', 'Flag': 'aq.png'}
    ANTIGUA_AND_BARBUDA = {'Name': 'Antigua and Barbuda',
                           'Code': 'ATG', 'Flag': 'ag.png'}
    ARGENTINA = {'Name': 'Argentina', 'Code': 'ARG', 'Flag': 'ar.png'}
    ARMENIA = {'Name': 'Armenia', 'Code': 'ARM', 'Flag': 'am.png'}
    ARUBA = {'Name': 'Aruba', 'Code': 'ABW', 'Flag': 'aw.png'}
    AUSTRALIA = {'Name': 'Australia', 'Code': 'AUS', 'Flag': 'au.png'}
    AUSTRIA = {'Name': 'Austria', 'Code': 'AUT', 'Flag': 'at.png'}
    AZERBAIJAN = {'Name': 'Azerbaijan', 'Code': 'AZE', 'Flag': 'az.png'}
    BAHAMAS = {'Name': 'Bahamas', 'Code': 'BHS', 'Flag': 'bs.png'}
    BAHRAIN = {'Name': 'Bahrain', 'Code': 'BHR', 'Flag': 'bh.png'}
    BANGLADESH = {'Name': 'Bangladesh', 'Code': 'BGD', 'Flag': 'bd.png'}
    BARBADOS = {'Name': 'Barbados', 'Code': 'BRB', 'Flag': 'bb.png'}
    BELARUS = {'Name': 'Belarus', 'Code': 'BLR', 'Flag': 'by.png'}
    BELGIUM = {'Name': 'Belgium', 'Code': 'BEL', 'Flag': 'be.png'}
    BELIZE = {'Name': 'Belize', 'Code': 'BLZ', 'Flag': 'bz.png'}
    BENIN = {'Name': 'Benin', 'Code': 'BEN', 'Flag': 'bj.png'}
    BERMUDA = {'Name': 'Bermuda', 'Code': 'BMU', 'Flag': 'bm.png'}
    BHUTAN = {'Name': 'Bhutan', 'Code': 'BTN', 'Flag': 'bt.png'}
    BOLIVIA = {'Name': 'Bolivia', 'Code': 'BOL', 'Flag': 'bo.png'}
    BOSNIA_AND_HERZEGOVINA = {
        'Name': 'Bosnia and Herzegovina', 'Code': 'BIH', 'Flag': 'ba.png'}
    BOTSWANA = {'Name': 'Botswana', 'Code': 'BWA', 'Flag': 'bw.png'}
    BRAZIL = {'Name': 'Brazil', 'Code': 'BRA', 'Flag': 'br.png'}
    BRITISH_INDIAN_OCEAN_TERRITORY = {
        'Name': 'British Indian Ocean Territory', 'Code': 'IOT', 'Flag': 'io.png'}
    BRITISH_VIRGIN_ISLANDS = {
        'Name': 'British Virgin Islands', 'Code': 'VGB', 'Flag': 'vg.png'}
    BRUNEI = {'Name': 'Brunei', 'Code': 'BRN', 'Flag': 'bn.png'}
    BULGARIA = {'Name': 'Bulgaria', 'Code': 'BGR', 'Flag': 'bg.png'}
    BURKINA_FASO = {'Name': 'Burkina Faso', 'Code': 'BFA', 'Flag': 'bf.png'}
    BURUNDI = {'Name': 'Burundi', 'Code': 'BDI', 'Flag': 'bi.png'}
    CAMBODIA = {'Name': 'Cambodia', 'Code': 'KHM', 'Flag': 'kh.png'}
    CAMEROON = {'Name': 'Cameroon', 'Code': 'CMR', 'Flag': 'cm.png'}
    CANADA = {'Name': 'Canada', 'Code': 'CAN', 'Flag': 'ca.png'}
    CAPE_VERDE = {'Name': 'Cape Verde', 'Code': 'CPV', 'Flag': 'cv.png', 'special':'Cabo Verde'}
    CAYMAN_ISLANDS = {'Name': 'Cayman Islands',
                      'Code': 'CYM', 'Flag': 'ky.png'}
    CENTRAL_AFRICAN_REPUBLIC = {
        'Name': 'Central African Republic', 'Code': 'CAF', 'Flag': 'cf.png', 'special':'CAR'}
    CHAD = {'Name': 'Chad', 'Code': 'TCD', 'Flag': 'td.png'}
    CHILE = {'Name': 'Chile', 'Code': 'CHL', 'Flag': 'cl.png'}
    CHINA = {'Name': 'China', 'Code': 'CHN', 'Flag': 'cn.png'}
    CHRISTMAS_ISLAND = {'Name': 'Christmas Island',
                        'Code': 'CXR', 'Flag': 'cx.png'}
    COCOS_ISLANDS = {'Name': 'Cocos Islands', 'Code': 'CCK', 'Flag': 'cc.png'}
    COLOMBIA = {'Name': 'Colombia', 'Code': 'COL', 'Flag': 'co.png'}
    COMOROS = {'Name': 'Comoros', 'Code': 'COM', 'Flag': 'km.png'}
    COOK_ISLANDS = {'Name': 'Cook Islands', 'Code': 'COK', 'Flag': 'ck.png'}
    COSTA_RICA = {'Name': 'Costa Rica', 'Code': 'CRI', 'Flag': 'cr.png'}
    CROATIA = {'Name': 'Croatia', 'Code': 'HRV', 'Flag': 'hr.png'}
    CUBA = {'Name': 'Cuba', 'Code': 'CUB', 'Flag': 'cu.png'}
    CURACAO = {'Name': 'Curacao', 'Code': 'CUW',
               'Flag': 'cw.png', 'special': 'Curaçao'}
    CYPRUS = {'Name': 'Cyprus', 'Code': 'CYP', 'Flag': 'cy.png'}
    CZECH_REPUBLIC = {'Name': 'Czech Republic',
                      'Code': 'CZE', 'Flag': 'cz.png', 'special':'Czechia'}
    DEMOCRATIC_REPUBLIC_OF_THE_CONGO = {
        'Name': 'Democratic Republic of the Congo', 'Code': 'COD', 'Flag': 'cd.png', 'special':'DRC'}
    DENMARK = {'Name': 'Denmark', 'Code': 'DNK', 'Flag': 'dk.png'}
    DJIBOUTI = {'Name': 'Djibouti', 'Code': 'DJI', 'Flag': 'dj.png'}
    DOMINICA = {'Name': 'Dominica', 'Code': 'DMA', 'Flag': 'dm.png'}
    DOMINICAN_REPUBLIC = {'Name': 'Dominican Republic',
                          'Code': 'DOM', 'Flag': 'do.png'}
    EAST_TIMOR = {'Name': 'East Timor', 'Code': 'TLS', 'Flag': 'tl.png', 'special':'Timor-Leste'}
    ECUADOR = {'Name': 'Ecuador', 'Code': 'ECU', 'Flag': 'ec.png'}
    EGYPT = {'Name': 'Egypt', 'Code': 'EGY', 'Flag': 'eg.png'}
    EL_SALVADOR = {'Name': 'El Salvador', 'Code': 'SLV', 'Flag': 'sv.png'}
    EQUATORIAL_GUINEA = {'Name': 'Equatorial Guinea',
                         'Code': 'GNQ', 'Flag': 'gq.png'}
    ERITREA = {'Name': 'Eritrea', 'Code': 'ERI', 'Flag': 'er.png'}
    ESTONIA = {'Name': 'Estonia', 'Code': 'EST', 'Flag': 'ee.png'}
    ETHIOPIA = {'Name': 'Ethiopia', 'Code': 'ETH', 'Flag': 'et.png'}
    FALKLAND_ISLANDS = {'Name': 'Falkland Islands',
                        'Code': 'FLK', 'Flag': 'fk.png'}
    FAROE_ISLANDS = {'Name': 'Faroe Islands', 'Code': 'FRO', 'Flag': 'fo.png'}
    FIJI = {'Name': 'Fiji', 'Code': 'FJI', 'Flag': 'fj.png'}
    FINLAND = {'Name': 'Finland', 'Code': 'FIN', 'Flag': 'fi.png'}
    FRANCE = {'Name': 'France', 'Code': 'FRA', 'Flag': 'fr.png'}
    FRENCH_POLYNESIA = {'Name': 'French Polynesia',
                        'Code': 'PYF', 'Flag': 'pf.png'}
    GABON = {'Name': 'Gabon', 'Code': 'GAB', 'Flag': 'ga.png'}
    GAMBIA = {'Name': 'Gambia', 'Code': 'GMB', 'Flag': 'gm.png'}
    GEORGIA = {'Name': 'Georgia', 'Code': 'GEO', 'Flag': 'ge.png'}
    GERMANY = {'Name': 'Germany', 'Code': 'DEU', 'Flag': 'de.png'}
    GHANA = {'Name': 'Ghana', 'Code': 'GHA', 'Flag': 'gh.png'}
    GIBRALTAR = {'Name': 'Gibraltar', 'Code': 'GIB', 'Flag': 'gi.png'}
    GREECE = {'Name': 'Greece', 'Code': 'GRC', 'Flag': 'gr.png'}
    GREENLAND = {'Name': 'Greenland', 'Code': 'GRL', 'Flag': 'gl.png'}
    GRENADA = {'Name': 'Grenada', 'Code': 'GRD', 'Flag': 'gd.png'}
    GUAM = {'Name': 'Guam', 'Code': 'GUM', 'Flag': 'gu.png'}
    GUATEMALA = {'Name': 'Guatemala', 'Code': 'GTM', 'Flag': 'gt.png'}
    GUERNSEY = {'Name': 'Guernsey', 'Code': 'GGY', 'Flag': 'gg.png'}
    GUINEA = {'Name': 'Guinea', 'Code': 'GIN', 'Flag': 'gn.png'}
    GUINEA_BISSAU = {'Name': 'Guinea-Bissau', 'Code': 'GNB', 'Flag': 'gw.png'}
    GUYANA = {'Name': 'Guyana', 'Code': 'GUY', 'Flag': 'gy.png'}
    HAITI = {'Name': 'Haiti', 'Code': 'HTI', 'Flag': 'ht.png'}
    HONDURAS = {'Name': 'Honduras', 'Code': 'HND', 'Flag': 'hn.png'}
    HONG_KONG = {'Name': 'Hong Kong', 'Code': 'HKG', 'Flag': 'hk.png'}
    HUNGARY = {'Name': 'Hungary', 'Code': 'HUN', 'Flag': 'hu.png'}
    ICELAND = {'Name': 'Iceland', 'Code': 'ISL', 'Flag': 'is.png'}
    INDIA = {'Name': 'India', 'Code': 'IND', 'Flag': 'in.png'}
    INDONESIA = {'Name': 'Indonesia', 'Code': 'IDN', 'Flag': 'id.png'}
    IRAN = {'Name': 'Iran', 'Code': 'IRN', 'Flag': 'ir.png'}
    IRAQ = {'Name': 'Iraq', 'Code': 'IRQ', 'Flag': 'iq.png'}
    IRELAND = {'Name': 'Ireland', 'Code': 'IRL', 'Flag': 'ie.png'}
    ISLE_OF_MAN = {'Name': 'Isle of Man', 'Code': 'IMN', 'Flag': 'im.png'}
    ISRAEL = {'Name': 'Israel', 'Code': 'ISR', 'Flag': 'il.png'}
    ITALY = {'Name': 'Italy', 'Code': 'ITA', 'Flag': 'it.png'}
    IVORY_COAST = {'Name': 'Ivory Coast', 'Code': 'CIV', 'Flag': 'ci.png'}
    JAMAICA = {'Name': 'Jamaica', 'Code': 'JAM', 'Flag': 'jm.png'}
    JAPAN = {'Name': 'Japan', 'Code': 'JPN', 'Flag': 'jp.png'}
    JERSEY = {'Name': 'Jersey', 'Code': 'JEY', 'Flag': 'je.png'}
    JORDAN = {'Name': 'Jordan', 'Code': 'JOR', 'Flag': 'jo.png'}
    KAZAKHSTAN = {'Name': 'Kazakhstan', 'Code': 'KAZ', 'Flag': 'kz.png'}
    KENYA = {'Name': 'Kenya', 'Code': 'KEN', 'Flag': 'ke.png'}
    KIRIBATI = {'Name': 'Kiribati', 'Code': 'KIR', 'Flag': 'ki.png'}
    KOSOVO = {'Name': 'Kosovo', 'Code': 'XKX', 'Flag': 'xk.png'}
    KUWAIT = {'Name': 'Kuwait', 'Code': 'KWT', 'Flag': 'kw.png'}
    KYRGYZSTAN = {'Name': 'Kyrgyzstan', 'Code': 'KGZ', 'Flag': 'kg.png'}
    LAOS = {'Name': 'Laos', 'Code': 'LAO', 'Flag': 'la.png'}
    LATVIA = {'Name': 'Latvia', 'Code': 'LVA', 'Flag': 'lv.png'}
    LEBANON = {'Name': 'Lebanon', 'Code': 'LBN', 'Flag': 'lb.png'}
    LESOTHO = {'Name': 'Lesotho', 'Code': 'LSO', 'Flag': 'ls.png'}
    LIBERIA = {'Name': 'Liberia', 'Code': 'LBR', 'Flag': 'lr.png'}
    LIBYA = {'Name': 'Libya', 'Code': 'LBY', 'Flag': 'ly.png'}
    LIECHTENSTEIN = {'Name': 'Liechtenstein', 'Code': 'LIE', 'Flag': 'li.png'}
    LITHUANIA = {'Name': 'Lithuania', 'Code': 'LTU', 'Flag': 'lt.png'}
    LUXEMBOURG = {'Name': 'Luxembourg', 'Code': 'LUX', 'Flag': 'lu.png'}
    MACAU = {'Name': 'Macau', 'Code': 'MAC', 'Flag': 'mo.png', 'special':'Macao'}
    MACEDONIA = {'Name': 'Macedonia', 'Code': 'MKD', 'Flag': 'mk.png', 'special':'North Macedonia'}
    MADAGASCAR = {'Name': 'Madagascar', 'Code': 'MDG', 'Flag': 'mg.png'}
    MALAWI = {'Name': 'Malawi', 'Code': 'MWI', 'Flag': 'mw.png'}
    MALAYSIA = {'Name': 'Malaysia', 'Code': 'MYS', 'Flag': 'my.png'}
    MALDIVES = {'Name': 'Maldives', 'Code': 'MDV', 'Flag': 'mv.png'}
    MALI = {'Name': 'Mali', 'Code': 'MLI', 'Flag': 'ml.png'}
    MALTA = {'Name': 'Malta', 'Code': 'MLT', 'Flag': 'mt.png'}
    MARSHALL_ISLANDS = {'Name': 'Marshall Islands',
                        'Code': 'MHL', 'Flag': 'mh.png'}
    MAURITANIA = {'Name': 'Mauritania', 'Code': 'MRT', 'Flag': 'mr.png'}
    MAURITIUS = {'Name': 'Mauritius', 'Code': 'MUS', 'Flag': 'mu.png'}
    MAYOTTE = {'Name': 'Mayotte', 'Code': 'MYT', 'Flag': 'yt.png'}
    MEXICO = {'Name': 'Mexico', 'Code': 'MEX', 'Flag': 'mx.png'}
    MICRONESIA = {'Name': 'Micronesia', 'Code': 'FSM', 'Flag': 'fm.png'}
    MOLDOVA = {'Name': 'Moldova', 'Code': 'MDA', 'Flag': 'md.png'}
    MONACO = {'Name': 'Monaco', 'Code': 'MCO', 'Flag': 'mc.png'}
    MONGOLIA = {'Name': 'Mongolia', 'Code': 'MNG', 'Flag': 'mn.png'}
    MONTENEGRO = {'Name': 'Montenegro', 'Code': 'MNE', 'Flag': 'me.png'}
    MONTSERRAT = {'Name': 'Montserrat', 'Code': 'MSR', 'Flag': 'ms.png'}
    MOROCCO = {'Name': 'Morocco', 'Code': 'MAR', 'Flag': 'ma.png'}
    MOZAMBIQUE = {'Name': 'Mozambique', 'Code': 'MOZ', 'Flag': 'mz.png'}
    MYANMAR = {'Name': 'Myanmar', 'Code': 'MMR', 'Flag': 'mm.png'}
    NAMIBIA = {'Name': 'Namibia', 'Code': 'NAM', 'Flag': 'na.png'}
    NAURU = {'Name': 'Nauru', 'Code': 'NRU', 'Flag': 'nr.png'}
    NEPAL = {'Name': 'Nepal', 'Code': 'NPL', 'Flag': 'np.png'}
    NETHERLANDS = {'Name': 'Netherlands', 'Code': 'NLD', 'Flag': 'nl.png', 'special':'Caribbean Netherlands'}
    NETHERLANDS_ANTILLES = {
        'Name': 'Netherlands Antilles', 'Code': 'ANT', 'Flag': 'an.png'}
    NEW_CALEDONIA = {'Name': 'New Caledonia', 'Code': 'NCL', 'Flag': 'nc.png'}
    NEW_ZEALAND = {'Name': 'New Zealand', 'Code': 'NZL', 'Flag': 'nz.png'}
    NICARAGUA = {'Name': 'Nicaragua', 'Code': 'NIC', 'Flag': 'ni.png'}
    NIGER = {'Name': 'Niger', 'Code': 'NER', 'Flag': 'ne.png'}
    NIGERIA = {'Name': 'Nigeria', 'Code': 'NGA', 'Flag': 'ng.png'}
    NIUE = {'Name': 'Niue', 'Code': 'NIU', 'Flag': 'nu.png'}
    NORTH_KOREA = {'Name': 'North Korea', 'Code': 'PRK', 'Flag': 'kp.png'}
    NORTHERN_MARIANA_ISLANDS = {
        'Name': 'Northern Mariana Islands', 'Code': 'MNP', 'Flag': 'mp.png'}
    NORWAY = {'Name': 'Norway', 'Code': 'NOR', 'Flag': 'no.png'}
    OMAN = {'Name': 'Oman', 'Code': 'OMN', 'Flag': 'om.png'}
    PAKISTAN = {'Name': 'Pakistan', 'Code': 'PAK', 'Flag': 'pk.png'}
    PALAU = {'Name': 'Palau', 'Code': 'PLW', 'Flag': 'pw.png'}
    PALESTINE = {'Name': 'Palestine', 'Code': 'PSE', 'Flag': 'ps.png'}
    PANAMA = {'Name': 'Panama', 'Code': 'PAN', 'Flag': 'pa.png'}
    PAPUA_NEW_GUINEA = {'Name': 'Papua New Guinea',
                        'Code': 'PNG', 'Flag': 'pg.png'}
    PARAGUAY = {'Name': 'Paraguay', 'Code': 'PRY', 'Flag': 'py.png'}
    PERU = {'Name': 'Peru', 'Code': 'PER', 'Flag': 'pe.png'}
    PHILIPPINES = {'Name': 'Philippines', 'Code': 'PHL', 'Flag': 'ph.png'}
    PITCAIRN = {'Name': 'Pitcairn', 'Code': 'PCN', 'Flag': 'pn.png'}
    POLAND = {'Name': 'Poland', 'Code': 'POL', 'Flag': 'pl.png'}
    PORTUGAL = {'Name': 'Portugal', 'Code': 'PRT', 'Flag': 'pt.png'}
    PUERTO_RICO = {'Name': 'Puerto Rico', 'Code': 'PRI', 'Flag': 'pr.png'}
    QATAR = {'Name': 'Qatar', 'Code': 'QAT', 'Flag': 'qa.png'}
    REPUBLIC_OF_THE_CONGO = {
        'Name': 'Republic of the Congo', 'Code': 'COG', 'Flag': 'cg.png'}
    REUNION = {'Name': 'Reunion', 'Code': 'REU',
               'Flag': 're.png', 'special': 'Réunion'}
    ROMANIA = {'Name': 'Romania', 'Code': 'ROU', 'Flag': 'ro.png'}
    RUSSIA = {'Name': 'Russia', 'Code': 'RUS', 'Flag': 'ru.png'}
    RWANDA = {'Name': 'Rwanda', 'Code': 'RWA', 'Flag': 'rw.png'}
    SAINT_BARTHELEMY = {'Name': 'Saint Barthelemy',
                        'Code': 'BLM', 'Flag': 'bl.png', 'special':'St. Barth'}
    SAINT_HELENA = {'Name': 'Saint Helena', 'Code': 'SHN', 'Flag': 'sh.png'}
    SAINT_KITTS_AND_NEVIS = {
        'Name': 'Saint Kitts and Nevis', 'Code': 'KNA', 'Flag': 'kn.png'}
    SAINT_LUCIA = {'Name': 'Saint Lucia', 'Code': 'LCA', 'Flag': 'lc.png'}
    SAINT_MARTIN = {'Name': 'Saint Martin', 'Code': 'MAF', 'Flag': 'mf.png'}
    SAINT_PIERRE_AND_MIQUELON = {
        'Name': 'Saint Pierre and Miquelon', 'Code': 'SPM', 'Flag': 'pm.png', 'special':'Saint Pierre Miquelon'}
    SAINT_VINCENT_AND_THE_GRENADINES = {
        'Name': 'Saint Vincent and the Grenadines', 'Code': 'VCT', 'Flag': 'vc.png', 'special': 'St. Vincent Grenadines'}
    SAMOA = {'Name': 'Samoa', 'Code': 'WSM', 'Flag': 'ws.png'}
    SAN_MARINO = {'Name': 'San Marino', 'Code': 'SMR', 'Flag': 'sm.png'}
    SAO_TOME_AND_PRINCIPE = {
        'Name': 'Sao Tome and Principe', 'Code': 'STP', 'Flag': 'st.png'}
    SAUDI_ARABIA = {'Name': 'Saudi Arabia', 'Code': 'SAU', 'Flag': 'sa.png'}
    SENEGAL = {'Name': 'Senegal', 'Code': 'SEN', 'Flag': 'sn.png'}
    SERBIA = {'Name': 'Serbia', 'Code': 'SRB', 'Flag': 'rs.png'}
    SEYCHELLES = {'Name': 'Seychelles', 'Code': 'SYC', 'Flag': 'sc.png'}
    SIERRA_LEONE = {'Name': 'Sierra Leone', 'Code': 'SLE', 'Flag': 'sl.png'}
    SINGAPORE = {'Name': 'Singapore', 'Code': 'SGP', 'Flag': 'sg.png'}
    SINT_MAARTEN = {'Name': 'Sint Maarten', 'Code': 'SXM', 'Flag': 'sx.png'}
    SLOVAKIA = {'Name': 'Slovakia', 'Code': 'SVK', 'Flag': 'sk.png'}
    SLOVENIA = {'Name': 'Slovenia', 'Code': 'SVN', 'Flag': 'si.png'}
    SOLOMON_ISLANDS = {'Name': 'Solomon Islands',
                       'Code': 'SLB', 'Flag': 'sb.png'}
    SOMALIA = {'Name': 'Somalia', 'Code': 'SOM', 'Flag': 'so.png'}
    SOUTH_AFRICA = {'Name': 'South Africa', 'Code': 'ZAF', 'Flag': 'za.png'}
    SOUTH_KOREA = {'Name': 'South Korea', 'Code': 'KOR',
                   'Flag': 'kr.png', 'special': 'S. Korea'}
    SOUTH_SUDAN = {'Name': 'South Sudan', 'Code': 'SSD', 'Flag': 'ss.png'}
    SPAIN = {'Name': 'Spain', 'Code': 'ESP', 'Flag': 'es.png'}
    SRI_LANKA = {'Name': 'Sri Lanka', 'Code': 'LKA', 'Flag': 'lk.png'}
    SUDAN = {'Name': 'Sudan', 'Code': 'SDN', 'Flag': 'sd.png'}
    SURINAME = {'Name': 'Suriname', 'Code': 'SUR', 'Flag': 'sr.png'}
    SVALBARD_AND_JAN_MAYEN = {
        'Name': 'Svalbard and Jan Mayen', 'Code': 'SJM', 'Flag': 'sj.png'}
    SWAZILAND = {'Name': 'Swaziland', 'Code': 'SWZ', 'Flag': 'sz.png'}
    SWEDEN = {'Name': 'Sweden', 'Code': 'SWE', 'Flag': 'se.png'}
    SWITZERLAND = {'Name': 'Switzerland', 'Code': 'CHE', 'Flag': 'ch.png'}
    SYRIA = {'Name': 'Syria', 'Code': 'SYR', 'Flag': 'sy.png'}
    TAIWAN = {'Name': 'Taiwan', 'Code': 'TWN', 'Flag': 'tw.png'}
    TAJIKISTAN = {'Name': 'Tajikistan', 'Code': 'TJK', 'Flag': 'tj.png'}
    TANZANIA = {'Name': 'Tanzania', 'Code': 'TZA', 'Flag': 'tz.png'}
    THAILAND = {'Name': 'Thailand', 'Code': 'THA', 'Flag': 'th.png'}
    TOGO = {'Name': 'Togo', 'Code': 'TGO', 'Flag': 'tg.png'}
    TOKELAU = {'Name': 'Tokelau', 'Code': 'TKL', 'Flag': 'tk.png'}
    TONGA = {'Name': 'Tonga', 'Code': 'TON', 'Flag': 'to.png'}
    TRINIDAD_AND_TOBAGO = {'Name': 'Trinidad and Tobago',
                           'Code': 'TTO', 'Flag': 'tt.png'}
    TUNISIA = {'Name': 'Tunisia', 'Code': 'TUN', 'Flag': 'tn.png'}
    TURKEY = {'Name': 'Turkey', 'Code': 'TUR', 'Flag': 'tr.png'}
    TURKMENISTAN = {'Name': 'Turkmenistan', 'Code': 'TKM', 'Flag': 'tm.png'}
    TURKS_AND_CAICOS_ISLANDS = {
        'Name': 'Turks and Caicos Islands', 'Code': 'TCA', 'Flag': 'tc.png', 'special':'Turks and Caicos'}
    TUVALU = {'Name': 'Tuvalu', 'Code': 'TUV', 'Flag': 'tv.png'}
    US_VIRGIN_ISLANDS = {'Name': 'U.S.Virgin Islands',
                         'Code': 'VIR', 'Flag': 'vi.png'}
    UGANDA = {'Name': 'Uganda', 'Code': 'UGA', 'Flag': 'ug.png'}
    UKRAINE = {'Name': 'Ukraine', 'Code': 'UKR', 'Flag': 'ua.png'}
    UNITED_ARAB_EMIRATES = {
        'Name': 'United Arab Emirates', 'Code': 'ARE', 'Flag': 'ae.png', 'special':'UAE'}
    UNITED_KINGDOM = {'Name': 'United Kingdom', 'Code': 'GBR', 'Flag': 'gb.png', 'special':'UK'}
    UNITED_STATES = {'Name': 'United States', 'Code': 'USA', 'Flag': 'us.png'}
    URUGUAY = {'Name': 'Uruguay', 'Code': 'URY', 'Flag': 'uy.png'}
    UZBEKISTAN = {'Name': 'Uzbekistan', 'Code': 'UZB', 'Flag': 'uz.png'}
    VANUATU = {'Name': 'Vanuatu', 'Code': 'VUT', 'Flag': 'vu.png'}
    VATICAN = {'Name': 'Vatican', 'Code': 'VAT', 'Flag': 'va.png', 'special':'Vatican City'}
    VENEZUELA = {'Name': 'Venezuela', 'Code': 'VEN', 'Flag': 've.png'}
    VIETNAM = {'Name': 'Vietnam', 'Code': 'VNM', 'Flag': 'vn.png'}
    WALLIS_AND_FUTUNA = {'Name': 'Wallis and Futuna',
                         'Code': 'WLF', 'Flag': 'wf.png'}
    WESTERN_SAHARA = {'Name': 'Western Sahara',
                      'Code': 'ESH', 'Flag': 'eh.png'}
    YEMEN = {'Name': 'Yemen', 'Code': 'YEM', 'Flag': 'ye.png'}
    ZAMBIA = {'Name': 'Zambia', 'Code': 'ZMB', 'Flag': 'zm.png'}
    ZIMBABWE = {'Name': 'Zimbabwe', 'Code': 'ZWE', 'Flag': 'zw.png'}
