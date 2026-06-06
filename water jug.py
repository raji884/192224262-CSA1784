def water_jug():
    jug1 = 0
    jug2 = 0
    print("Initial State: ", (jug1, jug2))
    jug1 = 4
    print("Fill 4L Jug: ", (jug1, jug2))
    jug2 = 3
    jug1 = 1
    print("Pour 4L -> 3L: ", (jug1, jug2))
    jug2 = 0
    print("Empty 3L Jug: ", (jug1, jug2))
    jug2 = 1
    jug1 = 0
    print("Pour remaining water: ", (jug1, jug2))
    jug1 = 4
    print("Fill 4L Jug Again: ", (jug1, jug2))
    jug1 = 2
    jug2 = 3
    print("Goal State Reached: ", (jug1, jug2))
water_jug()
