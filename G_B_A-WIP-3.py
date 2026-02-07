# God Bless America
import datetime, random, time
from random import randint
def main():
    print("Welcome to God Bless America, ")
    version = "WIP-2"
    citations = 0
    score = 0
    while True:
        options_for_play = str(input("""
    1 - Day 1 (new game)
    2 - About my game and I
    3 - Quit
            --->"""))
        match options_for_play:
            case "1":
                day_one(citations, score)
            case "2":
                print("""
Hello!
        I am Brody Hart, enjoyer of literature and computers, and I
    created this game, it is still in progress, but I have a pretty
    good vision for it.
    
        I created this game with the vision of 1984 by George
    Orwell, and Papers, Please; a video game created to
    actually mimic the authoritarian government and harsh
    characteristics found in stories like 1984. 1984 was written by
    George Orwell, a sort of 'political writer' who wrote stories that
    pictured authoritarian and rich-ruled countries in his works like
    Animal Farm and 1984. On the contrary, Papers, Please is a
    video game that takes place in the fictional war-ridden
    country of Arstotzka, ruled by big brother-esque authority. In
    the game, you are working for the Ministry of Admission via
    work lottery, denying and accepting passports all day. I
    created this game and decided to call it 'God Bless America'
    due to the use of the common phrase, and the similarity to
    'Glory to Arstotzka' from Papers, Please, and even uses 'God'
    as a big brother figure, because the idea of a figure ALWAYS
    watching is scary and entertaining...
        Anyways, I like it, and if you dont, screw you...""")
            case "3":
                break
            case _:
                print("Not an option")
    print(f"Thank you for playing! This game is in version {version}.")
    
def day_one(citations, score):
    glorious_saying = "God bless America and its glorious leader, Robert Barron"
