import random

first_time = True


def random_numbers():
    num_1 = random.randint(0, 1)
    num_2 = random.randint(0, 1)
    num_3 = random.randint(0, 1)
    print("|" + str(num_1) + "|" + str(num_2) + "|" + str(num_3))
    return num_1, num_2, num_3


def natural_network():
    if not first_time:
        num_1_natural = num[0]
        num_2_natural = num[1]
        num_3_natural = num[2]
        inputs_natural = [num_1_natural, num_2_natural, num_3_natural]
        if what_wrongg[0] == 0:
            output_1_network = random.randint(0, 2)
        else:
            output_1_network = output[3]
        if what_wrongg[1] == 0:
            output_2_network = random.randint(0, 2)
        else:
            output_2_network = output[4]
        if what_wrongg[2] == 0:
            output_3_network = random.randint(0, 2)
        else:
            output_3_network = output[5]

    else:
        num_1_natural = num[0]
        num_2_natural = num[1]
        num_3_natural = num[2]
        inputs_natural = [num_1_natural, num_2_natural, num_3_natural]
        output_1_network = random.randint(0, 2)
        output_2_network = random.randint(0, 2)
        output_3_network = random.randint(0, 2)
    output_1 = inputs_natural[output_1_network]
    output_2 = inputs_natural[output_2_network]
    output_3 = inputs_natural[output_3_network]
    print(" " + "|", "|", "|")
    print(" " + "v", "v", "v")
    print("", output_1, output_2, output_3)
    return output_1, output_2, output_3, output_1_network, output_2_network, output_3_network


def what_wrong():
    if not first_time:
        what_wrongg = [int(input("the first one is: ")),
                       int(input("the second one is: ")), int(input("the thirds is: "))]
        return what_wrongg
    else:
        print("for the machine to learn")
        print("you need to tell her what good and what wrong")
        print("you can do it buy 0 for bad and 1 for good")
        what_wrongg = [int(input("the first one is: ")),
                       int(input("the second one is: ")), int(input("the thirds is: "))]
        return what_wrongg


num = random_numbers()
output = natural_network()
what_wrongg = what_wrong()
first_time = False
while 1 == 1:
    print("and now again")
    num = random_numbers()
    output = natural_network()
    what_wrongg = what_wrong()
