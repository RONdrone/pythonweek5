# Parent class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_level):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level
    
    def make_call(self, number):
        if self.battery_level > 0:
            print(f"Calling {number}...")
            self.battery_level -= 1  # Use some battery for each call
        else:
            print("Battery is too low to make a call.")
    
    def send_text(self, number, message):
        if self.battery_level > 0:
            print(f"Sending text to {number}: {message}")
            self.battery_level -= 1  # Use some battery for each text
        else:
            print("Battery is too low to send a text.")
    
    def check_battery(self):
        print(f"Battery level: {self.battery_level}%")
    
    def __str__(self):
        return f"{self.brand} {self.model}, Battery: {self.battery_level}%"

# Subclass: SmartphoneWithCamera (inherits from Smartphone)
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_level, camera_quality):
        super().__init__(brand, model, battery_level)
        self.camera_quality = camera_quality  # New attribute specific to this class
    
    # Overriding the make_call method to demonstrate polymorphism
    def make_call(self, number):
        print(f"Video calling {number}...")
        self.battery_level -= 2  # Video calls use more battery
    
    def take_picture(self):
        print(f"Taking a picture with {self.camera_quality} quality.")
    
    def __str__(self):
        return super().__str__() + f", Camera: {self.camera_quality}"

# Create instances of both classes
phone1 = Smartphone("Apple", "iPhone 13", 100)
phone2 = SmartphoneWithCamera("Samsung", "Galaxy S21", 100, "108MP")

# Use the methods
phone1.make_call("123-456-7890")
phone1.send_text("123-456-7890", "Hello!")
phone1.check_battery()
print(phone1)

phone2.make_call("987-654-3210")
phone2.take_picture()
phone2.check_battery()
print(phone2)
