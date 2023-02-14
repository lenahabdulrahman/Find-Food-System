def mainMenu():
    print("Enter the number of your option:\n1-Yes\n2-No")

def intro():
    print("FOOD FIND ia an expert system that assists you in \nfinding the most suitable meal for your health condition\n")
    print("Do you want to continue using FOOD FIND?\n1-Yes\n2-No")

def continueFun():
    print("Do you want to try another options?\n1-Yes\n2-No")

def servicemenu():
    print("Please select a service:\n")
    print("Enter the number of your option:\n1- Recomendation\n2- Calories Calculator\n3- Exit")

def healthConditions():
    print("Please select a health condition:\n")
    print("Enter the number of your option:\n1- Dabetic\n2- Glutin sensitive\n3- Maintaining a healthy diet\n4- Exit")

def typeMenu():
    print("Please select type of meal:\n1- Breakfast\n2- Lunch\n3- Dinner\n4- Exit")

def DabeticMenu(type):
    if(type ==1):
        print("We would recommend these meals for you:\n1-Oatmeal\n2-Multigrain Avocado Toast\n3-Greek Yougurt with Berries")
    elif(type==2):
        print("We would recommend these meals for you:\n1-Homemade Veggie Stir-Fry With Brown Rice\n2-Whole-Wheat Wrap with Lean Protein and Avocado\n3-Tuna Salad on Whole-Grain Toast")
    elif(type==3):
        print("We would recommend these meals for you:\n1-Lemon Garlic Salmon\n2-Quinoa Salad\n3-Vegetarian Lentil Tacos")
    elif (type == 4):
        print("THANK YOU FOR USING FOOD FIND")
        exit()
    print("Which recipe Would you like? (please enter a number):")
    num = validate_input_3()
    if(type==1 and num==1):
        print("The recipe of <<oatmeal>> is:\n 3/4 cup oats,2 eggs,1/2 cup milk,1 Tablespoon ground flaxseed,1 teaspoon cinnamon,\n1 banana mashed,Mix all ingredients together in a pot on the stove.\nTurn to medium-high heat. This will take about 5 minutes.\n")
    elif(type==1 and num==2):
        print("The recipe of <<multigrain avocado toast>> is:\n Mashed avocado, drizzled with extra-virgin olive oil. chopped parsley is sprinkled on top.\nAdd some red pepper flakes if you like a spicy kick. put it over multigrain bread.\n")
    elif (type == 1 and num == 3):
        print("The recipe of <<greek yougurt with berries>> is:\n  Place ¾ cup of yogurt in a bowl.\nSlice your berries, place them on top of the yogurt.\nDrizzle honey over top.\n")
    elif(type==2 and num==1):
        print("The recipe of <<homemade Veggie Stir-Fry With Brown Rice>> is:\n Start with ⅔ cup of cooked brown rice.\nTop it with plenty of cooked vegetables like green peppers, onions, broccoli, bok choy, celery, and carrots.\nThen add 3 to 5 oz of a lean protein like chicken, tofu, or beans.\nSteer clear of breaded or fried meats, which pack hidden carbs, Swift says. Cover your creation with 1 tablespoon of low-sodium soy sauce.\n")
    elif(type==2 and num==2):
        print("The recipe of <<whole-Wheat Wrap With Lean Protein and Avocado>> is:\n Start with a whole-wheat tortilla or pita (look for one with no more than 30 g of carbs).\nSpread it with 1 tablespoon of hummus or pesto, then add 3 oz of a lean protein of your choice.\nFeel free with veggies like lettuce, tomatoes, cucumbers, bell peppers, and shredded carrots.\nTop with a few slices of avocado.\n")
    elif(type==2 and num==3):
        print("The recipe of <<tuna Salad on Whole-Grain Toa>> is:\n Stir together one flavored tuna packet with a mini avocado, 1 tablespoon of olive oil-based mayo, and a ¼ cup of chopped veggies (onion, celery, or radish).\nSpoon the entire mixture on a slice of whole-grain toast.\n")
    elif(type==3 and num==1):
        print("The recipe of <<lemon garlic salmon>> is:\n Whisk lemon juice, garlic, oil, salt, and pepper into a bowl.\nPlace the salmon fillets over the lemon marinade. Let marinate for at least 30 minutes.\nBake the salmon for about 12-15 minutes.\n")
    elif(type==3 and num==2):
        print("The recipe of <<quinoa Salad>> is:\n Mix together the olive oil, garlic, lemon juice, vinegar, maple syrup or honey, salt, and pepper.\nIn a large bowl, combine quinoa, spinach, cucumber, tomatoes, avocado, and green onions.\nDrizzle salad with dressing and gently stir.\n")
    elif(type==3 and num==3):
        print("The recipe of <<vegetarian Lentil Tacos>> is:\n Lentils, tomatoes, onions, garlic, chili powders, and paprika can be added to a slow cooker.\nCover and cook on high 3 - 4 hours on high. Stir in cilantro and lime juice.\nServe warm with tortillas or toppings.\n")

