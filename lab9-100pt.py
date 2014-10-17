############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.

print "What is the patients temperature?"
Temp = int(raw_input())
if Temp > 105:
    print "send them to a hospital"
elif Temp < 105:
    if Temp > 102:
        print "has the patient been sick in the past 24 hours?"
        sickness = str(raw_input())
        if sickness == "yes":
            print "send them to a hospital"
        if sickness == "no":
            print "They are fine"
    elif Temp > 100:
        print "has the patient been sick in the past 24 hours?"
        sickness2 = str(raw_input())
        if sickness2 == "yes":
            print "has the patient been to West Africa lately"
            trip = str(raw_input())
            if trip == "yes":
                print "send them to a hospital"
            if trip == "no":
                print "they are fine"
        if sickness2 == "no":
            print "they are fine"
    elif Temp < 100:
        print "They are fine."