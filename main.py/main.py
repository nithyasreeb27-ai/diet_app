import json
def load_data():
    def load_food():
        with open("data/foods.json","r") as file:
            foods = json.load(file)
            return foods
    def load_conditions():
        with open("data/conditions.json","r") as file:
            conditions= json.load(file)
            return conditions
    return load_food(),load_conditions()

def display_conditions(conditions):
    print("\nCONDITIONS:\n")
    key=list(conditions.keys())
    for i,condition in enumerate(key,start=1):
        print(i,condition)
    print()

def user_choice(conditions):
    key=list(conditions.keys())
    choices=input("enter condition number separated by commas: ")
    choices=choices.split(",")
    selected_number=[]
    for i in choices:
        selected_number.append((int(i)))
    selected_condition=[]
    valid=True
    for a in selected_number:
        if 1 <= a <= len(key):
            selected_condition.append(key[a-1])
        else:
            print(a, "Invalid Choice")
            valid=False
    # print("number:",selected_number)
    # print(selected_condition)
    return valid, selected_number,selected_condition

def recommend(foods,valid,selected_number,selected_condition,conditions):
    if valid:
        for a in selected_number:
            all_recommendation=[]
            for i in selected_condition:
                if i in conditions:
                    print(i,"Valid entry")
                    rule=conditions[i]
                recommended_foods=[]
                for condi,value in rule.items():
                    for food,prop in foods.items(): 
                        if(condi=="max_glycemic_index"):
                            if(value>=prop["glycemic_index"]):
                                recommended_foods.append(food)
                        elif(condi=="min_protein"):    
                            if(value<=prop["protein"]):
                                recommended_foods.append(food)
                        elif(condi=="min_calories"):    
                            if(value<=prop["calories"]):
                                recommended_foods.append(food)
                all_recommendation.append(
                    {
                        "condition":i,
                        "foods": recommended_foods
                        }
                    )
                # choosen_food=[]
                # choosen_condition=[]
                # for recommendation in all_recommendation:
                #     choosen_condition.append(recommendation["condition"])
                #     for i in recommendation["foods"]:
                #         choosen_food.append(i)
            return all_recommendation
    if not valid:
        print("Choose valid number")

def separate_foods(all_recommendation):
    chosen_food=[]
    chosen_condition=[]
    for recommendation in all_recommendation:
        chosen_condition.append(recommendation["condition"])
        f=[]
        for i in recommendation["foods"]:
            f.append(i)
        chosen_food.append(f)
    
    return chosen_food,chosen_condition


def commonfoods(all_recommendation):
        common_foods=set(all_recommendation[0]["foods"])
        for recommendation in all_recommendation[1:]:
            common_foods=common_foods.intersection(
                set(recommendation["foods"])
            )
            common_food_lst=list(common_foods)
        return (common_food_lst)
    

def main():
    
    foods,conditions=load_data()
    display_conditions(conditions)
    valid,selected_number,selected_condition=user_choice(conditions)
    all_recommendation=recommend(foods,valid,selected_number,selected_condition,conditions)
    # print("separate:",separate_foods(all_recommendation))
    chosen_food,chosen_condition=separate_foods(all_recommendation)
    print()
    for i in range(len(chosen_food)):
        print(chosen_condition[i],":")
        for j in chosen_food[i]:
            print(j)
        print()
    
    print("Common foods:") 
    for j in commonfoods(all_recommendation):
        print(j)
main()