def GlutinSensitiveMenu(type):
    if(type == 1):
        print("We would recommend these meals for you:\n1-Coconut Flour Pancakes\n2-Cloud Eggs\n3-Breakfast Tomatoes")
    elif(type== 2):
        print("We would recommend these meals for you:\n1-Shrimp Avocado Salad\n2-Grilled Mango & Avocado Salad\n3-Grilled Broccoli")
    elif(type==3):
        print("We would recommend these meals for you:\n1-Vegan Chili\n2-Cheesesteak Stuffed Peppers\n3-Garlicky Lemon Mahi Mahi")
    elif (type == 4):
        print("THANK YOU FOR USING FOOD FIND")
        exit()
    print("Which recipe Would you like? (please enter a number):")
    num = validate_input_3()
    if (type==1 and num == 1):
        print("The recipe of <<coconut Flour Pancakes>> is:\n Mix together Greek yogurt, egg yolks, maple syrup, and melted butter in a bowl.\nAdd coconut flour, baking soda, and salt; gently fold until just combined.\nGrease a large nonstick pan with cooking spray and place over medium-low heat.\n")
    elif(type==1 and num==2):
        print("The recipe of <<cloud Eggs>> is:\n Beat egg whites and yolks in a bowl.\nFold in Parmesan and ham; season with salt and pepper.\nBake until lightly golden, about 3 minutes.\nGarnish with chives before serving.\n")
    elif(type==1 and num==3):
        print("The recipe of <<breakfast Tomatoes>> is:\n Preheat oven to 400° and line a baking sheet with parchment paper.\nSlice tops off tomatoes and hollow with a metal spoon.\nDrizzle with olive oil and season with salt and pepper.\nBake 10 minutes, until softened slightly.\nCrack eggs into center and place back in oven to bake 12 more minutes.\n")
    elif(type==2 and num==1):
        print("The recipe of <<shrimp Avocado Salad>> is:\n Green onions, shrimp, serrano pepper, and lime juice.\nMix ingredients together in a large bowl; mix to combine flavors.\nRefrigerate until flavors blend, about 1 hour.\n")
    elif(type==2 and num==2):
        print("The recipe of <<grilled Mango & Avocado Salad>> is:\n Garnish mangoes with lime juice, olive oil, cucumbers and avocados.\nCook mangoes over medium heat or broil for 6-8 minutes or until lightly browned, turning once\n")
    elif(type==2 and num==3):
        print("The recipe of <<grilled Broccoli>> is:\n Prepare grill for indirect heat using a drip pan.\nPlace broccoli over drip pan on an oiled grill rack. Grill, covered, over indirect medium heat for 8-10 minutes on each side or until crisp-tender.\nIf desired, garnish with grilled lemon slices and red pepper flakes.\n")
    elif(type==3 and num==1):
        print("The recipe of <<vegan Chili>> is:\n Add beer and bring to a boil, then reduce to a simmer until it has reduced by half.\nCook until sweet potatoes are cooked through, 30 to 35 minutes; serve with toppings of your choice.")
    elif(type==3 and num==2):
        print("The recipe of <<cheesesteak Stuffed Peppers>> is:\n Preheat oven to 325º.\nAdd onions and mushrooms to a large baking dish and bake until tender, 30 minutes.\nAdd provolone to bottom of baked peppers and top with steak mixture. Broil until golden, 3 minutes.\nGarnish with parsley before serving.\n")
    elif(type==3 and num==3):
        print("The recipe of <<garlicky Lemon Mahi Mahi>> is:\n In a large skillet over medium heat, melt butter and olive oil.\nAdd mahi-mahi and season with salt and pepper. Cook until golden, 4 to 5 minutes per side, then transfer to a plate.\nAdd asparagus and cook until tender, 2 to 4 minutes.\n")


