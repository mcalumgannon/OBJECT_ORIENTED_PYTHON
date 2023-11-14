
# making two different classes that contain a function with the same name
class French:
    def say_hello(self):
        print('bonjour')
class Spanish:
    def say_hello(self):
        print('hola')

# wagwan can be anything, i used such an absurd term to remember just that        
def intro(wagwan):
    wagwan.say_hello()

louis = French()
juan = Spanish()

intro(juan)

# Output for louis is bonjour
# Output for juan is hola 