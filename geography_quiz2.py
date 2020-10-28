import random
import itertools

country_city_dictionary = {'Afghanistan': 'Kabul', 'Albania': 'Tirana', 'Algeria': 'Algiers',
                           'Andorra': 'Andorra La Vella', 'Angola': 'Luanda', 'Antigua & Barbuda': "Saint John'S",
                           'Argentina': 'Buenos Aires', 'Armenia': 'Yerevan', 'Australia': 'Canberra',
                           'Austria': 'Vienna', 'Azerbaijan': 'Baku', 'Bahamas, The': 'Nassau', 'Bahrain': 'Manama',
                           'Bangladesh': 'Dhaka', 'Barbados': 'Bridgetown', 'Belarus': 'Minsk', 'Belgium': 'Brussels',
                           'Belize': 'Belmopan', 'Benin': 'Porto-Novo', 'Bhutan': 'Thimphu', 'Bolivia': 'Sucre',
                           'Bosnia & Herzegovina': 'Sarajevo', 'Botswana': 'Gaborone', 'Brazil': 'Brasilia',
                           'Brunei': 'Bandar Seri Begawan', 'Bulgaria': 'Sofia', 'Burkina Faso': 'Ouagadougou',
                           'Burundi': 'Bujumbura', 'Cabo Verde': 'Praia', 'Cambodia': 'Phnom Penh',
                           'Cameroon': 'Yaounde', 'Canada': 'Ottawa', 'Central African Republic': 'Bangui',
                           'Chad': "N'Djamena", 'Chile': 'Santiago', 'China': 'Beijing', 'Colombia': 'Bogotá',
                           'Comoros': 'Moroni', 'Democratic Republic Of Congo': 'Kinshasa',
                           'Republic Of Congo': 'Brazzaville', 'Costa Rica': 'San Jose',
                           "Côte D'Ivoire": 'Yamoussoukro', 'Croatia': 'Zagreb', 'Cuba': 'Havana', 'Cyprus': 'Nicosia',
                           'Czech Republic': 'Prague', 'Denmark': 'Copenhagen', 'Djibouti': 'Djibouti',
                           'Dominica': 'Roseau', 'Dominican Republic': 'Santo Domingo', 'Ecuador': 'Quito',
                           'Egypt': 'Cairo', 'El Salvador': 'San Salvador', 'Equatorial Guinea': 'Malabo',
                           'Eritrea': 'Asmara', 'Estonia': 'Tallinn', 'Eswatini (Formerly Swaziland)': 'Mbabane',
                           'Ethiopia': 'Addis Ababa', 'Fiji': 'Suva', 'Finland': 'Helsinki', 'France': 'Paris',
                           'Gabon': 'Libreville', 'Gambia': 'Banjul', 'Georgia': 'Tbilisi', 'Germany': 'Berlin',
                           'Ghana': 'Accra', 'Greece': 'Athens', 'Grenada': "Saint George'S",
                           'Guatemala': 'Guatemala City', 'Guinea': 'Conakry', 'Guinea-Bissau': 'Bissau',
                           'Guyana': 'Georgetown', 'Haiti': 'Port-Au-Prince', 'Honduras': 'Tegucigalpa',
                           'Hungary': 'Budapest', 'Iceland': 'Reykjavik', 'India': 'New Delhi', 'Indonesia': 'Jakarta',
                           'Iran': 'Tehran', 'Iraq': 'Baghdad', 'Ireland': 'Dublin', 'Israel': 'Jerusalem',
                           'Italy': 'Rome', 'Jamaica': 'Kingston', 'Japan': 'Tokyo', 'Jordan': 'Amman',
                           'Kazakhstan': 'Nur-Sultan', 'Kenya': 'Nairobi', 'Kiribati': 'South Tarawa',
                           'Kosovo': 'Pristina', 'Kuwait': 'Kuwait City', 'Kyrgyzstan': 'Bishkek', 'Laos': 'Vientiane',
                           'Latvia': 'Riga', 'Lebanon': 'Beirut', 'Lesotho': 'Maseru', 'Liberia': 'Monrovia',
                           'Libya': 'Tripoli', 'Liechtenstein': 'Vaduz', 'Lithuania': 'Vilnius',
                           'Luxembourg': 'Luxembourg', 'Madagascar': 'Antananarivo', 'Malawi': 'Lilongwe',
                           'Malaysia': 'Kuala Lumpur', 'Maldives': 'Male', 'Mali': 'Bamako', 'Malta': 'Valletta',
                           'Marshall Islands': 'Majuro', 'Mauritania': 'Nouakchott', 'Mauritius': 'Port Louis',
                           'Mexico': 'Mexico City', 'Micronesia,': 'Palikir', 'Moldova': 'Chisinau', 'Monaco': 'Monaco',
                           'Mongolia': 'Ulaanbaatar', 'Montenegro': 'Podgorica', 'Morocco': 'Rabat',
                           'Mozambique': 'Maputo', 'Myanmar': 'Nay Pyi Taw', 'Namibia': 'Windhoek',
                           'Nauru': 'Yaren District', 'Nepal': 'Kathmandu', 'Netherlands': 'Amsterdam',
                           'New Zealand': 'Wellington', 'Nicaragua': 'Managua', 'Niger': 'Niamey', 'Nigeria': 'Abuja',
                           'North Korea': 'Pyongyang', 'North Macedonia': 'Skopje', 'Norway': 'Oslo', 'Oman': 'Muscat',
                           'Pakistan': 'Islamabad', 'Palau': 'Ngerulmud', 'Palestine': 'East Jerusalem',
                           'Panama': 'Panama City', 'Papua New Guinea': 'Port Moresby', 'Paraguay': 'Asunción',
                           'Peru': 'Lima', 'Philippines': 'Manila', 'Poland': 'Warsaw', 'Portugal': 'Lisbon',
                           'Qatar': 'Doha', 'Romania': 'Bucharest', 'Russia': 'Moscow', 'Rwanda': 'Kigali',
                           'Saint Kitts & Nevis': 'Basseterre', 'Saint Lucia': 'Castries',
                           'Saint Vincent & The Grenadines': 'Kingstown', 'Samoa': 'Apia', 'San Marino': 'San Marino',
                           'São Tomé & Príncipe': 'São Tomé', 'Saudi Arabia': 'Riyadh', 'Senegal': 'Dakar',
                           'Serbia': 'Belgrade', 'Seychelles': 'Victoria', 'Sierra Leone': 'Freetown',
                           'Singapore': 'Singapore', 'Slovakia': 'Bratislava', 'Slovenia': 'Ljubljana',
                           'Solomon Islands': 'Honiara', 'Somalia': 'Mogadishu',
                           'South Africa': 'Bloemfontein, Cape Town, Pretoria', 'South Korea': 'Seoul',
                           'South Sudan': 'Juba', 'Spain': 'Madrid', 'Sri Lanka': 'Colombo, Sri Jayawardenepura Kotte',
                           'Sudan': 'Khartoum', 'Suriname': 'Paramaribo', 'Sweden': 'Stockholm', 'Switzerland': 'Bern',
                           'Syria': 'Damascus', 'Tajikistan': 'Dushanbe', 'Tanzania': 'Dodoma', 'Thailand': 'Bangkok',
                           'Timor-Leste': 'Dili', 'Togo': 'Lomé', 'Tonga': 'Nukuʻalofa',
                           'Trinidad & Tobago': 'Port Of Spain', 'Tunisia': 'Tunis', 'Turkey': 'Ankara',
                           'Turkmenistan': 'Ashgabat', 'Tuvalu': 'Funafuti', 'Uganda': 'Kampala', 'Ukraine': 'Kiev',
                           'United Arab Emirates': 'Abu Dhabi', 'United Kingdom': 'London',
                           'United States Of America': 'Washington, D.C.', 'Uruguay': 'Montevideo',
                           'Uzbekistan': 'Tashkent', 'Vanuatu': 'Port Vila', 'Vatican City': 'Vatican City',
                           'Venezuela': 'Caracas', 'Vietnam': 'Hanoi', 'Yemen': 'Sana', 'Zambia': 'Lusaka',
                           'Zimbabwe': 'Harare'}

wining_pair = random.choice(list(country_city_dictionary.items()))
country = wining_pair[0]
city = wining_pair[1].lower()
user_input = input("What is the capital city of " + str(country) + "?\n").lower()

def check_answer(user_input, city):
    if user_input == city:
        return ("Congratulations, you are correct!")
    else:
        return ("Sorry, correct answer is " + str(wining_pair[1]) +". Better luck next time!")


print(check_answer(user_input, city))