# ^ totally necessary ^
    rulebook = """
    Rules:
        * Entrant must have a passport
        * Deny all foreigners
    God bless America and its glorious leader, Robert Barron"""
    current_date = datetime.date(1984, 1, 1)
    print(f"the date now is {current_date}, you recieved a letter (continued)")
    input("Press enter to continue --->")
    print("The letter reads...")
    print("Congratulations")
    input("Press enter to continue --->")
    print("The New Year's Eve Work Lottery has been completed")
    input("Press enter to continue --->")
    print("Your name was pulled")
    input("Press enter to continue --->")
    print("(the letter shows a map of southeast florida - Miami by the looks of the big red X)")
    input("Press enter to continue --->")
    print("This is where you will work for immigrant admission")
    input("Press enter to continue --->")
    print("(the flag of the USA) God Bless America and its glorious leader, Robert Barron.")
    input("Press enter to begin --->")
    print("*a letter on the table*:")
    print("Hello inspector, welcome to your workplace...")
    print("You will decide if someone's visa is valid for entry...")
    print("many people were excited for the Miami checkpoint to open...")
    print("However the rules are as follows...")
    print(rulebook)
    input("Press enter to continue --->")
    expiration_dates = [f"1/{randint(2, 31)}/84",
                        f"1/{randint(2, 31)}/84",
                        f"1/{randint(2, 31)}/84",
                        f"1/{randint(2, 31)}/84",
                        f"1/{randint(2, 31)}/84",
                        f"1/{randint(2, 31)}/84",
                        f"1/{randint(2, 31)}/84",
                        f"1/{randint(2, 31)}/84",
                        f"1/{randint(2, 31)}/84",
                        f"1/{randint(2, 31)}/84",
                        f"1/{randint(2, 31)}/84",
                        f"1/{randint(2, 31)}/84",
                        f"1/{randint(2, 31)}/84",
                        f"1/{randint(2, 31)}/84",
                        f"1/{randint(2, 31)}/84",
                        f"{randint(2, 12)}/ {randint(1, 28)}/84",
                        f"{randint(2, 12)}/ {randint(1, 28)}/84",
                        f"{randint(2, 12)}/ {randint(1, 28)}/84",
                        f"{randint(2, 12)}/ {randint(1, 28)}/84",
                        f"{randint(2, 12)}/ {randint(1, 28)}/84",
                        f"{randint(2, 12)}/ {randint(1, 28)}/84",
                        f"{randint(2, 12)}/ {randint(1, 28)}/84",
                        f"{randint(2, 12)}/ {randint(1, 28)}/84",
                        f"{randint(2, 12)}/ {randint(1, 28)}/84",
                        f"{randint(2, 12)}/ {randint(1, 28)}/84",
                        f"{randint(1, 12)}, {randint(1, 28)}, {randint(82, 83)}",
                        f"{randint(1, 12)}, {randint(1, 28)}, {randint(82, 83)}",
                        f"{randint(1, 12)}, {randint(1, 28)}, {randint(82, 83)}",
                        f"{randint(1, 12)}, {randint(1, 28)}, {randint(82, 83)}",
                        f"{randint(1, 12)}, {randint(1, 28)}, {randint(82, 83)}",
                        f"{randint(1, 12)}, {randint(1, 28)}, {randint(82, 83)}",
                        f"{randint(1, 12)}, {randint(1, 28)}, {randint(82, 83)}",
                        f"{randint(1, 12)}, {randint(1, 28)}, {randint(82, 83)}",
                        ]
    person_date = random.choice(expiration_dates)
    if person_date == expiration_dates[4]:
        expired = True
    else:
        expired = False
    issuing_cities = ["New York City",
                      "Miami",
                      "Los Angeles",
                      "Bejing",
                      "Shanghai",
                      "Shenzhen",
                      "Toronto",
                      "Vancouver",
                      "Quebec City",
                      "Tokyo",
                      "Osaka",
                      "Kyoto",
                      "Volgograd",
                      "Moscow",
                      "Novosibirsk",
                      "Mexico City",
                      "Guadalajara",
                      "Monterrey",
                      "London",
                      "Manchester",
                      "Birmingham"
                      ]
    american_cities = ["New York City",
                      "Miami",
                      "Los Angeles"
                       ]
    chinese_cities = ["Bejing",
                      "Shanghai",
                      "Shenzhen"
                      ]
    canadian_cities = ["Toronto",
                      "Vancouver",
                      "Quebec City",
                      ]
    japanese_cities = ["Tokyo",
                      "Osaka",
                      "Kyoto"
                       ]
    russian_cities = ["Volgograd",
                      "Moscow",
                      "Novosibirsk"
                      ]
    mexican_cities = ["Mexico City",
                      "Guadalajara",
                      "Monterrey"
                      ]
    british_cities = ["London",
                      "Manchester",
                      "Birmingham"
                      ]
    first_names = [
    "James", "Alex", "Maria", "Sarah", "John",
    "Emily", "Michael", "David", "Anna", "Daniel",
    "Laura", "Chris", "Jessica", "Mark", "Olivia"
]

    last_names = [
    "Smith", "Johnson", "Brown", "Taylor", "Anderson",
    "Martinez", "Wilson", "Thompson", "Garcia", "Miller",
    "Davis", "Rodriguez", "Clark", "Lewis", "Walker"
]
    insults = ["You have doomed me, Idiot",
               "They must pay well for such obediance, dog...",
               "Fuck you!",
               "You'll pay, blind sheep",
               f"I spent {randint(3, 10)} damn hours in this stupid line for that!?",
               "*cough* *cough* screw *cough* you...",
               "I'm not leaving!",
               "Dog.",
               "You old-country ignorants are all the same..."
               ] # yeeeah one day i'll use these for events...
    arrestable_insults = ["I'm not leaving!"] 
    day_length = 360 # seconds (abt 6 minutes)
    start = time.monotonic()
    while True:
        elapsed = time.monotonic() - start
        if elapsed >= day_length:
            break
        name1 = random.choice(first_names)
        name2 = random.choice(last_names)
        issuing_city = random.choice(issuing_cities)
        if issuing_city in american_cities:
            correct_country =  "USA"
        elif issuing_city in chinese_cities:
            correct_country =  "China"
        elif issuing_city in canadian_cities:
            correct_country =  "Canada"
        elif issuing_city in japanese_cities:
            correct_country =  "Japan"
        elif issuing_city in russian_cities:
            correct_country =  "Russia"
        elif issuing_city in mexican_cities:
            correct_country =  "Mexico"
        elif issuing_city in british_cities:
            correct_country =  "The United Kingdom"
        if correct_country != "USA":
            foreigner = True # against the rules, Americans only
        else:
            foreigner = False
        print("...")
        time.sleep(2)
        print("YOU: Papers, please")
        time.sleep(1)
        while True:
            print(f"""
        Name: {name1} {name2}
        Issuing City: {issuing_city}
        From: {correct_country}
        Expiry: {person_date}
    """)
            options_for_access = str(input("""
    Options:
        1 - Accept
        2 - Deny
        3 - Rulebook
        4 - Quit
         --->"""))
            if expired == False and foreigner == False:
                allowed = True
            else:
                allowed = False
            match options_for_access:
                case "1":
                    player_allows_npc = True
                    if allowed != player_allows_npc:
                        print("BORDER CITATION:")
                        if expired == True and player_allows_npc == True:
                            print("* EXPIRED DOCUMENTS")
                        if foreigner == True and player_allows_npc == True:
                            print("* FOREIGNERS ARE NOT ALLOWED")
                        if allowed == True and player_allows_npc == False:
                            print("* VISA VIABLE FOR ENTRY")
                        citations += 1
                    else:
                        score += 1
                    break
                case "2":
                    player_allows_npc = False
                    if allowed != player_allows_npc:
                        print("BORDER CITATION:")
                        if expired == True and player_allows_npc == True:
                            print("* EXPIRED DOCUMENTS")
                        if foreigner == True and player_allows_npc == True:
                            print("* FOREIGNERS ARE NOT ALLOWED")
                        if allowed == True and player_allows_npc == False:
                            print("* VISA VIABLE FOR ENTRY")
                        citations += 1
                    else:
                        score += 1
                    break
                case "3":
                    print(rulebook)
                case "4":
                    print("ARE YOU SURE? Barron does not like a quitter!")
                    quit_or_stay = str(input("""
    1 - Quit
    2 - Stay
        --->"""))
                    if quit_or_stay != "2":
                        print("God Bless America and its glorious leader, Robert Barron")
                        count_variable = 4
                        print("Closing in 5")
                        for i in range(4):
                            print(f"...{count_variable}")
                            count_variable -= 1
                            time.sleep(1)
                        quit()
                case _:
                    print("Not an option... Barron does not like an idiot... Do better...")
            
                
    print("End of day 1 -")
    time.sleep(2)
    print(glorious_saying)
    time.sleep(1)
    return citations, score
if __name__ == "__main__":
    main()
