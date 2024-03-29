def determine_animal_type():
    internal_skeleton = input("The skeleton is (internal/external)?:\n").lower()
    
    if internal_skeleton == "internal":
        fertilization_within_body = input("The fertilization of eggs occurs (within the body/outside the body)?:\n").lower()
        
        if fertilization_within_body == "within the body":
            live_birth = input("Young are produced by (waterproof eggs/live birth)? (waterproof eggs/live birth):\n").lower()
            if live_birth == "live birth":
                print("Type of animal: Mammal")
            else:
                print("Type of animal: Reptile")
        else:
            waterproof_eggs = input("waterproof eggs? (yes/no): ").lower()
            if waterproof_eggs == "yes":
                print("Type of animal: Amphibian")
            else:
                print("Fish")
    else:
        skin_covered_by_scales = input("The skin is covered by scales? (scales/feathers):\n").lower()
        if skin_covered_by_scales == "scales":
            print("Type of animal: Reptile")
        else:
            feathers = input("Does the animal have feathers? (yes/no):\n").lower()
            if feathers == "yes":
                print("Type of animal: Bird")
            else:
                lives_in_water = input("Does it live in water? (yes/no):\n").lower()
                if lives_in_water == "yes":
                    print("Type of animal: Fish")
                else:
                    near_water = input("Does it live near water? (yes/no):\n").lower()
                    if near_water == "yes":
                        print("Type of animal: Amphibian.")
                    else:
                        print("Type of animal: Anthropod.")

if __name__ == "__main__":
    determine_animal_type()

