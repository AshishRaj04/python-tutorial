from random import choice

about = "Bihar"
capital = "Patna"
no_of_distric = 38

def facts_Bihar():
    facts = [
        "The word ‘Bihar’ is originally derived from the Sanskrit and Pali word ‘Vihara’ meaning abode",
        "In ancient times, Bihar was known as Vijayanagara or VikramNagar. It was ruled by the great Indian emperor Vikramaditya",
        "The idea of non-violence originated from Bihar around 2600 years ago",
        "Bihar is the origin of the biggest two religions in the world, namely Buddhism and Jainism",
        "The world-famous Nalanda University is located in the capital city of Patna",
        "The Mundeshwari temple in Bihar is known as the oldest Hindu temple in India",
        "Aryabhatta who gave zero number to the world, the nine planets theory, and trigonometric rules was from Bihar",
        "Vatsayana a great philosopher and author of the famous book ‘Kamasutra’ was from Bihar as well",
        "The first Prime Minister of Mauritius, Seewoosagur Ramgoolam hailed from Bihar",
        "Bihar is the birthplace of the tenth Guru that is Guru Gobind Singh, and the holy place of Sikhs is Harmandir Takht (Takht Sri Patna Sahib), which is in Patna",
        "India’s first president Dr. Rajendra Prasad belonged to Bihar"
    ]
    
    index = choice(range(0,10))
    print(facts[index])


if __name__ == "__main__":
    facts_Bihar()

# In Python, the __name__ variable is a special built-in variable that represents the name of the current module. When a Python script or module is executed, Python sets the __name__ variable to '__main__' if the script is being run as the main program.

# The if __name__ == '__main__': block is commonly used to determine whether the Python script is being run directly or if it is being imported as a module into another script. Here's what happens:

# When the script is run directly, Python sets __name__ to '__main__', indicating that it is the main program being executed.
# If the script is imported as a module into another script, then __name__ is set to the name of the module (not '__main__').
# So, when you see if __name__ == '__main__':, it's a way of checking if the script is being run as the main program and not being imported as a module. The code inside this block will only be executed if the script is the main program. This is often used for defining and executing code that should only run when the script is run directly and not when it's imported as a module into another script.