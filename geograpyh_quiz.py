import random

country_list = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua & Barbuda", "Argentina", "Armenia",
                "Australia", "Austria", "Azerbaijan", "Bahamas, The", "Bahrain", "Bangladesh", "Barbados", "Belarus",
                "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia & Herzegovina", "Botswana", "Brazil",
                "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada",
                "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros",
                "Democratic Republic Of Congo", "Republic Of Congo", "Costa Rica", "Côte D'Ivoire", "Croatia",
                "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic",
                "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia",
                "Eswatini (Formerly Swaziland)", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia",
                "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana",
                "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
                "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait",
                "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania",
                "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
                "Mauritania",
                "Mauritius", "Mexico", "Micronesia,", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco",
                "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua",
                "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau",
                "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal",
                "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts & Nevis", "Saint Lucia",
                "Saint Vincent & The Grenadines", "Samoa", "San Marino", "São Tomé & Príncipe", "Saudi Arabia",
                "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
                "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka",
                "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Tajikistan", "Tanzania", "Thailand",
                "Timor-Leste", "Togo", "Tonga", "Trinidad & Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu",
                "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
                "United States Of America", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela",
                "Vietnam", "Yemen", "Zambia", "Zimbabwe"
                ]

city_list = ["Kabul", "Tirana", "Algiers", "Andorra La Vella", "Luanda", "Saint John'S", "Buenos Aires", "Yerevan",
             "Canberra", "Vienna", "Baku", "Nassau", "Manama", "Dhaka", "Bridgetown", "Minsk", "Brussels", "Belmopan",
             "Porto-Novo", "Thimphu", "Sucre", "Sarajevo", "Gaborone", "Brasilia", "Bandar Seri Begawan", "Sofia",
             "Ouagadougou", "Bujumbura", "Praia", "Phnom Penh", "Yaounde", "Ottawa", "Bangui", "N'Djamena", "Santiago",
             "Beijing", "Bogotá", "Moroni", "Kinshasa", "Brazzaville", "San Jose", "Yamoussoukro", "Zagreb", "Havana",
             "Nicosia", "Prague", "Copenhagen", "Djibouti", "Roseau", "Santo Domingo", "Quito", "Cairo",
             "San Salvador", "Malabo", "Asmara", "Tallinn", "Mbabane", "Addis Ababa", "Suva", "Helsinki", "Paris",
             "Libreville", "Banjul", "Tbilisi", "Berlin", "Accra", "Athens", "Saint George'S", "Guatemala City",
             "Conakry", "Bissau", "Georgetown", "Port-Au-Prince", "Tegucigalpa", "Budapest", "Reykjavik", "New Delhi",
             "Jakarta", "Tehran", "Baghdad", "Dublin", "Jerusalem", "Rome", "Kingston", "Tokyo", "Amman", "Nur-Sultan",
             "Nairobi", "South Tarawa", "Pristina", "Kuwait City", "Bishkek", "Vientiane", "Riga", "Beirut", "Maseru",
             "Monrovia", "Tripoli", "Vaduz", "Vilnius", "Luxembourg", "Antananarivo", "Lilongwe", "Kuala Lumpur",
             "Male", "Bamako", "Valletta", "Majuro", "Nouakchott", "Port Louis", "Mexico City", "Palikir", "Chisinau",
             "Monaco", "Ulaanbaatar", "Podgorica", "Rabat", "Maputo", "Nay Pyi Taw", "Windhoek", "Yaren District",
             "Kathmandu", "Amsterdam", "Wellington", "Managua", "Niamey", "Abuja", "Pyongyang", "Skopje", "Oslo",
             "Muscat", "Islamabad", "Ngerulmud", "East Jerusalem", "Panama City", "Port Moresby", "Asunción", "Lima",
             "Manila", "Warsaw", "Lisbon", "Doha", "Bucharest", "Moscow", "Kigali", "Basseterre", "Castries",
             "Kingstown", "Apia", "San Marino", "São Tomé", "Riyadh", "Dakar", "Belgrade", "Victoria", "Freetown",
             "Singapore", "Bratislava", "Ljubljana", "Honiara", "Mogadishu", "Bloemfontein, Cape Town, Pretoria",
             "Seoul", "Juba", "Madrid", "Colombo, Sri Jayawardenepura Kotte", "Khartoum", "Paramaribo", "Stockholm",
             "Bern", "Damascus", "Dushanbe", "Dodoma", "Bangkok", "Dili", "Lomé", "Nukuʻalofa", "Port Of Spain",
             "Tunis", "Ankara", "Ashgabat", "Funafuti", "Kampala", "Kiev", "Abu Dhabi", "London", "Washington, D.C.",
             "Montevideo", "Tashkent", "Port Vila", "Vatican City", "Caracas", "Hanoi", "Sana", "Lusaka", "Harare"
             ]

country = random.choice(country_list)
answer = input("What is the capital of " + str(country) + "?\n")
country_index = country_list.index(country)
city = city_list[country_index]

if answer.lower() == city.lower():
    print("Congratulations, you are correct!")
else:
    print("Sorry, the correct answer is " + str(city) + ". Better luck next time.")