def healthyDietMenu(type):
    if(type ==1):
        print("We would recommend these meals for you:\n1-Avocado Toast and Egg\n2-Warm Berry Bowl\n3-Spinach and Cheddar Microwave Quiche")
    elif(type==2):
        print("We would recommend these meals for you:\n1-Roasted Cauliflower Tacos\n2-Shaved Carrot and Radish Salad\n3-Tomato Panzanella")
    elif(type==3):
        print("We would recommend these meals for you:\n1-Lemon Chicken\n2-Chopped Chilli Chicken Stir Fry\n3-Raw Pad Thai")
    elif (type == 4):
        print("THANK YOU FOR USING FOOD FIND")
        exit()
    print("Which recipe Would you like? (please enter a number):")
    num = validate_input_3()
    if(type==1 and num==1):
        print("The recipe of <<avocado Toast and Egg>> is:\n Prepare toast and fried eggs.Peel,mash avocado with lime juice, salt and pepper.\nSpread avocado toast topp it with egg and prefered seasoning.\n")
    elif(type==1 and num==2):
        print("The recipe of <<warm Berry Bowl>> is:\n On baking sheet, pour fruit with cinnamon and pinch of sea salt, stir to evenly spread.\nBake for 20 minutes.\nTake out of the oven and sprinkle optional garnishes and dark chocolate on top.\nServe in a small bowl, pour milk on top.\n")
    elif(type==1 and num==3):
        print("The recipe of <<spinach and Cheddar Microwave Quiche>> is:\n Using fresh spinach, place it in mug with 2 tablespoons of water and microwave on high for one minute.\nAdd milk, cheese, bacon, salt and pepper and mix until combined.\nRemove from microwave.\n")
    elif(type==2 and num==1):
        print("The recipe of <<roasted Cauliflower Tacos>> is:\n Roast cauliflower on a rimmed baking sheet until it is golden brown and tender, 18 to 22 minutes.\nSpoon cauliflower into tortillas and top with slaw.\nAdd lime wedges and cilantro for garnish.\n")
    elif(type==2 and num==2):
        print("The recipe of <<shaved Carrot and Radish Salad>> is:\n In bowl, whisk together orange juice, lemon juice, honey, and 1/2 tsp each salt and pepper to dissolve honey, then whisk in oil.\nArrange vegetables, oranges, and mint on large platter and drizzle with vinaigrette.\n")
    elif(type==2 and num==3):
        print("The recipe of <<tomato Panzanella>> is:\n Roast bread, add olive oil, garlic, anchovies and basil, then toss with dressing.\nLet stand at room temp for 30 minutes.\nToss croutons with tomatoes, then fold in remaining basil leaves, then drizzle with extra oil and cracked pepper.\n")
    elif(type==3 and num==1):
        print("The recipe of <<lemon chicken>> is:\n Mix the cornflour with the soy sauce and lemon juice in a small bowl.\nHeat the oil in a frying pan or wok over a high heat and add the vegetables.\nStir-fry for 2–3 minutes, or until the chicken is lightly browned.\n")
    elif(type==3 and num==2):
        print("The recipe of <<chopped chilli chicken stir fry>> is:\n Heat oil in a wok or large frypan over medium-high heat. Add eggplants, season and cook, stirring, for 3-4 minutes until golden.\nAdd onion, chilli paste and half the chilli and basil; cook for 2-3 minutes.\n")
    elif(type==3 and num==3):
        print("The recipe of <<raw pad Thai>> is:\n Zucchini, carrot, capsicum, cabbage, snow peas, bean sprouts and edamame.\nAdd the dressing and toss to combine. Divide among serving plates, top with the basil and serve with toasted seed mix.\n")

def calories():
    print("Please choose your gender:\n1- Female\n2- Male\n ")
    G= int(input())
    if(G == 1):
        print("Please enter your weight in kg: ")
        W= float(validate_input5())
        print("Please enter your height in cm: ")
        H= float(validate_input5())
        print("Please enter your age: ")
        A= float(validate_input5())
        c = ((10*W)+(6.25*H)-(5*A)-161)
        print("The suggested calories to consume each day is: ")
        print(c)
    elif(G ==2):
        print("Please enter your weight in kg: ")
        W= float(validate_input5())
        print("Please enter your height in cm: ")
        H= float(validate_input5())
        print("Please enter your age: ")
        A= float(validate_input5())
        c = ((10*W)+(6.25*H)-(5*A)+5)
        print("The suggested calories to consume each day is: ")
        print(c)

def validate_input2():
    num = int(input())
    check = False
    while(not check):
        if (num>0 and num<3):
            check = True
        else:
            print("Invalid input .. please choose 1 or 2")
            num = int(input())
    return num

def validate_input_3():
    num = int(input())
    check = False
    while(not check):
        if (num>0 and num<4):
            check = True
        else:
            print("Invalid input .. please choose from 1 to 3")
            num = int(input())
    return num

def validate_input_4():
    num = int(input())
    check = False
    while(not check):
        if (num>0 and num<5):
            check = True
        else:
            print("Invalid input .. please choose from 1 to 4")
            num = int(input())
    return num

def validate_input5():
    num = input()
    
    check = False
    while(not check):
        if (num.isnumeric()):
            check = True
        else:
            print("Invalid input .. please enter a number not string")
            num = input()
    return num
print("Welcom to FOOD FIND ... is this your first time using FOOF FIND?\n")
mainMenu()
option = validate_input2()
if (option == 1):
    intro()
    decide = validate_input2()
    if (decide ==2): #first time?
        print("Hope to see you soon!")
        exit()

choice = 0
while (choice !=2):
    servicemenu()
    s = validate_input_3()
    if (s == 1):
        healthConditions()
        select = validate_input_4()
        if (select == 1):
            typeMenu()
            type = validate_input_4()
            DabeticMenu(type)
        elif (select == 2):
            typeMenu()
            type = validate_input_4()
            GlutinSensitiveMenu(type)
        elif (select == 3):
            typeMenu()
            type = validate_input_4()
            healthyDietMenu(type)
        elif (select == 4):
            print("THANK YOU FOR USING FOOD FIND")
            exit()

    elif (s == 2):
        calories()

    elif (s == 3):
        print("THANK YOU FOR USING FOOD FIND")
        exit()
    else:
        print("\nInvalid input .. please enter a number from 1 to 3")
        continue

    continueFun()
    choice = validate_input2()


print("THANK YOU FOR USING FOOD FIND")
exit()
