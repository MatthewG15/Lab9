############################################
#                                          # 
#                   70pt                   #
#                                          #
############################################

# Create a celcius to fahrenheit calculator.
# Multiply by 9, then divide by 5, then add 32 to calculate your answer.

# TODO:
# Ask user for Celcius temperature to convert
# Accept user input 
# Calculate fahrenheit
# Output answer

print "What is the temperature in celsius"
Temp = int(raw_input())
Temp = Temp * 9
Temp = Temp / 5
Temp = Temp + 32
print Temp